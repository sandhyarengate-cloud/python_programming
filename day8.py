#OOPS
#class Student:
    #data member
    #a=10
    #b=20
    #self is default argument
    #def add(self):
        #print(self.a+self.b)
#object creation
# obj=Student()
# obj.add()
# print(obj.b)
# class NewClass:
#     def _init_(self):
#         print("constructor always execute first")#constructor declaration (called automactially)
#     def show(self):
#         print("welcome to class level programming")
# obj=NewClass()#creating a object
# obj.show()
# obj1=NewClass()

# class Hod:
#     def __init__(self):#constructor
#         self.name='sandhya rengate'#2byte
#         self.age=21 #3 byte
#         self.empid=1001
#     def info(self):
#         print("My name is :",self.name)
#         print("My age is :",self.age)
#         print("My emp id:",self.empid)
# obj= Hod()
# obj.info()

#parameterize
# class Hod:
#     def __init__(self,name,age,rollno):
#         self.name=name
#         self.age=age
#         self.rollno=rollno
#     def show(self):
#         print('name=',self.name)
#         print('age=',self.age)
#         print('rollno=',self.rollno)
# obj=Hod('sandhya',21,81)
# obj.show()

# class Student:
#     def __init__(self):#constructor
#         self.s_name="sandhya"
#         self.s_rollno=81
#         self.s_branch='EC'
#     def getdata(self):#method
#         self.s_mb=282828828282882#instance variab;le
# obj=Student()
# obj.getdata()
# obj.s_branch="EC"#outside
# print(obj.__dict__)
# print(obj.s_mb)

# class New:
#     def __init__(self):
#         self.a=10
# Obj1=New()
# Obj2=New()
# Obj3=New()
# Obj1.a=20
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

#static vaiable
# class New:
#     a=10
#     def __init__(self):
#         self.name="sandhya"
# Obj1=New()
# Obj2=New()
# Obj3=New()
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)
# New.a=20# we are changing the value of static var using class name
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

# class Student:
#     def __init__(self,name,rollno,mob):
#         self.name=name
#         self.rollno=rollno
#         self.mob=mob
#     def display(self):
#         print(self.name," ",self.rollno," ",self.mob)
# stud=Student("sandhya",81,953555962132)
# stud.display()

#static method
# class Student:
    #by using class name we can access static method
#     @staticmethod #decorator
#     def get_personal_detail(firstname,lastname):
#         print("your personal detail=",firstname,lastname)
#     @staticmethod
#     def contact_detail(mobile_no,rollno):
#         print("your contact detail=",mobile_no,rollno)
# Student.get_personal_detail("sandhya","rengate")
# Student.contact_detail(576475647658,1001)
# class College:
#     def college_name(self):
#         print("pagal College")
# class Student(College):
#     def student_info(self):
#         print("Name:sandhya renagte")
#         print("Branch:ece")
# obj=Student()
# obj.college_name()
# obj.student_info()
#multilevel
# class College:
#     def college_name(self):
#         print("pagal College")
# class Student(College):
#     def student_info(self):
#         print("Name:sandhya renagte")
#         print("Branch:ece")
# class Exam(Student):
#     def subject(self):
#         print("Subject1:Designe Engineering")
#         print("Subject2:Math")
#         print("Subject1:C-Language")
# obj=Exam()
# obj=Student()
# obj.college_name()
# obj.student_info()

# class Submarks:
#     math=int(input("Enter paper marks of math:"))
#     DE=int(input("Enter paper marks of design engineering:"))
#     c=int(input("Enter paper marks of c language:"))
#     english=int(input("Enter paper marks of english:"))
# class PractMarks:
#     cpract=int(input("Enter practicals marks of c language:"))
# class Result(SubjMarks,PractMarks):
#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:
#             print("pass")
#         else:
#             print("fail")
# obj=Result()
# obj.total()

#polymorphism
class Principle:
    def role(self):
        print("i am managing all activity of college")
class Dean:
    def role(self):
        print





































