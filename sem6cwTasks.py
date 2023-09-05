# Задача 1
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

# from random import randint

# def dev_lists(list_1, list_2):
#     return [el for el in list_1 if el not in list_2]


# n = int(input('n: '))
# list_1 = [randint(1, 10) for i in range (n)]
# print(list_1)
# list_2 = [randint(1, 10) for i in range (n)]
# print(list_2)
# list_3 = dev_lists(list_1, list_2)

# print(*list_3)


# Вариант 2
# def dev_list(list1,list2):
#     return [el for el in list1 if el not in list2]

# list1=[int(input()) for i in range(int(input('количество элементов в 1 списке: ')))]
# list2=[int(input()) for i in range(int(input('количество элементов в 2 списке: ')))]
# print(dev_list(list1,list2))

# Вариант 3
# def sortArr (arr1, arr2):
#     arr3 = []
#     for i in arr1:
#        if i not in arr2:
#          arr3.append(i)
#     return arr3

# def elInput (n):
    
#     array_1 = []
#     for i in range(n):
#         array_1.append(int(input("Enter numbers of the array: ")))
#     return array_1

# n = int (input ("Enter quontity of elements for array: "))
# m = int (input ("Enter quontity of elements for array: "))

# array_3 = sortArr(elInput(n), elInput(m))
# print (array_3)


# Задача 2
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# 5
# 1 2 3 4 5 -> 0

# 5
# 1 5 1 5 1 -> 2

# def sosed(list1):
#     count=0
#     for i in range(1, len(list1) - 1):
#         if list1[i-1] < list1[i] > list1[i+1]:
#             count+=1
#     return count

# list1=[int(input()) for i in range(int(input('количество элементов в 1 списке: ')))]

# print(f'количество больших {sosed(list1)}')


# Задача 3
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:
# 1 2 1 2 2 2 3 4
# Вывод:
# 7

# from random import randint

# def count_p(list_1):
#     count = 0
#     for i in range(len(list_1)):
#         for j in range(i + 1, len(list_1)):
#             if list_1[i] == list_1[j]:
#                 count += 1
#     return count


# list_1 = [randint(1, 5) for i in range(int(input('Введите кол-во эл-тов: ')))]
# print(list_1)
# print(count_p(list_1))

# Вариант 2
# from random import randint

# def count_p(list_1):
#     count = 0
#     for i, el in enumerate(list_1):
#         count += list_1[i + 1:].count(el)
#     return count

# list_1 = [randint(1, 5) for i in range(int(input('Введите кол-во эл-тов: ')))]
# print(list_1)
# print(count_p(list_1))

# Вариант 3
# def countPairs (arr1):
#     counter = 0
#     for i in range(len(a)):
#         for j in range(i + 1, len(a)):
#             if a[i] == a[j]:
#                 counter += 1
#     return counter

# a = [int(s) for s in input().split()]
# print(countPairs(a))


# Задача 4
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284

# def sum_del(n):
#     summ = 0
#     for num in range(1, n // 2 + 1):
#         if n % num == 0:
#             summ += num
    
#     return summ
    

# k = 300

# for num_1 in range(1, k + 1):
#     num_2 = sum_del(num_1)
#     sum_del_2 = sum_del(num_2)
#     if (num_1 == sum_del_2) and (num_1 != num_2) and (num_1 < num_2):
#         print(num_1, num_2)
