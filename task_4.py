"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

""" линейный O(N)"""


def authorization_first(base_of_users, username, password):
    for key, value in base_of_users.items():
        if key == username:
            if value['password'] == password and value['activated']:
                return 'welcome back'
            elif value['password'] == password and not value['activated']:
                return 'your account is not activated'
            elif value['password'] != password:
                return 'wrong password'
    return "wrong username"


"""константная O(1)"""


def authorization_second(base_of_users, username, password):
    if base_of_users.get(username):
        if base_of_users[username]['password'] == password and base_of_users[username]['activated']:
            return 'welcome back'
        elif base_of_users[username]['password'] == password and not base_of_users[username]['activated']:
            return 'your account is not activated'
        elif base_of_users[username]['password'] != password:
            return 'wrong password'
    return "wrong username"


my_users = {
    'user_1': {'password': 'qwert', 'activated': True},
    'user_2': {'password': 'werty', 'activated': False},
    'user_3': {'password': '123456', 'activated': True},
    'user_4': {'password': '098765', 'activated': False},
}
print(authorization_first(my_users, 'user_1', 'qwert'))
print(authorization_second(my_users, 'user_2', 'qwert'))
print(authorization_first(my_users, 'user_2', 'werty'))
print(authorization_second(my_users, 'user_5', 'qwert'))

"""первая функция менее эфективна, т.к. в ней реализован цикл, а во второй используется встроенная функция"""