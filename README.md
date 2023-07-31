# API 文件

## 注冊帳戶

### URL 
`POST https://192e-163-13-201-95.ngrok-free.app/api/login/`


### 請求參數

| 參數名稱  |  描述       |
| --------- |  ---------- |
| name        | 用戶名稱   |
| email     | 用戶信箱   |
| password  | 用戶密碼   |
| phone     | 用戶電話   |

### Response

成功：

- Status Code：201 Created
- Response：注冊成功的用戶資訊

失敗：

- Status Code：400 Bad Request
- Response：錯誤訊息的詳細描述

## 登錄帳戶

### URL 
`POST https://192e-163-13-201-95.ngrok-free.app/api/login/`


### 請求參數

| 參數名稱  |  描述       |
| --------- | ---------- |
| email     | 用戶箱信   |
| password  | 用戶密碼   |

### Response

成功：

- Status Code：200 OK
- Response：登錄成功的訊息

失敗：

- Status Code：401 Unauthorized
- Response：登錄失敗的訊息

## 獲取用戶列表

### URL 
`GET https://192e-163-13-201-95.ngrok-free.app/api/accounts/?email=${encodeURIComponent(userEmail)}`


### Response

成功：

- Status Code：200 OK
- Response：用戶列表資訊，不包括密碼

## Superuser

- 帳號：admin
- 密碼：102938
  
## Runserver
    python manage.py runserver
- Python 3.8.8
- Django 4.2.3
