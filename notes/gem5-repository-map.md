# 六个 gem5 固定版本工作树的用途与一、二级目录导读

目录分析日期：2026-10-11。这里的“六个仓库”是**四个官方项目、六个固定版本工作树**：Bootcamp 额外固定了一份 gem5 和一份 gem5-resources。两份同名仓库的版本用途不同。本文基于旧电脑上的源码副本完成；当前 Mac 尚未取得这些工作树，现行版本与获取状态统一见 [上游登记](../gem5-official/README.md)。

目录按各自固定 commit 的 Git tree 核对，作用依据当时的 README、构建文件、文件内容与代表性入口归纳。文中的源码相对链接是取得依赖后的阅读入口，不代表当前 Mac 上文件已存在。本文覆盖目录职责，不表示已逐个读完目录中的算法或运行过其中的示例。

## 1. 六个仓库分别负责什么

| 工作树相对路径 | 官方来源与本次阅读快照 | 主要用途 | 与本项目的关系 | 一级 / 二级目录数 |
| --- | --- | --- | --- | ---: |
| [gem5-official/gem5/](../gem5-official/gem5/) | [gem5/gem5 @ c8222cc67a39](https://github.com/gem5/gem5/tree/c8222cc67a399bfc01e8658dd14b30d5bfd634f9) | 主实验基线：仿真器核心、CPU / 内存 / 设备模型、配置和测试。 | 建立自己的 SoC / DMA 性能模型，研究通用组件实现。 | 14 / 91 |
| [gem5-official/gem5-bootcamp-2024/](../gem5-official/gem5-bootcamp-2024/) | [gem5bootcamp/2024 @ 3ea9b7e3598c](https://github.com/gem5bootcamp/2024/tree/3ea9b7e3598cd15e8c0ea688fa850249eab0fad5) | 课程总仓库：讲义、练习、课程网站和固定版本子模块。 | 按讲义与练习配对学习 gem5 的使用和模型开发。 | 9 / 17 |
| [gem5-official/gem5-website/](../gem5-official/gem5-website/) | [gem5/website @ 07ebfaf9bb1a](https://github.com/gem5/website/tree/07ebfaf9bb1a0a4be2b822f3a4cf95abf20e4a4e) | 官方文档站点源码：教程、技术文档、博客、社区页面和附件。 | 查概念、接口与使用说明，并回到所用版本源码核对。 | 10 / 7 |
| [gem5-official/gem5-resources/](../gem5-official/gem5-resources/) | [gem5/gem5-resources @ 672d04917020](https://github.com/gem5/gem5-resources/tree/672d04917020934d452b2e767e97875c34693dee) | 主资源仓库：workload 源码、kernel 配置、磁盘镜像构建配方及元数据。 | 为实验准备可定位、可复现的输入。 | 3 / 16 |
| [gem5-official/gem5-bootcamp-2024/gem5/](../gem5-official/gem5-bootcamp-2024/gem5/) | [gem5/gem5 @ bb418d41eb6d](https://github.com/gem5/gem5/tree/bb418d41eb6d87c0a0591869097005c16420c6aa) | 课程固定的模拟器源码副本。 | 配合 Bootcamp 配置和练习；保持课程规定的版本关系。 | 12 / 88 |
| [gem5-official/gem5-bootcamp-2024/gem5-resources/](../gem5-official/gem5-bootcamp-2024/gem5-resources/) | [gem5/gem5-resources @ 6734bb4940dd](https://github.com/gem5/gem5-resources/tree/6734bb4940dd90f3b7c0349eedeefcf3ee405938) | 课程固定的 workload / 资源源码副本。 | 配合课程示例所需的资源与构建说明。 | 3 / 31 |

可以按一条工作流程理解它们：**Bootcamp 教你怎样使用和开发 → website 帮助查阅概念与接口 → gem5 组装并执行模型 → resources 提供被模型运行的程序和系统输入。** 本项目在外层维护自己的模型、配置、实验与分析。

计数口径：一级指仓库根目录下的子目录，二级指这些目录的直接子目录。包含版本化的 `.github` 等隐藏目录，不包含 Git 元数据 `.git`、普通文件、运行后才生成的 `build/` 或 `m5out/`。Bootcamp 的两个 gitlink 作为一级子模块入口计入，内部目录在各自工作树中统计。六份工作树合计 **301 个一、二级目录条目**；下表以 194 行合并说明共同目录，同时标明适用副本。某一级目录未列二级条目，表示该版本没有 Git 登记的直接子目录，子模块入口除外。

## 2. 两份 gem5：仿真器与模型代码

主库：[gem5-official/gem5/](../gem5-official/gem5/)；教学副本：[gem5-official/gem5-bootcamp-2024/gem5/](../gem5-official/gem5-bootcamp-2024/gem5/)。表中“主库、教学副本”表示两份都存在该目录、职责大体相同，**不表示目录内代码相同或配置可直接互换**。

主库比教学副本多出的这一级别目录共有 5 个：`.vscode/`、`docs/`、`util/disk-image-validator/`、`util/gem5_bridge/`、`util/hypercall_external_signal/`。其余 100 个目录路径两份共有。

### 2.1 一级目录

| 目录 | 作用与阅读提示 | 适用副本 |
| --- | --- | --- |
| `.devcontainer/` | VS Code Dev Containers / Codespaces 的开发容器配置与初始化脚本。 | 主库、教学副本 |
| `.github/` | GitHub 协作与自动化配置，包括问题模板、依赖更新和 CI。 | 主库、教学副本 |
| `.vscode/` | 仓库建议使用的 VS Code 工作区设置。 | 仅主库 |
| `build_opts/` | 预设构建选项，例如 ALL、ARM、RISCV、X86，以及部分 ISA / Ruby 协议组合；不是编译产物。 | 主库、教学副本 |
| `build_tools/` | 构建时调用的代码生成脚本，生成 SimObject 参数、枚举、debug flag、Python 嵌入等代码。 | 主库、教学副本 |
| `configs/` | 用 Python 组装与运行模型的配置、示例和实验脚本。 | 主库、教学副本 |
| `docs/` | gem5 standard library 的 Sphinx 文档构建入口，读取 src/python/gem5 等内容生成 API 文档。 | 仅主库 |
| `ext/` | 随仓库保存的外部库、配套组件和外部模拟器接入材料；其中部分目录只有接口与获取说明。 | 主库、教学副本 |
| `include/` | 提供给 guest 程序及外部调用方使用的头文件入口。 | 主库、教学副本 |
| `site_scons/` | SCons 构建系统的项目扩展。 | 主库、教学副本 |
| `src/` | 仿真器核心、硬件模型、Python 配置接口和 standard library 的主要实现。 | 主库、教学副本 |
| `system/` | 被模拟系统启动所需的辅助软件源码。 | 主库、教学副本 |
| `tests/` | 自动化测试配置、测试程序及其预期结果等。 | 主库、教学副本 |
| `util/` | 构建辅助、调试、运行控制、分析、开发维护等工具；通常按需选用。 | 主库、教学副本 |

### 2.2 二级目录：GitHub 与配置脚本

| 目录 | 作用与阅读提示 | 适用副本 |
| --- | --- | --- |
| `.github/ISSUE_TEMPLATE/` | 提交 bug 时使用的问题模板，帮助补齐版本、配置和复现信息。 | 主库、教学副本 |
| `.github/workflows/` | 编译、测试、容器构建及定时任务等 GitHub Actions 工作流。 | 主库、教学副本 |
| `configs/boot/` | 供被模拟系统启动后执行的 rcS / shell 脚本，例如启动 workload、退出或配合 checkpoint。 | 主库、教学副本 |
| `configs/common/` | 示例共用的 CPU、Cache、内存、全系统平台、命令行参数和 workload 配置辅助代码。 | 主库、教学副本 |
| `configs/deprecated/` | 已标记弃用的配置示例；适合核对旧教程，不作为新实验的默认入口。 | 主库、教学副本 |
| `configs/dist/` | dist-gem5 分布式仿真的配置，包括模拟以太网交换机。 | 主库、教学副本 |
| `configs/dram/` | DRAM 延迟、带宽、低功耗等扫描实验的配置与分析入口。 | 主库、教学副本 |
| `configs/example/` | 可运行配置的示例集合，包括 stdlib、全系统、GPU、流量发生器等用法；参数和资源仍需按版本核对。 | 主库、教学副本 |
| `configs/learning_gem5/` | Learning gem5 教程的分步配置，配合教学 SimObject 使用；研究实验需要另行确认其假设。 | 主库、教学副本 |
| `configs/network/` | Ruby 网络的共用配置入口，选择网络实现并连接 router、link 等对象。 | 主库、教学副本 |
| `configs/nvm/` | 非易失存储器以及 DRAM / NVM 混合内存的参数扫描示例。 | 主库、教学副本 |
| `configs/ruby/` | Ruby 协议与控制器的系统组装代码；具体状态机实现主要在 src/mem/ruby 体系内。 | 主库、教学副本 |
| `configs/splash2/` | 运行 SPLASH-2 并行 benchmark 的配置与 workload 选择逻辑。 | 主库、教学副本 |
| `configs/topologies/` | Mesh、Crossbar、Cluster 等网络拓扑的 Python 连接规则；目录内容不是某个目标 SoC 的既定拓扑。 | 主库、教学副本 |

### 2.3 二级目录：外部库与配套模拟器

`ext/` 不能简单理解为“所有第三方依赖都已经安装”。例如下表中的 DRAMSim2、DRAMsim3、DRAMSys 目录主要提供接入和构建说明，额外源码仍需按实验需要获取。

| 目录 | 作用与阅读提示 | 适用副本 |
| --- | --- | --- |
| `ext/Kconfiglib/` | Python Kconfig 库，支持解析和处理构建配置。 | 主库、教学副本 |
| `ext/dnet/` | 低层网络数据结构与辅助代码，例如地址、Ethernet、IP 等协议处理。 | 主库、教学副本 |
| `ext/drampower/` | DRAMPower 配套代码，用于根据 DRAM 活动估算功耗 / 能量。 | 主库、教学副本 |
| `ext/dramsim2/` | DRAMSim2 的构建接入文件与获取说明；此 checkout 未包含另外下载的完整 DRAMSim2 工程。 | 主库、教学副本 |
| `ext/dramsim3/` | DRAMsim3 的构建接入文件与获取说明；外部模拟器源码需要按说明另行取得。 | 主库、教学副本 |
| `ext/dramsys/` | DRAMSys 的 CMake / 构建接入与使用说明；完整 DRAMSys 源码属于额外依赖。 | 主库、教学副本 |
| `ext/dsent/` | DSENT 的网络组件功耗、面积等建模代码，供互连相关分析使用。 | 主库、教学副本 |
| `ext/fputils/` | fp64、fp80 等浮点数的位级处理、转换辅助代码与测试。 | 主库、教学副本 |
| `ext/gdbremote/` | GDB remote protocol 所需的信号定义等公共辅助内容。 | 主库、教学副本 |
| `ext/googletest/` | GoogleTest C++ 单元测试框架。 | 主库、教学副本 |
| `ext/iostream3/` | 压缩数据流的 C++ iostream 封装，例如基于 zlib 的输入输出。 | 主库、教学副本 |
| `ext/libelf/` | ELF 文件解析库，为可执行文件、目标文件等加载提供支持。 | 主库、教学副本 |
| `ext/libfdt/` | Flattened Device Tree 的读写操作库。 | 主库、教学副本 |
| `ext/magic_enum/` | C++ 枚举反射工具，提供枚举值与名称之间的转换等功能。 | 主库、教学副本 |
| `ext/mcpat/` | McPAT 处理器功耗、面积、时序估算相关代码；结果仍取决于输入与模型适用范围。 | 主库、教学副本 |
| `ext/nomali/` | NoMali stub GPU 库，提供 Mali 寄存器 / 设备交互模型；不能据此当作完整 GPU 性能模型。 | 主库、教学副本 |
| `ext/ply/` | Python Lex-Yacc 词法与语法分析工具，服务于代码生成和语言解析。 | 主库、教学副本 |
| `ext/pybind11/` | C++ 与 Python 绑定库，连接 gem5 的两种实现语言。 | 主库、教学副本 |
| `ext/softfloat/` | 软件浮点运算实现，为指令语义等提供浮点支持。 | 主库、教学副本 |
| `ext/sst/` | 将 gem5 接入 SST 的配套组件、构建与运行示例。 | 主库、教学副本 |
| `ext/systemc/` | 仓库携带的 Accellera SystemC 代码及构建接入；与 src/systemc 的 gem5 实现职责不同。 | 主库、教学副本 |
| `ext/testlib/` | gem5 回归测试框架的 Python 实现，包括测试发现、fixture、运行和结果处理。 | 主库、教学副本 |
| `ext/x11keysym/` | X11 键盘符号定义，供键盘输入等设备接口使用。 | 主库、教学副本 |

### 2.4 二级目录：公共接口、构建与核心源码

| 目录 | 作用与阅读提示 | 适用副本 |
| --- | --- | --- |
| `include/gem5/` | m5ops 接口及相关汇编头文件，与 util/m5 等配套；主库另有 hypercall 接口定义。 | 主库、教学副本 |
| `site_scons/gem5_scons/` | gem5 专用的构建配置、源码管理、builder 与公共辅助逻辑。 | 主库、教学副本 |
| `site_scons/site_tools/` | 提供给 SCons 的工具扩展，例如 Git 相关处理。 | 主库、教学副本 |
| `src/arch/` | ISA 相关的指令语义、寄存器、地址转换、异常及其他架构支持。 | 主库、教学副本 |
| `src/base/` | 通用基础设施，例如地址范围、统计、日志、加载器和数据结构。 | 主库、教学副本 |
| `src/cpu/` | CPU 执行模型与公共机制，包括 simple、Minor、O3、KVM、分支预测等。 | 主库、教学副本 |
| `src/dev/` | 设备与平台模型，包括 PIO、DMA、总线设备、串口、网卡及 AMDGPU 等；DMA / SDMA 学习重点入口。 | 主库、教学副本 |
| `src/doc/` | 源码侧的专题说明；此版本主要是 SE 模式文件访问与文件系统重定向说明 se-files.txt。 | 主库、教学副本 |
| `src/doxygen/` | Doxygen 的分组定义、模板、页面片段与图像等文档生成材料。 | 主库、教学副本 |
| `src/gpu-compute/` | GPU 计算执行模型，例如 compute unit、wavefront、调度与访存协作。 | 主库、教学副本 |
| `src/kern/` | guest OS 相关的 ABI、常量和系统调用支持；不是完整 Linux 内核源码。 | 主库、教学副本 |
| `src/learning_gem5/` | Learning gem5 教程使用的教学 SimObject，例如事件、端口和简单 Cache。 | 主库、教学副本 |
| `src/mem/` | 内存请求、Packet / Port、Cache、互连、内存控制器，以及 Ruby / Garnet 等实现；SoC 性能建模重点入口。 | 主库、教学副本 |
| `src/proto/` | Protocol Buffers 的 trace 格式定义，例如指令与内存请求记录。 | 主库、教学副本 |
| `src/python/` | m5 Python 接口、嵌入式 Python 支持和 gem5 standard library；连接系统配置与底层模型。 | 主库、教学副本 |
| `src/sim/` | SimObject、事件调度、仿真控制、checkpoint、drain、统计与 workload 等仿真基础机制。 | 主库、教学副本 |
| `src/sst/` | gem5 一侧的 SST 接口与请求桥接模型，配合 ext/sst 使用。 | 主库、教学副本 |
| `src/systemc/` | gem5 的 SystemC 支持 / 实现及 TLM 连接代码，包括内核、通道、数据类型和桥接。 | 主库、教学副本 |
| `src/test_objects/` | 专供测试使用的 SimObject，例如统计接口测试对象。 | 主库、教学副本 |
| `system/arm/` | ARM 全系统启动相关的 bootloader 与 Device Tree 材料。 | 主库、教学副本 |

### 2.5 二级目录：测试与工具

| 目录 | 作用与阅读提示 | 适用副本 |
| --- | --- | --- |
| `tests/deprecated/` | 旧测试布局和旧自动化入口，保留供历史兼容与查阅。 | 主库、教学副本 |
| `tests/gem5/` | 使用 gem5 测试框架组织的仿真回归测试，包括配置、fixture 和校验逻辑。 | 主库、教学副本 |
| `tests/pyunit/` | Python 层的单元测试，例如 standard library、统计和工具接口。 | 主库、教学副本 |
| `tests/test-progs/` | 供仿真与回归测试使用的小型 guest 程序及构建材料。 | 主库、教学副本 |
| `util/amdgpu/` | 收集 AMDGPU 全系统仿真所需 MMIO trace、GPU ROM 等输入的脚本；实际采集有硬件与 Linux 环境要求。 | 主库、教学副本 |
| `util/cpt_upgraders/` | 旧 checkpoint 到新格式的转换脚本。 | 主库、教学副本 |
| `util/crosstool-ng/` | 交叉编译工具链的配置材料，帮助构建不同 ISA 的 guest 程序。 | 主库、教学副本 |
| `util/cxx_config/` | 用 C++ 配置接口加载和实例化系统的示例，展示 Python 配置以外的嵌入方式。 | 主库、教学副本 |
| `util/disk-image-validator/` | 磁盘镜像验证工具，检查启动、退出事件及配套 guest 接口等行为。 | 仅主库 |
| `util/dist/` | dist-gem5 的多进程 / 多主机启动与运行辅助脚本。 | 主库、教学副本 |
| `util/dockerfiles/` | gem5 构建和开发环境的 Dockerfile 配方。 | 主库、教学副本 |
| `util/emacs/` | Emacs 的编辑与编码风格配置。 | 主库、教学副本 |
| `util/gem5-resources-manager/` | 资源元数据管理工具，含 JSON / MongoDB 操作和管理界面；不是 workload 源码仓库本身。 | 主库、教学副本 |
| `util/gem5_bridge/` | guest Linux 的 gem5_bridge 内核模块，将 m5ops MMIO 区域映射给用户程序。 | 仅主库 |
| `util/gem5art/` | 实验 artifact、运行任务及复现流程的管理工具代码。 | 主库、教学副本 |
| `util/gerrit-bot/` | 与 Gerrit 审查流程有关的自动化维护脚本。 | 主库、教学副本 |
| `util/github-runners-vagrant/` | 利用 Vagrant 准备 GitHub Actions runner 的配置与脚本。 | 主库、教学副本 |
| `util/helper_scripts_for_mongodb/` | gem5 资源目录数据库的整理、转换等维护脚本。 | 主库、教学副本 |
| `util/hypercall_external_signal/` | 通过 shared memory、进程信号和 socket 与运行中的 gem5 交互，例如查询状态、获取统计。 | 仅主库 |
| `util/m5/` | guest 内的 m5 命令和库，使 workload 能请求统计、退出、checkpoint 等模拟器操作。 | 主库、教学副本 |
| `util/maint/` | 生成变更记录、整理 patch 等项目维护工具。 | 主库、教学副本 |
| `util/mem/` | 宿主侧共享内存客户端及示例，可映射 gem5 提供的模拟物理内存范围。 | 主库、教学副本 |
| `util/minorview/` | MinorCPU 流水线 trace 的可视化工具。 | 主库、教学副本 |
| `util/offline_db/` | 为离线使用保存资源元数据及相关文件的工具；使用时需另行选择下载范围。 | 主库、教学副本 |
| `util/plot_dram/` | DRAM 扫描实验的结果绘图工具。 | 主库、教学副本 |
| `util/statetrace/` | 跟踪实际程序执行状态并与模拟器交互的调试辅助工具，可用于指令 / 寄存器状态比较。 | 主库、教学副本 |
| `util/streamline/` | 将 gem5 统计转换为 ARM Streamline 可使用的分析数据。 | 主库、教学副本 |
| `util/style/` | 检查和辅助修正源码风格的工具。 | 主库、教学副本 |
| `util/systemc/` | gem5 与 SystemC 相互嵌入的示例和构建材料。 | 主库、教学副本 |
| `util/tap/` | 与宿主 TAP 网络设备连接的辅助程序。 | 主库、教学副本 |
| `util/term/` | 连接模拟串口 / 控制台的终端客户端。 | 主库、教学副本 |
| `util/tlm/` | gem5 与 SystemC TLM 的连接示例及编译运行材料。 | 主库、教学副本 |
| `util/update_copyright/` | 检查和更新源码版权年份等信息的维护脚本。 | 主库、教学副本 |
| `util/vi/` | Vim 编辑器的风格配置。 | 主库、教学副本 |

理解主工程时，可先把 `src/sim` 看作仿真运行机制，`src/cpu`、`src/mem`、`src/dev` 看作被组装的模型实现，`src/python` 看作 Python 接口与可复用组装库，`configs` 看作具体组装和运行入口。构建系统再把这些内容及所需外部组件编译为 gem5 可执行文件。

## 3. gem5-bootcamp-2024：课程、练习与配套版本

入口：[gem5-official/gem5-bootcamp-2024/](../gem5-official/gem5-bootcamp-2024/)。建议把同一主题的 `slides/` 和 `materials/` 配对阅读：前者讲解，后者用于动手。父仓库的 README 含有旧环境描述，目录是否实际存在以此固定版本的 tree 为准。

### 3.1 一级目录

| 目录 | 作用与阅读提示 | 适用副本 |
| --- | --- | --- |
| `.devcontainer/` | 课程开发容器 / Codespaces 配置，以及创建和启动后的环境初始化脚本。 | Bootcamp 父仓库 |
| `.github/` | 课程仓库的 GitHub 自动化配置。 | Bootcamp 父仓库 |
| `.vscode/` | 课程建议使用的 VS Code 工作区设置。 | Bootcamp 父仓库 |
| `assets/` | 课程共用图片、图标等素材。 | Bootcamp 父仓库 |
| `gem5/` | 固定 commit 的 gem5 子模块，为教程提供配套模拟器源码；内部结构见下文两份 gem5 的对照表。 | Bootcamp 父仓库 |
| `gem5-resources/` | 固定 commit 的资源子模块，为教程提供配套 workload / 镜像构建材料；内部结构见 resources 对照表。 | Bootcamp 父仓库 |
| `materials/` | 上机练习、示例程序、配置脚本与参考完成版本，按课程主题组织。 | Bootcamp 父仓库 |
| `slides/` | 以 Markdown / Marp 编写的讲义和幻灯片，与 materials 的主题对应。 | Bootcamp 父仓库 |
| `web/` | 课程网页入口、课程列表和展示 / 交互脚本。 | Bootcamp 父仓库 |

### 3.2 二级目录

| 目录 | 作用与阅读提示 | 适用副本 |
| --- | --- | --- |
| `.github/workflows/` | 把 Markdown 课件构建为网页等产物的工作流。 | Bootcamp 父仓库 |
| `assets/img/` | CPU、ISA、gem5 标识等插图与图标，供课程页面和幻灯片引用。 | Bootcamp 父仓库 |
| `materials/01-Introduction/` | 仿真背景、工具入门与 Python 基础对应的练习材料。 | Bootcamp 父仓库 |
| `materials/02-Using-gem5/` | 使用 stdlib、资源、CPU、Cache、内存、全系统、加速 / 采样、功耗和 MultiSim 的练习。 | Bootcamp 父仓库 |
| `materials/03-Developing-gem5-models/` | 新增 SimObject、调试、事件、Port、CPU 模型、Cache coherence、CHI、Ruby 网络和扩展模型的练习。 | Bootcamp 父仓库 |
| `materials/04-GPU-model/` | GPU 全系统仿真的配置和示例 workload，包括矩阵运算与 PyTorch 相关材料。 | Bootcamp 父仓库 |
| `materials/05-Other-simulators/` | 与 SST、DRAM 模拟器、SystemC 配合的练习材料。 | Bootcamp 父仓库 |
| `materials/06-Contributing/` | 贡献代码相关的上机材料；此版本主要提供测试练习。 | Bootcamp 父仓库 |
| `materials/archive/` | 保留的旧课程 / 旧教程材料；查阅时确认版本与现行课程的关系。 | Bootcamp 父仓库 |
| `slides/01-Introduction/` | Bootcamp 介绍、仿真背景、gem5 入门和 Python 背景讲义。 | Bootcamp 父仓库 |
| `slides/02-Using-gem5/` | 从组装系统到运行 workload、采样、加速和多仿真的使用讲义。 | Bootcamp 父仓库 |
| `slides/03-Developing-gem5-models/` | SimObject、事件、接口、模型开发、一致性协议和 Ruby 网络讲义。 | Bootcamp 父仓库 |
| `slides/04-GPU-model/` | GPU 模型的 Markdown 讲义和 PDF 课件。 | Bootcamp 父仓库 |
| `slides/05-Other-simulators/` | SST、DRAM 模拟器与 SystemC 的联动讲义。 | Bootcamp 父仓库 |
| `slides/06-Contributing/` | 贡献流程、测试与 gem5-at-home 等社区开发讲义。 | Bootcamp 父仓库 |
| `slides/themes/` | Marp 主题 CSS、打印样式和 gem5 标识等课件外观素材。 | Bootcamp 父仓库 |
| `web/icons/` | 课程网站使用的导航、社区和媒体图标。 | Bootcamp 父仓库 |

`gem5/` 与 `gem5-resources/` 是独立 Git 子模块，不在本节重复展开。它们分别由第 2 节的“教学副本”和第 5 节的“教学 resources”说明；课程对应的实际版本由父仓库 gitlink 固定。

## 4. gem5-website：官方文档的源文件

入口：[gem5-official/gem5-website/](../gem5-official/gem5-website/)。这是 Jekyll 文档站点的源仓库，阅读技术内容优先进入 `_pages/documentation/`；只有维护网站时才需要深入模板、样式和站点构建代码。

### 4.1 一级目录

| 目录 | 作用与阅读提示 | 适用副本 |
| --- | --- | --- |
| `.github/` | 文档站点的 GitHub 自动化配置。 | website |
| `_data/` | 站点结构化数据，例如 documentation.yml 定义的文档导航。 | website |
| `_includes/` | 页面共用的 HTML 片段，例如页头、页脚和 head。 | website |
| `_layouts/` | Jekyll 页面模板，例如普通页面、文档、博客、目录和 tab 布局。 | website |
| `_pages/` | 官网的主体页面，以及社区、技术文档和静态资料。 | website |
| `_posts/` | 按日期归档的博客、版本发布和技术文章。 | website |
| `_sass/` | 可被样式入口复用的 Sass 模块，例如基础布局、提示框和语法高亮。 | website |
| `assets/` | 网站引用的下载文件、图片和浏览器端脚本。 | website |
| `blog/` | 博客列表 / 索引页面入口，文章正文主要在 _posts。 | website |
| `css/` | 站点样式入口 main.scss，组合 _sass 等样式生成网页 CSS。 | website |

### 4.2 二级目录

| 目录 | 作用与阅读提示 | 适用副本 |
| --- | --- | --- |
| `.github/workflows/` | 将 Sphinx 生成的文档纳入网站等自动化工作流。 | website |
| `_pages/community/` | 开发会议与社区活动页面。 | website |
| `_pages/documentation/` | 技术文档正文入口，包括 general_docs、Learning gem5、stdlib 和 gem5art 等专题。 | website |
| `_pages/static/` | 文档引用的脚本、patch、图形、活动与外部资料等配套静态内容。 | website |
| `assets/files/` | 教程课件、论文、示例配置 / 脚本等可下载附件。 | website |
| `assets/img/` | 文档与博客的架构图、教程截图、logo 等图像。 | website |
| `assets/js/` | 站内搜索、tab 切换等 JavaScript 代码。 | website |

文档仓库的提交时间与 gem5 release 不必一一对应。引用 API、参数或运行命令时，应再核对实际使用的 gem5 commit。

## 5. 两份 gem5-resources：程序、系统镜像配方与元数据

主资源仓库：[gem5-official/gem5-resources/](../gem5-official/gem5-resources/)；教学资源副本：[gem5-official/gem5-bootcamp-2024/gem5-resources/](../gem5-official/gem5-bootcamp-2024/gem5-resources/)。这里主要回答“拿什么程序、kernel 或磁盘镜像来运行”，仿真器和硬件模型实现主要在 gem5 中。克隆资源仓库不等于下载了资源目录指向的全部 binary、kernel 和 disk image；不少子目录保存的是生成这些资源的配方。

### 5.1 两份共有的一级目录与网站二级目录

| 目录 | 作用与阅读提示 | 适用副本 |
| --- | --- | --- |
| `prev-resources-json/` | 历史版本的资源索引 JSON，帮助查找旧资源定义；不是预编译资源文件。 | 主 resources、教学 resources |
| `src/` | workload、kernel / firmware、磁盘镜像等资源的源码、补丁、构建脚本和说明。 | 主 resources、教学 resources |
| `web/` | 资源文档页面所用的 Jekyll 模板与样式材料。 | 主 resources、教学 resources |
| `web/_includes/` | 资源条目等可复用的页面片段。 | 主 resources、教学 resources |
| `web/_layouts/` | 资源文档页面的布局模板。 | 主 resources、教学 resources |
| `web/_sass/` | 资源文档页面的 Sass 样式。 | 主 resources、教学 resources |
| `web/assets/` | 资源文档页面使用的样式等静态资源。 | 主 resources、教学 resources |

### 5.2 主 resources 的 src 二级目录

| 目录 | 作用与阅读提示 | 适用副本 |
| --- | --- | --- |
| `src/deprecated/` | 已归入旧材料的资源，例如 hack-back、PARSEC 和 simple；保留供旧配置与历史复现查阅。 | 主 resources |
| `src/examples/` | 小型教学 / 测试程序的集中位置，包括汇编测试、矩阵乘法、退出控制和打印示例。 | 主 resources |
| `src/gapbs/` | GAP Benchmark Suite 图计算 workload，以及构建相应全系统磁盘镜像的材料。 | 主 resources |
| `src/gpu/` | GPU benchmark / 示例程序源码与构建材料，例如 HIP、DNNMark、heterosync、pannotia 和 square。 | 主 resources |
| `src/linux-kernel/` | 为 gem5 构建 Linux kernel 的配置文件与说明；Linux 完整源码按构建流程另行取得。 | 主 resources |
| `src/npb-24.04-imgs/` | 包含 NAS Parallel Benchmarks 的 Ubuntu 24.04 磁盘镜像构建配方与安装脚本。 | 主 resources |
| `src/riscv-fs-alt/` | RISC-V 全系统的另一套构建材料，保留较早的 Linux / BusyBox / Ubuntu 等组合；使用时核对对应说明。 | 主 resources |
| `src/riscv-fs/` | RISC-V 全系统资源构建材料，包括 OpenSBI、Linux 与 Ubuntu 镜像的组合。 | 主 resources |
| `src/spec-2006/` | 运行 SPEC CPU2006 的磁盘镜像构建和 gem5 使用说明；benchmark 安装介质需要另行提供。 | 主 resources |
| `src/spec-2017/` | 运行 SPEC CPU2017 的镜像构建与 workload 配置材料；不等于取得了完整 SPEC 安装介质。 | 主 resources |
| `src/ubuntu-generic-diskimages/` | 通用 ARM / x86 Ubuntu 磁盘镜像构建材料，含 guest m5 工具和启动控制等配置。 | 主 resources |
| `src/x86-ubuntu-gpu-ml/` | 面向 x86 + AMDGPU 全系统机器学习 workload 的 Ubuntu 镜像构建材料，包含 ROCm / PyTorch 等安装配置。 | 主 resources |

### 5.3 教学 resources 的 src 二级目录

| 目录 | 作用与阅读提示 | 适用副本 |
| --- | --- | --- |
| `src/arm-ubuntu/` | ARM Ubuntu 全系统磁盘镜像的构建脚本、配置与启动材料。 | 教学 resources |
| `src/asmtest/` | 汇编级小测试及构建材料，用于检查指令和相关执行行为。 | 教学 resources |
| `src/gapbs/` | GAP 图计算 benchmark 的源码、安装与全系统磁盘镜像构建材料。 | 教学 resources |
| `src/getting-started/` | 入门 workload 集合的获取、构建和说明，涉及图计算、SAT 与 NPB 等例子。 | 教学 resources |
| `src/gpu-fs/` | 此固定版本主要保存 vega_mmio.log，作为 GPU 全系统仿真的 MMIO trace 输入。 | 教学 resources |
| `src/gpu/` | GPU benchmark / 示例源码与构建材料；使用课程配套版本和工具链。 | 教学 resources |
| `src/hack-back/` | 与启动后生成 / 恢复 checkpoint 相关的旧示例和辅助脚本。 | 教学 resources |
| `src/insttest/` | 通过内联汇编检查 load-store、swap、compare-and-swap 等指令行为的小测试。 | 教学 resources |
| `src/linux-kernel/` | Linux kernel 构建配置及说明，完整内核源码需按流程另取。 | 教学 resources |
| `src/lupv/` | 面向 LupV / LupIO RISC-V 平台的 bootloader、kernel 和磁盘镜像构建材料。 | 教学 resources |
| `src/m5-exit-repeat/` | 重复发出 m5_exit 的小程序，用于练习 / 测试模拟器退出事件处理。 | 教学 resources |
| `src/matrix-multiply-omp/` | OpenMP 并行矩阵乘法示例，可设置迭代次数与线程数。 | 教学 resources |
| `src/matrix-multiply/` | 普通矩阵乘法小程序，用作基础 workload。 | 教学 resources |
| `src/npb/` | NAS Parallel Benchmarks 的磁盘镜像构建和使用说明。 | 教学 resources |
| `src/parsec/` | PARSEC 并行 benchmark 的源码材料、安装脚本和磁盘镜像构建说明。 | 教学 resources |
| `src/print-this/` | 按指定次数打印字符串的小程序，适合入门与参数传递测试。 | 教学 resources |
| `src/riscv-boot-exit-nodisk/` | 无需磁盘镜像即可启动并退出的 RISC-V 资源构建材料，组合 kernel、bootloader 和小 workload。 | 教学 resources |
| `src/riscv-fs/` | 此课程版本的 RISC-V 全系统构建材料，涉及 BBL、Linux 和文件系统；与主 resources 同名目录的构建组合不同。 | 教学 resources |
| `src/riscv-opensbi-alt/` | 利用 Docker 等方式构建 RISC-V OpenSBI / kernel 的另一套脚本。 | 教学 resources |
| `src/riscv-opensbi/` | RISC-V OpenSBI 固件及相关内核构建材料。 | 教学 resources |
| `src/riscv-ubuntu-22.04/` | RISC-V Ubuntu 22.04 磁盘镜像的构建脚本和配置。 | 教学 resources |
| `src/riscv-ubuntu/` | RISC-V Ubuntu 镜像的较早构建材料；与 22.04 专用目录分开保留。 | 教学 resources |
| `src/simple/` | hello、退出和 checkpoint 等基础小程序，按 ISA 提供源码 / 构建材料。 | 教学 resources |
| `src/spec-2006/` | SPEC CPU2006 磁盘镜像构建与运行说明，安装介质需要另行提供。 | 教学 resources |
| `src/spec-2017/` | SPEC CPU2017 磁盘镜像构建与运行说明，安装介质需要另行提供。 | 教学 resources |
| `src/x86-ubuntu-gpu-ml/` | 教程对应的 x86 + AMDGPU 机器学习镜像构建材料；其 Ubuntu / ROCm 等组合需配合课程版本。 | 教学 resources |
| `src/x86-ubuntu/` | x86 Ubuntu 全系统磁盘镜像的构建脚本、m5 工具与启动配置。 | 教学 resources |

两份资源仓库的 `src/` 不能只按同名目录类推：主资源仓库把若干小例子集中到 `src/examples/`，把 PARSEC、hack-back、simple 等材料归入 `src/deprecated/`，也增加或调整了系统镜像配方。同名的 `src/riscv-fs/` 等目录，内部固件与内核组合也可能不同。应从所用副本的 README 和构建脚本确认依赖。

## 6. 不属于子目录、但应认识的根文件

下列是文件，不计入前面的 301 个目录条目。

| 所在仓库 | 根文件 | 作用 |
| --- | --- | --- |
| 两份 gem5 | `SConstruct` | SCons 顶层构建入口，组织配置、代码生成和编译。 |
| 两份 gem5 | `KCONFIG.md` | Kconfig 构建配置机制的说明。 |
| 两份 gem5 | `README.md`、`RELEASE-NOTES.md`、`TESTING.md` | 项目概况、版本变化与测试入口。 |
| 两份 gem5 | `pyproject.toml`、`requirements.txt`、`optional-requirements.txt` | Python 工具配置和相关依赖清单。 |
| Bootcamp | `.gitmodules` | 声明两个子模块的路径与来源；实际固定 commit 记录在父仓库 gitlink。 |
| Bootcamp | `pre-download-resources.py` | 为课程预取资源的脚本；执行时会产生额外下载。 |
| website | `_config.yml`、`Gemfile` | Jekyll 网站配置与 Ruby 依赖定义。 |
| 两份 resources | `resources.json` | 资源元数据索引；不是索引所指向的资源实体。 |
| 两份 resources | `_config.yml`、`Gemfile`、`index.md` | 资源说明网站的构建配置与首页。 |

## 7. 针对 soc_model 的阅读顺序

以下为学习入口建议，尚不表示已经完成相应课程、实现或实验。为便于实际定位，本节少数路径深入到三级及以下，不改变前文一、二级目录的覆盖口径。

| 研究问题 | 优先入口 | 希望建立的理解 |
| --- | --- | --- |
| 怎样搭建并运行一个 gem5 系统 | Bootcamp 的 `slides/01-Introduction/`、`slides/02-Using-gem5/` 与对应 `materials/`；gem5 的 `configs/example/`、`src/python/` | 选择处理器、Cache / 内存、workload，识别配置、运行与统计之间的关系。 |
| gem5 内部怎样工作 | Bootcamp 的 `03-Developing-gem5-models/`；gem5 的 `src/sim/`、`src/base/`、`src/learning_gem5/` | SimObject、事件调度、Port 交互、接纳 / 反压与完成语义。 |
| 怎样建立简单 SoC 性能模型 | gem5 的 `src/mem/`、`src/dev/`、`configs/example/`；按需要使用 resources 小 workload | 从流量源、互连、内存建立可解释的小模型，再加入 CPU、Cache 或设备约束。 |
| 怎样学习 DMA / SDMA | [dma_device.hh](../gem5-official/gem5/src/dev/dma_device.hh)、[dma_device.cc](../gem5-official/gem5/src/dev/dma_device.cc) 与 [AMDGPU 设备目录](../gem5-official/gem5/src/dev/amdgpu/) | 请求拆分、在途数量、端口反压、完成回调，以及已有 SDMA 命令处理路径。 |
| 怎样研究 NoC 的拥塞与流控 | [Garnet](../gem5-official/gem5/src/mem/ruby/network/garnet/)、`configs/network/`、`configs/topologies/` 与 [synthetic traffic 配置](../gem5-official/gem5/configs/example/garnet_synth_traffic.py) | Router、VC、credit、Buffer 与注入率如何影响延迟和吞吐。 |

gem5 的 AMDGPU SDMA 实现可作为学习和对照对象；是否适用于目标 SDMA 的性能预测，需要继续审查时间、资源、功能边界并做校准。已有初步分析见 [官方仓库报告](../gem5-official-repo-report.md)。本项目自己的模型仍放外层 `models/`，配置放外层 `configs/`，问题与结果放 `experiments/`；官方工作树内部保持原有结构。

## 8. 依据与覆盖核对

目录清单取自六个固定 commit 的 `git ls-tree`；表中的职责归纳结合对应 README、文件清单、代表性源码注释和脚本入口。主要可复查入口如下。

| 内容 | 阅读快照中的依据 |
| --- | --- |
| gem5 工程总结构 | [主库 README](../gem5-official/gem5/README.md)、[教学副本 README](../gem5-official/gem5-bootcamp-2024/gem5/README.md) |
| 课程与子模块 | [Bootcamp README](../gem5-official/gem5-bootcamp-2024/README.md)、[slides README](../gem5-official/gem5-bootcamp-2024/slides/README.md)、[子模块声明](../gem5-official/gem5-bootcamp-2024/.gitmodules) |
| website 的布局 | [website README 的 Directory Structure](../gem5-official/gem5-website/README.md)、[站点配置](../gem5-official/gem5-website/_config.yml) |
| 两份 resources 的职责与资源构建 | [主 resources README](../gem5-official/gem5-resources/README.md)、[教学 resources README](../gem5-official/gem5-bootcamp-2024/gem5-resources/README.md) 及各 `src` 子目录 README / 构建文件 |
| 外部模拟器依赖边界 | [DRAMSim2](../gem5-official/gem5/ext/dramsim2/README)、[DRAMsim3](../gem5-official/gem5/ext/dramsim3/README)、[DRAMSys](../gem5-official/gem5/ext/dramsys/README) 的接入说明 |
| 文档生成与特殊工具 | [Sphinx 文档入口](../gem5-official/gem5/docs/README)、[共享内存客户端](../gem5-official/gem5/util/mem/shared_memory_client.hh)、[外部控制脚本](../gem5-official/gem5/util/hypercall_external_signal/orchestrator_request.py) |

按适用副本展开后，本表覆盖六份工作树全部 301 个一、二级目录条目。这里的核对针对目录清单与文档定位，未执行编译、课程练习或仿真实验。
