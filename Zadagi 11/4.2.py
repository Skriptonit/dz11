#под а

def count():
    chetn = 0
    nechetn = 0
    n = 10
    a = 1
    while a <= 10:
        if a % 2 == 0:
            chetn  += 1
        elif a%2!=0:
            nechetn += 1
        a += 1
    return f'четные {chetn }, нечетные {nechetn}'
print(count())


# #под б
# chetn = 0
# nechetn = 0
# def rec(i):
#     if i > 0:
#         global chetn
#         global nechetn
#         if i%2 == 0:
#              chetn += 1
#         else:
#             nechetn += 1
#         return rec(i - 1)
#     else:
#         print(f'четные {chetn }, нечетные {nechetn}')
#         return
#
# rec(10)