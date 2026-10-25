# soc_model 项目入口

本项目使用 gem5 学习体系结构仿真，逐步建立能够解释和分析 SoC 性能的模型。研究目标由 [项目上下文](project-context.md)维护；[gem5 研究计划](plans/gem5-research-plan.md)说明先研究什么，[项目工作开展计划](plans/project-work-plan.md)说明怎样通过模型和实验实现目标。开始或接续工作时查看 [当前进度](records/PROGRESS.md)。

## 常用入口与文件职责

| 文件 | 唯一负责的内容 | 何时读取或更新 |
| --- | --- | --- |
| [AGENTS.md](AGENTS.md) | 长期协作规则、证据边界、修改与交付要求 | 开始任务；形成长期工作规则时更新 |
| [project-context.md](project-context.md) | 项目目标、范围、跨项目关系与已采用的研究方式 | 判断一个任务是否符合项目方向；研究方向改变时更新 |
| [plans/gem5-research-plan.md](plans/gem5-research-plan.md) | gem5 整体认识的研究范围、顺序、阅读边界和完成标准 | 确定资料与少量源码的学习内容 |
| [plans/project-work-plan.md](plans/project-work-plan.md) | 面向 SoC/SDMA 的工作阶段、推进方式与实验接续 | 确定怎样通过模型和实验实现项目目标 |
| [upstream/README.md](upstream/README.md) | 上游仓库、下载范围、选定版本、本地获取状态 | 下载、升级、复现或定位源码时使用 |
| [methods/experiment-workflow.md](methods/experiment-workflow.md) | 模型与实验组织方法、运行记录和结论验证要求 | 开始编写模型、运行实验或整理性能结论时使用 |
| [records/PROGRESS.md](records/PROGRESS.md) | 当前阶段、已完成工作、未完成事项与下一步 | 接续任务；发生实际进展时更新 |
| [.local/environment.md](.local/environment.md) | 本机 WSL、Linux 用户、构建选项、运行路径与验收记录 | 在本机启动、重建或诊断环境时使用；不纳入 Git |
| [.local/installed-software.md](.local/installed-software.md) | 本项目安装的软件、完整依赖清单、系统组件改动与未来清理归属 | 安装或升级后登记；以后卸载、迁移或核对残留时使用；不纳入 Git |
| [records/WORKING_NOTES.md](records/WORKING_NOTES.md) | 当前整体认识的研究所得与待讨论问题 | 继续补充同一份工作笔记；正式组织另行讨论 |
| [E001 注入率实验](experiments/E001-injection-rate/README.md) | 首个性能问题的配置、参数、统计口径与验证方法 | Linux 就绪后开展真实运行；当前只有准备成果 |
| [gem5-official-repo-report.md](gem5-official-repo-report.md) | 2026-10-11 的官方仓库调研、源码阅读入口及建议依据 | 了解现有组件、下载理由和 SDMA 模型边界 |
| [notes/gem5-repository-map.md](notes/gem5-repository-map.md) | 六个本地工作树的用途、一二级目录职责与版本结构差异 | 查找课程、源码、文档和 workload 的阅读入口 |

项目上下文说明“为什么研究、范围是什么”；两份计划分别说明“先研究什么”与“怎样开展工作”；AGENTS 说明“怎样协作和判断完成”；进度记录说明“实际做到哪里”。版本与下载状态放上游登记，研究所得放工作笔记，实验结论放对应实验，避免在多个管理文件中反复维护同一事实。

## 目录组织

根文件、两份计划、四个上游仓库、Bootcamp 的固定版本子模块、研究笔记、实验方法和进度记录已经建立。E001 已有配置与实验说明，尚未运行。版本、校验和 Windows 兼容性例外统一见 [上游登记](upstream/README.md)；标为“按需建立”的部分在有实际内容时创建。既有仓库报告保留原路径，后续专题笔记进入 `notes/`。

```text
soc_model/
  AGENTS.md
  README.md
  project-context.md
  .gitignore
  gem5-official-repo-report.md
  plans/
    gem5-research-plan.md          gem5 整体认识的研究计划
    project-work-plan.md           面向项目目标的工作开展计划
  upstream/
    README.md
    gem5/                         官方主实验基线，保留原目录结构
    gem5-bootcamp-2024/            完整教学材料及教程固定版本子模块
    gem5-website/                  完整官方文档仓库
    gem5-resources/                完整 workload 源码仓库
  methods/
    experiment-workflow.md
  records/
    PROGRESS.md
    WORKING_NOTES.md               已有研究笔记，继续原位补充
  notes/                          概念、源码与架构专题笔记
    gem5-repository-map.md         六个工作树的用途和一、二级目录导读
  models/                         按需建立：本项目的可复用模型实现
  configs/                        按需建立：可复用的系统组成与连接
  experiments/                    按问题组织研究输入、配置和结论
    E001-injection-rate/           已准备，未运行
      README.md
      config.py
      evidence/<run-id>/          按需建立：支撑结论的选定证据
  patches/                        按需建立：需要重放的上游修改
  tools/                          按需建立：跨实验复用的辅助工具
  resources/                      按需建立：下载的 binary、kernel、disk image
  runs/<experiment-id>/<run-id>/  按需建立：一次运行的原始输出
  .local/
    backups/                      本地文档备份
    environment.md                本机路径、已核查环境与兼容性说明
    installed-software.md         软件安装与未来清理台账
    software-inventory/           带日期的软件包及 Windows 安装身份快照
    acquisition/                  实际获取日志、检查脚本与验证记录
```

`<run-id>` 是命名示意。WSL 中已产生独立的 `runs/environment-check/<run-id>/` 环境验收输出，实际位置与启动方法见 [本机环境](.local/environment.md)。E001 参数扫描仍未运行；环境检查不等于已实现自建模型或完成性能研究。

## 内容放在哪里

| 内容 | 负责位置 | 组织方式 |
| --- | --- | --- |
| gem5 研究范围与项目工作路线 | `plans/` 中的两份现行计划 | 各自修订，保留分工；实际进度与研究结果另行记录 |
| SimObject、EventQueue、Cache、DMA 等知识 | `notes/<topic>.md`，内容较多时使用 `notes/<topic>/` | 按问题组织，保留源码与资料定位；不照搬整个 `soc_study` 模块树 |
| 新增的 C++ 与 Python 模型 | `models/<model>/` | 以模型 README 说明接口、抽象、参数、限制和相关验证 |
| Board、System、Cache Hierarchy 等可复用组装 | `configs/` | 管连接与默认配置，不混入某次实验结果 |
| 特定问题的 workload、参数组合、运行和分析脚本 | `experiments/<experiment-id>/` | 围绕一个问题建立目录，README 维护方法与结论 |
| 原始 `stats.txt`、`config.ini`、日志、trace | `runs/<experiment-id>/<run-id>/` | 一次运行一个目录，包含实际命令和运行身份，默认不纳入 Git |
| 支撑正式结论的选定配置、统计与图表 | 对应实验的 `evidence/` 及正文 | 保留来源 run ID、必要元数据与校验信息，便于审阅和重现分析 |
| 第三方程序、磁盘镜像、checkpoint | `resources/` 或已登记的外部缓存 | 实验记录其 ID、版本、获取方式和校验值；大文件不重复纳入项目 |
| 跨实验重复使用的提取、运行或绘图功能 | `tools/` | 实际出现复用需求后提取，单次实验脚本先留在实验内 |
| 上游源码修改 | `patches/<repository>/` 或已登记的可访问开发分支 | 必须能从记录的基线重放；保留顺序和应用说明 |
| 本机绝对路径、临时副本、受限输入、旧稿备份 | `.local/` | 本地保留；受限输入的派生内容继续遵守原有范围 |

Linux/WSL 中的源码和运行输出可以放在 Linux 文件系统中的实际工作目录，避免为了目录外观强制放进 Windows 磁盘。逻辑职责仍按上表，实际位置记录在 `.local/environment.md`；上游登记和实验记录保留足够的定位信息。当前根目录为 `E:\codex\soc_model`。

## 官方源码与本项目怎样连接

采用两层结构：外层按研究问题组织，四个官方仓库内部保留其原有结构。主库的 `src/`、`ext/`、`configs/`、`tests/`、`build_opts/`、`build_tools/`、`site_scons/`、`SConstruct` 等不拆散，也不与本项目的同名目录合并。官方示例留在官方 `configs/`，本项目可复用配置放外层 `configs/`。

| 本项目内容 | 与 gem5 的连接方式 |
| --- | --- |
| 新增 C++ / SimObject 模型 | 外层 `models/` 中提供 `SConscript`，由官方构建入口通过 `EXTRAS` 纳入编译 |
| Python 配置和实验入口 | 直接交给 gem5 可执行文件执行；需要导入本项目模块时使用 `--path` |
| 编译产物 | 由官方构建系统在对应 checkout 的 `build/` 中生成；不同基线分别构建 |
| 仿真统计、配置与日志 | 使用 `--outdir` 指定本项目的独立运行目录 |
| 对官方已有模型的修改 | 保留基线，通过开发 commit 或可重放 patch 管理；`EXTRAS` 本身不替换已有实现 |

接入步骤和未执行的命令示例见 [实验工作方法](methods/experiment-workflow.md)。源码下载完成与构建、运行环境就绪分别记录。

## 如何新增内容

1. 先判断内容属于长期规则、项目方向、来源、专题知识、模型、实验还是实际进展，再进入负责位置。
2. 检查是否已有同一问题的文件。已有文件继续修订，新问题才建立新的专题或实验目录。
3. 新模型或实验建立自己的 README，并链接所依赖的源码、配置与来源；根入口只维护必要导航，不复制全部内部说明。
4. 新增笔记较多、确实需要导航时，再建立该目录的索引；需要自动化版本登记时，再迁移为一个可机器读取的登记文件，不并行手工维护两份版本表。
5. 当前决定发生改变时更新负责文件；旧报告保留日期和当时的结论。受影响的实验标明其旧基线，不通过改写历史结果制造一致性。

## 版本管理范围

本项目使用独立的外层 Git 仓库管理自有内容，通过 GitHub 同步。官方 gem5 源码、文档、教程和资源仓库继续作为本地依赖，由 [.gitignore](.gitignore) 排除。

| 内容 | 是否纳入本项目同步 | 范围说明 |
| --- | --- | --- |
| 项目约定、上下文、研究报告、计划、笔记和进度 | 是 | 包括根目录文档及 `methods/`、`notes/`、`plans/`、`records/` 中的项目文件 |
| 自建模型、系统配置、实验代码、小型自建输入与选定证据 | 是 | 包括 `experiments/`，以及实际建立后的 `models/`、`configs/`、`tools/`、`patches/`；尚未建立的目录不预建 |
| 上游来源与版本登记 | 是 | 保留本项目编写的 [upstream/README.md](upstream/README.md)，供其他机器按固定版本取得依赖 |
| 官方仓库及其内部 Git 历史 | 否 | 排除 `upstream/gem5/`、`upstream/gem5-bootcamp-2024/`、`upstream/gem5-website/`、`upstream/gem5-resources/`；课程中的两个子模块随父目录一起排除 |
| 下载资源、原始运行输出、构建产物、虚拟环境与缓存 | 否 | 延续现有忽略规则；实际引入资源时，允许同步 `resources/README.md` 登记文件；支撑结论的选定小型证据放对应实验的 `evidence/` |
| 本机记录、安装日志和旧稿备份 | 否 | `.local/` 继续仅在本地保留 |

除上述忽略范围外，新增项目文件默认可以纳入 Git；实际同步需要将文件加入版本管理、提交，并配置本项目的 GitHub 远端。上游仓库自己的 `origin` 不代表本项目的远端。外部文件的许可与来源项目的保护范围继续适用。

在其他机器取得本项目后，按 [上游登记](upstream/README.md) 单独获取官方依赖。官方源码路径的本地链接需要依赖到位后才能使用。已完成的 Git 配置、检查与远端同步状态见 [当前进度](records/PROGRESS.md)，不根据文件存在或忽略规则推断已上传。
