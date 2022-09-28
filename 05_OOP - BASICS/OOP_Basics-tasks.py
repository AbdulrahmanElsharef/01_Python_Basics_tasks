

from ast import Pass
from msilib.schema import Class


class Iphone():
     ''' new class of iphone '''
     serial=""
     def __init__(self,model,color,stor,cam):
          self.model=model
          self.color=color
          self.stor=stor
          self.cam=cam
     def prod(self,status,date):
          if status == "Stable":
               print(f"iphone model ({self.model}) is {status} Edition ")
               print(f"iphone model ({self.model})is Redy fo Selling At {date} ")
          else:
               print(f"iphone model ({self.model}) Is {status} Edition ")
               print(f"iphone model ({self.model})Is Unavilabe for Selling Befor {date} ")


class Iphone_X(Iphone):
     ''' new class of iphone '''
     Pass

print("_____________________________________________________\n")
p_serial=input("Enter Product Serial :")
p_model=input("Enter Product Model :")
p_color = input("Enter Product Color :")
p_storage = input("Enter Product Storage :")
p_camera = input("Enter Product Cam Mega :")
print("*******************************************************\n")

iphone_01 = Iphone(p_model, p_color, p_storage, p_camera)
iphone_01.serial = p_serial
print(f"iphone_01 serial is ({iphone_01.serial}) ")
print(f"iphone_01 model is ({iphone_01.model}) ")
print(f"iphone_01 color is ({iphone_01.color}) ")
print(f"iphone_01 storage is ({iphone_01.stor}) ")
print(f"iphone_01 cam is ({iphone_01.cam}) ")
iphone_01.prod("Stable", "31/12/2022")


print("_____________________________________________________\n") 
p_serial = input("Enter Product Serial :")
p_model = input("Enter Product Model :")
p_color = input("Enter Product Color :")
p_storage = input("Enter Product Storage :")
p_camera = input("Enter Product Cam Mega :")
print("*******************************************************\n")

iphone_X02 = Iphone_X(p_model, p_color, p_storage, p_camera)
iphone_X02.serial = p_serial
print(f"iphone_X02 serial is ({iphone_X02.serial}) ")
print(f"iphone_X02 model is ({iphone_X02.model}) ")
print(f"iphone_X02 color is ({iphone_X02.color}) ")
print(f"iphone_X02 storage is ({iphone_X02.stor}) ")
print(f"iphone_X02 cam is ({iphone_X02.cam}) ")
iphone_X02.prod("Beta", "31/6/2023")
print("_____________________________________________________\n")


'''
_____________________________________________________

Enter Product Serial :iph-2022-1400afg

iphone_01 serial is (iph-2022-1400afg)
iphone_01 model is (iphone-14)
iphone_01 color is (black)
iphone_01 storage is (128G)
iphone_01 cam is (148Mg)
iphone model (iphone-14) is Stable Edition
iphone model (iphone-14)is Redy fo Selling At 31/12/2022
_____________________________________________________

Enter Product Serial :iph-2023-xp0145ak
Enter Product Model :
Enter Product Color :Gray
Enter Product Storage :256G
Enter Product Cam Mega :156Mg
*******************************************************

iphone_X02 serial is (iph-2023-xp0145ak)
iphone_X02 model is ()
iphone_X02 color is (Gray)
iphone_X02 storage is (256G)
iphone_X02 cam is (156Mg)
iphone model () Is Beta Edition
iphone model ()Is Unavilabe for Selling Befor 31/6/2023
_____________________________________________________
'''


class Student():
     ''' new class of class Student():'''

     def __init__(self, name):
          self.name = name
          # self.age = age
          # self.subject = subject
          self.marks = {}

     def add_mark(self, subject,mark):
          self.marks[subject] = mark

     def student_av(self):
          sub = list(self.marks.keys())         
          avr = sum(self.marks.values())/len(self.marks.values())
          print(f"student Subjects is {sub}")
          print(f"student avreage marks is {avr}")


print("____________________________________________________")

st_1 = Student("abdo")
st_1.add_mark('Math',53)
st_1.add_mark('Arabic', 66)
st_1.add_mark('English', 88)
st_1.add_mark('Science', 91)
st_1.student_av()

print("____________________________________________________")

'''____________________________________________________
student Subjects is ['Math', 'Arabic', 'English', 'Science']
student avreage marks is 74.5
_______________________________________________________'''



class Bank():
     '''creat bank class'''
     def __init__(self,name,gender,age):
          self.name=name
          self.gender=gender
          self.age=age          
     
class User(Bank):
     '''creat User class'''

     def __init__(self, name, gender, age,id):
          super().__init__( name, gender, age)
          self.id=id
          self.balance=0

     def craet_accont(self):
          print("New Acoount Is Created")
          print(f"Hello Mr {self.name} Your Account is *0028-9-2022{self.id}ah-he* Your Current Balance is {self.balance}")

     def account_details(self):
          print("show user account details".title())
          print(f"user_name = {self.name}\nuser_age = {self.age}\nuser_gender = {self.gender}\nuser_Id = {self.id}")

     def debosit_withdraw(self,cash,opreation):
          if opreation=="withdraw":
               if cash > self.balance:
                    print(f"Your Balance is {self.balance} withdraw Another mount")
               else:
                    self.balance-=cash
                    print(f"sucssufel withdrawour  your current Balance is {self.balance} ")
          elif opreation == "debosit":
               self.balance += cash
               print(f"sucssufel debosit  your current Balance is {self.balance} ")
          else:
               print("This Opreatin Is Invalid")

user01=User("abdo","male",35,"0105258")
user01.craet_accont()
print("___________________________________________\n")
user01.account_details()
print("___________________________________________\n")

user01.debosit_withdraw(1500, "debosit")
user01.debosit_withdraw(1050, "withdraw")
user01.debosit_withdraw(850, "debosit")
print("____________________________________________\n")
user01.debosit_withdraw(630, "debosit")
user01.debosit_withdraw(16800, "withdraw")
user01.debosit_withdraw(1680,"withdraw")
user01.debosit_withdraw(400, "debosit")
print("____________________________________________\n")


'''New Acoount Is Created
Hello Mr abdo Your Account is *0028-9-20220105258ah-he* Your Current Balance is 0
___________________________________________

Show User Account Details
user_name = abdo
user_age = 35
user_gender = male
user_Id = 0105258
___________________________________________

sucssufel debosit  your current Balance is 1500
sucssufel withdrawour  your current Balance is 450
sucssufel debosit  your current Balance is 1300
____________________________________________

sucssufel debosit  your current Balance is 1930
Your Balance is 1930 withdraw Another mount
sucssufel withdrawour  your current Balance is 250
sucssufel debosit  your current Balance is 650
____________________________________________
'''





