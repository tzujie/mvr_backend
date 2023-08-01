# API 文件

## 注冊帳戶

### URL 
`POST https://192e-163-13-201-95.ngrok-free.app/api/register/`


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



## 創建角色

**URL**: 
`POST`
  https://192e-163-13-201-95.ngrok-free.app/api/create_character/

**請求參數**:

| 參數名稱  |  描述       |
| --------- | ---------- |
| userId     | 用戶ID  |
| gender     | 角色性別  |
| beard     | 角色鬍鬚類型（可以為空） |
| glasses  | 角色眼鏡類型（可以為空） |
| hair  | 角色頭髮類型（可以為空） |
| hands  | 角色手部類型（預設為'HANDS_01_1'） |
| hat  | 角色帽子類型（可以為空） |
| head  | 角色頭部類型（預設為'HEAD_01_1'） |
| pants  | 角色褲子類型（預設為'PANTS_01_1'） |
| shoes  | 角色鞋子類型（預設為'SHOES_01_1'） |
| torso  | 角色身體類型（預設為'TORSO_02_3'） |

**Response**:

成功：

- Status Code：201 Created
- Response：創建成功的角色資訊

失敗：

- Status Code：400 Bad Request
- Response：錯誤訊息的詳細描述

## 獲取角色

**URL**: 
`POST`
  https://192e-163-13-201-95.ngrok-free.app/api/get_character/?userId={userId}

**Response**:

成功：

- Status Code：200 OK
- Response：角色的詳細資訊

失敗：

- Status Code：404 Not Found
- Response：角色未找到的訊息
