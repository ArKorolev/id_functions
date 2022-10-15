import collections


def group(client_id):
    """определяет номер группы клиентов по сумме цифр их ID"""
    total = 0  # счетчик суммы цифр числа
    while client_id > 0:  # разложение числа на цифры и их суммирование
        total += client_id % 10  # остаток от деления числа является его последней цифрой
        client_id //= 10  # убираем последнюю цифру в числе
    return total


print(f"клиент с ID 7412567 в группе {group(7412567)}")  # проверка функции, ответ 32

client_list = [_ for _ in range(10000, 10000000)]  # список 5-7 значных ID
group_list = []  # преобразование ID в номер группы
for i in client_list:
    group_list.append(group(i))


def sum_clients1(n_customers):
    """подсчитывает число покупателей, попадающих в каждую
    группу, если нумерация ID сквозная и начинается с 0"""
    list1 = group_list[:n_customers]
    customers_in_groups = collections.Counter(list1)  # группа: количество клиентов
    return customers_in_groups


print(sum_clients1(100000))  # в каких группах состоят первые 100000 клиентов


def sum_clients2(n_first_id, n_customers):
    """подсчитывает число покупателей, попадающих в каждую
    группу, если нумерация ID начинается с произвольного числа."""
    list2 = group_list[n_first_id:n_first_id + n_customers]
    customers_in_groups = collections.Counter(list2)  # группа: количество клиентов

    return customers_in_groups


print(sum_clients2(5000, 20000))  # в каких группах состоят 20000 клиентов
                                  # начиная c ID на 5000 позиции в списке
