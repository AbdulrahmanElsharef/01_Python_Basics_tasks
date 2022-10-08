# class of items for immplement in any system of company
# Parents  class of items . Inheritance
from random import randint as rnd
class Items():
      def __init__(self):
            ''' creat class of items (Add & Remove & Update & &cost Sales & Profit)  '''
            self.All_items = {}  # creat dictionry for all items
            while True:  # infinty loop
                  item_modify = input('''Choise Your Items Modify\n1-Add Item\t(key-"add")\n2-Update Item\t(key-"update")\n3-Del Item\t(key"del")\n4-Cost Item\t(key-"cost")\n5-Sales Item\t(key-"sales")\n6-profit Item\t(key-"profit")\n5-Exit\nEnter Choise  : ''')  # optins for user input

                  if item_modify.lower() == "add":
                        self.add_item()  # fun for adding item
                  elif item_modify.lower() == "update":
                        self.update_item()  # fun for update item
                  elif item_modify.lower() == "del":
                        self.delete_item()  # fun for del item
                  elif item_modify.lower() == "cost":
                        self.cost_item()  # fun for cost of item
                  elif item_modify.lower() == "sales":
                        self.sales_item()  # fun for sales of item
                  elif item_modify.lower() == "profit":
                        self.profit_item()  # fun for profit item
                  elif item_modify.lower() == "exit":  # fun for exit program
                        print(f"exit programm".upper())
                        break

      def add_item(self):
            '''functions for add items & update in all items'''
            add_items = {}
            item_name = input("Item Name :")
            # make serial for item
            item_seiral = f"{rnd(0,10)}{item_name.upper()}-{rnd(100,1000)}/022"
            item_cost = int((input("Item Cost :")))  # must be int
            item_sell = int((input("Item Sell Price :")))  # must be int
            item_inv = int((input("Item Inventory :")))  # must be int
            add_items[item_seiral] = {"item_name": item_name.upper(), "item_cost": item_cost, "item_sell": item_sell, "inventory": item_inv}
            print(f"Item You Have Add Is : {item_seiral}")
            self.All_items.update(add_items)
            print(list(self.All_items.keys()))

      def update_item(self):
            '''functions for update item in all items'''
            print(list(self.All_items.keys()))
            item_seiral = input("Item_Seiral number :")
            if item_seiral in self.All_items.keys():
                  del self.All_items[item_seiral]  # delet old item
                  n_item_name = input("Item Name :")  # add new item
                  # make serial for item
                  n_item_seiral = f"{rnd(0,10)}{n_item_name.upper()}-{rnd(100,1000)}/022"
                  n_item_cost = int((input("Item Cost :")))
                  n_item_sell = int((input("Item Sell Price :")))
                  n_item_inv = int((input("Item Inventory :")))
                  self.All_items[n_item_seiral] = {"item_name": n_item_name.upper(), "item_cost": n_item_cost, "item_sell": n_item_sell, "inventory": n_item_inv}
                  print(f"Item after Uppdate Is : {n_item_seiral}")
                  print(list(self.All_items.keys()))
            else:
                  print('"item_seiral invalid"\n"please try enter valid serial try again"'.title())

      def delete_item(self):
            '''functions for deleting items from  all items'''
            print(list(self.All_items.keys()))
            item_seiral = input("Item_Seiral number :")
            if item_seiral in self.All_items.keys():
                  del self.All_items[item_seiral]
                  print(list(self.All_items.keys()))
            else:
                  print('"item_seiral invalid"\n"please try enter valid serial try again"'.title())

      def cost_item(self):
            '''functions for cost item'''
            print(list(self.All_items.keys()))
            item_seiral = input("Item_Seiral number :")
            if item_seiral in self.All_items.keys():
                  # get item numbers $ cost
                  num_stock = self.All_items.get(item_seiral, {}).get("inventory")
                  price_cost = self.All_items.get(item_seiral, {}).get("item_cost")
                  total_cost = num_stock*price_cost
                  print(f"total cost of item ({item_seiral}) = {total_cost} $".title())

      def sales_item(self):
            '''functions for sales item'''
            print(list(self.All_items.keys()))
            item_seiral = input("Item_Seiral number :")
            if item_seiral in self.All_items.keys():
                  num_stock = self.All_items.get(item_seiral, {}).get("inventory")
                  price_sales = self.All_items.get(item_seiral, {}).get("item_sell")
                  total_sales = num_stock*price_sales
                  print(f"total cost of item ({item_seiral}) = {total_sales} $".title())

      def profit_item(self):
            '''functions for profit of item'''
            print(list(self.All_items.keys()))
            item_seiral = input("Item_Seiral number :")
            if item_seiral in self.All_items.keys():
                  num_stock = self.All_items.get(item_seiral, {}).get("inventory")
                  cost = self.All_items.get(item_seiral, {}).get("item_cost")
                  # cost = self.All_items[item_seiral]["item_cost"]
                  sell = self.All_items.get(item_seiral, {}).get("item_sell")
                  # sell = self.All_items[item_seiral]["item_sell"]
                  profit = (sell*num_stock)-(cost*num_stock)
                  print(f"total Profit OF Item ({item_seiral}) =  {profit} $ ".title())




