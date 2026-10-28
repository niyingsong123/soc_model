# 上游来源与版本登记

本文件唯一维护上游仓库的选取范围、使用版本、本地获取状态及后续使用入口。选择理由和源码阅读重点见 [仓库调研报告](../gem5-official-repo-report.md)，各工作树的用途和一、二级目录职责见 [仓库目录导读](../notes/gem5-repository-map.md)，项目工作进度见 [records/PROGRESS.md](../records/PROGRESS.md)。

## 当前登记

状态核查日期：2026-10-28；适用电脑：当前 Mac。`gem5-official/` 目前只有本登记文件，四个官方仓库与 Bootcamp 的两个子模块均未取得。当前电脑尚未安装 gem5 环境，也没有构建或运行验收结果。旧电脑上的源码副本、安装记录与二进制未随本仓库同步，其路径、文件量和验收结论已从本登记中移除。

已确认存放位置为项目根目录下的 `gem5-official/`，四个子目录继续沿用下表名称。计划在 2026-10-29 接续官方仓库下载，见 [下载任务记录](../records/PROGRESS.md#待办下载-gem5-官方仓库)。当前仅完成目录与登记文件迁移，实际源码尚未取得。

| 官方来源 | 已确认子目录（相对本目录） | 计划取得范围与用途 | 当前 Mac 获取状态 |
| --- | --- | --- | --- |
| [gem5/gem5](https://github.com/gem5/gem5) | `gem5/` | 全部源码、配置、测试、第三方依赖源码与构建文件；主实验底座 | 未获取 |
| [gem5bootcamp/2024](https://github.com/gem5bootcamp/2024) | `gem5-bootcamp-2024/` | 全部教学材料和父仓库固定的两个子模块 | 父仓库与子模块均未获取 |
| [gem5/website](https://github.com/gem5/website) | `gem5-website/` | 完整文档仓库，包括其版本化资源文件 | 未获取 |
| [gem5/gem5-resources](https://github.com/gem5/gem5-resources) | `gem5-resources/` | 完整 workload 源码、构建材料及仓库内版本化文件 | 未获取 |

## 固定版本

| 工作树 | 选定依据 | 目标 commit（不是本机 HEAD） |
| --- | --- | --- |
| `gem5` | Release `v25.1.0.1` | `c8222cc67a399bfc01e8658dd14b30d5bfd634f9` |
| `gem5-bootcamp-2024` | 获取计划核查时的 `main` | `3ea9b7e3598cd15e8c0ea688fa850249eab0fad5` |
| `gem5-website` | 获取计划核查时的 `stable` | `07ebfaf9bb1a0a4be2b822f3a4cf95abf20e4a4e` |
| `gem5-resources` | 获取计划核查时的 `stable` | `672d04917020934d452b2e767e97875c34693dee` |
| `gem5-bootcamp-2024/gem5` | Bootcamp 父仓库记录的 gitlink | `bb418d41eb6d87c0a0591869097005c16420c6aa` |
| `gem5-bootcamp-2024/gem5-resources` | Bootcamp 父仓库记录的 gitlink | `6734bb4940dd90f3b7c0349eedeefcf3ee405938` |

上述版本沿用项目已选定的基线；表中 commit 用于后续获取，不表示本机已有 checkout。取得后固定到对应 commit，并分别核对主库与 Bootcamp 子模块。Bootcamp README 描述其 v24 教学环境，实际依赖以父仓库的 gitlink 为准，不能用主实验基线替换教程版本。

计划采用 HTTPS 普通 clone 保留完整 Git 历史，不使用浅克隆或 partial clone。实际获取后再检查完整历史、工作树与文件内容，并登记本机取得范围和验证结果。`stable`、`develop` 等分支会移动，正式运行记录实际 commit。

## 后续获取与更新要求

每次实际获取或更新后，补齐来源 URL、tag/分支、解析后的 commit、获取日期、实际位置、取得范围与校验状态。使用 sparse checkout 时列明范围及原因；只有部分文件实际取得时，不标为完整获取。文件系统或平台兼容性例外须在实际电脑上重新核对，不沿用其他电脑的检出规则或验证结论。

核对 `HEAD`、工作树状态和关键构建文件；存在 submodule 或另需依赖时，记录其具体状态。Bootcamp 自带的 submodule 与主实验源码分别管理，不能因为源码已下载就声称教程的软件环境已经就绪。

更新基线时保留旧实验所引用的版本身份，并记录升级理由、兼容性影响和需要复查的实验。不能通过修改旧记录中的版本号代替重新运行。

## workload 与预编译资源

[gem5 Resources](https://resources.gem5.org/) 分发的 binary、kernel、disk image、checkpoint，与 `gem5-resources` 源码仓库分别登记。前者按具体实验需要取得，默认放 `resources/` 或已登记的外部缓存。

实验记录所用资源的 ID、版本、兼容性、获取方式和校验值；不根据源码仓库存在推断预编译资源已下载。缓存目录名称和本机绝对路径不能替代资源身份。

首次实际引入资源时再建立资源登记；如果同一资源被多个实验复用，建立一个共同登记入口，由实验引用，避免分别维护不同版本说明。

## 上游修改与保留范围

`gem5-official/` 下的实际副本默认由本项目 `.gitignore` 排除，登记文件保留。上游自身的 Git 历史、许可证和结构仍由其仓库管理。

本项目扩展优先放 `models/` 与 `configs/`。确需修改上游时，使用可定位的开发 commit，或在 `patches/<repository>/` 保留按顺序可应用的 patch 与基线说明；实验运行记录保存实际使用身份。只留在本地 checkout 的未记录修改不构成可重现的实验依赖。
