# Automation Description

每日检索 arXiv 最近 24 小时的新论文，生成中文订阅摘要，并按日期归档到本仓库。

## Scope

主题重点：

- LoRA / PEFT / low-rank adaptation
- 机器学习与深度学习理论
- optimizer / optimization / learning dynamics
- 量子计算 / tensor network
- abstract visual reasoning
- neural-symbolic / formal reasoning

分类优先覆盖 `cs.*`，尤其 `cs.LG`、`cs.AI`、`cs.CL`、`cs.CV`、`cs.NE`、`cs.DS`。高度相关的 `stat.ML`、`quant-ph`、`math-ph` 或其他分类可以纳入，但必须标注非 cs 分类，并在排序时降低分类优先级。

## Retrieval And Ranking

只把 arXiv `New submissions` 作为主榜来源；`Replacement submissions` 不进入主榜，除非是重大更新，并在末尾单独列出。需要去重同一论文不同版本，主榜优先保留首次提交的新论文。

排序先按主题相关性，再结合作者 affiliation/机构强弱。affiliation 优先从论文 PDF 首页、作者机构标注、项目页或可信学术页面推断；无法可靠确认时写“affiliation 未确认”，不要臆造。

## Output Format

每期输出到 `daily/YYYY/YYYY-MM-DD.md`，并同步更新 `README.md` 的 Archive。完成后提交并推送到 `wozhendetainanle/Daily-Arxiv`。

开头必须包含：

- 检索时间窗口
- 检索关键词/分类
- 总命中数和入选篇数
- 对 cross-list、replacement、非 cs 分类的处理说明

Top papers 默认入选 40 篇，最多 50 篇；如果当天高相关论文不足 40 篇，可以少于 40 篇，但必须在开头说明原因。

Top papers 表格列固定为：

| 排名 | 论文 | 分类 | 作者 | 推断 affiliation | 相关性 | 机构强度 | 优先级 | 要点速览 |
|---:|---|---|---|---|---:|---:|---|---|

逐篇要点不要单独列编号段落，直接统计到 Top papers 表格的“要点速览”列。该列用精简中文覆盖：核心问题、主要方法、关键贡献、可能局限、为什么值得关注。明确区分事实信息与推断。

Top papers 后必须单独列出“今日最值得细读的 5 篇”。

## Low-Compute Improvement Section

低算力改进部分固定为“10 篇低算力可改进论文”。从当日论文中选 10 篇最适合低算力延展的论文。

对每篇论文提出 3 个比较详细的方法级改进点。重点是改论文方法本身，不是泛泛复现、只换数据集、只调参或只做更多 baseline。

每个改进点必须包含：

- 具体方法改法
- 为什么低算力可行
- 一个可执行的小实验或复现实验
- 预期收益
- 主要风险

事实信息和推断必须明确区分；来源链接必须可点击。
