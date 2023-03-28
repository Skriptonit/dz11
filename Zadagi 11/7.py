c = []
while (len(c)<10):
    def login (a,b):
        if n in c:
            print  ("Доступ разрешен")
        elif n !=c:
            print  ("Доступ запрещен! Проходит регистрация... Регистрация прошла успешно !",)
            c.append(n)
            print(*c)
    print("Введите логин :")
    a = input()
    print("Введите пароль : ")
    b = input()
    n = {a:b}

    (login (a,b))

