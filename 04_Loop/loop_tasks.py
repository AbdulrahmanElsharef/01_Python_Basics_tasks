def loop(num1,num2):
    for x in range(num1,num2+1):
         print (x)
num1=int(input("enter mum1 : "))
num2=int(input("enter mum2 : "))
loop(num1,num2) 
'''

''' enter mum1 : 5
enter mum2 : 17
5
6
7
8
9
10
11
12
13
14
15
16
17 '''

'''enter mum1 : 6
enter mum2 : 17
6
7
8
9
10
11
12
13
14
15
16'''



'''
def while_loop(n):
    x=1
    while x <=100 :
            if x % n == 0:
                print(x)
            x+=1
num=int(input("enter mum1 : "))
while_loop(num) '''

'''enter mum1 : 7
7
14
21
28
35
42
49
56
63
70
77
84
91
98 '''
'''enter mum1 : 15
15
30
45
60
75
90'''


'''Write a Python program that prints each item and its corresponding type from the following list.'''
Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]'''


  '''datalist = [1452, 11.23, 1+2j, True, 'w3resource',(0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for x in datalist:
      print(f"curent item is {x} and type is {type(x)}")
print("datalist is finish")'''
  '''curent item is 1452 and type is <class 'int'>
curent item is 11.23 and type is <class 'float'>
curent item is (1+2j) and type is <class 'complex'>
curent item is True and type is <class 'bool'>
curent item is w3resource and type is <class 'str'>
curent item is (0, -1) and type is <class 'tuple'>
curent item is [5, 12] and type is <class 'list'>
curent item is {'class': 'V', 'section': 'A'} and type is <class 
'dict'>'''
datalist is finish


