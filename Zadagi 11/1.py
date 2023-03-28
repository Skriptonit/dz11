print ("Введите первое число ")
a = int (input())
print ("Введите второе  число ")
b = int (input())

def calculator (a,b,s):
    if s =="+":
        return a+b
    if s =="-":
        return a-b
    if s =="*":
        return a*b
    if s =="/":
        if b==0:
            return "На 0 делить нельзя дурачок !"
        else :
            return a/b
print ("Введите знак операции")
s=input()
print (calculator(a, b, s))

#Допонительно
# print ("Предупреждаю! На ноль нельзя делить ! Если ты это не знал ,иди в детский сад неуч! ")
# print("Первое число :")
# a = float(input())
# print("Второе число :")
# b = float(input())
# c = "*"
# d = "/"
# e = "+"
# f = "-"
# print("Введите операцию :")
# m = input()
#
# if (m == c):
#     print(a * b)
# elif (m == d):
#     print(a / b)
# elif (m == e):
#     print(a + b)
# elif (m == f):
#     print(a - b)




# Дополнительное , в этом случае пользователю выводятся все операции над его числами
# a = float (input())
# b =  float(input())
# k=0
#
# s=a+b
# r=a-b
# p=a*b
# d=a/b
#
# def calculator (a,b):
#     s =a+b
#     return(s)
# print ('Сумма чисел :')
# print (calculator(a,b))
#
# def calculator (a,b):
#     p =a*b
#     return(p)
# print ("Произведение чисел  :")
# print (calculator(a,b))
#
# def calculator (a,b):
#     r =a-b
#     return(r)
# print ("Разность чисел :")
# print (calculator(a,b))
#
# def calculator (a,b):
#     d =a/b
#     return(d)
# print ("Деление чисел  :")
# print (calculator(a,b))
# #
