# 项目架构说明

## 第一轮建议架构

当前先用 GitHub 可部署的数据驱动前端，原因是：

1. 你现在最需要先看清页面信息架构，而不是先上复杂工程。
2. 你已有的数据是 `csv`，适合先做 `csv -> json -> 前端渲染`，但发布时不暴露原始 `csv`。
3. 后面如果确认方向，再平移到 `Next.js`、`Astro`、数据库或服务端都很容易。

## 当前结构

```text
ai-io-site/
  index.html
  styles.css
  app.js
  config/
    action-sources.json
  data/
    orgs.json
    actions.json
    review-queue.json
    source-registry.json
    pipeline-status.json
    manual/
      org-overrides.json
  scripts/
    build_data.py
    build_actions.py
  PROJECT-ARCHITECTURE.md
```

## 页面模块

1. 首页 Hero
   展示项目定位：国际组织 AI 组织库 + AI 行动库 + 数据来源与更新逻辑。

2. Overview 概览
   展示当前组织总数、可直达官网数、组织型条目数、事件型条目数。

3. 组织库
   从 `orgs.json` 渲染组织卡片，可按：
   - 搜索
   - 角色建议
   - 组织类型
   - 层级
   进行筛选。

4. 行动库
   当前已经有第一批自动抓取结果，并预留开放互联网发现链路：
   - 行动标题
   - 发起组织
   - 行动类型
   - 来源链接
   - 更新时间

5. 自动收录链路区
   展示未来主数据源怎么进来，避免你后面忘掉系统边界。

6. 数据缺口区
   明示当前哪些数据还缺，哪些可以自动补，哪些需要人工审核。

## 后续升级路线

## 当前数据策略

1. 组织层
   `international_orgs_seed.csv -> orgs.json`

2. 人工修正层
   `manual/org-overrides.json -> 覆盖 orgs.json 中需要手工补充的字段`

3. Actions 层
   - 结构化来源页直抓
   - 开放互联网发现
   - 组织映射
   - AI/行动性评分
   - 发布队列 / 审核队列

## 后续升级路线

如果你确认这套信息架构成立，下一轮可以做：

1. 拆成多页面：
   - 首页
   - 组织库页
   - 行动库页
   - 数据来源页

2. 加详情页：
   - 组织详情页
   - 行动详情页

3. 加自动更新：
   - `GitHub Actions`
   - `CSV/JSON` 自动重建
   - 抓取源增量更新

4. 再决定是否切到更完整框架：
   - `Next.js`
   - `Astro`
   - 或静态站继续扩展
