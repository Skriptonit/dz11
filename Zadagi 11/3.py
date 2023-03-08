s=[]
def hello(a):
    if a in s :
     print ("Привет," +a+"!")
    else:
     print ("Привет," +a+"! Рад знакомству!")
     s.append(a)
a = input()
print (hello(a))
print (s)