# Software Company 外掛套件

## 用途

- 提供可從 Codex App 安裝的 Software Company 工作流程。

## 責任範圍

- 本層管理 `plugin.json` 的識別、版本、桌面本機執行設定與顯示資訊。根層管理 marketplace。

## 本地契約

- 套件包含技能及其參考文件，使用目前 Codex App 的訂閱、工作階段與工作區。
- `plugin.json` 的名稱須與 marketplace 一致。總入口與四個模式入口各在 `skills/` 下提供一份 `SKILL.md`。

## 工作指引

- 變更套件識別或封裝時同步檢查 marketplace、README 與套件測試。

## 驗證

- 在根目錄執行 `python -X utf8 -m unittest discover -s tests -v`。

## 子層 DOX 索引

- [技能入口](skills/AGENTS.md) 管理可供 Codex 探索的模式入口與共用流程的索引。
