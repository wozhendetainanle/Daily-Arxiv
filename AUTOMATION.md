# Automation Description

每日检索 arXiv 最近 24 小时的新论文，主题关注 LoRA/PEFT、机器学习和深度学习理论、optimizer/optimization、量子计算/tensor network、abstract visual reasoning、neural-symbolic/formal reasoning。分类优先覆盖 `cs.*`，尤其 `cs.LG`、`cs.AI`、`cs.CL`、`cs.CV`、`cs.NE`、`cs.DS`；高度相关的 `stat.ML`、`quant-ph`、`math-ph` 或其他分类可以纳入，但需要标注非 cs 分类并降低分类优先级。

筛选和排序先按主题相关性，再结合作者 affiliation/机构强弱。affiliation 优先从论文 PDF 首页、作者机构标注、项目页或可信学术页面推断；无法可靠确认时写“affiliation 未确认”，不要臆造。去重同一论文不同版本，主榜优先保留首次提交的新论文，重大更新可单独列出。

每期输出中文摘要并提交到 `daily/YYYY/YYYY-MM-DD.md`，同时更新 `README.md` 的 Archive。Top papers 默认入选 40 篇，最多 50 篇；如果当天高相关论文不足 40 篇，可以少于 40 篇，但需要在开头说明原因。必须包含检索窗口、关键词/分类、总命中数、入选篇数、Top papers 表格、“今日最值得细读的 5 篇”。逐篇要点不要单独列编号段落，直接统计到 Top papers 表格的“要点速览”列；该列用精简中文概括核心问题、主要方法、关键贡献、可能局限和关注理由。

低算力改进部分固定为“10 篇低算力可改进论文”。对每篇论文提出 3 个比较详细的方法级改进点，重点是对论文方法本身的改进，而不是泛泛复现或只换数据集。每个改进点应说明：具体改法、为什么低算力可行、一个可做的小实验或复现实验、预期收益与主要风险。明确区分事实信息与推断。
