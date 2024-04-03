def add_one(func):
    def deco_func(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            result += 1
        return result
    return deco_func

@add_one
def add_numbers(a, b):
    return a + b

print(add_numbers(1, 3))





# def my_decorator(func):
#     def deco_func():
#         print("Decoration of the function")
#         func()
#         print("End decoration")
#     return deco_func
#
# @my_decorator
# def my_func():
#     print("This is my first function")
#
# my_func()







# def my_result_deco(func):
#     def wrap(*args, **kwargs):
#         if 'name' in kwargs:
#             print(f'Function is called with name: {kwargs.get("name")}')
#         res = func(*args, **kwargs)
#         print(f'Deco result is {res}')
#         return res
#     return wrap
#
# @my_result_deco
# def add_numbers(x, y):
#     return x + y
#
# @my_result_deco
# def other_function(name , phone):
#     print(name, phone)
#     return "Finish"
#
# # print(add_numbers(1,2))
# print(other_function(name = "Andriy", phone = 123))