# Software Company 0.5.0

Software Company 是 Codex App 外掛。規劃、實作、測試與審查在同一個本機 Codex 聊天和工作區進行，模型使用 App 已登入的 ChatGPT 訂閱。外掛安裝與規劃無須 CLI 轉接、API key 或額外的模型執行環境。建置與測試使用目標專案自己的工具。

## 在 Windows 安裝

1. 取得 0.5.0 專案目錄。如果收到 ZIP，請完整解壓到固定位置。確認根目錄直接包含 `.agents/plugins/marketplace.json`、`plugins/` 和本說明。
2. 在 Windows 版 ChatGPT 桌面 App 使用 ChatGPT 帳戶登入，切到 **Codex**。新增本機專案，將解壓後的根目錄選為來源資料夾。重新啟動桌面 App 後，回到此專案。[Windows 桌面 App 指南](https://learn.chatgpt.com/docs/windows/windows-app) · [開啟本機專案](https://learn.chatgpt.com/training/codex-lab/index.html?step=project)
3. 開啟 **Plugins Directory**，從 **Software Company Marketplace** 選取 **Software Company**，按下安裝。若找不到來源，確認目前選的是解壓根目錄，再重新啟動 App。[本機 marketplace 安裝文件](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually)
4. 在此本機專案開啟 Codex 聊天，確認使用 **This computer**。在輸入框輸入 `$software-company` 搜尋技能入口，再選取要執行的模式。也可從 App 的提及清單選取相同技能。[Codex 執行環境](https://learn.chatgpt.com/docs/environments/modes)

### 在其他本機專案使用

此套件提供專案型 marketplace。要讓技能出現在另一個專案，將 `.agents/plugins/marketplace.json` 和 `plugins/software-company/` 放到該專案根目錄的同名相對路徑。若已有 marketplace，保留原檔和原有項目，加入 Software Company 的項目，並核對 `source.path`。在 App 開啟該專案，從它的 marketplace 確認 Software Company 已安裝並啟用。[本機 marketplace 設定文件](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work)

## 技能入口

| 入口 | 用途 |
| --- | --- |
| `$software-company` | 總入口，可查看或指定工作模式。 |
| `$software-company-plan` | 從需求產出三份計畫文件，停在規劃。 |
| `$software-company-generate` | 依既有計畫實作、測試及審查。 |
| `$software-company-review` | 審查現有實作並回報發現。 |
| `$software-company-boss` | 從一句需求完成規劃、實作、測試及審查。 |

## Plan 產出規劃文件

選取技能後，在聊天中輸入下列範例。將目錄與需求換成自己的專案即可使用。

> $software-company-plan 規劃一個攝氏轉華氏命令列工具，可驗證輸入並顯示結果。把計畫放在 `docs/software-company/temperature-cli/`。

`plan` 會依序寫出 `prd.md`、`system-design.md`、`task-list.md`，核對需求及驗收條件後停止。省略輸出路徑時，預設為 `docs/software-company/<專案名稱>/`。

## Generate 接續既有計畫

確認計畫後，在同一聊天和工作區授權實作，並指定沿用的計畫及實作位置。

> $software-company-generate 依 `docs/software-company/temperature-cli/` 的計畫，在 `temperature-cli/` 實作、測試並審查。請回報驗收結果。

Codex 會依任務順序實作，執行專案的測試與驗收檢查，並在計畫目錄留下 `test-report.md` 和 `review.md`。請查看實際執行的測試、結果及仍待處理的發現。

## Review 審查既有實作

> $software-company-review 依剛才的計畫審查目前實作與測試，只回報發現。

## Boss 從一句需求完成交付

> $software-company-boss 做一個可驗證輸入的攝氏轉華氏命令列工具，完成實作、測試和審查。

Boss 會先建立並檢查計畫，再在同一個聊天直接接續交付。省略實作路徑時，新專案會放在未使用的 `projects/<專案名稱>/`。階段交接無須再次下指令，App 的必要核准仍適用。

## 套件檢查

開發者可用 `python -X utf8 -m unittest discover -s tests -v` 驗證封裝。App 驗收在 Windows 的本機 Codex 工作區執行攝氏轉華氏 `plan`，核對三份文件、需求對應及停止範圍。
