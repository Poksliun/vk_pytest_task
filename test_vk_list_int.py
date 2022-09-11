import pytest
from math import pi
from .my_func.actions_on_elements import ActionsOnElements

@pytest.mark.list
@pytest.mark.int
def test_divisibility_of_the_sum_pi_numbers():
    """Проверка делимости суммы цифр числа пи на количество чисел"""
    #Выбор первых 13 чисел после запятой
    num = str(pi)[2:15]
    num_list = list(num)

    #Подсчет суммы чисел с помощью функции из директории my_func
    action = ActionsOnElements()
    sum_pi = action.sum_from_list(num_list)
    lenght_list = len(num_list)

    #Деление суммы чисел на их количество
    division = sum_pi % lenght_list

    assert division == 0, 'Сумма чисел не делится на их количество'

@pytest.mark.list
@pytest.mark.negative
def test_dividing_list_items():
    try:
        initial_list = [1, 3, 5, 'en']
        numb = 2
        action = ActionsOnElements()
        final_list = action.division_elements(initial_list, numb)
        assert True

    except TypeError:
        pass

@pytest.mark.int
@pytest.mark.parametrize('numbers', [1, 7])
def test_error_of_exponentiation(numbers):
    action = ActionsOnElements()
    exp_sqrt_num = action.exp_and_sqrt(int(numbers))
    diff = exp_sqrt_num - numbers
    assert diff == 0

@pytest.mark.int
def test_product_of_numbers_with_the_same_bases():
    base_num = 2
    degree1 = 5
    degree2 = 4

    exp1 = base_num ** degree1
    exp2 = base_num ** degree2
    sum_exp_i = exp1 * exp2
    sum_degree = base_num ** (degree1 + degree2)

    assert sum_degree == sum_exp_i

