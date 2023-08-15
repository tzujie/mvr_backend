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
- Response：錯誤訊息

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
- Response：登錄成功

失敗：
- Status Code：401 Unauthorized
- Response：登錄失敗

## 獲取用戶列表

### URL 
`GET https://192e-163-13-201-95.ngrok-free.app/api/accounts/?email=${encodeURIComponent(userEmail)}`


### Response

成功：

- Status Code：200 OK
- Response：用戶列表資訊，不包括密碼



## 創建角色

**URL**: 
`POST`
    https://192e-163-13-201-95.ngrok-free.app/api/update_character/

**請求參數**:

| 參數名稱  |  描述       |
| --------- | ---------- |
| userId     |   |
| gender     |   |
| beard     |女生自動寫入none |
| glasses  | 可以為空 |
| hair  | 可以為空 |
| hands  | 預設為'HANDS_01_1' |
| hat  | 可以為空 |
| head  | 預設為'HEAD_01_1' |
| pants  | 預設為'PANTS_01_1' |
| shoes  | 預設為'SHOES_01_1' |
| torso  | 預設為'TORSO_01_1' |

**Response**:

成功：
- Status Code：201 Created

失敗：
- Status Code：400 Bad Request

## 獲取角色

**URL**: 
`POST`
    https://192e-163-13-201-95.ngrok-free.app/api/get_character/?userId={userId}

**Response**:

成功：
- Status Code：200 OK

失敗：
- Status Code：404 Not Found

## 更新服裝

**URL**: 
`POST` 
    https://192e-163-13-201-95.ngrok-free.app/api/update_clothing/{user_id}/
   
`{user_id}`替換為實際的用戶ID。

**Response**:

- 成功：Status Code：200 OK, Response Body: `{"message": "Clothing data updated successfully"}`
- 失敗：Status Code：400 Bad Request, Response Body: `{"message": "Invalid id"}`

## 更新樂器

**URL**: 
`POST` 
    https://192e-163-13-201-95.ngrok-free.app/api/update_instruments/{user_id}/

`{user_id}`替換為實際的用戶ID。

**Response**:

- 成功：Status Code：200 OK, Response Body: `{"message": "Musical instruments data updated successfully"}`
- 失敗：Status Code：400 Bad Request, Response Body: `{"message": "Invalid id"}`

## 更新家具

**URL**: 
`POST` 
    https://192e-163-13-201-95.ngrok-free.app/api/update_furniture/{user_id}/
    
`{user_id}`替換為實際的用戶ID。

**Response**:

- 成功：Status Code：200 OK, Response Body: `{"message": "Furniture data updated successfully"}`
- 失敗：Status Code：400 Bad Request, Response Body: `{"message": "Invalid id"}`

## 獲取服裝

**URL**: 
`GET`
    https://192e-163-13-201-95.ngrok-free.app/api/get_clothing/{user_id}/
    
`{user_id}`替換為實際的用戶ID。

**Response**:

- 成功：Status Code：200 OK, Response Body: JSON array of clothing items
- 失敗：Status Code：404 Not Found, Response Body: `{"message": "Invalid id"}`

## 獲取樂器

**URL**: 
`GET` 
    https://192e-163-13-201-95.ngrok-free.app/api/get_instruments/{user_id}/
    
`{user_id}`替換為實際的用戶ID。

**Response**:

- 成功：Status Code：200 OK, Response Body: JSON array of musical instruments
- 失敗：Status Code：404 Not Found, Response Body: `{"message": "Invalid id"}`

## 獲取家具

**URL**: 
`GET` 
    https://192e-163-13-201-95.ngrok-free.app/api/get_furniture/{user_id}/
    
    

## 更新帳戶金錢
`PATCH` 
    https://192e-163-13-201-95.ngrok-free.app/api/update_money/
    
**Request Body**:
```json
{
    "id": "<ID>",
    "money": "<Amount>"
}
```

**Response**:
- 成功：Status Code：200 OK,
- Response Body: {
    "message": "Money updated successfully.",
    "current_money": "<Updated_Amount>"
}

- 失敗：Status Code：404 Not Found,
- Response Body: {
    "message": "<Error_Message>"
}

## 取得帳戶金錢
`GET` 
    https://192e-163-13-201-95.ngrok-free.app/api/get_furniture/{user_id}/
`{user_id}`替換為實際的用戶ID。

## 取得登入次數
`GET` 
    https://192e-163-13-201-95.ngrok-free.app/api/get_login_count/{user_id}/
`{user_id}`替換為實際的用戶ID。

## Superuser

- 帳號：admin
- 密碼：102938
  
## Runserver
    python manage.py runserver
- Python 3.8.8
- Django 4.2.3

