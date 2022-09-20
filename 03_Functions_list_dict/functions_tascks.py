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
