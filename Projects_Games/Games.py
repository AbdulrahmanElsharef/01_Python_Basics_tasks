class Game():
    def __init__(self) :
        '''creat games class of 5 games'''
        name = input("enter your name please : ")
        while True:      # infinty loop for games
            print(f'''hello {name} please choise your game :
            -1 odd_even_list game
            -2 No_double_string game
            -3 print_range_number game
            -4 divsion_number game
            -5 divsion_tow num game
            -6 list commands
            ''') # welcome masseage
            game_number=int(input("enter game number:")) # user choise game number
            if game_number == 1:
                n = input("enter numbers :") # must input number like : 1,2,3,4,5,6,7,8,9
                self.odd_even(n) # retrun odd num in list & even number in list
            elif game_number == 2:
                str = input("enter sentence :") 
                self.double_str(str) # fun return sentense without dublicate
            elif game_number == 3:
                num = int(input("enter your number :"))
                self.print_num(num)  # print numbers in range uor number
            elif game_number == 4:
                num_1 = int(input("enter range num :"))
                num_d = int(input("enter divsion number :"))
                self.divsion_num(num_1, num_d) # print all number in range is divsion by another number
            elif game_number == 5:
                num_1 = int(input("enter divsion number 1 :"))
                num_2 = int(input("enter divsion number 2 :"))
                num_3 = int(input("enter range numbers :"))
                self.divsion_2num(num_1, num_2, num_3) #print all number in range is divsion by tow number
            elif game_number == 6:
                num_1 = int(input("number of commands :"))
                self.lis_commands(num_1)
            else:
                print("wrong game number try again ;")
            ask_play=input("do you like play again ('y' or 'N') : ".lower())
            if ask_play== 'n':
                print("Good Bye")
                break
    # GAMES
    # game (1)
    def odd_even(self,numbers):
        lis = numbers.split(",")
        odd_lis = []
        even_lis = []
        for x in lis:
            if int(x) % 2 == 0:
                    even_lis.append(int(x))
            else:
                    odd_lis.append(int(x))
        print(f"even numbers is {even_lis}")
        print(f"odd numbers is {odd_lis}")
    # game(2)
    def double_str(self,sentence):
        lis = sentence.split(" ")
        new_str = []
        for x in lis:
            if x in new_str:
                pass
            else:
                new_str.append(x)
        str_1 = " ".join(new_str)
        print(f"Dry Sentense is ( {str_1} )")
    # game (3)
    def print_num(self,num):
        for x in range(num+1):
            print(x)
    # game (4)
    def divsion_num(self,n,d):
        for x in range (n+1):
            if x % d ==0 :
                print (f"{d} is dision by {x}")

    # game (5)
    def divsion_2num(self,n1,n2,nrange):
        for x in range(nrange+1):
                if x % n1 == 0 and x % n2 == 0:
                    print (f"{n1,n2} is dision by {x}")
                
    # game (6)
    def lis_commands(self,n):
        commands = input("Enter list Command : ")
        hol_lis = []
        for x in range(n):
                lis = list(commands.split())
                if lis[0] == "insert":
                    hol_lis.insert(int(lis[1]), (lis[2]))
                    # print(hol_lis)
                elif lis[0] == "append":
                    hol_lis.append((lis[1]))
                    # print(hol_lis)
                elif lis[0] == "remove":
                    hol_lis.remove((lis[1]))
                    # print(hol_lis)
                elif lis[0] == "pop":
                    hol_lis.pop()
                    # print(hol_lis)
                elif lis[0] == "sort":
                    hol_lis.sort()
                    # print(hol_lis)
                elif lis[0] == "reverse":
                    hol_lis.reverse()
                    # print(hol_lis)
                else:
                    print("Wrong Command")
        else:
            print(hol_lis)
