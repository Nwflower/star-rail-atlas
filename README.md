# Star-Rail-Atlas
Star-Rail-Atlas是一个主要由[`米游社@听语惊花`](https://bbs.mihoyo.com/ys/accountCenter/postList?id=289918413)（而不是西风驿站）制作的星穹铁道(StarRail)游戏图鉴。

【注意】本仓库内不会上线在正式服与创作体验服未实装的内容。

目前部分图片由@玖喵（QQ：2014340648）在维护，感谢各位共创者的大力支持。

## 目录结构
- [x] 角色图鉴（更新至2.7）
- [x] 角色攻略（更新至2.3）
- [x] 光锥图鉴（更新至3.5）
- [x] 遗器图鉴（更新至3.5）
- [ ] 奇物图鉴、祝福图鉴（可能不做了）

注意：请使用根目录下的path.json来获取准确的完整目录。

### 如何部署

本仓库仅为图片仓库，并非代码仓库。

您可以通过以下项目直接使用本仓库的资源。

| Bot(plugin)         | language | link                                                         |
| ------------------- | -------- | ------------------------------------------------------------ |
| Yunzai-Bot（Atlas） | Node.js  | [Atlas](https://github.com/Nwflower/atlas)                   |
| LittlePaimon        | python   | [LittlePaimon](https://github.com/CMHopeSunshine/LittlePaimon) |
| StarRailUID         | python   | [StarRailUID](https://github.com/qwerdvd/StarRailUID)        |
| March7th            | python   | [Mar-7th](https://github.com/Mar-7th/March7th)               |

以上项目仅为目前已知的引用本仓库的部分仓库，不代表本仓库认同、支持他们的立场或观点，上网冲浪，谨防受骗、上当。

请注意，本仓库的开源协议为AGPL-3.0，使用本仓库时，请开源您的项目源码。

### 如何维护

由于本人目前在三次元中因为不可抗力暂时无法及时更新，如果你想要自己更新图片，请按照以下方式更新：

#### 增设角色攻略

1. 将图片拷贝到路径`Atlas\star-rail-atlas\guide for role`中后（可以命名为角色名）
2. 在`Atlas\star-rail-atlas\othername\guide for role.yaml`中配置好角色别名
3. 在Python环境下运行`Atlas\star-rail-atlas\.github\update_index.py`脚本。如你的系统中未配置Python环境/不想配置Python环境，可以在Github（Gitee不行）上fork本仓库后，将修改后的仓库上传到你fork的私库中，Github工作流将会自动运行上述脚本。
4. （本段文字仅需阅读）该脚本会遍历`star-rail-atlas`的所有文件并生成文件索引`Atlas\star-rail-atlas\path.json`，Atlas插件不会回复不在该索引内的文件。注意如果你使用的是Github工作流，你应该在工作流跑完之后再将仓库pull到本地以同步变更。当然，如果修改的文件较少，你也可以手动更改索引文件`Atlas\star-rail-atlas\path.json`而不是运行自动脚本。

#### 增设其他图片

原理同上，复制到其他文件夹即可。

## 支持

如果你支持本项目，可以给个star或者[爱发电](https://afdian.net/a/Nwflower)，你的支持不会获得额外内容，但会提高本项目的更新积极性

本图鉴目前仅供学习交流使用，素材版权为米哈游所有。

您不应以任何形式使用本仓库进行盈利性活动，否则，我将立即停止所有图鉴制作并关闭图鉴的开源状态，不再提供更新支持。