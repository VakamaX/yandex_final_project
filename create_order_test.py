# Кирилл Ильючек, 27А когорта — Финальный проект.
import requests
import configuration
import data

# Тест для создания заказа и проверки данных по трек-номеру
def test_create_and_validate_order():
    # Шаг 1: Выполнить запрос на создание заказа
    create_order_response = requests.post(configuration.URL_SERVICE + configuration.ORDERS_MAIN_PATH, json=data.order_headers)
    # Шаг 2: Сохранить номер трека заказа
    track = create_order_response.json()["track"]
    # Шаг 3: Выполнить запрос на получение заказа по трек-номеру
    get_order_response = requests.get(configuration.URL_SERVICE + configuration.ORDERS_GET_PATH, params={"t": track})
    # Шаг 4: Проверить, что код ответа равен 200
    assert get_order_response.status_code == 200