# 网站内容维护与更新手册（本地阶段到 GitHub 阶段）

## 一、这份手册是给谁用的

这份手册针对你当前这个本地项目环境编写：

- 项目根目录：`C:\Users\14916\Desktop\ioaicollection`
- 前端目录：`C:\Users\14916\Desktop\ioaicollection\ai-io-site`

适用场景：

1. 你接下来两天先在本地补数据。
2. 本地补完后，再整体上传到 GitHub。
3. 之后优先采用“本地更新文件 -> 上传到 GitHub 覆盖旧文件”的方式维护，而不是完全依赖在线自动维护。

这份手册的目标是让你明确知道：

1. `机构`、`行动`、`资源` 三页分别由哪些文件控制。
2. 以后要改数据时应该改哪个源文件，而不是直接乱改生成文件。
3. 每次改完后应该运行什么命令。
4. 如何确认数据已经成功更新到前端。
5. 如何让新资源接入爬取，如何只让部分资源被爬取。
6. 未来上传 GitHub 后，本地维护和 GitHub 自动部署怎么配合。

---

## 二、整个网站的核心结构

你当前这个项目，最重要的是区分两类文件：

### 1. 源文件

源文件是你平时真正应该维护的地方。

主要包括：

- `C:\Users\14916\Desktop\ioaicollection\international_orgs_seed.csv`
- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\config\action-sources.json`
- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\index.html`
- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\app.js`
- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\styles.css`

### 2. 生成文件

生成文件是脚本跑出来给前端读的，不建议长期手工维护。

主要包括：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\data\orgs.json`
- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\data\actions.json`
- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\data\source-registry.json`
- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\data\pipeline-status.json`
- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\data\review-queue.json`

原则上：

1. `orgs.json` 不要作为主维护入口。
2. `actions.json` 不要作为主维护入口。
3. `source-registry.json` 不要作为主维护入口。
4. 真正维护的是上面的源文件。

---

## 三、三页分别由哪些文件控制

## 1. 机构页

前端读取文件：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\data\orgs.json`

这个文件来自：

- `C:\Users\14916\Desktop\ioaicollection\international_orgs_seed.csv`

生成脚本：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\scripts\build_data.py`

### 机构页维护逻辑

如果你要新增、修改、删除机构数据，优先改：

- `international_orgs_seed.csv`

改完后运行：

```powershell
python ai-io-site\scripts\build_data.py
```

运行完成后，会重新生成：

- `ai-io-site\data\orgs.json`

前端页面就会读取新的机构数据。

---

## 2. 行动页

前端读取文件：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\data\actions.json`

这个文件来自：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\config\action-sources.json`

生成脚本：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\scripts\build_actions.py`

### 行动页维护逻辑

如果你要调整行动来源、接入新的官网页面、改抓取范围、改是否抓取某个来源，优先改：

- `action-sources.json`

改完后运行：

```powershell
python ai-io-site\scripts\build_actions.py
```

运行完成后，会重新生成：

- `ai-io-site\data\actions.json`
- `ai-io-site\data\source-registry.json`
- `ai-io-site\data\pipeline-status.json`
- `ai-io-site\data\review-queue.json`

也就是说，`行动页` 和 `资源页` 的数据更新，其实都跟 `build_actions.py` 有关。

---

## 3. 资源页

前端读取文件：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\data\source-registry.json`

这个文件不是单独维护的，它是由下面两个东西共同决定的：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\config\action-sources.json`
- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\scripts\build_actions.py`

### 资源页维护逻辑

如果你想让资源页多一个资源入口，原则上应该去改：

- `action-sources.json`

然后运行：

```powershell
python ai-io-site\scripts\build_actions.py
```

生成后的 `source-registry.json` 会被资源页读取。

---

## 四、最常用的维护动作清单

## 场景 A：我要补充一个机构

### 该改哪里

改：

- `C:\Users\14916\Desktop\ioaicollection\international_orgs_seed.csv`

### 应该补什么

尽量补这些字段：

1. `规范英文名称`
2. `标准中文名称`
3. `官方网站`
4. `官网参考链接`
5. `UIA公开档案链接`
6. `成立年份`
7. `总部城市`
8. `总部国家或地区`
9. `组织类型`
10. `所属层级`
11. `是否建议前台展示`
12. `项目角色建议`
13. `核验状态`
14. `公开宗旨摘要`

### 改完后怎么更新

运行：

```powershell
python ai-io-site\scripts\build_data.py
```

### 怎么确认成功

确认这几个地方：

1. 终端输出里应看到 `built_records=...`
2. `ai-io-site\data\orgs.json` 时间应更新
3. 本地预览刷新后机构页能看到新条目

---

## 场景 B：我要修改机构页前端显示文案

例如：

1. 改页面标题
2. 改说明文字
3. 改按钮文字
4. 改筛选器名称
5. 改卡片字段名称

### 该改哪里

主要改：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\index.html`
- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\app.js`

如果还涉及样式，再改：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\styles.css`

### 三个文件分别负责什么

#### `index.html`

负责静态结构和固定文案，例如：

1. 页面标题
2. 模块标题
3. 按钮名称
4. 卡片模板
5. 筛选器标签

#### `app.js`

负责动态渲染文案，例如：

1. “当前显示多少条”
2. 空状态提示
3. 某些卡片里的动态文字
4. 资源页的公共说明映射

#### `styles.css`

负责视觉样式，例如：

1. 宽度
2. 排版
3. 字号
4. 卡片间距
5. 手机端展示

---

## 场景 C：我要新增一个行动来源

这类来源指的是：

1. 一个国际组织官网入口
2. 一个专题页
3. 一个活动列表页
4. 一个 AI 专题页面
5. 一个资源库入口

### 该改哪里

改：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\config\action-sources.json`

### 一个来源最重要的字段

通常要明确这些字段：

1. `id`
2. `name`
3. `labelZh`
4. `kind`
5. `kindZh`
6. `strategy`
7. `enabled`
8. `url`
9. `query`
10. `updateFrequency`
11. `outputObject`
12. `notesZh`

### 先判断你要接入的是哪一类

#### 第一类：结构化专题页

特点：

1. 页面上有清晰列表
2. 页面 HTML 结构比较固定
3. 可以直接抓条目

适合：

- 类似 `UN AI Resource Hub activities.php`

这种情况通常要：

1. 在 `action-sources.json` 中新增一条 source
2. 给它一个合适的 `strategy`
3. 如果现有 `build_actions.py` 没有支持该类结构，就补写解析逻辑

#### 第二类：官网发现型来源

特点：

1. 官网内容分散
2. 没有统一公开列表
3. 更适合用 RSS / 新闻发现 / 公开站内发现

适合：

- OECD
- UNESCO
- Council of Europe
- ITU / AI for Good

这种情况通常要：

1. 在 `action-sources.json` 新增来源
2. 提供合适的 `url`
3. 写清楚 `query`
4. 运行 `build_actions.py`

---

## 场景 D：我新增了一个资源入口，但不一定想让它立即参与爬取

这是你之后很可能会用到的。

## 做法 1：只展示在资源页，但不参与实际抓取

推荐做法：

1. 在 `action-sources.json` 中新增该资源
2. 设定：

```json
"enabled": false
```

这样做的效果通常是：

1. 资源页仍可作为“资源入口”展示
2. 但这个来源不会被 `build_actions.py` 实际抓取

注意：

因为 `source-registry.json` 是由脚本生成的，所以资源入口最好还是通过 `action-sources.json` 管，而不是手工改 `source-registry.json`。

## 做法 2：展示且参与抓取

如果你希望它既出现在资源页，也参与行动抓取，就设：

```json
"enabled": true
```

然后根据来源类型补齐：

1. `strategy`
2. `url`
3. `query`
4. `notesZh`

再运行：

```powershell
python ai-io-site\scripts\build_actions.py
```

---

## 场景 E：我只想抓部分资源，而不是抓资源页里的全部资源

这个需求是合理的，也应该这样做。

资源页是对用户开放的“可访问资源库”，但并不意味着每一个资源入口都适合立刻纳入自动抓取。

### 推荐策略

把资源分成三类：

#### 第一类：只展示，不抓取

适合：

1. 只是入口页
2. 结构不稳定
3. 暂时没有时间做解析
4. 需要先人工观察

处理方式：

- `enabled: false`

#### 第二类：展示 + 低风险抓取

适合：

1. 页面结构稳定
2. 公开可访问
3. 有近期更新
4. 内容确实是“国际组织 AI 行动”

处理方式：

- `enabled: true`

#### 第三类：展示 + 待补专用解析

适合：

1. 资源价值很高
2. 但不能靠通用发现法抓准
3. 需要未来单独写解析器

处理方式：

1. 先放进资源页
2. 先不抓，或者只做保守抓取
3. 等你确定优先级后再补代码

### 你当前最适合的原则

建议你不要一口气抓所有资源。

优先抓：

1. 联合国专题页
2. ITU / AI for Good
3. UNESCO AI 页面
4. Council of Europe AI 页面
5. 结构清晰、更新稳定的官方专题入口

暂缓抓：

1. 聚合类页面
2. 结构极不稳定的栏目页
3. 需要登录的页面
4. 更像目录页而不是内容页的资源入口

---

## 五、行动页抓取机制现在是怎么运作的

当前抓取主逻辑在：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\scripts\build_actions.py`

### 当前大致分为两层

#### 第一层：结构化来源直采

代表：

- `UN AI Resource Hub`

特点：

1. 直接从公开页面卡片抓取
2. 结果更稳
3. 通常更适合直接发布到前端

#### 第二层：官网发现层

代表：

- OECD.AI
- Council of Europe
- UNESCO
- ITU / AI for Good

特点：

1. 先从公开来源中发现候选
2. 再根据标题、来源、AI 词、行动词做归类
3. 只有较稳的条目进入 `actions.json`
4. 不够稳的进入 `review-queue.json`

### 现在为什么不是所有抓到的都直接公开

因为你的目标不是“泛 AI 新闻”。

你要的是：

- 国际组织自身的 AI 行动

而不是：

- AI 相关新闻
- 外部 AI 舆情
- 站内转载

所以当前脚本会做一层相对保守的筛选。

---

## 六、如果我要更新行动抓取机制，应该怎么做

## 1. 改来源配置

如果只是：

1. 换一个站
2. 补一个站
3. 改查询词
4. 暂停某个来源

优先改：

- `action-sources.json`

## 2. 改抓取逻辑

如果是：

1. 现有策略抓不准
2. 需要为某个站点单独解析
3. 需要改变发布 / 候选判断逻辑

就改：

- `build_actions.py`

常见可改位置包括：

1. `parse_un_aihub()`
2. `parse_google_news_rss()`
3. `score_item()`
4. `review_status_for()`
5. `classify_and_partition()`

### 一个实际建议

以后遇到特别重要的来源，不建议只靠通用发现逻辑。

更稳的做法是：

1. 先把它作为资源页入口接进去
2. 再为它补一个专门解析函数
3. 让它从“发现型”升级成“结构型”

这样数据质量会明显更好。

---

## 七、更新了新资源后，如何接入爬取

## 步骤 1：先决定是否立刻抓

先问自己三个问题：

1. 这个资源页是否公开可访问
2. 它上面是否真的有“国际组织 AI 行动”
3. 它是否值得持续抓，而不是一次性看一眼

如果答案大体是“是”，再进入下一步。

## 步骤 2：把资源写入 `action-sources.json`

至少补：

1. `id`
2. `labelZh`
3. `url`
4. `strategy`
5. `enabled`
6. `notesZh`

## 步骤 3：决定抓取方式

### 方式 A：暂时只展示

```json
"enabled": false
```

### 方式 B：直接纳入抓取

```json
"enabled": true
```

### 方式 C：先展示，再等以后补专用解析

也是先：

```json
"enabled": false
```

等你准备好了，再切到 `true`。

## 步骤 4：运行更新脚本

```powershell
python ai-io-site\scripts\build_actions.py
```

## 步骤 5：确认结果

至少检查这四处：

1. 终端输出
2. `actions.json`
3. `source-registry.json`
4. 预览页面

---

## 八、如何确认接入的资源都被爬取了

这一步非常重要，不要只看网页。

## 1. 看终端输出

运行：

```powershell
python ai-io-site\scripts\build_actions.py
```

正常会看到类似：

```text
published=10
review=16
sources=6
```

这只能说明脚本跑完了，不能说明每个来源都有效。

## 2. 看 `source-registry.json`

检查：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\data\source-registry.json`

重点看每一项：

1. `lastRunAt`
2. `lastResult`
3. `publishedCount`
4. `reviewCount`

### 怎么理解

#### `lastResult = ok`

表示脚本这一轮至少跑到了这个来源。

#### `publishedCount > 0`

表示这个来源有条目被公开放进前端。

#### `reviewCount > 0`

表示这个来源抓到了候选，但还没有进入前端公开展示层。

#### `publishedCount = 0` 且 `reviewCount = 0`

可能有三种情况：

1. 真没抓到
2. 抓到但被全部过滤掉
3. 站点本轮确实没有符合条件的新内容

这时就要结合 `actions.json` 和资源实际页面一起判断。

## 3. 看 `actions.json`

检查：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\data\actions.json`

重点确认：

1. 有没有来自你刚加的新来源的条目
2. 日期是否合理
3. 标题是否像“国际组织行动”而不是泛新闻

## 4. 看 `review-queue.json`

检查：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\data\review-queue.json`

这个文件可以告诉你：

1. 来源到底有没有抓到东西
2. 只是没进公开层，还是压根没抓到

---

## 九、前端显示文字怎么改

这部分你之后会频繁碰到。

## 1. 改固定文案

例如：

1. 页面标题
2. 模块标题
3. 卡片标签
4. 按钮文字

改：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\index.html`

## 2. 改动态生成文案

例如：

1. “当前显示 X 条”
2. 空状态文案
3. 某个资源的描述说明

改：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\app.js`

你现在资源页有一部分公共说明，就是在 `app.js` 里通过映射控制。

## 3. 改排版样式

例如：

1. 宽度太窄
2. 卡片太高
3. 模块导航太挤
4. 手机端太丑

改：

- `C:\Users\14916\Desktop\ioaicollection\ai-io-site\styles.css`

---

## 十、本地更新后的标准操作顺序

以后你每次本地维护，建议固定按这个顺序做。

## 1. 改机构数据

如果动了机构：

```powershell
python ai-io-site\scripts\build_data.py
```

## 2. 改行动 / 资源来源

如果动了来源或抓取逻辑：

```powershell
python ai-io-site\scripts\build_actions.py
```

## 3. 启动本地预览

如果本地服务没开：

```powershell
python -m http.server 4175 --bind 127.0.0.1
```

如果你希望后台运行，可以继续沿用我们现在已经在用的本地预览方式。

## 4. 打开预览检查

检查：

- `http://127.0.0.1:4175/ai-io-site/?v=20260623-1`
- `http://127.0.0.1:4175/ai-io-site/?v=20260623-1&view=organizations`
- `http://127.0.0.1:4175/ai-io-site/?v=20260623-1&view=actions`
- `http://127.0.0.1:4175/ai-io-site/?v=20260623-1&view=sources`

之所以带 `v=20260623-1`，是为了尽量避免本地缓存导致你看到旧的 `css/js`。

---

## 十一、当前本地阶段最推荐的维护方式

你已经明确说了，短期内更倾向于：

- 本地更新文件
- 本地验证
- 再上传 GitHub 覆盖旧文件

这个方式在你当前阶段是合理的。

### 推荐原因

1. 你现在还在快速调整结构
2. 数据源和规则还在变
3. 你需要能随时人工检查结果
4. 直接依赖在线自动更新，风险会更高

### 当前最稳的操作模式

1. 本地改源文件
2. 本地跑脚本生成 JSON
3. 本地打开网页检查
4. 确认无误后上传 GitHub

---

## 十二、未来上传 GitHub 后，建议怎么做

你当前仓库里已经有工作流：

- `C:\Users\14916\Desktop\ioaicollection\.github\workflows\refresh-data.yml`
- `C:\Users\14916\Desktop\ioaicollection\.github\workflows\deploy-pages.yml`

而且当前脚本里的绝对路径问题已经改成了相对路径，具备上 GitHub 的基础条件。

## 推荐你未来采用“双轨制”

### 轨道 1：本地主维护

适合：

1. 改机构库
2. 改资源入口
3. 改抓取策略
4. 改前端展示

流程：

1. 本地修改
2. 本地跑脚本
3. 本地预览
4. 再 push 到 GitHub

### 轨道 2：GitHub 定时刷新

适合：

1. 在你没有本地手动维护的日子里，维持基本更新
2. 自动刷新已有来源
3. 自动重新部署页面

流程是：

1. `refresh-data.yml` 定时跑数据刷新
2. 自动提交新的 `data` 文件
3. `deploy-pages.yml` 自动部署页面

### 你后续最适合的实际策略

不是“完全交给 GitHub 自动跑”，而是：

1. 平时你本地维护为主
2. GitHub 定时更新为辅

---

## 十三、上传 GitHub 后要做什么

## 1. 上传整个项目

确保这些目录和文件都进仓库：

1. `ai-io-site`
2. `.github/workflows`
3. `international_orgs_seed.csv`

## 1.1 如果你现在还没有把本地项目上传到 GitHub

可以按下面步骤操作。

### 第一步：在 GitHub 网站上新建仓库

建议：

1. 先登录你的 GitHub 账号
2. 点击 `New repository`
3. 仓库名建议与你当前项目对应，例如：
   - `ioaicollection`
   - 或你之后想公开展示的正式仓库名
4. 建议先不要在 GitHub 页面里额外勾选初始化 `README`、`.gitignore`、`LICENSE`

原因是你本地已经有完整项目，避免第一次 push 时产生不必要冲突。

### 第二步：在本地项目根目录初始化 / 检查 Git

你当前项目根目录是：

- `C:\Users\14916\Desktop\ioaicollection`

如果这个目录还没有 Git 仓库，就在这里打开 PowerShell，运行：

```powershell
git init
```

如果已经是 Git 仓库，这一步跳过。

### 第三步：把 GitHub 仓库地址关联到本地

先查看当前远程仓库：

```powershell
git remote -v
```

如果还没有远程仓库，就添加：

```powershell
git remote add origin 你的GitHub仓库地址
```

例如：

```powershell
git remote add origin https://github.com/你的用户名/你的仓库名.git
```

如果已经配过旧地址，但想替换成新仓库地址，可以改成：

```powershell
git remote set-url origin https://github.com/你的用户名/你的仓库名.git
```

### 第四步：把当前本地内容提交到 Git

建议先检查一下当前变更：

```powershell
git status
```

然后提交：

```powershell
git add .
git commit -m "init: local project setup"
```

如果之前已经提交过，只需要对本次新增或修改内容重新提交即可。

### 第五步：推送到 GitHub

如果默认分支还不是 `main`，建议先切到 `main`：

```powershell
git branch -M main
```

然后推送：

```powershell
git push -u origin main
```

第一次 push 成功后，后续就可以直接：

```powershell
git push
```

### 第六步：上传后先检查 GitHub 仓库页面

重点确认这些内容都已经在仓库里：

1. `ai-io-site/`
2. `.github/workflows/`
3. `international_orgs_seed.csv`
4. `ai-io-site/scripts/build_data.py`
5. `ai-io-site/scripts/build_actions.py`

如果这些都在，说明项目主体已经成功上 GitHub。

## 2. 打开 GitHub Actions

进入仓库设置，确保：

1. Actions 没被禁用
2. 工作流可执行

## 3. 配置 GitHub Pages

在仓库 `Settings -> Pages` 中：

1. 选择 `GitHub Actions`
2. 不要切到其他部署方式

## 3.1 GitHub Pages 具体怎么部署起来

你当前项目已经准备了工作流：

- `.github/workflows/deploy-pages.yml`

这个工作流的作用是：

1. 当 `main` 分支里 `ai-io-site/**` 有更新时自动触发
2. 把 `ai-io-site` 目录整体作为静态站点发布到 GitHub Pages

也就是说，你不需要再单独手工构建前端。

### 实际部署步骤

#### 步骤 A：确认仓库默认分支是 `main`

因为当前工作流监听的是：

- `main`

如果你的默认分支不是 `main`，要么：

1. 把默认分支改成 `main`

要么：

2. 修改 `.github/workflows/deploy-pages.yml` 里的分支监听配置

#### 步骤 B：去仓库设置里打开 Pages

在 GitHub 仓库页面中：

1. 点击 `Settings`
2. 进入 `Pages`
3. 在 `Build and deployment` 中选择：
   - `Source: GitHub Actions`

不要选传统的：

- `Deploy from a branch`

因为你现在已经是工作流部署模式。

#### 步骤 C：检查 Actions 是否成功执行

上传完成后，进入：

- `Actions`

你应该至少看到两个工作流：

1. `Deploy Pages`
2. `Refresh Data`

先重点看：

- `Deploy Pages`

它成功后，GitHub 会给出一个 Pages 访问地址。

#### 步骤 D：找到 GitHub Pages 的线上地址

通常部署成功后，会出现类似：

```text
https://你的用户名.github.io/你的仓库名/
```

因为当前工作流直接发布的是 `ai-io-site` 目录本身，所以理论上线上首页应该就是这个仓库根 Pages 地址，而不是再额外加一层 `/ai-io-site/`。

也就是说，GitHub Pages 上线后通常访问方式是：

```text
https://你的用户名.github.io/你的仓库名/
```

而不是：

```text
https://你的用户名.github.io/你的仓库名/ai-io-site/
```

### 如果部署成功但页面是空白或样式错乱，优先检查这几项

1. `Deploy Pages` 工作流是否真的成功
2. `Actions` 中是否有报错
3. `index.html` 是否在 `ai-io-site/` 根目录下
4. `styles.css`、`app.js`、`data/*.json` 是否都在 `ai-io-site/` 下
5. 前端路径是否仍然是相对路径

你当前项目这点已经基本是按相对路径写的，理论上适合 Pages 部署。

## 4. 首次手动运行一次

建议首次先手动运行：

- `Refresh Data`

确认：

1. 数据能成功生成
2. 工作流能成功 commit
3. Pages 能成功更新

## 4.1 建议你第一次上传 GitHub 后的最稳操作顺序

建议按下面顺序做，而不要一上来就同时验证所有东西。

### 第一步：先只验证静态页面能否上线

先 push 当前项目到 GitHub。

然后重点观察：

1. `Deploy Pages` 是否成功
2. GitHub Pages 地址能否打开
3. 机构页、行动页、资源页能否正常切换
4. 页面是否能正常读取 `data/*.json`

如果这一层成功，说明：

1. 仓库结构没问题
2. Pages 配置没问题
3. 前端相对路径没问题

### 第二步：再验证数据刷新工作流

然后再去看：

- `Refresh Data`

先手动运行一次。

重点检查：

1. `build_data.py` 是否成功
2. `build_actions.py` 是否成功
3. 是否成功 commit 新数据
4. commit 后是否再次触发 `Deploy Pages`

### 第三步：最后再决定要不要开启长期自动刷新

如果你短期还是以“本地维护 + 手工上传”为主，可以先这样用：

1. 保留工作流不删
2. 先不完全依赖它每日自动刷新
3. 主要仍然靠你本地更新后 push

这样风险更低。

---

## 十四、如何判断当前自动更新是否可靠

答案是：目前已经“能跑”，但还不能说“完全可靠”。

### 当前已经具备的能力

1. 可本地生成机构数据
2. 可本地生成行动数据
3. 可本地生成资源页数据
4. 可在 GitHub 定时运行刷新
5. 可在 GitHub 自动重新部署

### 当前仍然存在的风险

1. 外部页面结构可能改版
2. 有些官网会限流或 403
3. 通用发现策略精度仍不如专用解析
4. 个别来源会抓到候选，但不一定适合直接公开

### 你应当如何判断某次更新是否可信

不要只看脚本是否跑通，要同时看：

1. `source-registry.json`
2. `actions.json`
3. 本地或线上前端展示
4. 新增条目是否真的像“国际组织 AI 行动”

---

## 十五、你之后最常见的问题及处理办法

## 1. 我改了网页但页面没变化

先检查：

1. 是否只是改了生成文件，而不是源文件
2. 是否忘了重新运行脚本
3. 是否本地浏览器缓存了旧的 `css/js`

建议使用带版本参数的本地预览地址：

- `http://127.0.0.1:4175/ai-io-site/?v=20260623-1`

## 2. 我新增了来源，但资源页没出现

检查：

1. 是否已写入 `action-sources.json`
2. 是否重新运行了 `build_actions.py`
3. `source-registry.json` 是否真的被更新

## 3. 我新增了来源，但行动页没有条目

检查：

1. 这个来源是否 `enabled: true`
2. 这个来源本轮是否真的抓到内容
3. 内容是否被压进了 `review-queue.json`
4. 来源本身是否更适合以后写专用解析

## 4. 我只想把某个资源放在资源页，不想爬

处理方式：

在 `action-sources.json` 中保留该资源，但设：

```json
"enabled": false
```

## 5. 我想让某个来源参与抓取，但先不要对外展示太多

当前可行做法：

1. 让它参与抓取
2. 观察 `review-queue.json`
3. 等确认规律后，再调整 `build_actions.py` 的发布逻辑

---

## 十六、建议你接下来两天的本地工作顺序

## 第 1 步：补机构

优先完善：

- `international_orgs_seed.csv`

因为机构库是整个网站的基础。

## 第 2 步：补资源入口

继续补：

- `action-sources.json`

但先不要急着全部打开抓取。

## 第 3 步：决定哪些资源立刻抓

优先选：

1. 结构稳定
2. 内容确实是国际组织行动
3. 页面近期确实有更新

## 第 4 步：运行脚本

```powershell
python ai-io-site\scripts\build_data.py
python ai-io-site\scripts\build_actions.py
```

## 第 5 步：看本地页面

逐页检查：

1. 机构页
2. 行动页
3. 资源页

## 第 6 步：准备上传 GitHub

等你本地满意后，再整体 push。

---

## 十七、最后的操作总表

### 机构数据更新

改：

- `international_orgs_seed.csv`

运行：

```powershell
python ai-io-site\scripts\build_data.py
```

### 行动来源更新

改：

- `ai-io-site\config\action-sources.json`

运行：

```powershell
python ai-io-site\scripts\build_actions.py
```

### 资源页入口更新

改：

- `ai-io-site\config\action-sources.json`

运行：

```powershell
python ai-io-site\scripts\build_actions.py
```

### 前端文案更新

改：

- `ai-io-site\index.html`
- `ai-io-site\app.js`

### 前端样式更新

改：

- `ai-io-site\styles.css`

### 本地预览

打开：

- `http://127.0.0.1:4175/ai-io-site/?v=20260623-1`

### GitHub 之后的推荐模式

采用：

1. 本地更新源文件
2. 本地生成 JSON
3. 本地检查
4. 上传 GitHub 覆盖旧文件
5. GitHub Actions 作为辅助自动刷新

---

如果你后面愿意，我下一步可以继续给你再补一份更偏“表格式执行版”的清单：

1. 哪类改动改哪个文件
2. 改完运行哪条命令
3. 更新后看哪个结果文件
4. 页面上应该去哪一页检查

这样你后面维护时会更像对照工单，而不是读长文说明。
