
# import Car_Items from module company_items
# immplement object car_1 from car items class
from company_items import Car_Items


car_1 = Car_Items()
# #Choise Your Items Modify
# 1-Add Item(key-"add")
# 2-Update Item(key-"update")
# 3-Del Item(key"del")
# 4-Cost Item(key-"cost")
# 5-Sales Item(key-"sales")
# 6-profit Item(key-"profit")
# 5-Exit
# _____________add item_______________________________________________________________
# Enter Choise: add
# Item Name: bmw
# Item Cost: 155000
# Item Sell Price: 223000
# Item Inventory: 35
# Item You Have Add Is: 10BMW-799/022
# ['10BMW-799/022']
# # _____________add item_______________________________________________________________
# Enter Choise: add
# Item Name: fait
# Item Cost: 96000
# Item Sell Price: 145000
# Item Inventory: 45
# Item You Have Add Is: 9FAIT-151/022
# ['10BMW-799/022', '9FAIT-151/022']
# _____________add item_______________________________________________________________
# Enter Choise: add
# Item Name: volx
# Item Cost: 174000
# Item Sell Price: 260000
# Item Inventory: 27
# Item You Have Add Is: 8VOLX-826/022
# ['10BMW-799/022', '9FAIT-151/022', '8VOLX-826/022']
# # _____________add item_______________________________________________________________
# Enter Choise: add
# Item Name: skoda
# Item Cost: 185000
# Item Sell Price: 244000
# Item Inventory: 36
# Item You Have Add Is: 0SKODA-304/022
# ['10BMW-799/022', '9FAIT-151/022', '8VOLX-826/022', '0SKODA-304/022']
# # _____________update item_______________________________________________________________
# Enter Choise: update
# ['10BMW-799/022', '9FAIT-151/022', '8VOLX-826/022', '0SKODA-304/022']
# Item_Seiral number: 9FAIT-151/022
# Item Name: seat
# Item Cost: 205000
# Item Sell Price: 285000
# Item Inventory: 34
# Item after Uppdate Is: 5SEAT-319/022
# ['10BMW-799/022', '8VOLX-826/022', '0SKODA-304/022', '5SEAT-319/022']
# # _____________del item_______________________________________________________________
# Enter Choise: del
# ['10BMW-799/022', '8VOLX-826/022', '0SKODA-304/022', '5SEAT-319/022']
# Item_Seiral number: 5SEAT-319/022
# ['10BMW-799/022', '8VOLX-826/022', '0SKODA-304/022']
# # _____________cost of item_______________________________________________________________
# Enter Choise: cost
# ['10BMW-799/022', '8VOLX-826/022', '0SKODA-304/022']
# Item_Seiral number: 8VOLX-826/022
# Total Cost Of Item(8Volx-826/022) = 4698000 $
# # _____________sales item_______________________________________________________________
# Enter Choise: sales
# ['10BMW-799/022', '8VOLX-826/022', '0SKODA-304/022']
# Item_Seiral number: 0SKODA-304/022
# Total Cost Of Item(0Skoda-304/022) = 8784000 $
# # _____________profit item_______________________________________________________________
# Enter Choise: profit
# ['10BMW-799/022', '8VOLX-826/022', '0SKODA-304/022']
# Item_Seiral number: 10BMW-799/022
# Total Profit Of Item 10Bmw-799/022 Is = 2380000 $
# # _____________del by wrong serial item_______________________________________________________________
# Enter Choise: del
# ['10BMW-799/022', '8VOLX-826/022', '0SKODA-304/022']
# Item_Seiral number: adf
# "Item_Seiral Invalid"
# "Please Try Enter Valid Serial Try Again"
# # _______________sales by wrong serial itemm_______________________________________________________________
# Enter Choise: sales
# ['10BMW-799/022', '8VOLX-826/022', '0SKODA-304/022']
# Item_Seiral number: 10BMW-799/023
# ___________________exit_______________________________________________________
# Enter Choise: exit
# EXIT PROGRAMM
