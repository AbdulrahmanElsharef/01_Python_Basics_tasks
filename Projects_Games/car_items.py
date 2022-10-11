
# import Car_Items class from module folder from company_items file
# immplement object car_1 from car items class
from .company_items import Car_Items
car_1 = Car_Items()

# *** WELCOM TO ITEMS PROGRAMM ** *
# Choise Your Items Modify
# 1-Add Item(key - "add")
# 2-Update Item(key - "update")
# 3-Del Item(key - "del")
# 4-ShowAll Items(key - "items")
# 5-Item Details(key - "item")
# 7-Item Accounting(key - "account")
# 8-Exit(key - "exit")
#_____________________ADD ITEM_____________________________________________________________________
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
#_____________________UPDATE ITEM_____________________________________________________________________
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
#_____________________DELET ITEM_____________________________________________________________________
# Enter Choise: del
# ['0087BMW-476/022', '0050VOLVO-921/022']
# Item_Seiral number: 0087BMW-476/022
# Item: 0087Bmw-476/022 Is Delete
# *************************
# ##################################################
#_____________________ADD ITEM_____________________________________________________________________
# Enter Choise: add
# Item Name: seat
# Item Cost: 345000
# Item Sell Price: 495000
# Item Stosk: 36
# Item You Have Add Is: (0043Seat-656/022)
# *************************
# Add_New Items Is Finshed
# ##################################################
#_____________________SHOW ALL SERIAL ITEMS_____________________________________________________________________
# Enter Choise: items
# All Items Is['0050Volvo-921/022', '0043Seat-656/022']
# Show Of All Items Is Finshed
# *************************
# ##################################################
#_____________________SHOW ITEM DETAILS ITEM_____________________________________________________________________
# Enter Choise: item
# ['0050VOLVO-921/022', '0043SEAT-656/022']
# Item_Seiral number: 0050VOLVO-921/022
# Item: 0050Volvo-921/022 Details Is[('Item_Name', 'Volvo'), ('Item_Cost', 4650000), ('Item_Sell', 720000), ('Item_Stock', 45)]
# *************************
# ##################################################
# ##################################################
#_____________________ ITEM ACCOUNTING_____________________________________________________________________
# Enter Choise: account
# ['0087BMW-345/022']
# Item_Seiral number: 0087BMW-345/022
# Choise Your Items Accont
# 1-Stock Item(key - "stock")
# 2-Cost Item(key - "cost")
# 3-Sales Item(key - "sales")
# 4-Profit Item(key - "profit")
# 5-Exit(key - "exit")
#_____________________STOCK ITEM_____________________________________________________________________
# Enter Choise: stock
# Stok Of Item(0087Bmw-345/022) = (25 Items)
# *************************
#_____________________COST OF PURSHAES ITEM_____________________________________________________________________
# Enter Choise: cost
# Enter Number Of Purshaing Items: 10
# Cost Of Purshaing  Item(0087Bmw-345/022) = Items(10) * Cost Price(200000) = (2000000 $)
# Current Stock Of Item Is(35 Items)
# *************************
#_____________________SALES ITEM_____________________________________________________________________
# Enter Choise: sales
# Enter Number Of Sales Items: 15
# Total Sales Of Item(0087Bmw-345/022) = Sales Item(15) * Sales Price(350000) = (5250000 $)
# Current Stock Of Item Is(20 Items)
# *************************
#_____________________PROFIT ITEM_____________________________________________________________________
# Enter Choise: profit
# Profit Of Item(0087Bmw-345/022) = Total Sales(5250000) - Total Cost(2000000) = (3250000 $)
# *************************
#_____________________EXIT ACCONTING_____________________________________________________________________
# Enter Choise: exit
# *************************
# EXIT ITEM ACCOUNTING
# ##################################################
#_____________________EXIT PROGRAMM_____________________________________________________________________
# Enter Choise: exit
# *************************
# EXIT PROGRAMM
# ##################################################

