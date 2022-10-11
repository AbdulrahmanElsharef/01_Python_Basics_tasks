from abdo_oop import User as bank_user
user02 = bank_user("joud", "femal", 16, "0169852")
user02.craet_accont()
print("___________________________________________\n")
user02.account_details()
print("___________________________________________\n")

user02.debosit_withdraw(250, "debosit")
user02.debosit_withdraw(140, "withdraw")
user02.debosit_withdraw(480, "debosit")
print("____________________________________________\n")
user02.debosit_withdraw(210, "debosit")
user02.debosit_withdraw(10530, "withdraw")
user02.debosit_withdraw(105.30, "withdraw")
user02.debosit_withdraw(300, "debosit")
print("____________________________________________\n")


'''New Acoount Is Created                                           end/Django_FullStack_Project/python_ex.py"
Hello Mr joud Your Account is *0028-9-20220169852ah-he * Your Current Balance is 0                                                 ent Balance is 0
___________________________________________

Show User Account Details
user_name = joud
user_age = 16
user_gender = femal
user_Id = 0169852
___________________________________________

sucssufel debosit  your current Balance is 250
sucssufel withdrawour  your current Balance is 110
sucssufel debosit  your current Balance is 590
____________________________________________

sucssufel debosit  your current Balance is 800
Your Balance is 800 withdraw Another mount
sucssufel withdrawour  your current Balance is 694.7
sucssufel debosit  your current Balance is 994.7
____________________________________________'''
