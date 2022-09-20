#Write a function in Python that accepts a credit card number.
#It should return a string where all the characters are hidden with an asterisk except the last four.
#For example, if the function gets sent "4444444444444444", then it should return "4444".

def myCredit(num):
    cardnum=str(num)
    cardid=cardnum[-4:]
    astr="*"*len(cardnum[:-5])
    return astr + cardid
card=input("please enter card num: ")
output=myCredit(card)
print(output)
#_____
# please enter card num: 4444444444444444
# ***********4444
#___________________________________________________________________________
#Create a Python function that accepts a string.
##This function should count the number of Xs and the number of
#Os in the string.
#It# should then return a boolean value of either True or False.
#If the count of Xs and Os are equal, then the function should
#return True. If the count isn't the same, it should return False.
#If there are no Xs or Os
def equalFun(x,y):
    len1=len(x)
    len2=len(y)
    if len1 == len2:
        return True
    elif len1 != len2:
        return False
    else:
        return True
Xs=input("enter first string : ")
Os=input("enter last string : ")
out=equalFun(Xs,Os)
print(out)
#enter first string : abdo
#enter last string : abdo
#True
#______
#enter first string : 
#enter last string : 
#True
#______
#enter first string : abdoelsharef
#enter last string : noureldin
#False
#______

#__________________________________________________________
###Write a Python function that accepts three parameters.
#The first parameter is an integer.
#The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer.
def calculate(x,o,y):
    if o == "+":
        return x+y
    elif o == "-":
        return x-y
    elif o == "/":
        return x/y
    elif o == "*":
        return x*y
    elif o == "**":
        return x**y
    else:
        return "wrong input"
num1=float(input("enter  num 1 : "))
operators=input("enter operators  : ")
num2=float(input("enter num 2 : "))
calc=calculate(num1,operators,num2)
print(calc)
#________
#enter  num 1 : 10
#enter operators  : *
#enter num 2 : 15
#150
#___________
#enter  num 1 : -2
#enter operators  : -
#enter num 2 : 25
#-27.0
#_____________
#enter  num 1 : 4
#enter operators  : **
#enter num 2 : 4
#256.0
#__________________________________________________
#____________________________________________________________
#Create a function in Python that accepts two parameters.
#T#he first will be a list of numbers. The second parameter will be a string
#that can be one of the following values: asc, desc, and none.

#If the second parameter is "asc," then the function should return a list
#with the numbers in ascending order. If it's "desc," then the list should be
#in descending order, and if it's "none," it should return the original list unaltered
def reverslis(x,y):
    x=my_lis
    if y == "asc":
        x.sort()
        return x
    elif y == "desc":
        x.sort(reverse=True)
        return x
    else:
        return x
my_lis=[10,35,52,22,2,8,32,92,66,0,100,87]
lis_inp=input("enter reverse  :")
my_order_lis=reverslis(my_lis,lis_inp)
print(my_order_lis)
#enter reverse  :asc
#[0, 2, 8, 10, 22, 32, 35, 52, 66, 87, 92, 100]

#enter reverse  :desc
#[100, 92, 87, 66, 52, 35, 32, 22, 10, 8, 2, 0]

#enter reverse  :
#[10, 35, 52, 22, 2, 8, 32, 92, 66, 0, 100, 87]
#___________________________________________________________________
# Create a Python function that accepts a string. 
# The function should return a string, with each character in
#  the original string doubled. If you send the function "now" as a 
#  parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".
def repeat_chr(chr):
    y=[]
    repat=""
    for x in chr:
        # t=x*2
        y.append(x*2)
    return repat.join(y)
in_chr=input("enter chracter :")
out = repeat_chr(in_chr)
print(out)
# enter chracter: now
# nnooww
# __________________
# nter chracter: 123a!
# 112233aa!!
# _________________________________________________________________
