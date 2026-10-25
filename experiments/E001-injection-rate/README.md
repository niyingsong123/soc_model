# E001：请求注入率与完成吞吐

准备日期：2026-10-12；环境状态更新：2026-10-20。状态：**配置和测量方法已准备，E001 参数扫描尚未运行，没有本实验实测结果。** 本机 WSL2、Ubuntu、gem5 X86 构建及官方示例验收已完成；启动方式、构建选项和证据见 [本机环境](../../.local/environment.md)。

本实验落实 [项目工作开展计划](../../plans/project-work-plan.md) 的首个性能问题。实验记录和验证要求遵循 [实验工作方法](../../methods/experiment-workflow.md)。

## 问题、范围与模型

当请求注入率逐步超过内存的服务能力时，完成吞吐、请求延迟和反压怎样变化？

使用官方已有组件：单个 `LinearGenerator` → `SingleChannelSimpleMemory`，通过 `TestBoard(cache_hierarchy=None)` 直接连接。没有 CPU、Cache、真实应用、DMA 读写依赖或 OS；该实验只解释受控读流量下的服务能力，不能用于预测目标 DRAM 或 SDMA 性能。

配置入口为 [config.py](config.py)。唯一扫描参数是 `--rate`；其余参数在本实验中固定。上游来源以 [上游登记](../../upstream/README.md) 为准，本次接口与统计阅读快照为 gem5 commit `c8222cc67a399bfc01e8658dd14b30d5bfd634f9`，2026-10-12 核对主工作树未有改动。

| 参数 | 固定设置或扫描值 | 原因 |
| --- | --- | --- |
| 请求源与地址模式 | 单个 LinearGenerator，顺序访问 | 避免多个请求源或随机模式同时变化 |
| 请求大小、读比例 | 64 B、100% 读 | 先观察一种固定请求的服务过程 |
| 地址范围 | 从 0 到 64 MiB，发生器上界与内存容量一致 | 无其他地址映射因素 |
| 内存模型 | SimpleMemory，30 ns 延迟、0 ns 延迟变化、1 GiB/s 带宽 | 分别看固定返回延迟与请求接纳间隔 |
| 配置注入率 | 0.25、0.5、1、2 GiB/s | 覆盖低于、接近和高于配置服务能力 |
| 发生器时长 | 1 ms | 有限时间窗口；实际停止时间必须从输出读取 |
| outstanding | `max_outstanding_reqs=0`，此接口表示无限制 | 首轮不扫描并发上限；不把这一假设用于通用 DMA |
| 反压调度 | `elastic_req=False` | 固定发生器的速率调度策略，反压时仍须等待 retry |
| 测量区间 | 从仿真开始到发生器实际退出，不 reset stats，不添加 drain 阶段 | 明确统计窗口，单列结束时未完成请求 |

## 运行前的预期

以下为手算与源码推断，**不是仿真结果**。

- 每个 64 B 请求在 1 GiB/s 下对应约 59.6 ns 的接纳间隔。SimpleMemory 用带宽限制请求接纳，用延迟安排返回；不能把两者直接相加成不可重叠的服务时间。
- 供给较低时，完成吞吐应接近实际请求供给；供给达到或超过服务能力后，吞吐应在服务上限附近饱和。允许时间量化、起始与结束窗口带来的差异。
- SimpleMemory 忙时拒绝 Timing 请求并安排 retry；发生器等待重试会影响实际发出的请求。配置为 2 GiB/s 不意味着每秒已有 2 GiB 请求被内存接纳，也不表示存在一个无限增长的外部队列。
- 发生器的退出状态并不保证响应全部返回。不能用正常退出推断所有请求已完成。

## 统计口径与检查方法

先从实际 `config.ini` / `config.json` 确认发生器、内存对象路径、参数和直连关系，再定位统计。以下使用对象职责描述，不猜测首次运行中对象路径的完整拼写。

| 指标 | 计数来源或计算 | 适用边界 |
| --- | --- | --- |
| 已生成请求 G | 发生器 `numPackets` | 在尝试发送前增加；不等于已被内存接纳 |
| 已接纳读请求 A | 本实验 SimpleMemory 的 `numReads::total` | 由其继承的 AbstractMemory 访问路径计数；只适用于本例无其他请求源、无 Cache、无额外访问的条件 |
| 已完成读请求 C | 发生器 `totalReads` | 在 `recvTimingResp()` 中增加，表示请求方已经收到响应 |
| 已完成数据量 | 发生器 `bytesRead` | 应等于 C × 64 B；不能用内存侧 `bytesRead` 替代请求方完成量 |
| 完成吞吐 | 发生器 `bytesRead / simSeconds`，并与其 `readBW` 对照 | `readBW` 为 B/s，换算 GiB/s 要除以 2^30；采用实际统计时长 |
| 平均完成请求延迟 | 发生器 `avgReadLatency / simFreq` 换算为秒 | 从首次尝试发送前登记 waitingResp 到收到响应，包含该请求遇到的发送反压等待；不包含尚未生成的请求等待 |
| 结束时未被接纳 | G − A | 先验证三个计数来自同一窗口且统计路径符合本例 |
| 结束时在途 | A − C | 与“已生成但未完成”G − C 分开报告 |
| 反压迹象 | 发生器 `numRetries`、`retryTicks` | retry 次数与延迟统计需结合实现解释，不当作队列深度 |

首轮验证至少包含：实际参数仅注入率变化；`0 ≤ C ≤ A ≤ G`；`bytesRead = C × 64`；没有写请求与被抑制的地址访问；实际时长与退出原因合理；低负载与饱和趋势能由模型解释。延迟起点已核对源码，真实输出中仍需确认统计对象与单位。若计数不满足上述关系，先保留输出并调查，不能补造完成量。

无 warm-up 与 drain 的选择仅用于这个短小、无 Cache 的机制实验。报告全部有限窗口效应；必要时另开运行延长时长或检查尾部响应，不覆盖原结果。确定性首轮不机械重复多次。

## 已就绪环境与下一次运行入口

本机已构建 `X86/gem5.opt`，使用 `--without-tcmalloc -j 4`。重建须保留该分配器选项；原因与本机环境事实统一记录在 [本机环境](../../.local/environment.md)。

Linux 文件系统中的固定 commit 干净源码 checkout、依赖安装、构建，以及官方 `simple.py` 与 `memory_traffic.py LinearGenerator 100` 检查均已完成。环境诊断另运行过一个独立的 SimpleMemory 检查；这些结果保存于 `environment-check`，不替代本实验四档参数扫描和统计分析。

下面是**未执行**的单次实验命令，变量应按实际环境设置；配置脚本可从 Windows 项目读取，源码构建与原始运行目录放 Linux 文件系统。每次用新目录，禁止复用已产生结果的 run ID。

```bash
SOC_MODEL_ROOT=/mnt/e/codex/soc_model
GEM5_ROOT="$HOME/soc_model/upstream/gem5"
SOC_MODEL_RUNS="$HOME/soc_model/runs"
SOC_MODEL_RATE=0.25GiB/s
SOC_MODEL_RUN_ID="$(date +%Y%m%dT%H%M%S%N%z)-rate-${SOC_MODEL_RATE%GiB/s}"
SOC_MODEL_OUTDIR="$SOC_MODEL_RUNS/E001-injection-rate/$SOC_MODEL_RUN_ID"
mkdir -p "$SOC_MODEL_RUNS/E001-injection-rate"
mkdir "$SOC_MODEL_OUTDIR"
"$GEM5_ROOT/build/X86/gem5.opt" \
  --outdir="$SOC_MODEL_OUTDIR" \
  "$SOC_MODEL_ROOT/experiments/E001-injection-rate/config.py" \
  --rate="$SOC_MODEL_RATE" \
  >"$SOC_MODEL_OUTDIR/stdout.log" 2>"$SOC_MODEL_OUTDIR/stderr.log"
SOC_MODEL_EXIT_CODE=$?
printf '%s\n' "$SOC_MODEL_EXIT_CODE" >"$SOC_MODEL_OUTDIR/exit-code.txt"
```

真实执行前按实验方法准备运行记录：开始与结束时间、完整命令、gem5 commit 与工作树状态、构建依赖和二进制身份、配置脚本快照与校验值。脚本写入的 `experiment-input.json` 只记录实验输入，不替代完整运行身份。首次真实运行时落实记录与统计提取，不在尚未运行时生成模拟结果或空的 evidence 目录。

## 实际阅读依据

以下均为上述 gem5 commit 的局部阅读，不表示已通读模块。

| 源码位置 | 本次实际核对的行为 |
| --- | --- |
| [memory/simple.py](../../upstream/gem5/src/python/gem5/components/memory/simple.py)，`SingleChannelSimpleMemory.__init__()`、`set_memory_range()` | SimpleMemory 参数接口及单段地址范围 |
| [linear_generator.py](../../upstream/gem5/src/python/gem5/components/processors/linear_generator.py)、[linear_generator_core.py](../../upstream/gem5/src/python/gem5/components/processors/linear_generator_core.py)，构造与 `_create_traffic()` | 请求大小、速率、地址范围和生成时长的设置；线性流量后进入 exit 状态 |
| [test_board.py](../../upstream/gem5/src/python/gem5/components/boards/test_board.py)，`_connect_things()` | 无 Cache 时单发生器与单内存端口直连 |
| [BaseTrafficGen.py](../../upstream/gem5/src/cpu/testers/traffic_gen/BaseTrafficGen.py)，参数声明 | outstanding=0 与 elastic_req 的含义 |
| [base.cc](../../upstream/gem5/src/cpu/testers/traffic_gen/base.cc)，`update()`、`retryReq()`、`StatGroup`、`recvTimingResp()` | 生成与完成计数的区别、反压与统计公式 |
| [base.hh](../../upstream/gem5/src/cpu/testers/traffic_gen/base.hh)，`allocateWaitingRespSlot()` | 首次尝试发送前登记延迟计时起点，不能将平均延迟解释为纯内存延迟 |
| [simple_mem.cc](../../upstream/gem5/src/mem/simple_mem.cc)，`recvTimingReq()`、`release()`、`dequeue()` | 忙时拒绝与 retry、带宽控制接纳间隔、安排响应 |
| [abstract_mem.cc](../../upstream/gem5/src/mem/abstract_mem.cc)，`MemStats::regStats()`、`access()` | 内存侧读请求与字节数计数及 total 向量输出 |
| [exit_gen.cc](../../upstream/gem5/src/cpu/testers/traffic_gen/exit_gen.cc)，`ExitGen::enter()` | 请求结束仿真，不在此处等待所有返回 |
