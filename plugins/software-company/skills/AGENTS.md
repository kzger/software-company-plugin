# Software Company 技能入口

## 用途

- 讓 Codex 可分別探索總入口以及 Plan、Generate、Review、Boss。

## 責任範圍

- `software-company-plan/`、`software-company-generate/`、`software-company-review/` 和 `software-company-boss/` 各管理該模式的 `SKILL.md` 入口。

## 本地契約

- 入口名稱與資料夾名稱一致。各模式入口將流程交給 `software-company/SKILL.md`，共用流程及參考文件由總入口管理。

## 工作指引

- 更動入口時，同步核對根目錄 README 與套件探索測試。

## 驗證

- 在專案根目錄執行 `python -X utf8 -m unittest discover -s tests -v`，核對五個入口、共用連結與封裝邊界。

## 子層 DOX 索引

- [總入口與交付契約](software-company/AGENTS.md) 管理四個模式的流程與產物。
