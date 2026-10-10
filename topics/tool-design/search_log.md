# 检索与核验记录

检索截止：2026-10-04（Asia/Shanghai）。检索采用公开接口；检索结果是候选发现，不自动等同纳入证据。

本次合并去重后有 **2332 条候选题录**。主卡片 61 篇，A/B 为 45 篇设计、构造及其评估相关工作；C/D/E 为 16 篇邻近工作。53 篇取得了公开 HTML 或 PDF，8 篇仅核对题录与可获得摘要。未声称全部候选或全部收录文献已逐字阅读全文。

## 纳入与排除

- 纳入：物理工具创造或组装、任务/物体条件化工具和末端几何生成、形态/材料/机构优化、设计与控制联合优化、自动生产与验证。
- 分组：手持工具与专用抓手分别列出；普通机器人身体 co-design、工具选择/使用、认知玩具模型单独标注。
- 排除主体：LLM 软件/API 工具调用、刀具路径生成、手术工具分割/追踪、只有自动换工具机构而没有工具设计方法、一般人工机械结构介绍。
- 同文不同来源按规范化标题与 DOI/arXiv ID 合并；预印本和正式版保留在同一卡片。系列扩展论文保留，但标明重叠，不能将其当独立实验样本累加。

## 来源与核验层级

1. arXiv API 与 `/abs`：核对标题、作者、首次上传与版本、摘要、许可及会议备注。
2. arXiv HTML / 公开作者 PDF：定位方法、实验与限制，提取对应原文图。
3. Crossref DOI 记录：核对正式标题、作者、日期与刊载来源；当 arXiv 与正式记录有差异时分别保留。
4. OpenAlex：跨领域候选发现、摘要和公开全文位置。它是索引，不替代原始论文证据。
5. 核心论文参考文献回溯：HOT 的相关工作与参考文献引出 Tool Macgyvering、Autonomous Tool Construction、DiffHand、Task2Morph 等路线。

## 已确认的重要题录修正

- `Computational Design of Passive Grippers`：正式 ACM TOG / SIGGRAPH 2022，arXiv 2023；作者以正式记录的五人列表为准。arXiv 的作者元数据错误地将 Ian Good 与 Yu Lou 合并。
- `Tool Shape Optimization through Backpropagation of Neural Network`：IROS 2020，arXiv 2024。
- `Task2Morph`：IROS 2023，arXiv 2024。
- `Learning Tool Morphology ...`：ICRA 2023，arXiv 2022，正式 DOI 为 `10.1109/ICRA48891.2023.10161453`（大小写不影响解析）。
- `Computational Design of Customized Vacuum-Driven Soft Grippers`：正式卷期记录为 2025，DOI 内出现 2024 不能作为卷期年份。
- `A Mechanical Screwing Tool ...`：保留 arXiv 原标题；正式标题略有变化，按正式刊载记录显示 2022。

## 访问失败与检索边界

- 学术检索 MCP 在本会话不可用，按技能回退至公开 arXiv / Crossref / OpenAlex 接口。
- 首轮部分 Crossref 检索返回 HTTP 429；未持续快速重试，使用 OpenAlex 发现、arXiv 原文与精确 DOI 核验补足。
- 部分旧 arXiv HTML 图链接返回 406，使用公开 PDF / 作者仓库补图。
- 部分 IEEE / Elsevier / 作者仓库全文访问失败，9 篇保留摘要级解读与文字卡片。未绕过访问控制。
- Google 搜索页面仅返回需启用 JavaScript 的壳，本次不将其作为任何论文事实依据。
- 非主题宽泛 arXiv 检索有分页截断：`creation` 503 中取 250、`missing` 652 中取 250；不把它们称为完整检索。直接工具检索 195/195、抓手检索 253/253、2026 工具设计检索 86/86、机器人工具构造检索 31/31 则已取完。
- 截止日期指执行检索日。库索引延迟、受限数据库、非英语论文、未公开记录与长尾工业优化论文可能造成遗漏；不据此宣称“已经证明包含所有论文”。

## arXiv 检索式与返回数量

| 缓存批次 | 返回 / 总量 | 检索式 |
|---|---:|---|
| codesign | 8 / 8 | search_query=(ti:DiffuseBot OR ti:RoboGrammar OR ti:ToolGen OR ti:ToolMorph OR ti:ToolDreamer OR ti:graspforge OR ti:robocraft OR ti:AutoDex OR ti:SoftZoo OR ti:bodygen OR ti:physx-anything OR ti:physxanything) AND submittedDate:"199001010000 TO 202610042359"&id_list=&start=0&max_results=250 |
| construct-robot | 31 / 31 | search_query=( (ti:tool AND (ti:creation OR ti:construction OR ti:making OR ti:design) ) AND (all:robot OR all:robotic) ) AND submittedDate:"199001010000 TO 202610042359"&id_list=&start=0&max_results=250 |
| creation | 250 / 503 | search_query=( (ti:tool AND (ti:creation OR ti:construction OR ti:making OR ti:design) ) OR (ti:gripper AND (ti:computational OR ti:generative OR ti:automatic OR ti:automated OR ti:optimization OR ti:optimisation) ) ) AND submittedDate:"199001010000 TO 202610042359"&id_list=&start=0&max_results=250 |
| direct | 195 / 195 | search_query=(ti:tool AND (all:design OR all:generation OR all:morphology OR all:fabrication) AND (all:robot OR all:robotic OR all:embodied) ) AND submittedDate:"199001010000 TO 202610042359"&id_list=&start=0&max_results=250 |
| gripper-rest | 3 / 253 | search_query=( (ti:gripper OR ti:grippers OR ti:end-effector) AND (all:design OR all:generation OR all:optimization) ) AND submittedDate:"199001010000 TO 202610042359"&id_list=&start=250&max_results=100 |
| gripper | 250 / 253 | search_query=( (ti:gripper OR ti:grippers OR ti:end-effector) AND (all:design OR all:generation OR all:optimization) ) AND submittedDate:"199001010000 TO 202610042359"&id_list=&start=0&max_results=250 |
| missing | 250 / 652 | search_query=(ti:RoboGrammar OR ti:EvolutionGym OR ti:DiffTaichi OR ti:ChainQueen OR ti:ToolGen OR ti:TOG OR ti:PhysicsAnything OR ti:GenCAD OR ti:PhysX OR ti:ToolMaker OR ti:ToolWeaver OR ti:ToolForge OR ti:AutoTool OR ti:GripperGen OR ti:GenDex OR ti:DexGen OR ti:GraspForge OR ti:AutoDex OR ti:Robustness-Aware) AND submittedDate:"199001010000 TO 202610042359"&id_list=&start=0&max_results=250 |
| seeds | 14 / 14 | search_query=( (ti:contact-aware AND ti:design) OR (ti:tool AND ti:construction AND all:robot) OR (ti:Tool AND ti:MacGyvering) OR (ti:integrated AND ti:design AND ti:tactile) OR ti:RoboGrammar OR ti:EvolutionGym OR ti:DiffTaichi OR ti:ChainQueen OR (ti:Beyond AND ti:Representations AND all:grippers) ) AND submittedDate:"199001010000 TO 202610042359"&id_list=&start=0&max_results=100 |
| tool2026 | 86 / 86 | search_query=(all:tool AND (ti:design OR ti:creation OR ti:invention OR ti:synthesis OR ti:generation OR ti:morphology) AND (all:robot OR all:robotic OR all:embodied) ) AND submittedDate:"202601010000 TO 202610042359"&id_list=&start=0&max_results=250 |

## Crossref / OpenAlex 公开检索

| 来源 | 查询 | 返回候选数 |
|---|---|---:|
| crossref | [Computational Design of Passive Grippers](https://api.crossref.org/works?query.bibliographic=Computational+Design+of+Passive+Grippers&rows=20&filter=until-pub-date%3A2026-10-04) | 20 |
| crossref | [Designing Tools for Robotic Manipulation](https://api.crossref.org/works?query.bibliographic=Designing+Tools+for+Robotic+Manipulation&rows=20&filter=until-pub-date%3A2026-10-04) | 20 |
| crossref | [end effector automatic design](https://api.crossref.org/works?query.bibliographic=end+effector+automatic+design&rows=20&filter=until-pub-date%3A2026-10-04) | 20 |
| crossref | [Learning to Design and Use Tools](https://api.crossref.org/works?query.bibliographic=Learning+to+Design+and+Use+Tools&rows=20&filter=until-pub-date%3A2026-10-04) | 20 |
| crossref | [Learning Tool Morphology for Dynamic Manipulation](https://api.crossref.org/works?query.bibliographic=Learning+Tool+Morphology+for+Dynamic+Manipulation&rows=20&filter=until-pub-date%3A2026-10-04) | 20 |
| openalex | [An end-to-end differentiable framework for contact-aware robot design](https://api.openalex.org/works?search=An+end-to-end+differentiable+framework+for+contact-aware+robot+design&per-page=10&filter=to_publication_date%3A2026-10-04) | 10 |
| openalex | [An integrated design pipeline for tactile sensing robotic manipulators](https://api.openalex.org/works?search=An+integrated+design+pipeline+for+tactile+sensing+robotic+manipulators&per-page=10&filter=to_publication_date%3A2026-10-04) | 10 |
| openalex | [Automatic Design Customized Robotic Gripper Fingers Song](https://api.openalex.org/works?search=Automatic+Design+Customized+Robotic+Gripper+Fingers+Song&per-page=20&filter=to_publication_date%3A2026-10-04) | 20 |
| openalex | [Automatic Design of Compliant Grippers](https://api.openalex.org/works?search=Automatic+Design+of+Compliant+Grippers&per-page=20&filter=to_publication_date%3A2026-10-04) | 20 |
| openalex | [Automatic Design of Versatile Grippers](https://api.openalex.org/works?search=Automatic+Design+of+Versatile+Grippers&per-page=20&filter=to_publication_date%3A2026-10-04) | 20 |
| openalex | [automatic gripper design](https://api.openalex.org/works?search=automatic+gripper+design&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [Automatic Gripper Finger Design Production Application](https://api.openalex.org/works?search=Automatic+Gripper+Finger+Design+Production+Application&per-page=10&filter=to_publication_date%3A2026-10-04) | 10 |
| openalex | [automatic tool design robotics](https://api.openalex.org/works?search=automatic+tool+design+robotics&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [Autonomous tool construction using part shape and attachment prediction](https://api.openalex.org/works?search=Autonomous+tool+construction+using+part+shape+and+attachment+prediction&per-page=10&filter=to_publication_date%3A2026-10-04) | 10 |
| openalex | [autonomous tool design](https://api.openalex.org/works?search=autonomous+tool+design&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [Beyond Representations Flow-based Generative Design of Soft Grippers](https://api.openalex.org/works?search=Beyond+Representations+Flow-based+Generative+Design+of+Soft+Grippers&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [Beyond Representations Flow based Generative Design Soft Grippers](https://api.openalex.org/works?search=Beyond+Representations+Flow+based+Generative+Design+Soft+Grippers&per-page=10&filter=to_publication_date%3A2026-10-04) | 10 |
| openalex | [Computational Design of Customized Vacuum Driven Soft Grippers](https://api.openalex.org/works?search=Computational+Design+of+Customized+Vacuum+Driven+Soft+Grippers&per-page=10&filter=to_publication_date%3A2026-10-04) | 10 |
| openalex | [Computational Design of General-Purpose Grippers](https://api.openalex.org/works?search=Computational+Design+of+General-Purpose+Grippers&per-page=20&filter=to_publication_date%3A2026-10-04) | 20 |
| openalex | [Computational Design Robotic Grippers Caging](https://api.openalex.org/works?search=Computational+Design+Robotic+Grippers+Caging&per-page=20&filter=to_publication_date%3A2026-10-04) | 20 |
| openalex | [computational tool design robot](https://api.openalex.org/works?search=computational+tool+design+robot&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [Designing Tools with Control Confidence](https://api.openalex.org/works?search=Designing+Tools+with+Control+Confidence&per-page=10&filter=to_publication_date%3A2026-10-04) | 10 |
| openalex | [Diffusion robot design](https://api.openalex.org/works?search=Diffusion+robot+design&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [end effector automatic design](https://api.openalex.org/works?search=end+effector+automatic+design&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [Evolution of robotic tool](https://api.openalex.org/works?search=Evolution+of+robotic+tool&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [Feature Guided Search Creative Problem Solving Tool Construction](https://api.openalex.org/works?search=Feature+Guided+Search+Creative+Problem+Solving+Tool+Construction&per-page=20&filter=to_publication_date%3A2026-10-04) | 20 |
| openalex | [Finger design automation](https://api.openalex.org/works?search=Finger+design+automation&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [Fit2Form](https://api.openalex.org/works?search=Fit2Form&per-page=20&filter=to_publication_date%3A2026-10-04) | 20 |
| openalex | [functional 3D generation robot](https://api.openalex.org/works?search=functional+3D+generation+robot&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [Generative Robot Tool Design 2026](https://api.openalex.org/works?search=Generative+Robot+Tool+Design+2026&per-page=20&filter=to_publication_date%3A2026-10-04) | 20 |
| openalex | [gripper design large language models](https://api.openalex.org/works?search=gripper+design+large+language+models&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [gripper generative design](https://api.openalex.org/works?search=gripper+generative+design&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [Latent Diffeomorphic Co Design End Effectors](https://api.openalex.org/works?search=Latent+Diffeomorphic+Co+Design+End+Effectors&per-page=20&filter=to_publication_date%3A2026-10-04) | 20 |
| openalex | [Learning to Optimize Manipulation Tasks Using Tool Geometry](https://api.openalex.org/works?search=Learning+to+Optimize+Manipulation+Tasks+Using+Tool+Geometry&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [LLM tool design robot](https://api.openalex.org/works?search=LLM+tool+design+robot&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [passive gripper design](https://api.openalex.org/works?search=passive+gripper+design&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [physical tool invention robot](https://api.openalex.org/works?search=physical+tool+invention+robot&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [ReefFlex](https://api.openalex.org/works?search=ReefFlex&per-page=20&filter=to_publication_date%3A2026-10-04) | 1 |
| openalex | [RoboGrammar](https://api.openalex.org/works?search=RoboGrammar&per-page=10&filter=to_publication_date%3A2026-10-04) | 10 |
| openalex | [robot gripper computational design](https://api.openalex.org/works?search=robot+gripper+computational+design&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [robot gripper design diffusion model](https://api.openalex.org/works?search=robot+gripper+design+diffusion+model&per-page=20&filter=to_publication_date%3A2026-10-04) | 20 |
| openalex | [robot gripper design optimization](https://api.openalex.org/works?search=robot+gripper+design+optimization&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [robot gripper topology optimization](https://api.openalex.org/works?search=robot+gripper+topology+optimization&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [robot morphology co-design manipulation](https://api.openalex.org/works?search=robot+morphology+co-design+manipulation&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [robot tool construction assembly](https://api.openalex.org/works?search=robot+tool+construction+assembly&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [robot tool creation](https://api.openalex.org/works?search=robot+tool+creation&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [robot tool design 2026 HOT](https://api.openalex.org/works?search=robot+tool+design+2026+HOT&per-page=20&filter=to_publication_date%3A2026-10-04) | 20 |
| openalex | [robot tool design](https://api.openalex.org/works?search=robot+tool+design&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [robot tool fabrication](https://api.openalex.org/works?search=robot+tool+fabrication&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [robot tool generation](https://api.openalex.org/works?search=robot+tool+generation&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [robot tool synthesis](https://api.openalex.org/works?search=robot+tool+synthesis&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [Robot tool use A survey](https://api.openalex.org/works?search=Robot+tool+use+A+survey&per-page=10&filter=to_publication_date%3A2026-10-04) | 10 |
| openalex | [robotic gripper design survey](https://api.openalex.org/works?search=robotic+gripper+design+survey&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [Task and Context Sensitive Gripper Design Learning Using Dynamic Grasp Simulation](https://api.openalex.org/works?search=Task+and+Context+Sensitive+Gripper+Design+Learning+Using+Dynamic+Grasp+Simulation&per-page=10&filter=to_publication_date%3A2026-10-04) | 10 |
| openalex | [task oriented tool design](https://api.openalex.org/works?search=task+oriented+tool+design&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [task specific gripper design](https://api.openalex.org/works?search=task+specific+gripper+design&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [Task2Morph](https://api.openalex.org/works?search=Task2Morph&per-page=20&filter=to_publication_date%3A2026-10-04) | 5 |
| openalex | [Tool design reinforcement learning](https://api.openalex.org/works?search=Tool+design+reinforcement+learning&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [tool embodied design 2026](https://api.openalex.org/works?search=tool+embodied+design+2026&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [Tool Macgyvering Novel Framework Combining Tool Substitution Construction](https://api.openalex.org/works?search=Tool+Macgyvering+Novel+Framework+Combining+Tool+Substitution+Construction&per-page=20&filter=to_publication_date%3A2026-10-04) | 11 |
| openalex | [Tool MacGyvering Tool Construction Using Geometric Reasoning](https://api.openalex.org/works?search=Tool+MacGyvering+Tool+Construction+Using+Geometric+Reasoning&per-page=10&filter=to_publication_date%3A2026-10-04) | 10 |
| openalex | [tool morphology optimization](https://api.openalex.org/works?search=tool+morphology+optimization&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [tool robot co design](https://api.openalex.org/works?search=tool+robot+co+design&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [Tool shape optimization backpropagation neural network](https://api.openalex.org/works?search=Tool+shape+optimization+backpropagation+neural+network&per-page=10&filter=to_publication_date%3A2026-10-04) | 10 |
| openalex | [tool shape robot optimization](https://api.openalex.org/works?search=tool+shape+robot+optimization&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [ToolDreamer](https://api.openalex.org/works?search=ToolDreamer&per-page=35&filter=to_publication_date%3A2026-10-04) | 13 |
| openalex | [ToolGen manipulation](https://api.openalex.org/works?search=ToolGen+manipulation&per-page=30&filter=to_publication_date%3A2026-10-04) | 30 |
| openalex | [ToolGen](https://api.openalex.org/works?search=ToolGen&per-page=35&filter=to_publication_date%3A2026-10-04) | 35 |
| openalex | [ToolMorph](https://api.openalex.org/works?search=ToolMorph&per-page=35&filter=to_publication_date%3A2026-10-04) | 1 |

## 资源与图片核验

正文 Project/Code/Data 链接均来自原文或作者页面并检查访问。SoftZoo 的一个项目页入口返回 404，未列入正文；保留已确认的论文入口。每张本地图片与元数据中的论文、原图地址和图说明一一对应；9 篇无可靠配图不使用伪造占位图。

本仓库不附大量完整论文 PDF；通过 Paper/PDF 链接访问原文。图片与文字解读作为引用展示，元数据保留可获得的论文许可信息。

## 中文摘要译文补充

61 张卡片均增加完整中文 Abstract 译文，置于卡片内可展开区块。元数据保存 `abstract_en`、`abstract_zh`、`abstract_source` 与 `abstract_source_type`，支持原文核对。来源为 45 篇 arXiv、5 篇 Crossref 原始摘要、2 篇已与出版 PDF 摘要核对的记录，以及 9 篇 OpenAlex 索引摘要。索引摘要明确标注来源，不能冒充直接从出版社取得的原文。译文保留作者表述，不替代正文的事实、边界和推断。

## 全文翻译补充核验

2026-10-04 补获 #36 `Automatic simulation-based design and validation of robotic gripper fingers` 的 4 页正式 PDF（[Zenodo 7233391](https://zenodo.org/records/7233391)，文件 `1-s2.0-S0007850622001007-main.pdf`，CC BY 4.0），与 DOI/标题一致。公开全文取得数更新为 53，原文缩略图仍为 52 张。

全文译文与题录核验分开统计：25 篇有允许制作译文的来源并已生成自动双语草稿，36 篇仍需用户提供原稿或取得允许全文译文的来源。自动译稿尚未逐段人工校订；图内文字、参考文献题录保持原文，PDF 栏顺序及数学排版需要核对。

PMLR 正式版本补查：#7 [Liu et al., CoRL 2023 / PMLR 229:887–905](https://proceedings.mlr.press/v229/liu23b.html)（19 页），#23 [Ha et al., CoRL 2020 / PMLR 155:176–187](https://proceedings.mlr.press/v155/ha21b.html)（12 页，正文 PDF 已含附录），#56 [Tang et al., CoRL 2025 / PMLR 305:4473–4492](https://proceedings.mlr.press/v305/tang25a.html)（20 页）。[PMLR 出版协议](https://proceedings.mlr.press/pmlr-license-agreement.pdf)第 2 条采用 CC BY 4.0，第 3 条规定引用原出版论文和 PMLR 原文链接。因此新增译稿采用正式 PDF，未把该许可套用于 arXiv 预印本。

Fit2Form 页面 Supplementary PDF 链接返回的是另一篇 `Learning a Decentralized Multi-arm Motion Planner` 的 2 页文档，未纳入译稿。OpenReview API 的补查返回 403，未据此推定 DiffTaichi、BodyGen 等论文的许可。

修正 PDF 阅读顺序和附录识别：按正文块是否跨栏判断单栏 / 双栏，保留原始块 ID 并更新 reading_order；参考文献后 A/B 编号附录恢复为正文并补译。未识别的 PDF 排版字形以 � 和段落警示标明，提供整页原图核对，未猜测数学符号。
