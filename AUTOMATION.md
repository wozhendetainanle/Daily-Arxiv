# Automation Description

每天检索 arXiv 官方 `New submissions`，生成带三列 Markdown 卡片的中文日报。以 **3D 与物理交叉** 为核心，同时收录有实质机器人任务、方法或实验的 **具身智能** 工作。

## Scope and ranking

优先检索 `cs.CV`、`cs.GR`、`cs.RO`、`cs.AI`、`cs.LG`，补充高度相关的 `physics.*`、`cond-mat.*`、`eess.*`、`math.*` 等分类；非 cs 论文标明原分类，不因分类本身排除高相关论文。按标题与摘要核实研究对象，不能只凭关键词命中。

从高到低优先考虑：

1. 3D 表示、重建、生成或理解与物理动力学、力、接触、碰撞、形变、材料、流体、刚体/软体运动的交叉；
2. 3D 物理世界模型、物理一致的 4D 场景、动态 Gaussian/NeRF/mesh/point cloud、可微仿真、inverse graphics 与物理参数估计；
3. 3D 场景中的机器人操作与具身交互，包括抓取、手物接触、触觉、sim-to-real 和物理规划；
4. 有具体机器人任务与方法贡献的具身工作，包括 VLA/机器人策略、模仿学习、灵巧操作、移动导航、动作世界模型、具身感知与具身评测；即使摘要未明确提出 3D/物理新方法，也可在 3D/物理交叉论文之后入选；
5. 有明确三维贡献的基础 3D vision、graphics、reconstruction、generation、spatial reasoning 方法。

纯泛化 Agent/LLM、只有具身标签而缺少机器人任务、方法或实验证据的论文降权或排除。HOI、affordance 和灵巧手若有明确三维几何、接触或物理机制则优先；其他具有具体具身贡献的工作也可入选。每期最多 **100 篇、100 张对应卡片**；符合范围的论文不足时少收，不用宽泛论文凑数。

主榜只收官方 `New submissions`。同一 arXiv ID 去重；重大 Replacement 可在末尾单列。机构信息优先核对 PDF 首页、项目页和可信学术页面；无法确认则写“affiliation 未确认”。明确区分 arXiv/论文事实与相关性、局限、改进建议等推断。

## Outputs

1. 写入 `daily/YYYY/YYYY-MM-DD.md`，更新 `README.md` 的 Archive。日报说明官方批次日期、检索窗口、分类、总命中数和入选数。Top papers 表格最多 100 篇，包含标题、arXiv 链接、分类、作者、机构、相关性和阅读优先级；每篇有 3–5 条中文要点。另列 Top 5 和最多 10 篇适合低算力改进的论文。如果没有新官方批次，写明原因，不重复旧论文。
2. 为卡片补充 `data/enrichment.json`，以 arXiv ID 为键。每篇新入选论文必须保存 `abstract_en`（原始 Abstract）、`abstract_zh`（完整中文译文）、`abstract_source`（原摘要来源 URL）。以官方 arXiv/出版页面或 PDF 的原始摘要为依据忠实翻译，保留数字、缩写、引用标记、任务条件和结论强度；不可用中文要点代替摘要，不把解读或全文结论补写成摘要。如果原摘要确实无法取得，明确标注“原摘要暂未取得”并报告缺摘要篇数，不编造。其他可选字段：`venue`、`code`、`project`、`video`、`data`、`image`、`image_source`。`venue` 仅在会议/期刊官方或论文明确写出时填写；否则卡片显示 arXiv 日期和分类。资源链接必须逐一打开核实，不能猜测。
3. 为每篇入选论文尽量保存真实配图到 `assets/papers/YYYY-MM-DD/<arxiv-id>.webp`，并填写相对 `image` 路径及 `image_source` 原始论文/项目页 URL。使用工作区依赖提供的 Python（Pillow、pypdf），运行 `scripts/fetch_figures.py --date YYYY-MM-DD` 可从 arXiv HTML 的论文图自动取图，缺图时尝试官方 PDF；如果只有矢量图，可人工从官方 PDF 裁出图并记录 PDF URL。逐张核对缩略图属于对应论文，不能用无关素材、截图示例或未经核实的热链。确实无图时才显示明确标注的占位图，并在日报/结果中报告缺图篇数。
4. 运行 `python3 scripts/build_cards.py`。脚本在每日 `.md` 的标题后嵌入三列 GitHub Markdown 卡片表格，包含真实缩略图、venue/arXiv 标签、标题、作者、**机构**及已核实的 Paper/Code/Project/Video/Data 链接，并在**每张卡片内**用可展开的“中文摘要”区块显示完整 Abstract 译文和原摘要来源；机构未可靠确认时写“affiliation 未确认”。它保留原有检索概况、表格和分析。检查当天卡片数与 Top papers 表格相同，中文摘要区块数等于卡片数，逐卡核对译文与原摘要对应，图片没有错配或破图；历史未补译文的卡片明确标注待补，不能假称已翻译。不使用独立 HTML 页面或 GitHub Pages。
5. 只提交本轮的日报、README 索引、必要的 enrichment/配图；按现有仓库流程推送。记录 commit SHA 和 push 成败。不要改写已发布日报的筛选内容来迎合新主题。

## Low-compute section

从当日高相关论文中选最多 10 篇真正适合低算力延展的论文，优先 3D 物理建模、物理一致重建、接触/动力学估计、可微仿真和 3D 机器人交互。每篇提出具体方法改法、一个可执行的小实验、低算力原因、预期收益和风险。若不足 10 篇，说明原因。不要把复现、换数据集或调参冒充方法创新。
