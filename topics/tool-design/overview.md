# 文献调研综述与检索边界

[专题卡片](../tool-design.md) · [原项目方向](https://github.com/wozhendetainanle/ToolAutoDesign/blob/0a906a74a160082be7a3a291c7ab73b3c213c0a3/docs/project_direction.md)


## 从文献中看，哪些问题仍值得做

以下是研究判断，不是这些论文已经证明的结论。

| 方向 | 已有工作给出的起点 | 需要独立验证的问题 |
|---|---|---|
| 结构、形状、动作共同搜索 | HOT、DiffHand、RobotSmith | 同物理评估预算下，结构变化是否优于只调整形状；制造后能否复现仿真动作 |
| 机器人条件化工具生成 | 被动抓手、Fit2Form、robot-aware passive pipeline | 同一功能换机器人、夹爪、接近方向后，设计是否仍可抓、可到达、可用 |
| 材料与扰动鲁棒性 | 粉末称量 co-design、Control Confidence、ReefFlex | 未见摩擦、刚度、颗粒流动性与位姿扰动下的失效率，而非单个 nominal 分数 |
| 候选评价的成本与可信度 | Neural Physics、Fin-QD、高保真物理筛选 | 同一预算下 surrogate 选中的最优候选是否被真实物理复评推翻 |
| 真实制造闭环 | PaperBot、in-materio evolution、自动指尖生产 | 从任务输入到制造、安装和任务完成的总时间、试制次数与失败成本 |
| 设计与执行解耦 | ToolGen、FUNCTO、MimicFunc、SimToolReal | 新工具收益来自形态还是更强控制；需固定执行器或做成对对照 |

## 已找到但尚未充分核验的扩展题录

下列条目保留检索线索，未作为上方 61 篇完整解读卡片计数。后续取得可靠原文后再补方法与实验，不根据标题猜测实现。

| 题录 / 资源 | 当前状态 |
|---|---|
| [Finger design automation for industrial robot grippers: A review](https://doi.org/10.1016/j.robot.2016.10.003) | 2016 综述；本次未读取全文 |
| [Fast finger design automation for industrial robots](https://doi.org/10.1016/j.robot.2018.12.011) | 2019 题录；摘要 / 全文未充分核验 |
| [Automatic design algorithm of a robotic end-effector for a set of sheet-metal parts](https://doi.org/10.1109/iccis.2015.7274590) | 2015；已发现工业对象族适配线索，未读取全文 |
| [Topology-shape-size optimization design synthesis of compliant grippers for robotics: A comprehensive review and prospective advances](https://doi.org/10.1016/j.robot.2025.105106) | 2025 综述；未读取全文 |
| [Design and development of a soft gripper with topology optimization](https://doi.org/10.1109/iros.2017.8206527) | 2017；需补全文与设计变量核验 |
| [Efficient automatic design of robots](https://doi.org/10.1073/pnas.2305180120) | 2023；机器人整体设计扩展阅读，非工具专项结果 |
| [Beyond Representations: Flow-based Generative Design of Soft Grippers 的数据与 checkpoints](https://doi.org/10.25919/j8yy-c617) | 已发现数据记录；不能据数据记录补造论文题录或宣称已读论文 |

## 检索范围与复用说明

检索使用 arXiv、Crossref 和 OpenAlex 公共接口，并从 HOT 等核心论文的参考文献追溯工具部件构造、可微设计和早期自动指形设计。检索式、筛选边界、去重方法与访问失败见 [search_log.md](search_log.md)。

图片属于各自论文作者 / 出版方，本仓库以研究文献解读的引用配图方式展示，并逐图保留来源；相关许可可在 [metadata.json](metadata.json) 的 `license_url` 字段或原论文页查看。BibTeX 使用已核对题录；缺少正式刊载记录的文章保留预印本标识。

## 阅读说明与完整导航

本页沿用每日 arXiv 任务的三列论文卡片。点击标题进入论文，点击「解读」跳到逐篇中文要点。重点是机器人如何设计、生成、制造或优化能够完成物理任务的工具；也收录任务专用抓手、设计与控制联合优化，以及必要的邻近工作。

这里的 tool 指物理工具。软件/API 工具调用论文不纳入主体；只使用、选择现成工具的工作放在 D 类。A/B 类共 45 篇，但包括设计工具链、专用结构优化和评估模型，**并非全部都是完全自主、开放世界的工具生成系统**。

这是截至检索日公开可核对文献的系统整理，不把检索结果视作“已证明无遗漏”。数据库未索引、没有公开全文的工作和大量工业抓手优化算法论文仍可能存在；已找到但尚未充分核验的题录另列在末尾。

年份优先采用出版社/Crossref 的正式记录；缺少正式记录时采用 arXiv 首次上传年份，并写明预印本或已确认的会议备注。**首次上传、版本更新、会议举办和论文集出版不是同一个日期**。文中数字为论文报告，未在本仓库复现实验；不同协议的成功率不直接互比。

配图来自相应论文 HTML 或公开 PDF；少数以论文首页作预览，卡片注明图源。9 篇暂未取得可靠配图，保留文字卡片，不以装饰图替代。作者机构仅依据明确机构栏或 PDF 首页；无法确认时写 `affiliation 未确认`。
