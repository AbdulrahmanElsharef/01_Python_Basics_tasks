from pip import main


if __name__ == "__main__":
    main()


def main():
    global X_O_GAME
    X_O_GAME = {9: "9(_)", 8: "8(_)", 7: "7(_)", 6: "6(_)",
                5: "5(_)", 4: "4(_)", 3: "3(_)", 2: "2(_)", 1: "1(_)"}
    game()


def game():
    while True:
        print(f"\n{X_O_GAME[9]}\t{X_O_GAME[8]}\t{X_O_GAME[7]} \n{X_O_GAME[6]}\t{X_O_GAME[5]}\t{X_O_GAME[4]} \n{X_O_GAME[3]}\t{X_O_GAME[2]}\t{X_O_GAME[1]}\n".upper())
        X_O_CHOISE = input("please enter X OR O : ")
        X_O_PLACE = int(input("please enter place num : "))
        if X_O_CHOISE != X_O_GAME[X_O_PLACE]:
            X_O_GAME[X_O_PLACE] = X_O_CHOISE.upper()
            # print(f"\n{X_O_GAMEX_O_GAME[1]}\t{X_O_GAME[2]}\t{X_O_GAME[3]} \n{X_O_GAME[4]}\t{X_O_GAME[5]}\t{X_O_GAME[6]} \n{X_O_GAME[7]}\t{X_O_GAME[8]}\t{X_O_GAME[9]}\n".upper())
        elif X_O_CHOISE == X_O_GAME[X_O_PLACE]:
            print("enter right plase try again")

#     while True:      # infinty loop for games
#         print(f'''hello {name} please choise your game :
#         -1 odd_even_list game
#         -2 No_double_string game
#         -3 print_range_number game
#         -4 divsion_number game
#         -5 divsion_tow num game
#         -6 list commands
#         '''.title())  # welcome masseage
#         try:
#             # user choise game number
#             game_number = int(input("enter game number:"))
#             if game_number == 1:
#                 # help(odd_even)
#                 odd_even()
#             elif game_number == 2:
#                 help(double_str)
#                 double_str()  # fun return sentense without dublicate
#             elif game_number == 3:
#                 print_num()
#             elif game_number == 4:
#                 divsion_num()
#             elif game_number == 5:
#                 divsion_2num()
#             elif game_number == 6:
#                 lis_commands()
#             else:
#                 print("wrong game number try again ;")
#             ask_play = input("do you like play again ('y' or 'N') : ".lower())
#             if ask_play == 'y':
#                 continue
#             if ask_play == 'n':
#                 print("Good Bye")
#                 break
#             else:
#                 print("please only enter 'y'  or  'n'".title())
#                 ask_play = input(
#                     "do you like play again ('y' or 'N') : ".lower())
#         except:
#             print("enter game nmuber first please try again ".title())

#     # game(1)


# def odd_even():
#     ''' function for odd & even numbers
#     args:list of numbers like this[1,2,3,4,5,6,7,8,9,10]
#     return :
#     list of odd numbers
#     list of even numbers
#     '''
#     numbers = input("enter numbers :")
#     lis = numbers.split(",")
#     odd_lis = []
#     even_lis = []
#     for x in lis:
#         if int(x) % 2 == 0:
#             even_lis.append(int(x))
#         else:
#             odd_lis.append(int(x))
#     print(f"even numbers is {even_lis}")
#     print(f"odd numbers is {odd_lis}")
#     # game(2)


# def double_str():
#     ''' function for double words in strings
#     args: input your string
#     return : print your string without double words
#     '''
#     sentence = input("enter sentence :")  # string with double words
#     lis = sentence.split(" ")
#     new_str = []
#     for x in lis:
#         if x in new_str:
#             pass
#         else:
#             new_str.append(x)
#     str_1 = " ".join(new_str)
#     print(f"Dry Sentense is ( {str_1} )")
#     # game (3)


# def print_num():
#     '''function return sum of all numbers
#     args: input numbers
#     return: sum of all numbers
#     '''
#     num = int(input("enter your number :"))
#     for x in list(range(num+1)):
#         print(x)
#     # game (4)


# def divsion_num():
#     num_1 = int(input("enter range num :"))
#     num_d = int(input("enter divsion number :"))
#     for x in range(num_1+1):
#         if x % num_d == 0:
#             print(f"{num_d} is dision by {x}")
#     # game (5)


# def divsion_2num():
#     num_1 = int(input("enter divsion number 1 :"))
#     num_2 = int(input("enter divsion number 2 :"))
#     nrange = int(input("enter range numbers :"))
#     for x in range(nrange+1):
#         if x % num_1 == 0 and x % num_2 == 0:
#             print(f"{num_1,num_2} is dision by {x}")
#     # game (6)


# def lis_commands():
#     '''function for modifing list
#     args: list & list commands
#     return:list after modify
#     '''
#     num = int(input("number of commands :"))
#     new_lis = []
#     for _ in range(num):
#         commands = input("Enter list Command : ")
#         lis = list(commands.split())
#         if lis[0] == "insert":
#             new_lis.insert(int(lis[1]), (lis[2]))
#             print(new_lis)
#         elif lis[0] == "append":
#             new_lis.append(lis[1])
#             print(new_lis)
#         elif lis[0] == "remove":
#             new_lis.remove(lis[1])
#             print(new_lis)
#         elif lis[0] == "pop":
#             new_lis.pop()
#             print(new_lis)
#         elif lis[0] == "sort":
#             new_lis.sort()
#             print(new_lis)
#         elif lis[0] == "reverse":
#             new_lis.reverse()
#             print(new_lis)
#         else:
#             print("Wrong Command")
#     else:
#         print("finish game")
