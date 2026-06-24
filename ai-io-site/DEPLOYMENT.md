# GitHub 执行说明

## 目标

1. 不公开原始 `csv/xlsx`
2. 用 GitHub 托管代码、自动更新数据、部署站点
3. 页面只暴露前端需要的 `json`

## 仓库建议

建议把以下内容上传到 GitHub：

- `ai-io-site/`
- `.github/workflows/`
- `.gitignore`

不要上传：

- `AI领域的国际组织.xlsx`
- `international_orgs_seed.csv`
- 各类本地核验缓存

根目录 `.gitignore` 已经为这些原始文件做了排除。

## 本地首次准备

1. 本地先确认 `ai-io-site/data/orgs.json` 已构建好
2. 如需手工补官网，改 `ai-io-site/data/manual/org-overrides.json`
3. 运行：

```powershell
python .\ai-io-site\scripts\build_data.py
python .\ai-io-site\scripts\build_actions.py
```

4. 把生成后的 `json` 一起提交

## GitHub 上的自动流程

已经配置：

1. `.github/workflows/refresh-data.yml`
   - 每日定时刷新组织数据和 actions 数据
   - 自动提交更新后的 `json`

2. `.github/workflows/deploy-pages.yml`
   - `push` 到 `main` 后自动部署 `ai-io-site/` 到 GitHub Pages

## 重要限制

GitHub Pages 本身不提供私有服务端。

所以当前方案是：

- 原始种子表不进仓库
- 仓库中只保留清洗后的 `orgs.json`
- 定时任务基于 `orgs.json + overrides + action sources` 做后续 actions 更新

如果你以后需要：

- 私有后台审核
- 登录态管理
- 服务端 API
- 抓取失败重试队列

那就要从 GitHub Pages 升级到：

- Vercel / Netlify Functions
- Cloudflare Workers
- 或独立后端
