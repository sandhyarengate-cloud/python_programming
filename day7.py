#predefined module
# import math
# print(math.sqrt(16))
# print(math.pi)

#using as operator
# import math as m
# print(m.sqrt(16))
# print(m.pi)

#program to use the multiple function of module
# from math import *
# print(int(sqrt(4)))
# print(ceil(10.1))
# print(floor(10.1))
# print(fabs(-10.6))
# print(fabs(10.6))

# from random import*
# for i in range(10):
#      print(random())
#random() function will return the random floating values

# from random import*
# for i in range(10):
#       print(randint(1,100000))
      #randint() will retun the integer values

# from random import*
# list=["prashant","rahul","ashish","sandip","sunil","nikuuu"]
# for i in range(10):
#     print(choice(list))
#module1 is the file saved in vs code
# import module1
# module1.square(4)
# module1.login("admin","admin")
# print(module1.pi)

# import module1 as mod
# module1.square(4)
# module1.login("admin","admin")
# print(module1.pi)
# from module import pi,square,login,welcome
# print(pi)
# square(4)
# login('user','user')
# welcome('prashant','jha')
# from module1 import*
# print(pi)
# square(4)
# login('user','user')
# welcome
# a=[1,2,3,4,5,6,7,8,9]
# a[: : 2]=10,20,30,40,50,60
# print(a)
# a=[1,2,3,4,5]
# print(a[3:0:-1])

# def func(value,values):
#     var=1
#     values[1]=55
# t=3
# v=[1,2,3]
# func(t,v)
# print(t,v[1])

# arr=[[1,2,3,4],
#     [4,5,6,7],[8,9,10,11],[12,13,14,15]]
# for i in range(0,2):
#     print(arr[i].pop())

# def f(i,values=[]):
#      values.append(i)
#      print(values)
# f(1)
# f(2)
# f(3)

# fruit_list1=["Apple","Berry","Cherry","Papaya"]
# fruit_list2=fruit_list1
# fruit_list3=fruit_list1[:]
# fruit_list2[0]="Guava"
# fruit_list3[1]="Kiwi"
# sum=0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] =="Guava":
#         sum += 1
#     if ls[1] =="Kiwi":
#         sum += 20
# print(sum)

arr=[1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1]=arr[i]
    for i in range(0,6):
        print(arr[i],end =" ")







































































































