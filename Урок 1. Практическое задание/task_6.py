"""
Задание 6.

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
 и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

dist_1 = int(input("Введите результат в километрах в первый день тренировок: "))
target_dist = int(input("Введите целевой результат в километрах: "))
day = 1
while dist_1 < target_dist:
    day += 1
    dist_1 *= 1.1
    print(dist_1)
print(f"Ответ: на {day}-й день спортсмен достиг результата - не менее {target_dist} километров")