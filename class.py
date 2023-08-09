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
    def __init__(self,Name='defult',Age=18,Grade=1,City='irbid',Speacialise='computer'):
        self.name=Name
        self.age=Age
        self.grade=Grade
        self.city=City
        self.speacialise=Speacialise
    def __str__(self):
       return f'name is{self.name} and age {self.age} and grade{self.grade}and city{self.city}and speacialise{self.speacialise}'

    def addCorse(self, newCoures):
       return f'hello{self.name} you have added{newCoures}to youer coures'


print('hito my programe')
name=input('enter the name')
age=int(input('enter the age'))
grade=int(input('enter the grade'))
city=input('enter the city')
speacialise=input('enter the speacialise')
studint1=Studint(name,age,grade,city,speacialise)
print("information added succes")
print("added new croues")
coures=input('enter the coures')
print(studint1. addCorse(coures))
print(studint1)