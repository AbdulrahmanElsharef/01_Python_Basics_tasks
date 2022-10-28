class Game():
    def __init__(self):
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
            ''')  # welcome masseage
            game_number = int(input("enter game number:"))  # user choise game number
            if game_number == 1:
                # must input number like : 1,2,3,4,5,6,7,8,9
                n = input("enter numbers :")
                # retrun odd num in list & even number in list
                self.odd_even(n)
            elif game_number == 2:
                str = input("enter sentence :")
                self.double_str(str)  # fun return sentense without dublicate
            elif game_number == 3:
                num = int(input("enter your number :"))
                self.print_num(num)  # print numbers in range uor number
            elif game_number == 4:
                num_1 = int(input("enter range num :"))
                num_d = int(input("enter divsion number :"))
                # print all number in range is divsion by another number
                self.divsion_num(num_1, num_d)
            elif game_number == 5:
                num_1 = int(input("enter divsion number 1 :"))
                num_2 = int(input("enter divsion number 2 :"))
                num_3 = int(input("enter range numbers :"))
                # print all number in range is divsion by tow number
                self.divsion_2num(num_1, num_2, num_3)
            elif game_number == 6:
                num_1 = int(input("number of commands :"))
                self.lis_commands(num_1)
            else:
                print("wrong game number try again ;")
            ask_play = input("do you like play again ('y' or 'N') : ".lower())
            if ask_play == 'n':
                print("Good Bye")
                break
    # GAMES
    # game (1)

    def odd_even(self, numbers):
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

    def double_str(self, sentence):
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

    def print_num(self, num):
        for x in range(num+1):
            print(x)
    # game (4)

    def divsion_num(self, n, d):
        for x in range(n+1):
            if x % d == 0:
                print(f"{d} is dision by {x}")

    # game (5)
    def divsion_2num(self, n1, n2, nrange):
        for x in range(nrange+1):
            if x % n1 == 0 and x % n2 == 0:
                print(f"{n1,n2} is dision by {x}")

    # game (6)
    def lis_commands(self, n):
        new_lis = []
        for _ in range(n):
            commands = input("Enter list Command : ")
            lis = list(commands.split())
            if lis[0] == "insert":
                new_lis.insert(int(lis[1]), (lis[2]))
                print(new_lis)
            elif lis[0] == "append":
                new_lis.append(lis[1])
                print(new_lis)
            elif lis[0] == "remove":
                new_lis.remove(lis[1])
                print(new_lis)
            elif lis[0] == "pop":
                new_lis.pop()
                print(new_lis)
            elif lis[0] == "sort":
                new_lis.sort()
                print(new_lis)
            elif lis[0] == "reverse":
                new_lis.reverse()
                print(new_lis)
            else:
                print("Wrong Command")
        else:
            print("finish game")

        # hellllllllllllllllllllo
