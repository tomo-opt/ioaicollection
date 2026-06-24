# AI IO Site Prototype

这是基于当前文件夹真实数据做的第一轮前端原型。

## 目录

- `index.html`
- `styles.css`
- `app.js`
- `data/orgs.json`
- `data/actions.json`
- `data/review-queue.json`
- `data/source-registry.json`
- `data/manual/org-overrides.json`
- `scripts/build_data.py`
- `scripts/build_actions.py`
- `PROJECT-ARCHITECTURE.md`

## 本地启动

在本目录执行：

```powershell
python -m http.server 4173
```

然后访问：

- `http://localhost:4173/ai-io-site/`

## 当前状态

- 已接入 `international_orgs_seed.csv` 生成组织前端数据
- 已接入 `UN AI Resource Hub` 结构化抓取
- 已接入 `Google News RSS + 阅读式归类` 的开放互联网发现链路
- 已输出 `actions.json`、`review-queue.json`、`source-registry.json`

## 关于你后面人肉补官网

当前数据构建脚本会保留：

- `officialUrl`
- `officialUrlStatus`
- `officialUrlNote`

如果某条官网暂时没有稳定 URL，可以后续直接补到：

- `ai-io-site/data/manual/org-overrides.json`

然后重新运行：

```powershell
python .\ai-io-site\scripts\build_data.py
```

前端不需要改代码。

## Actions 管线

运行：

```powershell
python .\ai-io-site\scripts\build_actions.py
```

会生成：

- `data/actions.json`
- `data/review-queue.json`
- `data/source-registry.json`
- `data/pipeline-status.json`
