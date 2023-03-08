#Программа предназначена для нахождения факториала сложным путем , и для нахождения умножения
# нескольких заданых чисел (это  дополнительно)!Удачи в наченанеях!
def factorial(number):
    z=1
    for i in range (number):
        s = int ( input())
        z*=s
        print (z)

number = int(input('Введите число: '))
print(factorial(number))
