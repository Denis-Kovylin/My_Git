# Дебильный калькулятор version_1

what = input("Что делаем, отсталый?  (+, -): ")

a = float(input( "Введи палец в жо... кхм, первое число: " ))
b = float(input( "Введи второе число, не тупи: " ))

if what == "+":
    c = a + b
    print("Результат: " + str(c))

elif what == "-":
    c = a - b
    print("Результат: " + str(c))

else:
    print("А ты тупее чем я думал)))=D)))")