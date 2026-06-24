# 国际组织 AI 行动与机构展示网站调研

调研日期：2026-06-19  
调研范围：面向“国际组织 AI 机构、AI 行动、AI 政策、AI 工具、AI 活动”主题的公开网站、数据库、开源项目与资源库。  
调研目标：

1. 盘点现有类似产品分别收录了什么、提供了什么功能。
2. 判断你的项目还能填补哪些空白。
3. 给出尽量不与现有产品正面重合、但能解决真实使用问题的产品规划建议。

---

## 一、先说结论

如果把目前公开可见的相关产品放在一起看，已经有不少“单点很强”的资源，但仍然缺一个真正把**国际组织作为主对象**、把**AI 行动作为持续更新对象**、把**政策、项目、活动、工具、标准、合作关系**统一到一个数据模型里的公开站点。

现有资源的大致问题是：

- 很多平台只覆盖一个体系内部，例如联合国系统内部、欧盟内部、非洲区域内部。
- 很多平台以“政策文件”或“规范框架”为核心，不是以“国际组织及其实际 AI 行动”作为核心对象。
- 很多平台能看“某个国家或区域做了什么”，但很难看“某个国际组织具体做了什么、和谁合作、落在哪些国家、处于什么阶段、产生了什么结果”。
- 很多平台不是实时或准实时的，更新节奏偏报告式、年度式、专题式。
- 很少有产品把“组织目录、行动目录、治理工具目录、新闻监测、合作网络、时间线变化”同时做好。
- 很少有面向中文用户、研究者和媒体的“全球国际组织 AI 行动索引站”。

所以，你的项目如果继续做，很适合把定位从“又一个 AI 政策库”改成：

> **国际组织 AI 行动观察站 / International Organizations AI Action Observatory**

核心不是泛泛收集 AI 资料，而是解决下面几个痛点：

- 我想知道“哪些国际组织在做 AI”，现在哪个站最全？没有。
- 我想知道“它们到底在做政策、能力建设、项目试点、标准制定、治理倡议，还是只是开会发报告”，现在哪个站能一眼分清？很少。
- 我想知道“同一议题上 UN、OECD、UNESCO、EU、CoE、GPAI、ASEAN、非洲区域机构分别做了什么”，现在哪个站能横向比较？几乎没有。
- 我想知道“最近一个月有哪些国际组织新增了 AI 行动或政策动作”，现在哪个站能持续追踪？很少。

---

## 二、现有类似资源调研

下面按“官方或机构型资源”“跨区域数据库与知识平台”“开源项目与资源库”三类整理。

## 1. 联合国与国际组织体系内的官方或半官方资源

### 1. UN AI Resource Hub

URL：<https://unaihub.aiforgood.itu.int/>

定位：

- 联合国系统范围内的 AI 活动集中平台。

公开可见收录内容：

- UN system 中的 AI-related activities。
- 55 个 UN entities。
- 覆盖 165+ countries。
- 平台首页明确提供 `Browse Activities`、`Submit Activity`、全球地图、UN entities 展示。

公开可见功能：

- 活动浏览。
- 提交活动。
- 全球地图浏览。
- 按 UN entity 查看活动。
- 平台登录后还有 `Expert Directory` 入口：<https://unaihub.aiforgood.itu.int/unai/>
- 搜索与筛选能力在公开说明中可见，支持 agency、country、region、SDG 等维度。

价值：

- 这是目前最接近“国际组织 AI 行动数据库”的官方产品。
- 它的优势是“行动级别”而不是只做政策文件。

局限：

- 目前基本只覆盖 UN 系统。
- 更偏“UN 内部协同和展示”，不是面向全世界国际组织的统一比较平台。
- 对外部研究者来说，跨体系对比仍然不够。

相关来源：

- <https://unaihub.aiforgood.itu.int/>
- <https://unaihub.aiforgood.itu.int/unai/>
- <https://www.itu.int/hub/2025/12/un-working-group-launches-new-ai-resource-hub/>

### 2. ITU / AI for Good 的 UN AI Actions 与 UN Activities on AI 报告体系

URL：

- <https://www.itu.int/en/action/ai/Pages/default.aspx>
- <https://aiforgood.itu.int/about-us/un-ai-actions/>
- <https://aiforgood.itu.int/eventcat/un-ai-activities/>

定位：

- 联合国 AI 行动的长期汇总、活动展示和年度或专题报告入口。

公开可见收录内容：

- ITU 页面说明：自 2018 年起持续发布 `UN Activities on AI Report`。
- 2023 版报告页面说明，收录 408 个 UN system AI cases and projects，并覆盖 17 个 SDGs。
- `UN AI activities` 页面更像 AI for Good 体系下的活动和议程归档。

公开可见功能：

- 报告汇编。
- AI for Good 活动目录。
- 专题页面与博客。
- 议题分类浏览。

价值：

- 对理解“联合国系统如何叙述自己的 AI 工作”很重要。
- 适合做你项目中的“来源层”和“历史层”。

局限：

- 报告型内容强，但实时数据库能力不如专门平台。
- 主要还是 UN 体系叙事，不是跨组织横向对比产品。

### 3. UNESCO Global AI Ethics and Governance Observatory

URL：

- <https://www.unesco.org/ethics-ai/en>
- <https://www.unesco.org/ethics-ai/en/global-hub>

定位：

- 全球 AI 伦理与治理观察平台。

公开可见收录内容：

- Country Profiles。
- Readiness Assessment Methodology，简称 RAM，相关结果。
- AI Ethics and Governance Lab。
- good practices、toolkits、research、expert networks。

公开可见功能：

- 按国家查看 AI 治理画像。
- 展示 RAM 的政策建议和关键洞见。
- 提供实验室和知识库型内容。
- 提供专家网络入口，如 Women4Ethical AI、Business Council、AI Ethics Experts Without Borders 等。

典型条目特征：

- Ecuador 页面直接给出治理碎片化、政策建议数量、人才缺口、多方参与生态等摘要。

价值：

- 在“国别 AI 治理准备度与伦理治理实践”这一层很强。
- 适合作为你项目中“国际组织影响到哪些国家、如何形成治理能力建设”的证据来源。

局限：

- 核心对象是“国家画像”和“AI ethics governance”，不是“国际组织行动总表”。
- 行动颗粒度偏政策与能力建设，不是实时行动流。

相关来源：

- <https://www.unesco.org/ethics-ai/en>
- <https://www.unesco.org/ethics-ai/en/global-hub>
- <https://www.unesco.org/ethics-ai/en/ecuador>

### 4. OECD.AI Policy Navigator

URL：

- <https://oecd.ai/en/dashboards/policy-initiatives>
- <https://oecd.ai/en/dashboards/overview>

定位：

- OECD.AI 的政策导航数据库。

公开可见收录内容：

- 来自 80+ jurisdictions and organisations 的 live repository。
- national initiatives。
- international initiatives。
- categories 包括：
  - AI Policy Frameworks and Programmes
  - AI Governance Bodies and Mechanisms
  - Regulations, guidelines and standards
  - AI policy initiatives, programmes and projects

公开可见功能：

- 搜索。
- 按国家、地区、国际组织、类别、状态、是否具有法律约束力、起始年份、原则、目标行业、AI tags 等筛选。
- National、International、All initiatives 切换。
- 显示提交或更新记录。

价值：

- 这是当前全球 AI 政策信息结构化程度最高的公开平台之一。
- 很适合作为你项目的“国际组织政策与倡议种子库”。

局限：

- 主体仍然是“政策与倡议”，不是“国际组织行动全景”。
- 国际组织条目虽然有，但不是按“国际组织画像 + 行动流”来组织。
- 不是实时新闻监测站。

### 5. OECD AI Policy Toolkit

URL：

- <https://oecd.ai/en/ai-toolkit/get-started>
- <https://oecd.ai/en/wonk/the-oecd-ai-policy-toolkit-better-ai-policies-for-better-lives>

定位：

- 帮助政府和利益相关方把 AI 原则转化为实际政策设计的工具。

公开可见收录内容：

- 六个政策支柱。
- 各国政策优先事项映射。
- 具体政策实例。

公开可见功能：

- 调查式“识别政策优先级”模块。
- AI-powered module，按优先事项查找全球政策样例。
- FAQ、方法说明、系统文档。

价值：

- 说明国际 AI 治理产品正在从“数据库”往“决策支持工具”发展。
- 对你项目是一个重要启发：不要只做列表，要做“比较和判断辅助”。

局限：

- 它不做国际组织行动的持续公开监测。
- 更偏政策设计辅助工具。

### 6. GPAI，现与 OECD.AI 集成

URL：

- <https://www.oecd.org/en/about/programmes/global-partnership-on-artificial-intelligence.html>
- <https://oecd.ai/>

定位：

- 全球 AI 多边合作伙伴关系。

公开可见收录内容：

- 成员、专家社区、Expert Support Centres、工作计划与合作机制。
- OECD.AI 页面现在已将 GPAI 与 OECD AI work 更紧密整合。

公开可见功能：

- 组织介绍。
- 成员资格与申请说明。
- 专家社区展示。
- 与 OECD AI 生态下其他工具联通。

价值：

- 是理解“跨国多边 AI 治理合作机制”非常关键的一环。
- 适合你项目纳入“国际组织或国际合作机制”对象层。

局限：

- 不是一个 action-tracking 数据库。
- 更像治理机制与合作架构。

### 7. Council of Europe：Framework Convention on AI + HUDERIA

URL：

- <https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence>
- <https://www.coe.int/en/web/artificial-intelligence/huderia-risk-and-impact-assessment-of-ai-systems>

定位：

- 欧洲委员会在国际 AI 条约和风险评估工具层面的核心资源。

公开可见收录内容：

- Framework Convention on Artificial Intelligence。
- HUDERIA 风险与影响评估方法。

公开可见功能：

- 公约要求解释。
- 适用范围说明。
- 风险与影响评估结构化方法。
- COBRA、Stakeholder Engagement、RIA、Mitigation Plan 等方法组件介绍。

价值：

- 它不是“数据库型平台”，但属于国际组织 AI 治理工具的重要基础设施。
- 如果你的站只展示“组织名称”，而不展示“这个组织到底产出了什么治理工具”，会损失很多信息价值。

局限：

- 更偏规范与方法，不是行动流。

### 8. European AI Office 与 EU AI literacy repository

URL：

- <https://digital-strategy.ec.europa.eu/en/policies/ai-office>
- <https://digital-strategy.ec.europa.eu/en/policies/repository-ai-literacy-practices>

定位：

- 欧盟 AI Act 实施与治理体系的官方入口。

公开可见收录内容：

- AI Office 的结构、任务、国际合作职责。
- AI literacy repository，收录 40+ initiatives。

公开可见功能：

- 机构介绍。
- 实施与国际合作说明。
- AI literacy practices 的公共资源库。
- 仓库经过搜索性优化，并持续征集案例。

价值：

- 展示了一个很值得借鉴的思路：官方站点不只发布规则，也开始做“实践案例库”。
- 对你项目有启发：除了政策和行动本身，还可以整理“治理实践”。

局限：

- 只覆盖欧盟体系。
- 议题很聚焦，不是国际组织全景。

### 9. ASEAN AI 治理资源

URL：

- <https://asean.org/book/asean-guide-on-ai-governance-and-ethics/>
- <https://asean.org/book/expanded-asean-guide-on-ai-governance-and-ethics-generative-ai/>
- <https://www.imda.gov.sg/about-imda/international-relations/asean-working-group-on-ai-governance>

定位：

- 东盟区域 AI 治理框架、指南与工作机制。

公开可见收录内容：

- ASEAN Guide on AI Governance and Ethics。
- Expanded ASEAN Guide on Generative AI。
- ASEAN Working Group on AI Governance 项目、活动和联系入口。

公开可见功能：

- 区域指南下载。
- 工作组项目和活动介绍。
- 政策框架展示。

价值：

- 说明区域组织的 AI 行动不止是法规，还有指南、路线图、工作组和能力建设机制。

局限：

- 分散在多个页面。
- 不像数据库产品那样利于比较与追踪。

---

## 2. 跨区域数据库、政策追踪与知识平台

### 10. African Observatory on Responsible AI：Africa AI Policy Tool

URL：

- <https://www.globalcenter.ai/aorai/africa-policy-tool>
- <https://www.africanobservatory.ai/>

定位：

- 非洲区域 AI 政策与框架的交互工具。

公开可见收录内容：

- national AI strategies、policies、frameworks。
- regional policies。
- 当前页面显示 1505 条结果。

公开可见功能：

- 地图筛选。
- 按国家筛选。
- 按 primary focus、年份等查看。
- 支持 peer learning、comparative analysis、evidence-informed policymaking。

价值：

- 这是很强的区域性政策追踪样板。
- 它说明“按地区做深”是可行的，但也反过来说明全球层面还缺更统一的国际组织视角产品。

局限：

- 以非洲国家或区域政策为主。
- 不以国际组织行动作为主要对象。

### 11. Carnegie Africa Technology Policy Tracker，AfTech

URL：

- <https://carnegieendowment.org/features/africa-digital-regulations>
- <https://carnegieendowment.org/programs/africa/collections/understanding-africas-digital-economy-policy-landscape>

定位：

- 非洲数字经济政策聚合追踪工具。

公开可见收录内容：

- Carnegie 页面明确称其为非洲大陆范围的 aggregate of digital economy laws, policies and regulations。
- 涵盖 AI 以及更广的数据、基础设施、平台等议题。

公开可见功能：

- 交互式追踪。
- 政策聚合。
- 区域层面研究与分析文章联动。

价值：

- 对你的启发不是“照搬它”，而是它证明了：一个强产品不必只追 AI 本体，也可以把 AI 放在更大的数字治理结构里。

局限：

- 重点是非洲数字经济政策，不是国际组织 AI 行动总览。

### 12. IGF Policy Network on AI，PNAI

URL：

- <https://intgovforum.org/en/content/igf-policy-network-on-ai>

定位：

- 联合国互联网治理论坛下的多利益相关方 AI 政策网络。

公开可见收录内容：

- Policy briefs。
- activities。
- publications and resources。
- thematic focus，如 accountability、interoperability、sustainability、labour rights。

公开可见功能：

- 参与入口。
- 资源发布。
- 活动与年度成果展示。

价值：

- 它是“国际 AI 治理讨论场域”的一个重要 actor。
- 适合在你项目里作为“机构页”和“行动页”的数据源之一，而不是核心数据库替代品。

局限：

- 更像开放政策网络，不是监测数据库。

### 13. Digital Watch Observatory

URL：

- <https://dig.watch/>
- <https://dig.watch/technologies/artificial-intelligence>

定位：

- 全球数字政策观察站，AI 只是其中一个议题。

公开可见收录内容：

- technologies。
- policy topics。
- processes。
- actors。
- resources。
- updates。

公开可见功能：

- 议题导航。
- actor 页面。
- resource 页面。
- process 页面。
- 新闻和更新流。

价值：

- 它非常接近“全球数字治理知识图谱入口”。
- 但 AI 只是其中一部分，所以它的启发更偏信息架构和观察站方法。

局限：

- 不聚焦国际组织 AI 行动。
- 深度不一定落到每个组织的 AI 行动颗粒度。

### 14. IAPP Global AI Law and Policy Tracker

URL：

- <https://iapp.org/resources/article/global-ai-legislation-tracker>

定位：

- 全球 AI 法律与政策追踪器。

公开可见收录内容：

- 一组 jurisdictions 的 AI legislation 和 policy developments。
- brief commentary。
- chart、map、directory。

公开可见功能：

- 图表。
- 地图。
- 目录。
- 更新节奏明确，页面标注最近更新时间。

价值：

- 适合作为对比对象，帮助你判断“不要把项目做成纯法律追踪站”。

局限：

- 重点是 jurisdiction-level law 和 policy，不是国际组织行动。
- 页面也明确说明不覆盖所有地区、所有 initiatives。

### 15. AI Standards Exchange Database，ITU / AI for Good

URL：

- <https://aiforgood.itu.int/ai-standards-exchange/>

定位：

- 全球 AI standards development organizations 的标准总入口。

公开可见收录内容：

- 870+ AI standards and related technical publications。
- standards news。
- capacity building。
- 涉及 IEC、ISO、ITU、IEEE、IETF、ETSI、TTA 等。

公开可见功能：

- standards 搜索。
- 按 AI use、industry vertical、human-AI activity 分类。
- news feed。
- capacity building。

价值：

- 这是国际组织 AI “标准行动”维度的关键站点。
- 说明你的项目如果只收“政策”和“项目”，会忽略标准治理。

局限：

- 聚焦标准，不覆盖国际组织整体行动生态。

---

## 3. 开源项目与资源库

### 16. Fairly Regulation and Policy Tracker，GitHub

URL：

- <https://github.com/fairlyAI/fairly-regulation-policy-tracker>

定位：

- 面向全球 AI 监管与政策地图的开源协作仓库。

公开可见收录内容：

- 按 General、Generative AI、Data、Privacy、Advertising、Employment、Government and Military、Health、Finance and Insurance、Other 等分类收录法规。

公开可见功能：

- GitHub 协作。
- 公开问题反馈与建议。
- 规则分类说明。

价值：

- 这是一个“用 GitHub 组织法规情报”的典型开源样板。
- 适合借鉴其数据协作方式，而不适合直接作为国际组织行动站的产品模型。

局限：

- 主题仍是 regulation map。
- 不以国际组织为核心对象。

### 17. MAIR，Monitoring of AI Regulations

URL：

- <https://github.com/ModelOriented/MAIR>

定位：

- 监测 AI 监管与相关研究的开源项目。

公开可见收录内容：

- AI regulations 数据库目标。
- 相关 research papers。
- 自动分析工具构想。

公开可见功能：

- GitHub 仓库协作。
- 面向自动化分析的项目描述。

价值：

- 对你项目的启发是：监测体系可以做成“数据库 + 自动分析”。

局限：

- 更偏研究原型。
- 公开前端产品完成度有限。

### 18. aiPolicyResources，GitHub

URL：

- <https://github.com/chinasatokolo/aiPolicyResources/>

定位：

- AI policy 学习者和研究者使用的资源导航库。

公开可见收录内容：

- AI Governance and Regulation Trackers。
- AI indices。
- 组织、出版物、研究资源等。

公开可见功能：

- 资源导航。
- 人工策展链接清单。

价值：

- 这类项目证明“资源导航”本身有需求。
- 但也说明只做链接清单天花板很低。

局限：

- 不是结构化数据库。
- 不提供统一对象模型、比较、监测和时间线。

### 19. Awesome Artificial Intelligence Regulation，GitHub

URL：

- <https://github.com/ethicalml/awesome-artificial-intelligence-regulation>

定位：

- AI regulation、principles、guidelines、standards 资源清单。

公开可见收录内容：

- 各国、各类 AI regulation、guidelines、principles、standards。

公开可见功能：

- 按国家和主题汇总链接。

价值：

- 是很典型的 awesome list 模式。
- 适合做早期种子来源，不适合直接替代你想做的产品。

局限：

- 不是数据库。
- 缺少时间维度、组织维度和行动维度。

---

## 三、把这些资源放在一起后，能看出什么结构性空白

## 1. 最大空白：没有一个真正围绕“国际组织”展开的 AI 观察站

现有产品大多围绕以下对象之一展开：

- 国家政策。
- 区域法规。
- 某个组织体系内部行动。
- 某类标准。
- 某个专题社区。

但很少有产品把下面三个对象同时做成主对象：

- 国际组织，organization
- AI 行动，action
- 治理工具或文件，instrument

你的项目最适合补这一块。

## 2. 第二个空白：缺“横向比较”

现有站点常见的组织方式是：

- 按国家看。
- 按单一机构体系看。
- 按专题看。

但研究者、政策分析师、记者常常真正想问的是：

- 联合国、UNESCO、OECD、GPAI、欧盟、欧洲委员会、ASEAN、非洲区域机构，在 AI 上各自扮演什么角色？
- 谁偏规范制定？谁偏项目落地？谁偏标准？谁偏培训？谁偏风险评估？
- 谁在全球南方国家有实际项目覆盖？谁主要停留在原则层？

这类问题目前缺少好用入口。

## 3. 第三个空白：缺“行动颗粒度 + 时间线”

很多站要么只有：

- 年度报告。
- 框架文件。
- 静态目录。

要么只有：

- 新闻稿。
- 活动页面。

但缺少一个统一的 action record：

- 行动名称。
- 发起组织。
- 参与组织。
- 行动类型。
- 发布时间、启动时间、最新更新时间。
- 适用国家或地区。
- 是否形成政策、标准、工具、培训、资金、试点。
- 证据来源。
- 当前状态。

这一点非常适合你来做。

## 4. 第四个空白：缺“把政策行动和实际项目区分开”

现在很多 AI 治理站把这些混在一起：

- 战略。
- 法规。
- 原则。
- 活动。
- 项目。
- 工具。
- 培训。
- 合作倡议。

但用户经常需要区分：

- 这是规范性动作，还是运营性动作？
- 这是机构内部治理，还是对成员国的外部能力建设？
- 这是常设机制，还是一次性活动？

如果你的项目把这一层分类做清楚，就会很有价值。

## 5. 第五个空白：缺“国际组织之间的合作网络”

现有平台几乎都不擅长回答：

- 哪些 AI 行动是联合发布的？
- 哪些组织反复合作？
- 哪些项目覆盖多个国际组织体系？
- 哪些组织在同一议题上有重叠？

这是非常适合做网络图谱和关系可视化的。

## 6. 第六个空白：缺“持续公开更新的中文入口”

这块英文资源并不少，但中文世界几乎没有一个结构化、持续维护、可搜索、可比较、可引用的国际组织 AI 行动观察站。

这本身就是一个明显空白。

---

## 四、你的项目最适合怎么定位

不建议定位成：

- 全球 AI 政策库。
- AI 法规追踪器。
- 国际组织 AI 新闻站。

这些方向都已经有强竞争者，且容易和 OECD.AI、IAPP、各类 regulation tracker 重合。

更建议定位成：

> **国际组织 AI 行动观察站**
>
> 一个以国际组织为主线、以 AI 行动为核心记录单位、兼顾政策、标准、项目、活动、工具、合作网络、时间线的公开数据库与可视化站点。

一句话版本可以是：

> 让用户能够看清“哪些国际组织在做 AI、在怎么做、做到了哪里、和谁一起做、留下了哪些公开证据”。

---

## 五、建议的产品信息架构

## 模块 1：国际组织图谱，Organization Atlas

这是最应该放在首页第一层的模块。

每个组织页面建议包含：

- 组织名称、中英文、缩写。
- 组织类型。
  - intergovernmental organization
  - UN entity
  - treaty body
  - regional organization
  - standards body
  - multistakeholder initiative
  - NGO、think tank、network
- 所属体系。
  - UN、EU、CoE、OECD-GPAI、ASEAN、AU、others
- AI 相关角色。
  - policymaker
  - standard-setter
  - implementing agency
  - convening platform
  - funder or capacity builder
  - watchdog or knowledge hub
- 重点 AI 议题。
- 相关页面链接。
- 主要 AI 行动总数。
- 最近更新。
- 典型成果。

为什么这个模块重要：

- 它会让你的站和纯政策库、纯新闻站立刻区分开。

## 模块 2：AI 行动数据库，Action Tracker

这是你项目真正的核心。

建议把每一条 action 设计成结构化记录，至少包括：

- title
- organization lead
- partner organizations
- action type
  - policy or strategy
  - standard or guideline
  - report or assessment
  - programme or project
  - training or capacity building
  - event or summit or dialogue
  - expert network
  - funding or facility
  - technical tool or platform
- thematic area
  - ethics
  - governance
  - standards
  - health
  - education
  - labour
  - environment
  - humanitarian
  - public sector
  - gender or inclusion
- geography
- sdg mapping
- status
  - announced
  - active
  - completed
  - dormant
- start date
- latest update date
- evidence url
- source type
  - official website
  - report
  - press release
  - event page
  - database entry
- summary
- why it matters

为什么这个模块重要：

- 你要做的不是“列机构”，而是“让机构的 AI 行动变得可查询、可比较、可更新”。

## 模块 3：治理工具与文件库，Instrument Explorer

建议单独拆出来，而不是混在 action 里。

对象包括：

- treaties
- conventions
- recommendations
- principles
- standards
- toolkits
- assessment methodologies
- policy frameworks

典型对象：

- UNESCO Recommendation on the Ethics of AI
- CoE Framework Convention on AI
- HUDERIA
- OECD AI Principles
- ASEAN Guide on AI Governance and Ethics
- AI Standards Exchange 中的标准资源

为什么值得单独做：

- 很多国际组织的价值不在“做了多少项目”，而在“产出了什么规则、框架、方法、标准”。

## 模块 4：专题 Collections

这个模块会很适合你，因为你已经提到 collection。

建议把 collection 做成站点的策展层，而不是数据底层。

可以做：

- UN system AI actions
- Regional organizations and AI governance
- International AI standards bodies
- AI ethics and readiness initiatives
- AI capacity building for Global South
- AI and humanitarian action
- AI and education in international organizations
- AI governance tools for public sector use

为什么这个模块有价值：

- 相同底层数据库可以被重新组织成很多主题入口。
- 这能提高网站的“编辑感”和“研究导向”，而不是冷冰冰的数据表。

## 模块 5：时间线与实时收录，Live Monitor

这是最能拉开差异化的地方。

建议做两层：

- `Latest updates`
  - 最近新增条目
  - 最近更新条目
  - 最近新增政策文件
  - 最近新增活动、峰会、报告
- `Change log`
  - 某条目第一次收录时间
  - 最近一次变更时间
  - 变更内容摘要

如果能做自动化，可以重点盯：

- 官方 newsroom
- official publications pages
- event calendars
- resource libraries
- RSS、sitemap、release pages

为什么重要：

- 这会让你的项目不只是“目录”，而是“观察站”。

## 模块 6：合作网络图，Collaboration Graph

建议把组织关系图放成一个高辨识度模块。

可以展示：

- 组织与组织的共同行动次数。
- 共发报告。
- 共办活动。
- 共建平台。
- 共推标准或治理框架。

为什么重要：

- 这是大多数现有站点没有认真做的。
- 研究者会很需要这种“网络结构”视角。

## 模块 7：比较页，Compare

非常建议做。

可以支持：

- 组织对比。
- 区域对比。
- 行动类型对比。
- 议题分布对比。

例如：

- UNESCO vs OECD.AI vs EU AI Office
- UN entities 中谁更偏 operational deployment，谁更偏 governance
- 哪些组织更关注 Global South capacity building

这会让站点真正有“分析工具”属性。

---

## 六、你最应该避免和现有产品正面重合的地方

## 1. 不要做成“又一个国家 AI 法规追踪器”

因为这条赛道已经有：

- OECD.AI
- IAPP
- Fairly tracker
- 其他 AI regulation trackers

而且你的优势不在这里。

## 2. 不要只做“国际组织名录”

因为那样很快会沦为静态黄页。

真正有用的是：

- 名录 + 行动
- 名录 + 时间线
- 名录 + 关系
- 名录 + 证据

## 3. 不要只做“新闻聚合”

国际组织 AI 新闻站很容易变成低价值信息流。你应该做的是“新闻驱动的结构化更新”，而不是纯新闻列表。

## 4. 不要把所有东西混成一个列表

一定要区分：

- 组织
- 行动
- 工具或政策文件
- 活动
- 新闻或更新

一旦不区分，站点会迅速失去可用性。

---

## 七、最值得做的差异化功能

这里给出一个优先级最高的功能清单。

### A 级：强烈建议做

1. 国际组织主页卡片与详情页。
2. 结构化 AI action 数据库。
3. Collections 策展页。
4. 最近更新和实时收录流。
5. 每条记录都附原始公开来源链接。
6. 多维筛选。
   - 组织类型
   - 行动类型
   - 区域
   - 议题
   - 时间
   - SDG

### B 级：很值得做

1. 合作网络图。
2. 比较页。
3. 方法说明页。
4. 数据导出。
   - CSV
   - JSON
5. “为什么收录、为什么不收录”的标准页。

### C 级：如果你后续想做深

1. 自动监测与人工审核工作流。
2. API。
3. 机构认领或投稿机制。
4. 存档快照。
5. 周报或月报自动生成。

---

## 八、建议的收录标准

这是项目成败关键之一。建议你尽早写清楚。

## 1. 收录对象类型

建议至少覆盖：

- intergovernmental organizations
- UN entities and affiliated bodies
- regional organizations
- treaty-based institutions
- standards development bodies
- multistakeholder international initiatives
- global NGO or nonprofit networks directly engaged in AI governance or implementation

## 2. 什么算“AI 行动”

建议明确定义，至少满足下列之一：

- 发布 AI 相关政策、框架、指南、标准、工具。
- 组织 AI capacity building、training、fellowship、network。
- 落地 AI 相关项目、平台、试点、数据库。
- 开展 AI 专项治理合作、国际对话、峰会。
- 形成公开可验证的 AI governance、deployment、oversight 机制。

## 3. 什么不收

建议排除：

- 仅提到 AI 但无实质动作的泛泛新闻。
- 无公开证据的宣传性内容。
- 与 AI 关系极弱、只是数字化转型泛表述的项目。

---

## 九、建议的数据模型

最少建议四张主表：

### 1. organizations

字段建议：

- id
- name_en
- name_zh
- acronym
- organization_type
- parent_system
- region
- description
- official_url
- ai_relevance_summary
- created_at
- updated_at

### 2. actions

字段建议：

- id
- title
- summary
- action_type
- thematic_tags
- status
- start_date
- end_date
- latest_update_date
- geography_scope
- sdg_tags
- lead_org_id
- evidence_url
- source_name
- source_date
- created_at
- updated_at

### 3. instruments

字段建议：

- id
- title
- instrument_type
- issuing_org_id
- publication_date
- legal_status
- official_url
- summary
- keywords

### 4. organization_action_relations

字段建议：

- organization_id
- action_id
- role
  - lead
  - partner
  - funder
  - participant
  - standard-setter

如果后面还想加，可以再扩：

- events
- updates
- sources
- collections

---

## 十、推荐的 MVP 范围

不建议一开始就追求“全球所有国际组织 + 全自动实时监测”。

更现实的 MVP 是：

## Phase 1：先做 6 个体系

- UN system
- UNESCO
- OECD / GPAI
- EU
- Council of Europe
- ASEAN

为什么先做这 6 个：

- 都有公开来源可抓。
- 覆盖规范、政策、能力建设、活动、标准等不同类型。
- 足以形成有辨识度的跨体系比较。

## Phase 2：再扩 2 个区域或专题层

- African Observatory / AfTech
- AI Standards bodies / AI for Good standards layer

## Phase 3：再加 NGO、think tank、multistakeholder layer

- IGF PNAI
- Digital Watch Observatory
- 其他全球非政府治理网络

---

## 十一、一个可行的首页结构

如果你想让站和 `China-io-index` 保持“索引型项目”的气质，但更成熟，首页可以这样：

### Hero

- 标题：国际组织 AI 行动观察站
- 副标题：追踪全球国际组织如何治理、部署、推广与协调人工智能
- 入口按钮：
  - 浏览组织
  - 浏览行动
  - 最近更新
  - 专题 Collections

### Overview Metrics

- 收录组织数
- 收录行动数
- 收录工具或文件数
- 覆盖区域数
- 最近 30 天新增数

### Browse by Type

- 国际组织
- AI 行动
- 治理工具
- 活动或对话
- 标准
- 能力建设

### Featured Collections

- 联合国 AI 行动
- 国际 AI 治理框架
- 区域组织 AI 路线图
- 全球南方 AI 能力建设

### Latest Updates

- 最近新增动作
- 最近新发布报告或政策
- 最近更新机构页

### Network Snapshot

- 热门合作关系
- 高频共现组织

---

## 十二、最关键的方法论建议

你的项目如果想长期成立，最重要的不是前端，而是下面三件事：

## 1. 统一对象模型

你必须从一开始就想清楚：

- 什么是组织
- 什么是行动
- 什么是工具
- 什么是活动
- 什么是更新

否则后续会越来越乱。

## 2. 坚持“每条记录必须可回到原始公开来源”

建议每一条都保留：

- 原始 URL
- 来源机构
- 公开日期
- 抓取日期
- 证据摘录或摘要

这是你和纯内容站、纯 AI 摘要站最大的区别。

## 3. 先半自动，不要一开始就全自动

很适合的流程是：

- 脚本发现候选更新
- 人工审核后入库
- 页面展示结构化结果

这样比一开始盲目追求“实时全自动”更稳。

---

## 十三、我对你项目的最终建议

如果直接回答“我的项目可以填补哪些空白”，我会概括成四点：

1. 填补“国际组织作为主对象”的空白。现在多数站点以国家、法规或单一机构体系为主，不是以国际组织全景为主。
2. 填补“AI 行动可比较、可追踪”的空白。现在有政策库、有报告库、有活动页，但缺少把行动做成结构化记录并长期更新的公开站。
3. 填补“跨体系比较”的空白。用户很难在一个地方比较 UN、UNESCO、OECD、GPAI、EU、CoE、ASEAN、非洲区域平台分别在做什么。
4. 填补“中文世界的国际组织 AI 观察入口”的空白。这是一个真实存在、且目前竞争不强的空白。

如果回答“应当如何规划”，我的建议是：

- 不要从“全球所有 AI 相关组织大全”起步。
- 先从“6 个关键体系 + 结构化 action tracker + collections + recent updates”做一个可用 MVP。
- 用“组织页 + 行动页 + 工具页 + 专题页 + 更新流”五层架构搭站。
- 把实时收录理解为“持续发现并审核更新”，不是“全自动抓取后一股脑堆上去”。
- 把差异化重点放在：
  - 跨机构比较
  - 行动颗粒度
  - 合作网络
  - 时间线
  - 中文可读性

---

## 十四、建议优先纳入的首批来源清单

建议你第一批优先接入这些来源：

1. UN AI Resource Hub  
   <https://unaihub.aiforgood.itu.int/>

2. ITU AI / UN Activities on AI  
   <https://www.itu.int/en/action/ai/Pages/default.aspx>

3. AI for Good / UN AI Actions  
   <https://aiforgood.itu.int/about-us/un-ai-actions/>

4. UNESCO Global AI Ethics and Governance Observatory  
   <https://www.unesco.org/ethics-ai/en>

5. OECD.AI Policy Navigator  
   <https://oecd.ai/en/dashboards/policy-initiatives>

6. OECD AI Policy Toolkit  
   <https://oecd.ai/en/ai-toolkit/get-started>

7. GPAI / OECD integrated partnership  
   <https://www.oecd.org/en/about/programmes/global-partnership-on-artificial-intelligence.html>

8. European AI Office  
   <https://digital-strategy.ec.europa.eu/en/policies/ai-office>

9. EU Repository of AI literacy practices  
   <https://digital-strategy.ec.europa.eu/en/policies/repository-ai-literacy-practices>

10. Council of Europe Framework Convention on AI  
    <https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence>

11. HUDERIA  
    <https://www.coe.int/en/web/artificial-intelligence/huderia-risk-and-impact-assessment-of-ai-systems>

12. ASEAN Guide on AI Governance and Ethics  
    <https://asean.org/book/asean-guide-on-ai-governance-and-ethics/>

13. ASEAN Working Group on AI Governance  
    <https://www.imda.gov.sg/about-imda/international-relations/asean-working-group-on-ai-governance>

14. African Observatory on Responsible AI / Africa AI Policy Tool  
    <https://www.globalcenter.ai/aorai/africa-policy-tool>

15. Carnegie Africa Technology Policy Tracker  
    <https://carnegieendowment.org/features/africa-digital-regulations>

16. IGF Policy Network on AI  
    <https://intgovforum.org/en/content/igf-policy-network-on-ai>

17. Digital Watch Observatory  
    <https://dig.watch/>

18. AI Standards Exchange Database  
    <https://aiforgood.itu.int/ai-standards-exchange/>

19. IAPP Global AI Law and Policy Tracker  
    <https://iapp.org/resources/article/global-ai-legislation-tracker>

20. 开源参考
    - <https://github.com/fairlyAI/fairly-regulation-policy-tracker>
    - <https://github.com/ModelOriented/MAIR>
    - <https://github.com/chinasatokolo/aiPolicyResources/>
    - <https://github.com/ethicalml/awesome-artificial-intelligence-regulation>

---

## 十五、附：适合你项目的英文副标题候选

如果你后面要做站点文案，下面几个方向比较贴切：

- Mapping International Organizations in AI
- Tracking Global AI Actions by International Organizations
- An Observatory of International Organizations’ AI Actions
- Who Is Doing What in Global AI Governance
- International Organizations, AI Governance, and Action

我认为最稳的一版是：

> **An Observatory of International Organizations’ AI Actions**

---

## 十六、附：一句更尖锐的项目问题意识

如果你想把项目的问题意识说得更明确，可以这样表达：

> 全球 AI 治理讨论很多，但关于“国际组织究竟在做什么”的公开信息仍然分散、异构、难比较、难持续追踪。本项目希望把国际组织的 AI 机构、政策、标准、项目、活动与合作关系放到同一张可更新的公共地图中。

---

## 参考说明

本文基于 2026-06-19 可公开访问的网页内容整理。部分站点是交互式页面，公开页面可直接确认其定位、范围与功能，但更细颗粒度的数据字段可能需进入页面交互后才能完整查看。对于这类站点，本文只陈述可由公开页面直接支持的功能和范围，不对未公开展示的内部能力做推断。
