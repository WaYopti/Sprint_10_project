import requests
import configuration
import data


# функция на создание пользователя
def post_new_user():
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH  # подставляем полный url до ендпоинта
    return requests.post(url, json=data.user_body, headers=data.headers)  # передаем тело и заголовки для создания user


response = post_new_user()
print(response.status_code)
print(response.json())


# создание нового набора для созданного ранее пользователя
def post_new_kit_for_created_user(token, kit_body):
    url = configuration.URL_SERVICE + configuration.CREATE_KIT_PATH
    body = {
        "name": kit_body
    }
    new_headers = data.headers.copy()
    new_headers['Authorization'] = f'Bearer {token}'
    return requests.post(url, json=body, headers=new_headers)


response = post_new_kit_for_created_user('token', 'kit_body')
print(response.status_code)
print(response.json())

# def post_products_kits(products_ids):
#    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids,
#                         headers=data.headers)


# response = post_products_kits(data.product_ids)
# print(response.status_code)
# print(response.json())
