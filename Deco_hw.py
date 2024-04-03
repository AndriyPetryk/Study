import time


def my_func(func):
    def time_funk(*args):
        print(f'{time.asctime()} - {func.__name__}')
        func(*args)  # for using func
    return time_funk
#
@my_func
def pol():
    print('Hello')
#
# pol()
#
#
# a = int(input('Enter a number: '))
# b = int(input('Enter another number: '))
#
# @my_func
# def pol2(a, b):
#     print(f'{a + b}')
#
#
# print(pol2(a, b))






# class MyCustomException(Exception):
#     pass
#
# raise MyCustomException("Custom Exception is occured")

class MyManager:
    def __enter__(self):
        print("==========")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("==========")

with MyManager():
    print(pol())
#

