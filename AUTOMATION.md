# Automation Description

每日检索 arXiv 最近 24 小时的新论文，生成中文订阅摘要，并按日期归档到本仓库。

## Scope

主题重点：

- HOI / Human-Object Interaction
- Affordance / actionable affordance / human-object affordance / object affordance / manipulation affordance
- 灵巧手 / dexterous hand / dexterous manipulation / robotic hand / in-hand manipulation
- 3D / 3D vision / 3D reconstruction / 3D understanding
- 具身智能 / embodied AI / embodied agents / robotics / VLA
- Agent / LLM agent / multimodal agent / autonomous agent / tool-use agent

分类优先覆盖 `cs.*`，尤其 `cs.CV`、`cs.AI`、`cs.RO`、`cs.LG`、`cs.CL`、`cs.NE`、`cs.HC`、`cs.GR`。高度相关的 `stat.ML`、`eess.IV`、`eess.SY`、`math.OC` 或其他非 cs 分类可以纳入，但必须标注非 cs 分类，并在排序时降低分类优先级。

检索时不要只依赖精确短语；需要覆盖同义词、缩写和相关表达，例如 `HOI detection`、`human-object affordance`、`actionable affordance`、`visual affordance`、`object affordance`、`functional affordance`、`grasp affordance`、`manipulation affordance`、`contact-rich affordance`、`dexterous hand`、`robotic hand`、`anthropomorphic hand`、`multi-finger hand`、`multi-fingered manipulation`、`in-hand manipulation`、`dexterous grasping`、`hand-object interaction`、`hand-object reconstruction`、`hand pose estimation`、`tactile manipulation`、`bimanual manipulation`、`Allegro Hand`、`Shadow Hand`、`LEAP Hand`、`3D scene understanding`、`robot manipulation`、`vision-language-action`、`VLA`、`world model`、`spatial reasoning`、`navigation`、`task planning`。

## Retrieval And Ranking

只把 arXiv `New submissions` 作为主榜来源；`Replacement submissions` 不进入主榜，除非是重大更新，并在末尾单独列出。需要去重同一论文不同版本，主榜优先保留首次提交的新论文。

排序先按与 HOI、Affordance、灵巧手/灵巧操作、3D、具身智能、Agent 六类主题及其交叉方向的相关性，再结合作者 affiliation/机构强弱。Affordance 和灵巧手是独立高优先主题，不只是 HOI 或 robotics 的附属关键词。

交叉优先级大致为：Affordance × dexterous hand/robot manipulation、3D HOI/3D hand-object interaction、dexterous manipulation × tactile/vision-language-action、affordance-guided embodied manipulation、3D world model/agent × robot manipulation、通用 Agent 或通用 3D 论文。对纯泛化的 “affordance” 社会科学/经济学/语言学用法、非视觉/非机器人/非交互意义的 hand/agent 论文要降权或排除。

affiliation 优先从论文 PDF 首页、作者机构标注、项目页或可信学术页面推断；无法可靠确认时写“affiliation 未确认”，不要臆造。

## Output Format

每期输出到 `daily/YYYY/YYYY-MM-DD.md`，并同步更新 `README.md` 的 Archive。完成后提交并推送到 `wozhendetainanle/Daily-Arxiv`。

开头必须包含：

- 检索时间窗口
- 检索关键词/分类
- 总命中数和入选篇数
- 对 cross-list、replacement、非 cs 分类的处理说明

Top papers 默认入选 40 篇，最多 50 篇；如果当天高相关论文不足 40 篇，可以少于 40 篇，但必须在开头说明原因。

Top papers 表格列固定为：

| 排名 | 标题 | arXiv 链接 | 分类 | 作者 | 推断 affiliation | 相关性分数 | 机构强度分数 | 推荐阅读优先级 |
|---:|---|---|---|---|---|---:|---:|---|

每篇论文后用 3-5 条中文要点覆盖：核心问题、主要方法、关键贡献、可能局限、为什么值得关注。明确区分事实信息与推断。

Top papers 后必须单独列出“今日最值得细读的 5 篇”。

## Low-Compute Improvement Section

低算力改进部分固定为“10 篇低算力可改进论文”。从当日论文中选 10 篇最适合低算力延展的论文，优先选择 Affordance、灵巧手/灵巧操作、3D HOI、VLA manipulation、tactile manipulation、hand-object reconstruction 相关论文。

对每篇论文提出 3 个比较详细的方法级改进点。重点是改论文方法本身，不是泛泛复现、只换数据集、只调参或只做更多 baseline。

每个改进点必须包含：

- 具体方法改法
- 为什么低算力可行
- 一个可执行的小实验或复现实验
- 预期收益
- 主要风险

事实信息和推断必须明确区分；来源链接必须可点击。
