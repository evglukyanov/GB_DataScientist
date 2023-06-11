'''
# 5
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

'''
try:
    revenue = float(input("Введите пожалуйста значение выручки: "))
except ValueError:
    print('Число введено неверно. Будет заменено на 0.')
    revenue = 0

try:
    cost = float(input("Введите пожалуйста значение издержек: "))
except ValueError:
    print('Число введено неверно. Будет заменено на 0.')
    cost = 0

financial_result = revenue - cost

if financial_result > 0:
    print(f"При заданных параметрах финансовый результат: прибыль")
    profitability = financial_result / revenue
    print(f"Рентабильность: {profitability}")

    try:
        size = int(input("Укажите количество сотрудников: "))
    except ValueError:
        print('Число введено неверно. Будет заменено на 1. Уж вы-то точно сотрудник')
        size = 1

    if size <= 0:
        print('Число введено неверно. Будет заменено на 1.')
        size = 1

    print(f'Прибыль в  расчете на одного сотрудника: {financial_result/size}')
else:
    print(f"При заданных параметрах финансовый результат: убыток")
