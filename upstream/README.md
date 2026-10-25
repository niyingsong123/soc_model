# 上游来源与版本登记

本文件唯一维护上游仓库的选取范围、使用版本、本地获取状态及后续使用入口。选择理由和源码阅读重点见 [仓库调研报告](../gem5-official-repo-report.md)，各工作树的用途和一、二级目录职责见 [仓库目录导读](../notes/gem5-repository-map.md)，项目工作进度见 [records/PROGRESS.md](../records/PROGRESS.md)。

## 当前登记

获取登记日期：2026-10-11，首次完整性验证完成于北京时间 20:03:36；运行状态更新于 2026-10-20。四个 Windows 学习副本均位于 `E:\codex\soc_model\upstream\`，Bootcamp 中另有两个固定版本子模块。已取得完整 Git 历史与选定版本的全部文件；主库另有 Linux 独立完整 clone，已完成 X86 构建和官方示例验收。Windows 文件表示和检出规则的例外见下文。

| 官方来源 | 本地入口 | 取得范围与用途 | 本地状态 |
| --- | --- | --- | --- |
| [gem5/gem5](https://github.com/gem5/gem5) | [gem5/](gem5/) | 全部源码、配置、测试、第三方依赖源码与构建文件；主实验底座 | 版本、文件内容与 Git 对象完整性已核对；同基线 Linux 副本构建及环境验收通过 |
| [gem5bootcamp/2024](https://github.com/gem5bootcamp/2024) | [gem5-bootcamp-2024/](gem5-bootcamp-2024/) | 全部教学材料和父仓库固定的两个子模块 | 父仓库及子模块均已核对；本次未构建课程固定版本或运行练习 |
| [gem5/website](https://github.com/gem5/website) | [gem5-website/](gem5-website/) | 完整文档仓库，包括其版本化资源文件 | 已核对；未构建网站 |
| [gem5/gem5-resources](https://github.com/gem5/gem5-resources) | [gem5-resources/](gem5-resources/) | 完整 workload 源码、构建材料及仓库内版本化文件 | 已核对；未构建 workload 或额外下载外部镜像 |

## 固定版本

| 工作树 | 选定依据 | 实际 HEAD |
| --- | --- | --- |
| `gem5` | Release `v25.1.0.1` | `c8222cc67a399bfc01e8658dd14b30d5bfd634f9` |
| `gem5-bootcamp-2024` | 获取计划核查时的 `main` | `3ea9b7e3598cd15e8c0ea688fa850249eab0fad5` |
| `gem5-website` | 获取计划核查时的 `stable` | `07ebfaf9bb1a0a4be2b822f3a4cf95abf20e4a4e` |
| `gem5-resources` | 获取计划核查时的 `stable` | `672d04917020934d452b2e767e97875c34693dee` |
| `gem5-bootcamp-2024/gem5` | Bootcamp 父仓库记录的 gitlink | `bb418d41eb6d87c0a0591869097005c16420c6aa` |
| `gem5-bootcamp-2024/gem5-resources` | Bootcamp 父仓库记录的 gitlink | `6734bb4940dd90f3b7c0349eedeefcf3ee405938` |

全部工作树固定在上述 commit，采用 detached HEAD；未跟随分支自动更新。主 gem5 的 release tag 经远端查询与本地 HEAD 双重核对。Bootcamp README 描述其 v24 教学环境，但实际版本以父仓库的 gitlink 为准，不能用当前主实验基线替换教程依赖。

获取采用 HTTPS 普通 clone，未使用 `--depth` 或 partial clone，保留提交历史；六个仓库均确认 `--is-shallow-repository=false`，没有 partial-clone/promisor 配置。`stable`、`develop` 等分支名会移动，正式运行仍记录实际 commit。

## 实际文件量与验证

以下为验证完成时的文件长度合计，单位 MiB；不是网络传输量，也不是 NTFS 分配簇占用。Bootcamp 父仓库的工作树和 Git 数据均排除已单独列出的子模块，避免重复计算。

| 工作树 | 已校验文件数 | 工作树文件 MiB | Git 数据 MiB | 小计 MiB |
| --- | ---: | ---: | ---: | ---: |
| gem5 | 10,933 | 100.38 | 237.52 | 337.90 |
| gem5-resources | 21,584 | 248.01 | 54.72 | 302.73 |
| gem5-website | 930 | 145.80 | 123.34 | 269.14 |
| gem5-bootcamp-2024 | 948 | 185.61 | 402.44 | 588.05 |
| Bootcamp / gem5 | 10,436 | 95.76 | 237.43 | 333.19 |
| Bootcamp / gem5-resources | 21,660 | 263.64 | 54.52 | 318.16 |

合计 **66,491 个版本化文件**；工作树文件 `1,089,691,063` 字节，Git 数据 `1,163,883,169` 字节，两者合计 `2,253,574,232` 字节，约 **2.10 GiB**。不含本项目管理文档、获取日志和诊断目录。

本轮完成的检查：

- 六个 origin、HEAD、完整历史状态及 Bootcamp gitlink 与子模块实际 HEAD 相符。
- 对全部 66,491 个文件读取实际内容，按 Git blob 格式计算 SHA-1，与对应 commit 的 tree 条目逐一比较；内容及字节数均一致，工作树文件计数也相符。
- 六次 `git fsck --full` 均以退出码 0 完成。
- 检查普通 Git 状态并明确区分下述 Windows 预期差异；没有发现其他状态变化。

本机验证记录为 `.local/acquisition/20261011T194744+0800/verification.json`，脚本、各仓库 fsck 输出、初次失败日志及恢复说明保存在同目录。这些本机诊断文件默认不纳入项目 Git。检查证明下载内容完整，不证明 gem5 已构建、教程环境可运行或模型性能正确。

## Windows 学习副本的兼容性例外

所有正式仓库均使用局部 `core.autocrlf=false`、`core.longpaths=true`、`core.symlinks=false`。两个 resources 工作树各有 4 个符号链接，Bootcamp 根目录另有 `pyproject.toml` 链接；共 9 个链接在 Windows 中以保存原始链接目标的普通文件表示，Git 原始模式仍保留。

两个 resources 版本还各有一个尾点文件：

| 所属工作树 | 官方相对路径 |
| --- | --- |
| gem5-resources | `src/deprecated/parsec/disk-image/parsec/parsec-benchmark/pkgs/libs/mesa/src/mms-config.` |
| Bootcamp / gem5-resources | `src/parsec/disk-image/parsec/parsec-benchmark/pkgs/libs/mesa/src/mms-config.` |

普通 Git for Windows 拒绝这类文件名。仅关闭 NTFS 保护又会丢掉尾点，已通过独立小样验证，因此没有采用改名检出。实际处理为：各资源工作树只对这个路径设置 sparse 检出兼容例外，单次允许读取原始树，再经 Win32 扩展路径将原始 blob 写回原始文件名。**没有省略这两个文件；其 457 字节内容、blob 和磁盘中的尾点名称均已独立核对。** 正式仓库没有持久关闭 NTFS 保护，也没有使用 assume-unchanged 隐藏状态。

这两处文件仍会在普通 `git status` 中显示 ` M`，Bootcamp 父仓库也会报告 resources 子模块工作树变化。该状态不能直接解释成源文件内容修改；本轮逐文件校验已证明内容与固定 commit 一致。后续不得仅凭空白 Git 状态判断完整性，也不要强制 reset 或改名“修复”该差异。

2026-10-20 已在 Ubuntu 的 `/home/niyingsong/soc_model/upstream/gem5` 建立主库的独立完整 clone，从上表主 gem5 commit 正常检出，未复制 Windows 的 Git index、局部配置或 sparse 规则。Linux origin 指向官方仓库，`git fsck --full` 通过，构建及运行后工作树干净。

该 Linux 副本已用 `scons build/X86/gem5.opt --without-tcmalloc -j 4` 构建，实际二进制位于该 checkout 的 `build/X86/gem5.opt`；没有上游源码修改。官方 SE Hello World 和 HBM 流量示例均通过验收。选择该构建选项的对照、二进制校验值、WSL 与依赖版本、独立 run ID 和未验证范围统一见 [本机环境](../.local/environment.md)。上面的 66,491 文件计数是 10 月 11 日 Windows 获取记录，不包含新建 Linux 副本和编译产物。

## 后续获取与更新要求

每次实际获取或更新后，补齐来源 URL、tag/分支、解析后的 commit、获取日期、实际位置、取得范围与校验状态。使用 sparse checkout 时列明范围及原因；只有部分文件实际取得时，不标为完整获取。当前 Windows 例外也必须随更新重新核对，不照搬旧规则后直接宣布成功。

核对 `HEAD`、工作树状态和关键构建文件；存在 submodule 或另需依赖时，记录其具体状态。Bootcamp 自带的 submodule 与主实验源码分别管理，不能因为源码已下载就声称教程的软件环境已经就绪。

更新基线时保留旧实验所引用的版本身份，并记录升级理由、兼容性影响和需要复查的实验。不能通过修改旧记录中的版本号代替重新运行。

## workload 与预编译资源

[gem5 Resources](https://resources.gem5.org/) 分发的 binary、kernel、disk image、checkpoint，与 `gem5-resources` 源码仓库分别登记。前者按具体实验需要取得，默认放 `resources/` 或已登记的外部缓存。

实验记录所用资源的 ID、版本、兼容性、获取方式和校验值；不根据源码仓库存在推断预编译资源已下载。缓存目录名称和本机绝对路径不能替代资源身份。

首次实际引入资源时再建立资源登记；如果同一资源被多个实验复用，建立一个共同登记入口，由实验引用，避免分别维护不同版本说明。

## 上游修改与保留范围

`upstream/` 下的实际副本默认由本项目 `.gitignore` 排除，登记文件保留。上游自身的 Git 历史、许可证和结构仍由其仓库管理。

本项目扩展优先放 `models/` 与 `configs/`。确需修改上游时，使用可定位的开发 commit，或在 `patches/<repository>/` 保留按顺序可应用的 patch 与基线说明；实验运行记录保存实际使用身份。只留在本地 checkout 的未记录修改不构成可重现的实验依赖。
