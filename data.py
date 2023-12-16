# В файле будут лежать заголовки и тело запроса.

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {authToken}"
}

user_body = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}

kit_body = {
       "name": "Мой набор"
}

product_ids = {
    "ids": [1, 2, 3]
}