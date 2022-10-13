# import class of items from company_items file
import sys
import os
from ITEMS_Class import Items

class Iphone_Items(Items):
      pass


iphone_1 = Iphone_Items()


'''*** WELCOM TO ITEMS PROGRAMM ** *
Choise Your Items Modify
1-Add Item(key - "add")
2-Update Item(key - "update")
3-Del Item(key - "del")
4-ShowAll Items(key - "items")
5-Item Details(key - "item")
7-Item Accounting(key - "account")
8-Exit(key - "exit")
Enter Choise: add
Item Name: iphone_x
Item Cost: 1500
Item Sell Price: 2650
Item Stosk: 45
Item You Have Add Is: (0063Iphone_X-337/022)
*************************
Add_New Items Is Finshed
##################################################
Enter Choise: add
Item Name: iphone-14
Item Cost: 7800
Item Sell Price: 10500
Item Stosk: 86
Item You Have Add Is: (0067Iphone-14-155/022)
*************************
Add_New Items Is Finshed
##################################################

Enter Choise: items
All Items Is['0063Iphone_X-337/022', '0067Iphone-14-155/022']
Show Of All Items Is Finshed
*************************
##################################################

Enter Choise: update
['0063IPHONE_X-337/022', '0067IPHONE-14-155/022']
Item_Seiral number: 0063IPHONE_X-337/022
Item Name: iphone-13
Item Cost: 5400
Item Sell Price: 7500
Item Stosk: 49
New Item Is: 0094Iphone-13-219/022
*************************
##################################################
Choise Your Items Modify
Enter Choise: item
['0067IPHONE-14-155/022', '0094IPHONE-13-219/022']
Item_Seiral number: 0094IPHONE-13-219/022
Item: 0094Iphone-13-219/022 Details Is[('Item_Name', 'Iphone-13'), ('Item_Cost', 5400), ('Item_Sell', 7500), ('Item_Stock', 49)]
*************************
##################################################
Choise Your Items Modify
Enter Choise: account
['0067IPHONE-14-155/022', '0094IPHONE-13-219/022']
Item_Seiral number: 0094IPHONE-13-219/022
Choise Your Items Accont
1-Stock Item(key - "stock")
2-Cost Item(key - "cost")
3-Sales Item(key - "sales")
4-Profit Item(key - "profit")
5-Exit(key - "exit")
Enter Choise: stock
Stok Of Item(0094Iphone-13-219/022) = (49 Items)
*************************

Enter Choise: cost
Enter Number Of Purshaing Items: 11
Cost Of Purshaing  Item(0094Iphone-13-219/022) = Items(11) * Cost Price(5400) = (59400 $)
Current Stock Of Item Is(60 Items)
*************************

Enter Choise: sales
Enter Number Of Sales Items: 20
Total Sales Of Item(0094Iphone-13-219/022) = Sales Item(20) * Sales Price(7500) = (150000 $)
Current Stock Of Item Is(40 Items)
*************************

Enter Choise: profit
Profit Of Item(0094Iphone-13-219/022) = Total Sales(150000) - Total Cost(59400) = (90600 $)
*************************

Enter Choise: stock
Stok Of Item(0094Iphone-13-219/022) = (40 Items)
*************************
Stock Of Item Is Finshed
)
5-Exit(key - "exit")
Enter Choise: exit
*************************
EXIT ITEM ACCOUNTING
##################################################
##################################################
Enter Choise: exit
*************************
EXIT PROGRAMM''''''
