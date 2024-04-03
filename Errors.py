# pin = 1234
# max_tries = 3
# permision = False
#
# while permision is False and max_tries > 0:
#     try:
#         _pin = input("Enter a pin: ")
#         if int(_pin) == pin:
#             print("Pin is correct")
#             permision = True
#     except ValueError:
#         print("Pin should be only digits")
#     finally:
#         max_tries -= 1
#         print(f'{max_tries} attempts left. Permission {"granted" if permision else "denied"}')


pin = 1234
max_tries = 3
permision = False

while permision is False and max_tries > 0:
    try:
        _pin = int(input("Enter a pin: "))
    except ValueError:
        print("Pin should be only digits")
    else:
        if int(_pin) == pin:
            print("Pin is correct")
            permision = True
    finally:
        max_tries -= 1
        print(f'{max_tries} attempts left. Permission {"granted" if permision else "denied"}')