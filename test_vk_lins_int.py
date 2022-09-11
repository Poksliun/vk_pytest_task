import pytest
from math import pi
from .my_func.sum_numb_from_list import SumNumb

@pytest.mark.list
@pytest.mark.int
def test_divisibility_of_the_sum_pi_numbers():
    """Проверка делимости суммы цифр числа пи на количество чисел"""
    #Выбор первых 13 чисел после запятой
    num = str(pi)[2:15]
    num_list = list(num)

    #Подсчет суммы чисел с помощью функции из директории my_func
    sum_pi = SumNumb(num_list).sum_from_list()
    lenght_list = len(num_list)

    #Деление суммы чисел на их количество
    division = sum_pi % lenght_list

    assert division == 0, 'Сумма чисел не делится на их количество'

@pytest.mark.list
def test_dividing_list_items()

