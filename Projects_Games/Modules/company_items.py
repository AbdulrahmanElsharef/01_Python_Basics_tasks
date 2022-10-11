# class of items for immplement in any system of company
from random import randint as rnd
class Items(): # parents class
      def __init__(self):
            ''' creat class of items (Add & Remove & Update & &cost Sales & Profit)  '''
            print("*** welcom to items programm ***".upper()) # welcome message
            # creat dictionry for all items
            self.All_items = {}
            # _____________________________________________________________
            while True:  # infinty loop
                  item_modify = input('''Choise Your Items Modify\n1-Add Item\t\t(key - "add")\n2-Update Item\t\t(key - "update")\n3-Del Item\t\t(key - "del")\n4-ShowAll Items\t\t(key - "items")\n5-Item Details\t\t(key - "item")\n7-Item Accounting\t(key - "account")\n8-Exit\t\t\t(key - "exit")\nEnter Choise  : ''')  # optins for user input
                  # ________________________________________________________________
                  if item_modify.lower() == "add":
                        self.add_item()  # fun for adding items
                        print("#####"*10)
                  elif item_modify.lower() == "update":
                        self.update_item()  # fun for update items
                        print("#####"*10)
                  elif item_modify.lower() == "del":
                        self.delete_item()  # fun for del items
                        print("#####"*10)
                  elif item_modify.lower() == "items": # def for show all serail items
                        self.show_All_items()
                        print("#####"*10)
                  elif item_modify.lower() == "item":  # def for show items details
                        self.show_item_details()
                        print("#####"*10)
                  elif item_modify.lower() == "account":
                        self.item_accounting()  # fun for accounting item
                        print("#####"*10)
                  elif item_modify.lower() == "exit":  # fun for exit program
                        print("*****"*5)
                        print(f"exit programm".upper())
                        print("#####"*10)
                        break
                  else:
                        print("*****"*5)  # wrong enter modify
                        print("**wrong item modify**".title())
                        print("#####"*10)
      # ___________________________________________________________
      def add_item(self):
            '''functions for add items in all items'''
            add_items = {}
            item_name = input("Item Name :")
            # make serial for item
            item_seiral = f"00{rnd(10,100)}{item_name.upper()}-{rnd(100,1000)}/022"
            item_cost = int((input("Item Cost :")))  # must be int
            item_sell = int((input("Item Sell Price :")))  # must be int
            item_stock = int((input("Item Stosk :")))  # must be int
            add_items[item_seiral] = {"item_name": item_name.upper(), "item_cost": item_cost, "item_sell": item_sell, "item_stock": item_stock}
            print(f"Item You Have Add Is : ({item_seiral})".title())
            print("*****"*5)
            self.All_items.update(add_items)
            print("add_new items is finshed".title())
      # ___________________________________________________________
      def update_item(self):
            '''functions for update item in all items'''
            print(list(self.All_items.keys()))
            item_seiral = input("Item_Seiral number :")
            if item_seiral in self.All_items.keys():
                  del self.All_items[item_seiral]  # delet old item
                  n_item_name = input("Item Name :")  # add new item
                  # make serial for item
                  n_item_seiral = f"00{rnd(10,100)}{n_item_name.upper()}-{rnd(100,1000)}/022"
                  n_item_cost = int((input("Item Cost :")))
                  n_item_sell = int((input("Item Sell Price :")))
                  n_item_inv = int((input("Item Stosk :")))
                  self.All_items[n_item_seiral] = {"item_name": n_item_name.upper(), "item_cost": n_item_cost, "item_sell": n_item_sell, "item_stock": n_item_inv}
                  print(f"new item Is : {n_item_seiral}".title())
                  print("*****"*5)
            elif item_seiral not in self.All_items.keys():
                        print('"item_seiral invalid"\n"please try enter valid serial try again"'.title())
                        print("*****"*5)
            else:
                  print("update items is finshed".title())
      #_________________________________________________________________
      def delete_item(self):
            '''functions for deleting items from  all items'''
            print(list(self.All_items.keys()))
            item_seiral = input("Item_Seiral number :")
            if item_seiral in self.All_items.keys():
                  del self.All_items[item_seiral]
                  print(f"Item : {item_seiral} is delete".title())
                  print("*****"*5)
            elif item_seiral not in self.All_items.keys():
                  print('"item_seiral invalid"\n"please try enter valid serial try again"'.title())
                  print("*****"*5)
            else:
                  print("delete items is finshed".title())
      # ___________________________________________________________
      def show_All_items(self):
            '''functions for deleting items from  all items'''
            show_items = list(self.All_items.keys())
            print(f"all items is {show_items}".title())
            print("show of all items is finshed".title())
            print("*****"*5)
      # ________________________________________________________________
      def show_item_details(self):
            '''functions for deleting items from  all items'''
            print(list(self.All_items.keys()))
            item_seiral = input("Item_Seiral number :")
            if item_seiral in self.All_items.keys():
                  show_item = list(self.All_items.get(item_seiral, {}).items())
                  print(f"Item : {item_seiral} details is {show_item}".title())
                  print("*****"*5)
            elif item_seiral not in self.All_items.keys():
                  print('"item_seiral invalid"\n"please try enter valid serial try again"'.title())
                  print("*****"*5)
            else:
                  print("details of items is finshed".title())
      # _______________________________________________________________________
      def item_accounting(self):
            '''functions for item accounting  '''
            print(list(self.All_items.keys()))
            item_seiral = input("Item_Seiral number :")
            global stock_item #stock of item change in sales or purshase
            stock_item = self.All_items.get(item_seiral, {}).get("item_stock")
            while True:
                  item_account = input('''Choise Your Items Accont\n1-Stock Item\t\t(key - "stock")\n2-Cost Item\t\t(key - "cost")\n3-Sales Item\t\t(key - "sales")\n4-Profit Item\t\t(key - "profit")\n5-Exit\t\t\t(key - "exit")\nEnter Choise  : ''')  # optins for user input
                  if item_seiral in self.All_items.keys():
                        if item_account.lower() == "stock":
                              # get cuurent stock of item
                              cur_stock=stock_item
                              print(f"stok of item ({item_seiral}) = ({cur_stock} items)".title())
                              print("*****"*5)
                              print("stock of item is finshed".title())
                              pass
                        elif item_account.lower() == "cost":
                              # get total cost of purshaing item and plus to stock of item
                              item_cost_price = self.All_items.get(item_seiral, {}).get("item_cost")
                              item_buy = int(input("Enter Number Of Purshaing Items : "))
                              stock_item += item_buy
                              item_cost = item_buy*item_cost_price
                              print(f"cost of Purshaing  item ({item_seiral}) = items ({item_buy}) * cost price ({item_cost_price}) = ({item_cost} $)".title())
                              print(f"current stock of item is ({stock_item} items)".title())
                              print("*****"*5)
                              print("cost of items is finshed".title())
                        elif item_account.lower() == "sales":
                              # get total sales of selling item and decress it from stock of item
                              item_sell_price = self.All_items.get(item_seiral, {}).get("item_sell")
                              sales_item = int(input("Enter Number Of Sales Items : "))
                              stock_item -= sales_item
                              item_sales = sales_item*item_sell_price
                              print(f"total sales of item ({item_seiral}) = sales item ({sales_item}) * sales price ({item_sell_price}) = ({item_sales} $)".title())
                              print(f"current stock of item is ({stock_item} items)".title())
                              print("*****"*5)
                              print("sales of all items is finshed".title())
                        elif item_account.lower() == "profit":
                              # get total profit of item 
                              total_profit = item_sales-item_cost
                              print(f"profit of item ({item_seiral}) = total sales ({item_sales}) - total cost ({item_cost}) = ({total_profit} $)".title())
                              print("*****"*5)
                              print("profit of items is finshed".title())
                        elif item_account.lower() == "exit":  # fun for exit program
                              print("*****"*5)
                              print(f"exit item accounting".upper())
                              print("#####"*10)
                              break
                        else:
                              print("wrong accont item".title())
                  else :
                        print('"item_seiral invalid"\n"please try enter valid serial try again"'.title())
                        print("*****"*5)



class Car_Items(Items): #inhhrant class from items class
      pass
