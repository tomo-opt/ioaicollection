# 收录与自动更新方法说明

更新时间：2026-06-19

## 一、免费主数据源和自动更新

1. UIA 公开档案：用 `https://uia.org/org_xml/<name>` 按英文名检索 profile，再读 profile 页中的 URL、Founded、Aims。
2. UN AI Resource Hub / UN for Good ：用“列表页定时抓取 + 详情页解析 + diff 检测”。
3. 其他国际组织 AI 页面：像 OECD、UNESCO、Council of Europe、ITU、WEF 这类官方公开页面，同样用 HTML 列表抓取或 RSS/JSON 增量拉取。
4. 免费技术栈：Python + urllib + lxml + pandas + GitHub Actions cron + csv/jsonl/sqlite。
5. 更新机制：定时拉取列表 -> 计算记录 hash -> 新增/变更项进 review queue -> 审核后再入前台。

## 二、`activities.php` 这类页面怎么进你的项目

不是直接 iframe，而是拆成你自己的 action 记录。
每条 action 至少存 `action_id`、`title`、`summary`、`source_org`、`source_program`、`action_type`、`theme`、`region`、`published_at`、`deadline`、`source_url`、`last_seen_at`。
前台上再把 action 挂到对应的组织卡片下。

## 三、如何避免“硬关键词过滤”的 bug

不把关键词当成裁决门槛，只把它当成召回手段。
先限定源域为已确认的国际组织及其项目页，再阅读标题、摘要、about 与发布主体来归类。
这个模式类似学术论文追踪项目：先从权威 source 增量拉取，再做记录层面的阅读式归类与人工复核。

## 四、Excel 里这批机构后续的项目作用

- 种子组织库：用来确定“谁是国际组织”。
- 行动挂载主体：后续抓到的 action 需要能回挂到这个组织库。
- 信任过滤层：只要行动发起方能映射回种子库，就比一般 AI 政策/产业新闻更可信。
- 前台导航层：可按组织类型、地域、是否政府间、是否标准/伦理/教育/研究导向分区。