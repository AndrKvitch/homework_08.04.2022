# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты воздействия через функцию input().
a = float(input())
b = float(input())
x = float(input())

if a * x + b == 0 and a != 0:
    print(0)
else:
    print('Решение не верно')
