import sender_stand_request
import data


# Эта функция меняет значение в параметре firstName

def get_user_body(first_name):
    current_body = data.user_body.copy()  # Копирование словаря с телом запроса из файла data
    current_body["firstName"] = first_name  # Меняем значение в поле ферстнейм
    return current_body  # Возвращаем новый словарь с нужным значением firstName


def positive_assert(first_name):
    user_body = get_user_body(first_name) # В переменную user_body сохраняется обновленное тело запроса
    # В переменную user_response сохраняется результат запроса на создание пользователя:
    user_response = sender_stand_request.post_new_user(user_body)
    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201
    # Проверяется, что в ответе есть поле authToken, и оно не пустое
    assert user_response.json()["authToken"] != ""

    # В переменную users_table_response сохраняется результат запрос на получение данных из таблицы user_model
    users_table_response = sender_stand_request.get_user_table()
    # Строка, которая должна быть в ответе запроса на получение данных из таблицы users
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
             + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Проверка, что такой пользователь есть, и он единственный
    assert users_table_response.text.count(str_user) == 1


# Тест 1. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")