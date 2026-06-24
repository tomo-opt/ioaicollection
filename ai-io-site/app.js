const state = {
  orgs: [],
  actions: [],
  sources: [],
  pipelineStatus: null,
  activeModule: "organizations",
};

const elements = {
  heroOrgCount: document.querySelector("#hero-org-count"),
  search: document.querySelector("#search-input"),
  typeFilter: document.querySelector("#type-filter"),
  officialFilter: document.querySelector("#official-filter"),
  resultsSummary: document.querySelector("#results-summary"),
  orgGrid: document.querySelector("#org-grid"),
  actionDateFilter: document.querySelector("#action-date-filter"),
  actionSourceFilter: document.querySelector("#action-source-filter"),
  actionsSummary: document.querySelector("#actions-summary"),
  actionsGrid: document.querySelector("#actions-grid"),
  actionCount: document.querySelector("#action-count"),
  actionSourceCount: document.querySelector("#action-source-count"),
  sourceCount: document.querySelector("#source-count"),
  sourceKindCount: document.querySelector("#source-kind-count"),
  sourceGrid: document.querySelector("#source-grid"),
  moduleTabs: [...document.querySelectorAll(".module-tab")],
  modulePanels: [...document.querySelectorAll(".module-panel")],
};

const TYPE_MAP = {
  "协会/学会/联盟": "国际组织",
  "倡议/伙伴关系/基金/委员会": "倡议与合作机制",
  "研究中心/网络/联合体": "研究网络与中心",
  "会议系列/活动平台": "会议与活动平台",
  "规范文件/框架": "规则与框架",
  "待人工细分": "其他相关条目",
};

const RESOURCE_COPY = {
  "un-aihub-activities": {
    description: "联合国体系下可直接浏览的 AI 行动专题页，适合查看项目、报告、倡议与治理相关条目。",
    content: "联合国 AI 行动与项目",
    useCase: "快速浏览联合国体系近期 AI 动态",
  },
  "oecd-ai-open-web": {
    description: "OECD.AI 的官方入口，适合继续查看政策观察、专题研究与制度讨论。",
    content: "政策观察与专题研究",
    useCase: "延伸阅读 OECD.AI 议题页面",
  },
  "coe-ai-open-web": {
    description: "欧洲委员会人工智能页面入口，可继续查看公约、指导说明、会议动态与治理讨论。",
    content: "治理文件与会议动态",
    useCase: "了解欧洲委员会 AI 治理进展",
  },
  "unesco-ai-open-web": {
    description: "UNESCO 人工智能页面入口，覆盖 AI 伦理、教育、能力建设与规范工具。",
    content: "AI 伦理、教育与框架工具",
    useCase: "查找 UNESCO AI 规范与教育资源",
  },
  "itu-ai-open-web": {
    description: "ITU 与 AI for Good 相关公开页面入口，适合继续查看标准化、能力建设和专题活动。",
    content: "标准化、培训与活动平台",
    useCase: "进入 ITU / AI for Good 专题资源",
  },
  "seed-org-open-web": {
    description: "围绕已收录国际组织延伸出的公开入口集合，可作为继续查找机构页面的补充线索。",
    content: "机构延伸入口",
    useCase: "按组织继续扩展检索范围",
  },
};

function uniq(values) {
  return [...new Set(values.filter(Boolean))].sort((a, b) => a.localeCompare(b, "zh-CN"));
}

function truncate(text, limit = 200) {
  if (!text) return "暂无公开摘要";
  return text.length > limit ? `${text.slice(0, limit)}...` : text;
}

function isUsableUrl(url) {
  return typeof url === "string" && /^https?:\/\//i.test(url);
}

function formatDate(value) {
  if (!value) return "未标注";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return date.toISOString().slice(0, 10);
}

function formatYear(value) {
  if (!value) return "未公开";
  return String(value).replace(/\.0$/, "");
}

function getDisplayType(org) {
  return TYPE_MAP[org.orgType] || "其他相关条目";
}

function getEffectiveDate(action) {
  return action.effectiveDate || action.publishedAt || action.lastSeenAt || "";
}

function getSixMonthsAgoDate() {
  const date = new Date();
  date.setDate(date.getDate() - 180);
  return date.toISOString().slice(0, 10);
}

async function loadJson(path) {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`Failed to load ${path}`);
  }
  return response.json();
}

function updateHero() {
  elements.heroOrgCount.textContent = state.orgs.length;
  elements.actionSourceCount.textContent = state.sources.length;
  elements.sourceCount.textContent = state.sources.length;
  elements.sourceKindCount.textContent = uniq(state.sources.map((source) => source.kindZh || source.kind)).length;
}

function populateOrgFilters() {
  uniq(state.orgs.map((org) => getDisplayType(org))).forEach((value) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    elements.typeFilter.append(option);
  });
}

function populateActionFilters() {
  uniq(state.actions.map((action) => action.sourceLabelZh || action.sourceName)).forEach((value) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    elements.actionSourceFilter.append(option);
  });

  const sixMonthsAgo = getSixMonthsAgoDate();
  const today = new Date().toISOString().slice(0, 10);
  elements.actionDateFilter.min = sixMonthsAgo;
  elements.actionDateFilter.max = today;
  elements.actionDateFilter.value = sixMonthsAgo;
}

function filterOrgs() {
  const searchTerm = elements.search.value.trim().toLowerCase();
  const type = elements.typeFilter.value;
  const official = elements.officialFilter.value;

  return state.orgs.filter((org) => {
    const haystack = [
      org.nameEn,
      org.nameZh,
      org.acronym,
      org.aims,
      org.hqCountry,
      org.hqCity,
      org.orgType,
      getDisplayType(org),
    ]
      .join(" ")
      .toLowerCase();

    const matchesSearch = !searchTerm || haystack.includes(searchTerm);
    const matchesType = !type || getDisplayType(org) === type;
    const matchesOfficial =
      !official ||
      (official === "has-site" && isUsableUrl(org.officialUrl)) ||
      (official === "no-site" && !isUsableUrl(org.officialUrl));

    return matchesSearch && matchesType && matchesOfficial;
  });
}

function renderOrgs() {
  const items = filterOrgs();
  elements.orgGrid.innerHTML = "";

  if (!items.length) {
    elements.orgGrid.innerHTML = `<div class="empty-state">当前筛选条件下没有匹配的机构。</div>`;
    elements.resultsSummary.textContent = "共 0 条";
    return;
  }

  const template = document.querySelector("#org-card-template");
  const fragment = document.createDocumentFragment();

  items.forEach((org) => {
    const node = template.content.cloneNode(true);
    node.querySelector(".org-category").textContent = getDisplayType(org);
    node.querySelector(".org-name").textContent = org.nameEn;
    node.querySelector(".org-chip").textContent = org.level === "event" ? "活动/会议" : "机构";
    node.querySelector(".org-cn").textContent = org.nameZh || "中文名称待补";
    node.querySelector(".org-aims").textContent = truncate(org.aims, 220);
    node.querySelector(".org-founded").textContent = formatYear(org.foundedYear);
    node.querySelector(".org-location").textContent = [org.hqCity, org.hqCountry].filter(Boolean).join(", ") || "未公开";
    node.querySelector(".org-type").textContent = org.orgType || "未标注";

    const orgLink = node.querySelector(".org-link");
    if (isUsableUrl(org.officialUrl)) {
      orgLink.href = org.officialUrl;
      orgLink.textContent = "访问官网";
    } else {
      orgLink.removeAttribute("href");
      orgLink.textContent = "官网待补";
      orgLink.classList.add("ghost");
      orgLink.setAttribute("aria-disabled", "true");
    }

    fragment.append(node);
  });

  elements.orgGrid.append(fragment);
  elements.resultsSummary.textContent = `当前显示 ${items.length} / ${state.orgs.length} 条`;
}

function filterActions() {
  const dateAfter = elements.actionDateFilter.value;
  const source = elements.actionSourceFilter.value;

  return state.actions
    .filter((action) => {
      const actionDate = getEffectiveDate(action).slice(0, 10);
      const matchesDate = !dateAfter || !actionDate || actionDate >= dateAfter;
      const publicSource = action.sourceLabelZh || action.sourceName;
      const matchesSource = !source || publicSource === source;
      return matchesDate && matchesSource;
    })
    .sort((a, b) => getEffectiveDate(b).localeCompare(getEffectiveDate(a)));
}

function renderActions() {
  const items = filterActions();
  elements.actionsGrid.innerHTML = "";
  elements.actionCount.textContent = items.length;

  if (!items.length) {
    elements.actionsGrid.innerHTML = `<div class="empty-state">当前时间范围和来源条件下还没有可展示的行动。</div>`;
    elements.actionsSummary.textContent = "当前无结果";
    return;
  }

  const template = document.querySelector("#action-card-template");
  const fragment = document.createDocumentFragment();

  items.forEach((action) => {
    const node = template.content.cloneNode(true);
    node.querySelector(".action-title").textContent = action.title || "未命名行动";
    node.querySelector(".action-date-inline").textContent = `日期：${formatDate(getEffectiveDate(action))}`;
    node.querySelector(".action-org-line").textContent = action.sourceOrg || action.sourceOrgLabel || "发起机构待识别";
    node.querySelector(".action-summary").textContent = truncate(action.summary, 260);
    node.querySelector(".action-date-badge").textContent = formatDate(getEffectiveDate(action));
    node.querySelector(".action-link").href = action.sourceUrl || action.publisherUrl || "#";
    fragment.append(node);
  });

  elements.actionsGrid.append(fragment);
  elements.actionsSummary.textContent = `当前显示 ${items.length} 条；时间范围限定为近半年`;
}

function renderSources() {
  elements.sourceGrid.innerHTML = "";

  if (!state.sources.length) {
    elements.sourceGrid.innerHTML = `<div class="empty-state">当前还没有可展示的来源。</div>`;
    return;
  }

  const template = document.querySelector("#source-card-template");
  const fragment = document.createDocumentFragment();

  state.sources.forEach((source) => {
    const publicCopy = RESOURCE_COPY[source.id] || {};
    const node = template.content.cloneNode(true);
    node.querySelector(".source-kind").textContent = source.kindZh || source.kind || "公开来源";
    node.querySelector(".source-name").textContent = source.labelZh || source.name;
    node.querySelector(".source-notes").textContent = publicCopy.description || source.notesZh || source.notes || "";
    node.querySelector(".source-output").textContent = publicCopy.content || "公开资源入口";
    node.querySelector(".source-frequency").textContent = publicCopy.useCase || "继续延伸阅读";
    node.querySelector(".source-link").href = source.url;
    fragment.append(node);
  });

  elements.sourceGrid.append(fragment);
}

function switchModule(nextModule) {
  state.activeModule = nextModule;

  elements.moduleTabs.forEach((tab) => {
    tab.classList.toggle("is-active", tab.dataset.moduleTarget === nextModule);
  });

  elements.modulePanels.forEach((panel) => {
    panel.classList.toggle("is-active", panel.dataset.modulePanel === nextModule);
  });

  const url = new URL(window.location.href);
  url.searchParams.set("view", nextModule);
  window.history.replaceState({}, "", url);
}

function bindEvents() {
  [elements.search, elements.typeFilter, elements.officialFilter].forEach((el) => {
    el.addEventListener("input", renderOrgs);
    el.addEventListener("change", renderOrgs);
  });

  [elements.actionDateFilter, elements.actionSourceFilter].forEach((el) => {
    el.addEventListener("input", renderActions);
    el.addEventListener("change", renderActions);
  });

  elements.moduleTabs.forEach((tab) => {
    tab.addEventListener("click", () => switchModule(tab.dataset.moduleTarget));
  });
}

async function init() {
  try {
    const [orgs, actions, sources, pipelineStatus] = await Promise.all([
      loadJson("./data/orgs.json"),
      loadJson("./data/actions.json"),
      loadJson("./data/source-registry.json"),
      loadJson("./data/pipeline-status.json"),
    ]);

    state.orgs = orgs;
    state.actions = actions;
    state.sources = sources;
    state.pipelineStatus = pipelineStatus;

    updateHero();
    populateOrgFilters();
    populateActionFilters();
    renderOrgs();
    renderActions();
    renderSources();
    bindEvents();
    const requestedView = new URL(window.location.href).searchParams.get("view");
    const allowedViews = new Set(["organizations", "actions", "sources"]);
    switchModule(allowedViews.has(requestedView) ? requestedView : "organizations");
  } catch (error) {
    console.error(error);
    elements.orgGrid.innerHTML = `<div class="empty-state">数据加载失败，请确认页面通过本地服务或 GitHub Pages 打开。</div>`;
  }
}

init();
