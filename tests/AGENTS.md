# 外掛驗證

## 用途

- 驗證 Codex App 外掛的封裝與技能參考。

## 責任範圍

- `test_company.py` 驗證 marketplace、manifest、技能及參考文件。

## 本地契約

- 離線封裝檢查使用 Python 標準函式庫。外掛安裝和執行使用 Codex App。
- App 驗收在 Windows 本機工作區核對 `plan` 的三份文件及停止範圍。
- 發行 ZIP 在乾淨目錄解壓後再跑封裝測試，並以隔離的 Windows Codex App 服務核對 marketplace 探索、安裝、技能啟用及額外驗證需求。

## 工作指引

- 封裝測試著重可探索的檔案、有效的連結及純技能套件邊界。

## 驗證

- 在專案根目錄執行 `python -X utf8 -m unittest discover -s tests -v`。

## 子層 DOX 索引
