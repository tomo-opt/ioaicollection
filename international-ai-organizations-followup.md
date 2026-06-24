# 国际组织 AI 项目补充说明

更新时间：2026-06-19

对应文件：
- 既有调研：[international-ai-organizations-research.md](C:\Users\14916\Desktop\ioaicollection\international-ai-organizations-research.md)
- 组织样本表：[AI领域的国际组织.xlsx](C:\Users\14916\Desktop\ioaicollection\AI领域的国际组织.xlsx)
- 页面示意图：[site-structure-diagram.md](C:\Users\14916\Desktop\ioaicollection\site-structure-diagram.md)

---

## 一、首批来源应该怎么接入

原则不是“整站照收”，而是“按对象类型接入”。你的项目只应接入三类对象：
- 国际组织本体 `organization`
- 由国际组织正式发起、发布、实施或承办的 AI 行动 `action`
- 由国际组织产出的框架、标准、指南、方法、工具 `instrument`

### 1. 核心主数据源
这些来源可以直接产出正式条目：
- UN AI Resource Hub：适合接 `UN entities`、`activities`、国家覆盖范围、SDG 等字段。
- UNESCO AI Ethics / Global Hub：适合接 UNESCO 自身的 recommendation、RAM、toolkit、country engagement。
- OECD.AI Policy Navigator：只接 `International initiatives`，不接 `National initiatives`。
- EU AI Office / AI literacy repository：只接欧盟机构本身的治理动作和官方仓库，不把成员国实践当作核心主条目。
- Council of Europe AI pages：主要接 `instrument`，如 convention、HUDERIA。
- ASEAN AI governance pages：接 regional guide、working group、regional coordination。
- AI Standards Exchange：接 standards body、standard、capacity building，不接企业宣传材料。

### 2. 辅助发现源
这些来源适合发现候选条目，但不应直接作为正式证据源：
- Digital Watch
- IGF PNAI
- African Observatory / Africa AI Policy Tool
- Carnegie Africa tracker
- IAPP AI tracker

使用方式是：先在这些站里发现候选条目，再回到官方原始页面核验，确认后再入库。

### 3. 开源参考源
这些来源更适合参考数据结构和补漏：
- Fairly regulation tracker
- MAIR
- aiPolicyResources
- awesome-artificial-intelligence-regulation

它们不应直接作为你的正式收录依据。

---

## 二、怎么保证收进来的真的是“国际组织 AI 行动”

建议设置四道过滤门槛。

### 1. 组织门槛
每条 action 必须绑定至少一个核心国际组织主体。没有主体，不入核心库。

### 2. 证据门槛
每条记录至少保留一个官方来源链接，优先保留以下域名：
- `.int`
- `.org`
- `europa.eu`
- `coe.int`
- `oecd.ai`
- `unesco.org`
- `itu.int`
- `asean.org`

只有媒体报道、二手数据库、博客转载而没有官方原始链接的，不进正式库。

### 3. 动作门槛
只有以下内容进入核心 `action`：
- 发布 framework / recommendation / convention / standard
- 发起 programme / project / initiative
- 建立 observatory / repository / expert network
- 组织 summit / forum / consultation
- 发布 methodology / toolkit / assessment

以下内容不进入核心 `action`：
- 纯评论文章
- 泛泛提到 AI 的新闻
- 没有国际组织动作的国家政策列表

### 4. 归属门槛
如果一条内容主要归属于国家部委、地方政府、企业、园区或行业协会，而不是国际组织，就不要作为核心条目收录。最多可以作为相关背景链接保留。

---

## 三、我读完 Excel 之后的判断

文件 [AI领域的国际组织.xlsx](C:\Users\14916\Desktop\ioaicollection\AI领域的国际组织.xlsx) 目前的有效内容都在 `Sheet1`。

我读到的关键信息：
- `Sheet1` 共 127 条记录。
- `Sheet2` 和 `Sheet3` 为空。
- 现有字段包括：`Name`、`Acronym`、`Founded`、`City HQ`、`Country/Territory HQ`、`Type I`、`Type II`、`UIA Org ID`。
- 这不是“纯国际组织目录”，而是一个按 AI 关键词检索出来的“国际组织样本池”。

这个样本池里混有多种对象：
- 真正可作为前台主对象的国际合作机制或国际治理主体，如 `GPAI`、`IRCAI`。
- 国际学会、专业协会、研究网络，如 `EurAI`、`AAAI`、`IAAIL`。
- 会议系列和活动品牌，如 `PRICAI`、`AISTATS`、`AJCAI`。
- 工具或规范性对象，如 `Council of Europe Framework Convention on AI`，它更像 `instrument`，不应直接当作 `organization`。

所以这个 Excel 不能直接当作你网站的前台目录，而应该先清洗分层。

---

## 四、这些组织在项目里可以起什么作用

### 1. 作为组织种子库
它最直接的作用，是给你提供一批待清洗的组织样本。你可以从中先拿到：
- 标准名称
- 缩写
- 成立年份
- 总部地点
- UIA ID

然后再补：
- official URL
- 组织类型
- 是否属于前台核心主体
- 是否属于国际组织核心范围
- 主要 AI 角色

### 2. 作为边界测试集
这个表非常适合帮你决定“什么收、什么不收”。

你需要尽快回答这些问题：
- conference series 算不算组织？
- academic society 算不算核心国际组织主体？
- research center 算不算？
- advocacy campaign 算不算？
- convention 算 organization 还是 instrument？

### 3. 作为分层样本
建议先把 127 条粗分成四层：
- `org_core`：核心国际组织或国际治理主体，前台重点展示。
- `org_ecosystem`：国际学会、协会、研究网络，可展示但不放首页主舞台。
- `event_or_series`：会议、竞赛、活动品牌，挂到 action / event 层，不作为组织主对象。
- `exclude_or_reference_only`：国际性弱、组织性不足、与 AI 行动关联弱的条目。

### 4. 作为 watchlist
后面做自动监测时，这个表很适合变成监测名单：
- 给核心组织补官网
- 给官网补新闻页、publication 页、resource 页
- 定期扫描是否出现新的 AI action

这比全网盲抓稳定得多。

---

## 五、我建议你怎么清洗这个 Excel

建议新增这些字段：
- `official_url`
- `entity_class`
- `is_core_for_frontend`
- `is_international_org_core`
- `suggested_project_role`
- `notes`

建议先做这四类标注：
- `org_core`
- `org_ecosystem`
- `event_or_series`
- `exclude_or_reference_only`

建议特别拆出的对象：
- conference / symposium / congress / olympiad
- convention / framework / guideline
- fund / initiative / campaign
- research center / academic society

---

## 六、我建议的简化版网站结构

如果追求清晰、可落地、差异化，我建议先只做 5 个主分区。

### 1. 首页 Home
首页只回答三件事：
- 谁在做 AI？
- 最近有什么动作？
- 我从哪里切进去看？

首页建议放：
- 项目定位
- 3 到 5 个核心统计数
- 精选组织
- 精选行动
- 最近更新
- 专题入口

### 2. 组织库 Organizations
这是第一核心页。

建议功能：
- 组织卡片列表
- 搜索
- 筛选：组织类型、所属体系、区域、AI 角色
- 组织详情页

组织详情页只要回答：
- 它是谁
- 它在 AI 上做什么
- 最近动作有哪些
- 代表性文件或工具有哪些

### 3. 行动库 Actions
这是第二核心页。

建议功能：
- action 列表
- 搜索
- 筛选：行动类型、议题、时间、组织、区域
- action 详情页

每条 action 只要回答：
- 谁发起
- 做了什么
- 什么时候
- 官方证据在哪里
- 为什么值得看

### 4. 专题页 Collections
这是你项目最有辨识度的部分。建议先做 4 个专题：
- 联合国 AI 行动
- 区域组织 AI 治理
- 国际组织 AI 标准与工具
- 全球南方 AI 能力建设

### 5. 更新页 Updates
这是变更记录页，不是新闻门户。

建议只放：
- 最近新增 action
- 最近新增 instrument
- 最近更新的 organization

---

## 七、最小可用版本

如果你要先做 MVP，可以只保留三个页面：
- 首页
- 组织库
- 行动库

专题和更新可以先作为首页中的两个区块，不必立即做成独立复杂栏目。

---

## 八、最实际的下一步

我建议你按这个顺序推进：
1. 先清洗 Excel，把 127 条分层。
2. 先确定前台核心主体，第一批控制在 30 到 50 个。
3. 先做组织页和行动页，不要一开始就做复杂关系图。
4. 先接 3 个最强来源：`UN AI Resource Hub`、`OECD.AI International initiatives`、`UNESCO AI Ethics / Global Hub`。
5. 单独写一页“收录方法”，把过滤规则公开出来。

---

## 九、最短结论

你的来源不能整站照收，必须按“国际组织主体 + 官方证据 + 明确 action”过滤。

你的 Excel 很有用，但它不是前台目录，而是一个待清洗的组织样本池、边界测试集和 watchlist。

你的网站最简洁、最稳的一版就是：
- 首页
- 组织库
- 行动库
- 专题页
- 更新页

真正决定项目质量的不是页面多少，而是四件事：
- 组织边界清楚
- action 定义清楚
- 来源归属清楚
- 每条记录都能回到官方原文
