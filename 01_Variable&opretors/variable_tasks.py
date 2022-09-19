x=True   #boolean variable
print(type(x))
# ________________________________
y=120   #int variable
print(type(y))
# ________________________________
z=2.3   #float varibale
print(type(z))
# __________________________________
s="abdulrahman"  #str variable
print(type(s))
# ___________________________________
c=int(y)    #convert int to float
print(type(c))
# ____________________________________
#we can convert str to in int if string its include number only not text
d="15"
r=int(d)
print(type(r))
# ____________________________________
glis=[1,2,3,4,5] #list
print(type(glis))
# _____________________________________
ftuble=(10,11,12,13,14,15)  #tuble
print(type(ftuble))
# _____________________________________
a = tuple(glis)
print(type(a))
# _____________________________________
# ____________________________________
edic={1:"abdo",2:"python",3:"django"}
# ______________________________________
# yes we can use semi colon ; with python to make other statmen in same line 
# examble
q=15 ; u=";"
print(u)
# _____________________________________
# ___________________________________________
###python is interprated or compiled?###
# python is interpreted language
# _________________________________________________________
# ## Low-Level Languages? ##
# Debugging them is very difficult.
# They are not very easy to understand.
# All the languages come with complex maintenance.
# They are not portable.
# These languages depend on machines. Thus, one can run it on various platforms.
# They always require assemblers for translating instructions.
# Low-level languages do not have a very wide application in today’s times. 
# _________________________________________________
# ## High-Level Languages?  ##
# One can easily interpret and combine these languages as compared to the low-level languages.
# They are very easy to understand.
# Such languages are programmer-friendly.
# Debugging is not very difficult.
# They come with easy maintenance and are thus simple and manageable.
# One can easily run them on different platforms.
# They require a compiler/interpreter for translation into a machine code.
# A user can port them from one location to another.
# Such languages have a low efficiency of memory. So it consumes more memory than the low-level languages.
# They are very widely used and popular in today’s times.
# Java, C, C++, Python, etc., are a few examples of high-level languages.
# ____________________________________________________
# diffrence between = , ==
# x=5  this mean variable x is assign by 5
# x==5 this mean ask if variable x  is equal to 5 and result (true or false)
# _________________________________________________________________
# ## what do we mean using != ##
# x==5 this mean ask if variable x is not equal to 5 and result (true or false)
# _________________________________________________________________
#   $$ what is operator precedence in python
# Operator precedence in Python simply refers to the order of operations.
#  Operators are used to perform operations on variables and values. 
# Python classifies its operators in the 
# following groups: Arithmetic operators. Assignment operators.
# _________________________________________________________________
x=10 #varaibll
# __________________
x+=15 #increas x by 5
# ______________
x/=5 #divid x  by  5
# _________________
x*=10 #mult x by 10
# _______________________
x%=3 #module or remainig division x by 3
# _________________________
print(11%4) #print module 11,4
# ____________________________
print(2**3) #print exponent 2,3
# ________________________________
print(11/3) #divid 11 by 3
# ___________________________________
#_____________________________________________-
# we can divid 11 by 3 and get integer num
print(11//3) # using floor division
# ____________________________________

