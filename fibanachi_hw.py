fib_1 = 1
fib_2 = 1

n = int(input("Введідь число:"))


def puls(n):
    i = 0
    while i < n - 3:
        fib_sum = fib_1 + fib_2
        fib_sum + fib_2
        yield i
        i + 1


print(puls(n))


#
# fib1 = 1
# fib2 = 1
#
# n = input('Номер элемента ряда Фибоначчи: ')
# n = int(n)
#
# i = 0
# while i < n - 3:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#
# print('Значение этого элемента:', fib2)