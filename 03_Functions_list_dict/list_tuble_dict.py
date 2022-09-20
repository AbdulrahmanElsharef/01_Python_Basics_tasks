# 2: The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1].
# Approac
def swapLis(lis):
      first = lis.pop(0)  
      last = lis.pop(-1)
      lis.insert(0, last) 
      lis.append(first)  
      return lis
newList = [12, 35, 9, 56, 24]
out = swapLis(newList)
print(out)

# output : [24, 35, 9, 56, 12]
# _____________________________________________________
# Code #1 : Demonstrating finding length of a list using the Naive Method
test_list = [ 1, 4, 5, 7, 8 ]
count=0
for x in test_list:
      count+=1
print(count)
# _______________
print(len(test_list))
# ________________________________________________________


# python code to Check if element exists in list or not
lst = [1, 6, 3, 5, 3, 4]

if 7 in lst:
      print("exist")
else:
      print("not exist")

# ___________________________________________________
# The task is to perform the operation of removing all the occurrences of a given item/element present in a list
lis = [1, 3, 4, 6, 5, 1]
newlis=[] 
for x in lis:
      y=lis.count(x)
      if y == 1:
            newlis.append(x)
else:
      newlis
print(newlis)
#_________________________________________________________________________

# Exercise 1: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)
# ______________________________________________________
# Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dic3=dict1.copy()
dic3.update(dict2)
print(dic3)
#____________________________________________________________
# Exercise 3: Print the value of key ‘history’ from the below dict

sampleDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80
                  }
            }
      }
}
print(sampleDict["class"]["student"]["marks"]["history"])
# ________________________________________________________________________

row = int(input("Enter number of rows: "))
for x in range(row):
      for j in range(x):
            print(j+1,end="-")
      print("\n")
