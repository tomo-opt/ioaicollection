# Actions Pipeline 说明

## 为什么不是简单关键词抓取

这个项目的目标不是收一切 AI 新闻，而是收“国际组织在 AI 领域做的事情”。

所以当前代码采用的是：

1. `source-driven`
   优先从已知国际组织来源页直接抓

2. `discovery + reading-based classification`
   对开放互联网发现结果，不直接用关键词裁决，而是继续做：
   - 组织映射
   - 来源域判断
   - AI 相关性判断
   - 行动性判断
   - 发布 / 审核分流

## 当前已实现策略

### 1. 结构化来源直抓

- `UN AI Resource Hub Activities`
- 策略：`structured_html_cards`
- 结果：直接产出 `actions.json`

### 2. 可信来源开放发现

当前已接入：

- `OECD AI`
- `Council of Europe AI`
- `UNESCO AI`
- `ITU AI`

策略：

- `Google News RSS` 做召回
- 对跳转后的真实页面做二次读取
- 再进行来源归属与行动性评分

### 3. 种子组织轮转发现

策略：

- 从 `orgs.json` 中抽取组织层条目
- 每日轮转一批组织
- 用组织精确英文名 + AI 术语做发现
- 命中结果进入发布队列或审核队列

这样不会每次只盯着少数几个固定来源。

## 当前生成文件

- `data/actions.json`
  已自动发布的 actions

- `data/review-queue.json`
  需要人工复核的候选 actions

- `data/source-registry.json`
  每个来源的运行状态、策略、最近一次执行情况

- `data/pipeline-status.json`
  总体统计

## 借鉴过的开源模式

下面这些项目不是直接复用代码，而是借鉴了其工作流思路：

1. `basic-git-scraper-template`
   链接：<https://github.com/olivernn/basic-git-scraper-template>
   借鉴点：定时抓取、GitHub Actions 自动提交、把抓取结果版本化

2. `nlp-arxiv-daily`
   链接：<https://github.com/monologg/nlp-arxiv-daily>
   借鉴点：日更数据源、结构化记录、前端展示与数据生成分离

3. `Google-News-Feed`
   链接：<https://github.com/SSujitX/google-news-feed>
   借鉴点：把 Google News RSS 作为发现层，而不是最终可信来源

## 下一步最值得做的增强

1. 给 `UN AI Resource Hub` 补详情页解析
2. 给 `review-queue.json` 做人工审核页面
3. 给 `actions` 加主题标签、地区标签、组织映射置信度
4. 给 `source-registry` 增加每个来源的失败日志与重试状态
