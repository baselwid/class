# class Client:




#     def __init__(self,Nameobj='deafult',Phoneobj=123456789,Emailobj='mohad@gmail.com',Purobj=0):
#          self.name=Nameobj
#          self.phone=Phoneobj
#          self.email=Emailobj
#          self.purchies=Purobj
#     def __str__(self):
#        return f'nameis{self.name} and phone{self.phone} and email{self.email} and purchies{self.purchies}'
#     def talk(self):
#         return f'hello my name is {self.name}'
# obj1=Client(Nameobj='mohammed',Phoneobj=123456789,Emailobj='sadsafas')
# obj2=Client('ahmed',123456789)
# print(obj1.name)



class Studint:
    def __init__(self,Name='defult',Age=18,Grade=1,City='irbid',Speacialise='computer',passowrd='123456'):
        self.name=Name
        self.age=Age
        self.grade=Grade
        self.city=City
        self.speacialise=Speacialise
        self.password=passowrd
    def __str__(self):
       return f'name is{self.name} and age {self.age} and grade{self.grade}and city{self.city}and speacialise{self.speacialise}'
    def talk(self):
        return f'hello my name is {self.name}'
    def addCorse(self, newCoures):
       return f'hello{self.name} you have added{newCoures}to youer coures'

students=[]
while True:

    print('welcome to programe')
    print('1-login')
    print('2-register')
    print('3-exit')
    userchoice=int(input('emter the choice'))
    if userchoice ==1:
        print('welcome to our longin page')
        while True:

         username=input('enter th name  ')
         password=input('enter the password  ')
         for i in range(len(students)):
            if students[i].name==username and students[i].password==password:
                print('your are logged in succesfully')
                print(students[i])
                break
            
            else:
                print('wrong username or password')
                #  OR
        # for student in students:
        #      if student.name==username and student.password==password:
        #         print('your are logged in succesfully')
        #         print(student)
        #         break



    
    elif userchoice==2:
        print('hello my programe')
        name=input('enter the name  ')
        age=int(input('enter the age  '))
        grade=int(input('enter the grade  '))
        city=input('enter the city  ')
        speacialise=input('enter the speacialise  ')
        password=input('enter the password  ')
        studint1=Studint(name,age,grade,city,speacialise)
        print("information added succes")
        print("added new croues")
        coures=input('enter the coures  ')
        print(studint1. addCorse(coures))
        print(studint1)
        students.append(studint1)
        print(students)
    elif userchoice==3:
        break