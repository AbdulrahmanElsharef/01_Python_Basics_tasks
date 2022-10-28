
# import Car_Items class from module folder from company_items file
# immplement object car_1 from car items class
# from .ITEMS_Class import Car_Items
# car_1 = Car_Items()

# *** WELCOM TO ITEMS PROGRAMM ** *
# Choise Your Items Modify
# 1-Add Item(key - "add")
# 2-Update Item(key - "update")
# 3-Del Item(key - "del")
# 4-ShowAll Items(key - "items")
# 5-Item Details(key - "item")
# 7-Item Accounting(key - "account")
# 8-Exit(key - "exit")
# _____________________ADD ITEM_____________________________________________________________________
# Enter Choise: add
# Item Name: bmw
# Item Cost: 450000
# Item Sell Price: 600000
# Item Stosk: 50
# Item You Have Add Is: (0087Bmw-476/022)
# *************************
# Add_New Items Is Finshed
# ##################################################
# Enter Choise: add
# Item Name: fiat
# Item Cost: 230000
# Item Sell Price: 335000
# Item Stosk: 25
# Item You Have Add Is: (0050Fiat-667/022)
# *************************
# Add_New Items Is Finshed
# ##################################################
# _____________________UPDATE ITEM_____________________________________________________________________
# Enter Choise: update
# ['0087BMW-476/022', '0050FIAT-667/022']
# Item_Seiral number: 0050FIAT-667/022
# Item Name: volvo
# Item Cost: 4650000
# Item Sell Price: 720000
# Item Stosk: 45
# New Item Is: 0050Volvo-921/022
# *************************
# ##################################################
# _____________________DELET ITEM_____________________________________________________________________
# Enter Choise: del
# ['0087BMW-476/022', '0050VOLVO-921/022']
# Item_Seiral number: 0087BMW-476/022
# Item: 0087Bmw-476/022 Is Delete
# *************************
# ##################################################
# _____________________ADD ITEM_____________________________________________________________________
# Enter Choise: add
# Item Name: seat
# Item Cost: 345000
# Item Sell Price: 495000
# Item Stosk: 36
# Item You Have Add Is: (0043Seat-656/022)
# *************************
# Add_New Items Is Finshed
# ##################################################
# _____________________SHOW ALL SERIAL ITEMS_____________________________________________________________________
# Enter Choise: items
# All Items Is['0050Volvo-921/022', '0043Seat-656/022']
# Show Of All Items Is Finshed
# *************************
# ##################################################
# _____________________SHOW ITEM DETAILS ITEM_____________________________________________________________________
# Enter Choise: item
# ['0050VOLVO-921/022', '0043SEAT-656/022']
# Item_Seiral number: 0050VOLVO-921/022
# Item: 0050Volvo-921/022 Details Is[('Item_Name', 'Volvo'), ('Item_Cost', 4650000), ('Item_Sell', 720000), ('Item_Stock', 45)]
# *************************
# ##################################################
# ##################################################
# _____________________ ITEM ACCOUNTING_____________________________________________________________________
# Enter Choise: account
# ['0087BMW-345/022']
# Item_Seiral number: 0087BMW-345/022
# Choise Your Items Accont
# 1-Stock Item(key - "stock")
# 2-Cost Item(key - "cost")
# 3-Sales Item(key - "sales")
# 4-Profit Item(key - "profit")
# 5-Exit(key - "exit")
# _____________________STOCK ITEM_____________________________________________________________________
# Enter Choise: stock
# Stok Of Item(0087Bmw-345/022) = (25 Items)
# *************************
# _____________________COST OF PURSHAES ITEM_____________________________________________________________________
# Enter Choise: cost
# Enter Number Of Purshaing Items: 10
# Cost Of Purshaing  Item(0087Bmw-345/022) = Items(10) * Cost Price(200000) = (2000000 $)
# Current Stock Of Item Is(35 Items)
# *************************
# _____________________SALES ITEM_____________________________________________________________________
# Enter Choise: sales
# Enter Number Of Sales Items: 15
# Total Sales Of Item(0087Bmw-345/022) = Sales Item(15) * Sales Price(350000) = (5250000 $)
# Current Stock Of Item Is(20 Items)
# *************************
# _____________________PROFIT ITEM_____________________________________________________________________
# Enter Choise: profit
# Profit Of Item(0087Bmw-345/022) = Total Sales(5250000) - Total Cost(2000000) = (3250000 $)
# *************************
# _____________________EXIT ACCONTING_____________________________________________________________________
# Enter Choise: exit
# *************************
# EXIT ITEM ACCOUNTING
# ##################################################
# _____________________EXIT PROGRAMM_____________________________________________________________________
# Enter Choise: exit
# *************************
# EXIT PROGRAMM
# ##################################################


# immplement object car_1 from car items class
from ITEMS_Class import Items


class Car(Items):
    pass


car_1 = Car()


# *** WELCOM TO PROGRAMM ** *

# 1-SIGHN IN(key - "1")
# 2-SIGHN UP(key - "2")
# 3-USER UPDATE(key - "3")
# 4-EXIT(key - "4")
# ___________add user_____________________________________________________
# Enter Choise: 2
# User Name & Email: nour
# Pass_Word: n2810
# User Department: stock
# Hello Welcome Nour Please Sighn In
# dict_keys(['abdo.elsharef', 'nour'])
# *************************
# Enter Choise: 2
# User Name & Email: zian
# Pass_Word: z132018
# User Department: accounting
# Hello Welcome Zian Please Sighn In
# dict_keys(['abdo.elsharef', 'nour', 'zian'])
# *************************
# ##################################################
# ___________update user_____________________________________________________
# Enter Choise: 3
# ['abdo.elsharef', 'nour', 'zian']
# User Name & Email: nour
# New User Name & Email: joud
# New Pass_Word: j1732020
# New User Department: stock
# New User Is: Joud Please Sighn In
# *************************
# ##################################################
# ___________sign in_____________________________________________________
# Enter Choise: 1
# dict_items([('abdo.elsharef', {'user_pass': 'abdo123456789', 'user_depart': 'admin'}), ('zian', {
#            'user_pass': 'z132018', 'user_depart': 'accounting'}), ('joud', {'user_pass': 'j1732020', 'user_depart': 'stock'})])
# User Name & Email: joud
# Pass Name: j1732020
# User Department: stock
# Hello: (Joud) Welcome Back
# Choise Your Items Modify
# 1-Add Item(key - "add")
# 2-Update Item(key - "update")
# 3-Del Item(key - "del")
# 4-ShowAll Items(key - "items")
# 5-Item Details(key - "item")
# 7-Exit(key - "exit")
# ___________add item____________________________________________________
# Enter Choise: add
# Item Name: bmw
# Item Cost: 255000
# Item Sell Price: 375000
# Item Stosk: 35
# Item You Have Add Is: (0046Bmw-497/022)
# *************************
# Add_New Items Is Finshed
# ##################################################
# ___________add item____________________________________________________
# Enter Choise: volvo
# *************************
# **Wrong Item Modify**
# ##################################################
# ___________add item____________________________________________________
# Enter Choise: add
# Item Name: volvo
# Item Cost: 275000
# Item Sell Price: 415000
# Item Stosk: 45
# Item You Have Add Is: (0073Volvo-677/022)
# *************************
# Add_New Items Is Finshed
# ##################################################
# ___________add item____________________________________________________
# Enter Choise: add
# Item Name: sf
# Item Cost: 150
# Item Sell Price: 200
# Item Stosk: 36
# Item You Have Add Is: (0077Sf-218/022)
# *************************
# Add_New Items Is Finshed
# ##################################################
# ___________update item____________________________________________________

# ['0046BMW-497/022', '0073VOLVO-677/022', '0077SF-218/022']
# Item_Seiral number: 0077SF-218/022
# Item Name: seat
# Item Cost: 205000
# Item Sell Price: 315000
# Item Stosk: 65
# New Item Is: 0032Seat-102/022
# *************************
# ##################################################
# ___________del item____________________________________________________
# Enter Choise: del
# ['0046BMW-497/022', '0073VOLVO-677/022', '0032SEAT-102/022']
# Item_Seiral number: 0073VOLVO-677/022
# Item: 0073Volvo-677/022 Is Delete
# *************************
# ##################################################
# Choise Your Items Modify
# 1-Add Item(key - "add")
# 2-Update Item(key - "update")
# 3-Del Item(key - "del")
# 4-ShowAll Items(key - "items")
# 5-Item Details(key - "item")
# 7-Exit(key - "exit")
# Enter Choise: DD
# *************************
# **Wrong Item Modify**
# ##################################################
# ___________add item____________________________________________________
# Enter Choise: ADD
# Item Name: FAIT
# Item Cost: 145000
# Item Sell Price: 215000
# Item Stosk: 84
# Item You Have Add Is: (0037Fait-591/022)
# *************************
# Add_New Items Is Finshed
# ##################################################
# ___________all items____________________________________________________
# Enter Choise: ITEMS
# All Items Is['0046Bmw-497/022', '0032Seat-102/022', '0037Fait-591/022']
# Show Of All Items Is Finshed
# *************************
# ##################################################
# ___________ item detail____________________________________________________
# Enter Choise: ITEM
# ['0046BMW-497/022', '0032SEAT-102/022', '0037FAIT-591/022']
# Item_Seiral number: 0046BMW-497/022
# Item: 0046Bmw-497/022 Details Is[('Item_Name', 'Bmw'), ('Item_Cost', 255000), ('Item_Sell', 375000), ('Item_Stock', 35)]
# *************************
# ##################################################

# Enter Choise: EXIT
# *************************
# EXIT PROGRAMM
# ##################################################
# ##################################################
# Enter Choise: 1
# dict_items([('abdo.elsharef', {'user_pass': 'abdo123456789', 'user_depart': 'admin'}), ('zian', {
#            'user_pass': 'z132018', 'user_depart': 'accounting'}), ('joud', {'user_pass': 'j1732020', 'user_depart': 'stock'})])
# User Name & Email: zain
# Pass Name: z132018
# User Department: accounting
# Hello: (Zain) Welcome Back
# "User_Nam Or User_Pass Invalid"
# "Please Try Enter Valid Name Or Password Again"
# *************************
# ##################################################

# 1-SIGHN IN(key - "1")
# 2-SIGHN UP(key - "2")
# 3-USER UPDATE(key - "3")
# 4-EXIT(key - "4")
# Enter Choise: 1
# dict_items([('abdo.elsharef', {'user_pass': 'abdo123456789', 'user_depart': 'admin'}), ('zian', {
#            'user_pass': 'z132018', 'user_depart': 'accounting'}), ('joud', {'user_pass': 'j1732020', 'user_depart': 'stock'})])
# User Name & Email: zian
# Pass Name: z132018
# User Department: accounting
# Hello: (Zian) Welcome Back
# Choise Your Items Modify
# 1-ShowAll Items(key - "items")
# 2-Item Details(key - "item")
# 3-Accounting(key - "account")
# 8-Exit(key - "exit")
# Enter Choise: item
# ['0046BMW-497/022', '0032SEAT-102/022', '0037FAIT-591/022']
# Item_Seiral number: 0032SEAT-102/022
# Item: 0032Seat-102/022 Details Is[('Item_Name', 'Seat'), ('Item_Cost', 205000), ('Item_Sell', 315000),
#                                   ('Item_Stock', 65)]
# *************************
# ##################################################
# Choise Your Items Modify
# 1-ShowAll Items(key - "items")
# 2-Item Details(key - "item")
# 3-Accounting(key - "account")
# 8-Exit(key - "exit")
# Enter Choise: account
# ['0046BMW-497/022', '0032SEAT-102/022', '0037FAIT-591/022']
# Item_Seiral number: 0037FAIT-591/022
# Choise Your Items Accont
# 1-Stock Item(key - "stock")
# 2-Cost Item(key - "cost")
# 3-Sales Item(key - "sales")
# 4-Profit Item(key - "profit")
# 5-Exit(key - "exit")
# Enter Choise: stock
# Stok Of Item(0037Fait-591/022) = (84 Items)
# *************************
# Stock Of Item Is Finshed
# Choise Your Items Accont
# 1-Stock Item(key - "stock")
# 2-Cost Item(key - "cost")
# 3-Sales Item(key - "sales")
# 4-Profit Item(key - "profit")
# 5-Exit(key - "exit")
# Enter Choise: cost
# Enter Number Of Purshaing Items: 12
# Cost Of Purshaing  Item(0037Fait-591/022) = Items(12) * Cost Price(145000) = (1740000 $)
# Current Stock Of Item Is(96 Items)
# *************************
# Cost Of Items Is Finshed
# Choise Your Items Accont
# 1-Stock Item(key - "stock")
# 2-Cost Item(key - "cost")
# 3-Sales Item(key - "sales")
# 4-Profit Item(key - "profit")
# 5-Exit(key - "exit")
# Enter Choise: sales
# Enter Number Of Sales Items: 23
# Total Sales Of Item(0037Fait-591/022) = Sales Item(23) * Sales Price(215000) = (4945000 $)
# Current Stock Of Item Is(73 Items)
# *************************
# Sales Of All Items Is Finshed
# Choise Your Items Accont
# 1-Stock Item(key - "stock")
# 2-Cost Item(key - "cost")
# 3-Sales Item(key - "sales")
# 4-Profit Item(key - "profit")
# 5-Exit(key - "exit")
# Enter Choise: profit
# Profit Of Item(0037Fait-591/022) = Total Sales(4945000) - Total Cost(1740000) = (3205000 $)
# *************************
# Profit Of Items Is Finshed
# Choise Your Items Accont
# 1-Stock Item(key - "stock")
# 2-Cost Item(key - "cost")
# 3-Sales Item(key - "sales")
# 4-Profit Item(key - "profit")
# 5-Exit(key - "exit")
# Enter Choise: exit
# *************************
# EXIT ITEM ACCOUNTING
# ##################################################
# ##################################################
# Choise Your Items Modify
# 1-ShowAll Items(key - "items")
# 2-Item Details(key - "item")
# 3-Accounting(key - "account")
# 8-Exit(key - "exit")
# Enter Choise: exit
# *************************
# EXIT PROGRAMM
# ##################################################
# ##################################################

# 1-SIGHN IN(key - "1")
# 2-SIGHN UP(key - "2")
# 3-USER UPDATE(key - "3")
# 4-EXIT(key - "4")
# Enter Choise: 4
# *************************
# EXIT PROGRAMM
# ##################################################
