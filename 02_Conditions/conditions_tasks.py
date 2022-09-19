x=10
if x>15:
      print("true")
else:
      print("x is smaller than 15")
# _____________________________________
# we use all in case we need all conditions true
# _______________________________________
# there no diffrence between all & "and" is all when we need all conditions true
#  "and" is logical opreator to Returns True if both statements are true
# _________________________________________________________
#  if we need all conditions true we use "and"
# ___________________________________________________________________
# diffrence between if & elif is 
# "if" is the first and hole conditon
# "elif" when if statment is false then i need another conditons is by using "elif"
# ___________________________________________________________________________
# diffrence between elif & else is
# "elif" when if statment is false then i need another conditons is by using "elif"
# "else" when all conditions notcatches anything do this code
# ___________________________________________________________
# can we use more "elif"
# yes we can use it alot of times if last conditions is false
# __________________________________________________
# can we use more "else"
# no we use else only at the end of statment
# __________________________________________________
# in "elif" we use "else" for if nothing is true
# _______________________________________________________________
abd_lis=[2,6,4,8,10]
if 4 in abd_lis:
      print("4 in list")
elif 4 and 6 in abd_lis:
      print("4 & 6 in list")_
elif 3 or 6 in abd_lis:
      print ("3 or 6 in list")
elif 2 and 4 and 5 in abd_lis:
      print("2 & 4 & 5 in list")
else:
      print("number not in list")
# ______________________________________________
total =int(input("Enter Your Country :"))
country =input("Enter Your Country :")
if country == "US":
      if total <= 50:
            print("Shipping Cost is  $50")
      elif total <= 100:
            print("Shipping Cost is $100")
      elif total <= 150:
            print("Shipping Costs $150")
      else:
            print("FREE")
if country == "AU": 
      if total <= 50:
            print("Shipping Cost is  $100")
      else:
            print("FREE")
