# x=True   #boolean variable
# print(type(x))
# # ________________________________
# y=120   #int variable
# print(type(y))
# # ________________________________
# z=2.3   #float varibale
# print(type(z))
# # __________________________________
# s="abdulrahman"  #str variable
# print(type(s))
# # ___________________________________
# c=int(y)    #convert int to float
# print(type(c))
# # ____________________________________
# #we can convert str to in int if string its include number only not text
# d="15"
# r=int(d)
# print(type(r))
# # ____________________________________
# glis=[1,2,3,4,5] #list
# print(type(glis))
# # _____________________________________
# ftuble=(10,11,12,13,14,15)  #tuble
# print(type(ftuble))
# # _____________________________________
# a = tuple(glis)
# print(type(a))
# # _____________________________________
# # ____________________________________
# edic={1:"abdo",2:"python",3:"django"}
# # ______________________________________
# # yes we can use semi colon ; with python to make other statmen in same line 
# # examble
# q=15 ; u=";"
# print(u)
# # _____________________________________
# # ___________________________________________
# ###python is interprated or compiled?###
# # python is interpreted language
# # _________________________________________________________
# # ## Low-Level Languages? ##
# # Debugging them is very difficult.
# # They are not very easy to understand.
# # All the languages come with complex maintenance.
# # They are not portable.
# # These languages depend on machines. Thus, one can run it on various platforms.
# # They always require assemblers for translating instructions.
# # Low-level languages do not have a very wide application in today’s times. 
# # _________________________________________________
# # ## High-Level Languages?  ##
# # One can easily interpret and combine these languages as compared to the low-level languages.
# # They are very easy to understand.
# # Such languages are programmer-friendly.
# # Debugging is not very difficult.
# # They come with easy maintenance and are thus simple and manageable.
# # One can easily run them on different platforms.
# # They require a compiler/interpreter for translation into a machine code.
# # A user can port them from one location to another.
# # Such languages have a low efficiency of memory. So it consumes more memory than the low-level languages.
# # They are very widely used and popular in today’s times.
# # Java, C, C++, Python, etc., are a few examples of high-level languages.
# # ____________________________________________________
# # diffrence between = , ==
# # x=5  this mean variable x is assign by 5
# # x==5 this mean ask if variable x  is equal to 5 and result (true or false)
# # _________________________________________________________________
# # ## what do we mean using != ##
# # x==5 this mean ask if variable x is not equal to 5 and result (true or false)
# # _________________________________________________________________
# #   $$ what is operator precedence in python
# # Operator precedence in Python simply refers to the order of operations.
# #  Operators are used to perform operations on variables and values. 
# # Python classifies its operators in the 
# # following groups: Arithmetic operators. Assignment operators.
# # _________________________________________________________________
# x=10 #varaibll
# # __________________
# x+=15 #increas x by 5
# # ______________
# x/=5 #divid x  by  5
# # _________________
# x*=10 #mult x by 10
# # _______________________
# x%=3 #module or remainig division x by 3
# # _________________________
# print(11%4) #print module 11,4
# # ____________________________
# print(2**3) #print exponent 2,3
# # ________________________________
# print(11/3) #divid 11 by 3
# # ___________________________________
# #_____________________________________________-
# # we can divid 11 by 3 and get integer num
# print(11//3) # using floor division
# # ____________________________________


import datetime as dt
from unittest.mock import patch
'''Write a Python program to display the current date and time.
Sample Output :
Current date and time :'''
'''def  date_now():
      now=dt.datetime.now()
      print(f"current datetime is : {now}")
date_now()'''



'''Write a Python program to accept a filename from the user and print the extension of that

path=input("enter yor path : ")
ext = path[path.index(".")+1:]
print(f"your extintion is : {ext}")
_________________________________________________________

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print(f_extns[-1])'''

'''x=(input("enter num"))
print(int(x)+int(x*2)+int(x*3))'''


'''import calendar

y=int(input("enter year :"))
m=int(input("enter month :"))
cal=calendar.month(y,m)
print(cal)'''


''''from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
sub_date = l_date - f_date
print(f"{sub_date.days} days")
'''''


'''def cup(n):
      sum=0
      for x in range(n):
            if x >0:
                  y = pow(x, 3)
                  sum+=y
      return f"Sum of cubes smaller than the specified number is {sum}"
num=int(input("enter num :"))
print(cup(num))'''


'''lis = [19, 19, 15, 5, 5, 5, 1, 2]

print(lis)
if lis.count(19)==2 and lis.count(5)==3:
      print (True)
else:
      print(False)'''


x=lambda *lis:lis.sort()
# num=int(input("enter num :"))

result = x(('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82))
print(result)
