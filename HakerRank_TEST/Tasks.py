def lis_commands():
# input_range = int(input())
       hol_lis = []
       while True:
              commands=input("Enter list Command : ")
              lis = list (commands.split())
              if lis[0]== "insert":
                     hol_lis.insert(int(lis[1]), (lis[2]))
                     print(hol_lis)
              elif lis[0] == "append":
                     hol_lis.append((lis[1]))
                     print(hol_lis)
              elif lis[0] == "remove":
                     hol_lis.remove((lis[1]))
                     print(hol_lis)
              elif lis[0] == "pop":
                     hol_lis.pop()
                     print(hol_lis)
              elif lis[0] == "sort":
                     hol_lis.sort()
                     print(hol_lis)
              elif lis[0] == "reverse":
                     hol_lis.reverse()
                     print(hol_lis)
              elif lis[0] == "out":
                     print("good Bye")
                     break
              else:
                     print("Wrong Command")
lis_commands()
