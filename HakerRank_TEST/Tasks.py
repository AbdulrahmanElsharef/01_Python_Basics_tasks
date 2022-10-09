# Try finding your ancestors and offspring with code.

# Create a function that takes a number x and a character y("m" for male, "f" for female), and returns the name of an ancestor(m/f) or descendant(m/f).

# If the number is negative, return the related ancestor.
# If positive, return the related descendant.
# You are generation 0. In the case of 0 (male or female), return "me!".
# Examples
# generation(2, "f") ➞ "granddaughter"

# generation(-3, "m") ➞ "great grandfather"

# generation(1, "f") ➞ "daughter"
# Notes
# Check the Resources tab for helpful hints.

# Generation	Male	Female
# -3	great grandfather	great grandmother
# -2	grandfather	grandmother
# -1	father	mother
# 0	me! me!
# 1	son	daughter
# 2	grandson	granddaughter
# 3	great grandson	great granddaughter
# # 

'''def generation(x, y):
       # dictionry for data
       dict_fam = {-3: {"m": "great grandfather", "f": "great grandmother"},
              -2: {"m": "grandfather", "f": "grandmother"}, -1: {"m": "father", "f": "mother"}, 1: {"m": "son", "f": "daughter"}, 2: {"m": "grandson", "f": "granddaughter"}, 3: {"m": "great grandson", "f": "great granddaughter"}}
       if y == "m":
              if x==0:
                     print("me!")
              else :
                     print(dict_fam.get(x, {}).get("m"))
              
       elif y == "f":
              if x == 0:
                     print("me!")
              else:
                     print(dict_fam.get(x, {}).get("f"))
       else:
              print("weong gen or num")

gen=input("enter gender :")
num=int(input("number :"))
generation(num,gen)'''


# // Calling makePlusFunction(5) returns a new function that takes an input,
# // and returns the result when adding 5 to it.

# const plusFive = makePlusFunction(5)

# plusFive(2) ➞ 7

# plusFive(-8) ➞ - 3

# // Calling makePlusFunction(10) returns a new function that takes an input,
# // and returns the result when adding 10 to it.

# const plusTen = makePlusFunction(10)

# plusTen(0) ➞ 10

# plusTen(188) ➞ 198

# plusFive(plusTen(0)) ➞ 15


'''def consit(num):
       return num


def sum(n):
       fun=consit(int(input("enter consit:")))
       x=fun+n
       return x


print(sum(188))'''


# Your task is to create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two methods getArea() (PI*r ^2) and getPerimeter() (2*PI*r) which give both respective areas and perimeter (circumference).

# For help with this class , I have provided you with a Rectangle constructor which you can use as a base example.

# Examples
# let circy = new Circle(11)
# circy.getArea()

# // Should return 380.132711084365
# let circy = new Circle(4.44)
# circy.getPerimeter()

# // Should return 27.897342763877365
# Notes
# Don't worry about floating point precision - I've factored in the chance that your answer may be more or less accurate than mine. This is more of a tutorial than a challenge so the topic covered may be considered advanced, yet the challenge is more simple - so if this challenge gets labelled as easy, don't worry too much.


'''class new_Circle():
       def __init__(self, area):
              self.area = float(area)
              self.pi = 22/7

       def getArea(self):
              Area = self.pi * self.area * self.area
              print (Area)
              
       def getPerimeter(self):
              perimeter = 2*self.pi*self.area  
              print (perimeter)


circy = new_Circle(11)
circy.getArea()#380.2857142857143

# // Should return 380.132711084365
circy = new_Circle(4.44)
circy.getPerimeter()#27.90857142857143

# // Should return 27.897342763877365'''
