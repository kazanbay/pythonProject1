# отрезки

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# один в другом, границы совпадают
# if a1 == a2:
#     if b1 <= b2:
#         print(a1, b1)
#     else:
#         print(a1, b2)
# if b1 == b2:
#     if a1 <= a2:
#         print(a2, b2)
#     else:
#         print(a1, b2)
# elif a1 < a2 and b2 < b1:
#     print (a2, b2)
# elif a2 < a1 and b1 < b2:
#     print (a1, b1)
# elif

if a1 <= a2 and b2 <= b1:
    print (a2, b2)
elif a2 <= a1 and b1 <= b2:
    print (a1, b1)
elif a1 < a2 and b1 < b2:
    if a2 == b1:
        print(a2)
    else:
        print(a2, b1)
elif a2 < a1 and b2 < b1:
    if a1 == b2:
        print(a1)
    else:
        print(a1, b2)
else:
    print('пустое множество')
# # рулетка
# n = int(input())
# if n == 0:
#     print("зеленый")
# elif 0 < n <= 10:
#     if n % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif 10 < n <= 18:
#     if n % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# elif 18 < n <= 28:
#     if n % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif 28 < n <= 36:
#     if n % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# else:
#     print("ошибка ввода")
#



# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print('Равносторонний')
# elif a==b or b==c or a==c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')

# a = int(input('введите первое число'))
# b = int(input('введите второе число'))
# c = int(input('введите третье число'))
# if a == b:
#     if b == c:
#         print(3)
#     else:
#         print(2)
# else:
#     if b == c:
#         print(2)
#     else:
#         if a == c:
#             print(2)
#         else:
#             print(0)

# a = int(input('введите первое число'))
# b = int(input('введите второе число'))
# c = int(input('введите третье число'))
# if a == b == c:
#     print(3)
# elif a == b or a == c or b == c:
#     print(2)
# else:
#     print(0)



# x = int(input())
# y = int(input())
# if x > 0:
#     if y > 0:
#         print('Первая четверть')
#     else:
#         print('Четвертая четверть')
# else:
#     if y > 0:
#         print('Вторая четверть')
#     else:
#         print('Третья четверть')


# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print("Первая четверь")
# if x < 0 and y > 0:
#     print("Вторая четверь")
# if x < 0 and y < 0:
#     print("Третья четверь")
# if x > 0 and y < 0:
#     print("Четвёртая четверь")


#
# x =int(input())
# a = x // 100
# b = (x // 10) % 10
# c = x % 10
# if a != b and b!= c and a !=c:
#     print('все цифры в числе', x, 'различны')
# else:
#     print('не все цифры в числе', x, 'различны')
#
#
# x = int(input())
# if 100<=x<=999:
#     print(x, 'является трёхзначным')
# else:
#     print(x, 'не является трёхзначным')


# a = int(input('введите первое число'))
# b = int(input('введите второе число'))
# c = int(input('введите третье число'))
# d = 0
# if a % 2 == 0:
#     d = d + 1
# if b % 2 == 0:
#     d = d + 1
# if c % 2 == 0:
#     d = d + 1
# print('количество чётных чисел =', d)



# n = int(input())
# n1 = n // 10
# n2 = n % 10
# if n1 == n2:
#     print('ДА')
# else:
#     print('НЕТ')