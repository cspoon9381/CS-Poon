# 不用 Slack 也能用 Cursor Cloud Agents

**結論：放棄連 Slack。** Cursor 不依賴 Slack；你現在的 Desktop / Web 啟動方式已足夠。

本 repo（`CS-Poon`）已接好 GitHub，建議改用下面替代路徑。

## 建議優先順序

| 優先 | 方式 | 適合情境 | 怎麼做 |
| --- | --- | --- | --- |
| 1 | **Cursor Desktop** | 日常改 code、設計迭代 | Agent 輸入框選 **Cloud**，直接下任務 |
| 2 | **Cursor Web** | 手機／另一台電腦跟進度 | 開 [cursor.com/agents](https://cursor.com/agents) |
| 3 | **GitHub `@cursor`** | Issue／PR 上委派、團隊協作 | 在 Issue 或 PR 留言 `@cursor` + 任務說明 |
| 4 | **Automations（非 Slack）** | 排程、PR 事件、Webhook | Dashboard → Automations；觸發選 Schedule／GitHub／Webhook |
| 5 | **iOS／Web PWA** | 外出查看與下單 | 官方 iOS App，或 Chrome 安裝 agents 網站 |
| 6 | **Cloud Agents API** | 腳本／內部工具觸發 | 見 [API 文件](https://cursor.com/docs/cloud-agent/api/endpoints) |

不要用：**Slack `@cursor`**、Slack Automations 觸發。

## GitHub 替代（推薦給本 repo）

1. 確認 Integrations 已連 GitHub，且 `cspoon9381/CS-Poon` 在授權範圍內。
2. 開一個 Issue（或 PR），留言例如：

```text
@cursor 幫我在這個 repo 加一個 hello.py，執行後印出 Hello, CS
```

3. Agent 會開 branch、改 code、必要時開 PR；在 [Agents](https://cursor.com/agents) 跟進度。

官方說明：[Cloud Agents](https://cursor.com/docs/cloud-agent)、[GitHub 整合](https://cursor.com/docs/integrations/github)。

## Automations（略過 Slack）

可用觸發（**不要選 Slack**）：

- **Scheduled** — cron／固定週期
- **Source control** — PR 開立、推送、合併、branch push、CI 完成、PR 留言
- **Webhook** — 對你自己的系統 POST
- **Linear／PagerDuty／Sentry** — 若你有在用再接

入口：[Automations 說明](https://cursor.com/docs/cloud-agent/automations)。

## 對照：Slack 本來在做什麼 → 改用什麼

| 以前用 Slack 想做的事 | 改用 |
| --- | --- |
| 打字叫 agent 開工 | Desktop Cloud 或 Web Agents |
| 手機看進度 | Web Agents 或 iOS |
| 頻道裡自動回應訊息 | Automations：GitHub／Webhook／排程 |
| 跟隊友分享一次 run | 分享 agent URL（同 team + 有 repo 權限） |

## 不要做的事

- 不要再安裝／授權 Cursor Slack app
- 不要為了「能叫 agent」去等 Slack workspace admin 核准
- 不要把 Slack token 寫進這個 repo

## 參考連結

- [Cloud Agents 總覽](https://cursor.com/docs/cloud-agent)
- [Automations](https://cursor.com/docs/cloud-agent/automations)
- [GitHub 整合](https://cursor.com/docs/integrations/github)
- [Agents 控制台](https://cursor.com/agents)
