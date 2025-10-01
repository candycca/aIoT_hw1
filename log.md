# Project Log

本檔記錄了與使用者互動的過程，包含專案的初始化、Streamlit 應用程式的開發與功能增強、文件建立以及版本控制操作。

## Global Step 1 — Initialize Logging
**1.1 User request**  
> from now on, i want to do the logging, 把我們的對話紀錄記錄在log.md , log.md should be noted by #.#, first # indicate global steps, the second # indicate detail form

**1.2 Actions**  
- 創建 `log.md` 檔案。

**1.3 Response / Result**  
- `log.md` 檔案已創建並記錄了首次互動。

## Global Step 2 — Plan Project Steps
**2.1 User request**  
> read `./ref/idea.md` then layout steps in detail then save to `steps.md`

**2.2 Actions**  
- 讀取檔案 `/Users/tianxinqiao/Desktop/aiotHW1/ref/idea.md`。
- 根據 `idea.md` 內容，制定詳細的專案步驟。
- 創建 `steps.md` 檔案，並寫入詳細步驟。

**2.3 Response / Result**  
- 已讀取 `ref/idea.md` 並創建 `steps.md` 檔案，其中包含詳細的專案計畫。
- 產物：`steps.md`

## Global Step 3 — Develop Streamlit App - Core Features
**3.1 User request**  
> ok,fllow `steps.md` to do everything for me.

**3.2 Actions**  
- 讀取 `steps.md` 以理解計畫。
- 創建 `app.py` 檔案，包含 Streamlit 應用程式的初始結構、資料生成和視覺化功能。
- 實作線性迴歸模型和評估功能於 `app.py`。
- 執行 `streamlit run app.py &` 啟動應用程式伺服器。

**3.3 Response / Result**  
- 已根據 `steps.md` 創建 `app.py` 檔案，並實作了核心功能。
- 應用程式已在背景執行，通常可在 `http://localhost:8501` 存取。
- 產物：`app.py`

**3.4 User request**  
> 你沒給我網址 (You didn't give me the URL)

**3.5 Actions**  
- _(missing)_

**3.6 Response / Result**  
- 提供了 Streamlit 應用程式的預設網址：`http://localhost:8501`。

## Global Step 4 — Handle API Error
**4.1 User request**  
> ✕ [API Error: Model stream ended with an invalid chunk or missing finish reason.]fix it

**4.2 Actions**  
- 分析錯誤訊息。
- 確認錯誤為 Gemini API 內部問題，與專案程式碼無關。

**4.3 Response / Result**  
- 解釋了錯誤為內部 API 問題，無法直接修復，但會繼續處理請求。

## Global Step 5 — User Greeting
**5.1 User request**  
> 哈囉 (Hello)

**5.2 Actions**  
- _(missing)_

**5.3 Response / Result**  
- 回應了使用者的問候。

## Global Step 6 — Enhance App - Outlier Display
**6.1 User request**  
> 你要在圖上標示出top 5 outliers，並且outliers的表格還要紀錄residual，表格的位置也要在最下方 (You need to mark the top 5 outliers on the plot, and the outlier table should also record the residual, and the table should be at the very bottom.)

**6.2 Actions**  
- 修改 `app.py` 以識別、標記並顯示前 5 個離群值及其殘差。

**6.3 Response / Result**  
- `app.py` 已更新，現在應用程式會在圖表上標示前 5 個離群值，並在頁面底部顯示包含其殘差的表格。

## Global Step 7 — Refine App - Outlier IDs & Remove Table
**7.1 User request**  
> 你的圖上還要標離群點的id，然後把最上面那個就表格刪掉 (You also need to mark the outlier IDs on the plot, and delete the table at the very top.)

**7.2 Actions**  
- 修改 `app.py` 以在圖表上新增離群點的 ID，並移除初始的資料表格。

**7.3 Response / Result**  
- `app.py` 已更新，現在應用程式會在圖表上標示離群點的 ID，並移除了應用程式頂部的初始資料表格。

## Global Step 8 — Refine App - Remove Data Generation Header
**8.1 User request**  
> 刪掉網頁上面那行Data Generation (Delete the "Data Generation" line from the web page)

**8.2 Actions**  
- 修改 `app.py` 以移除「Data Generation」標題。

**8.3 Response / Result**  
- `app.py` 已更新，移除了「Data Generation」標題。

## Global Step 9 — Create `README.md`
**9.1 User request**  
> 我希望你可以寫一個`readme.md` (I hope you can write a `readme.md`)

**9.2 Actions**  
- 創建 `README.md` 檔案，包含專案描述、功能、設定和執行方式。

**9.3 Response / Result**  
- `README.md` 檔案已創建。
- 產物：`README.md`

## Global Step 10 — Create `requirements.txt`
**10.1 User request**  
> 還有`requirements.txt` (Also `requirements.txt`)

**10.2 Actions**  
- 創建 `requirements.txt` 檔案，列出專案的所有 Python 依賴。

**10.3 Response / Result**  
- `requirements.txt` 檔案已創建。
- 產物：`requirements.txt`

## Global Step 11 — Push to GitHub - Initial Commit
**11.1 User request**  
> 我要推到 github 上，我已經在github上創建好repo:`https://github.com/candycca/aIoT_hw1.git`，幫我將這個專案 add, commit, push 上去 (I want to push to GitHub, I have already created the repo on GitHub: `https://github.com/candycca/aIoT_hw1.git`, help me add, commit, and push this project.)

**11.2 Actions**  
- 初始化 Git 儲存庫。
- 將所有檔案加入 Git 暫存區。
- 提交變更，訊息為 "Initial commit: Implement interactive linear regression app"。
- 新增遠端 GitHub 儲存庫：`https://github.com/candycca/aIoT_hw1.git`。
- 推送變更到 GitHub 儲存庫。

**11.3 Response / Result**  
- 專案已成功推送到 GitHub 儲存庫。
- 儲存庫連結：`https://github.com/candycca/aIoT_hw1.git`

## Global Step 12 — Update `README.md` with Streamlit URL
**12.1 User request**  
> 幫我把我的streamlit url: `https://aiothw1-candy.streamlit.app`，記錄到 `README`

**12.2 Actions**  
- 讀取 `README.md` 檔案。
- 在 `README.md` 的「How to Run」部分加入 Streamlit 應用程式的 URL。

**12.3 Response / Result**  
- `README.md` 檔案已更新，包含了 Streamlit 應用程式的 URL。
- 產物：`README.md`

## Global Step 13 — Reformat `log.md`
**13.1 User request**  
> 你可以用markdown的形式幫我排版一下`log.md`嗎 (Can you help me format `log.md` using Markdown?)

**13.2 Actions**  
- 讀取 `log.md` 檔案。
- 根據新的 Markdown 規範重新排版 `log.md`。

**13.3 Response / Result**  
- `log.md` 檔案已使用 Markdown 重新排版，以提高可讀性。
- 產物：`log.md`

## Global Step 14 — Push to GitHub - Updated Files
**14.1 User request**  
> 幫我把更新的檔案push到github上 (Help me push the updated files to GitHub)

**14.2 Actions**  
- 將更新後的 `README.md` 和 `log.md` 加入 Git 暫存區。
- 提交變更，訊息為 "Update README.md with Streamlit URL and reformat log.md"。
- 推送變更到 GitHub 儲存庫。

**14.3 Response / Result**  
- 更新後的檔案已成功推送到 GitHub 儲存庫。

## Global Step 15 — Acknowledge Logging Format
**15.1 User request**  
> `log.md` should be noted by #.#, first # indicate global steps, the second  indicate detail form

**15.2 Actions**  
- _(missing)_

**15.3 Response / Result**  
- 確認已遵循 `#.#` 的日誌格式。
