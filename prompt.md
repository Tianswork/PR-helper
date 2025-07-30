# 📄 prompt.md

為了確保程式碼品質一致並方便維護，請在提交 PR 前務必遵守以下規範。這些規範適用於所有 Python 檔案與其內容。

---

## 📌 一、通用規範

### 1.1 CopyRight 標示
- 所有檔案最上方需加上 CopyRight 標示：
  ```python
  # Copyright (c) 2025 <Your Company Name>. All rights reserved.
  ```
- 必須為檔案中的第一行。
- `<Your Company Name>` 可根據實際公司名稱替換。

### 1.2 檔案編碼
- 所有檔案皆需使用 UTF-8 編碼，無 BOM。
- 可加上以下編碼宣告（可選）：
  ```python
  # -*- coding: utf-8 -*-
  ```

---

## 🧹 二、格式規範（PEP8 + 內部規範）

### 2.1 換行與縮排
- 使用 4 個空格 做為縮排（**禁止使用 Tab**）。
- 每行不得超過 **100 個字元**。
- 函式之間需空兩行。
- 類別之間需空兩行。
- 類別中的方法之間空一行。

### 2.2 空白規則（Spaces）
- 運算子前後需空一格：
  ```python
  total = price * quantity
  ```
- 函式定義與呼叫時，括號內不要多餘空格：
  ```python
  def func(a, b)     # ✅
  func(a, b)         # ✅
  func( a, b )       # ❌
  ```
- 逗號 `,` 後應留空格：
  ```python
  items = [1, 2, 3]
  ```

### 2.3 匿名函式禁止多行
- `lambda` 僅允許一行，複雜邏輯請改用 `def`。

---

## 🚫 五、禁止事項

- ❌ 提交 `print()` 或 `pdb.set_trace()` 等 Debug 訊息  
- ❌ 提交任何敏感資訊（帳密、token 等）  
- ❌ 違反上述任一規範

---

請在提交 Pull Request 前再次確認所有修改均符合以上規範，確保程式碼整潔、一致、可維護。
