import random
import time


class showBoard:
    def __init__(self, xstate, zstate):
        self.xstate = xstate
        self.zstate = zstate

    def board(self, xstate, zstate):
        zero = "X" if xstate[0] else ("O" if zstate[0] else 0)
        one = "X" if xstate[1] else ("O" if zstate[1] else 1)
        two = "X" if xstate[2] else ("O" if zstate[2] else 2)
        three = "X" if xstate[3] else ("O" if zstate[3] else 3)
        four = "X" if xstate[4] else ("O" if zstate[4] else 4)
        five = "X" if xstate[5] else ("O" if zstate[5] else 5)
        six = "X" if xstate[6] else ("O" if zstate[6] else 6)
        seven = "X" if xstate[7] else ("O" if zstate[7] else 7)
        eight = "X" if xstate[8] else ("O" if zstate[8] else 8)

        """
        print out he board in the form of 
        
        0 |1 |2
        --|--|--
        3 |4 |5
        --|--|--
        6 |7 |8
        
        """
        print(f"{zero} |{one} |{two}")
        print(f"--|--|--")
        print(f"{three} |{four} |{five}")
        print(f"--|--|--")
        print(f"{six} |{seven} |{eight}")
        return "Game is going on"

    """
------------------------------------------------------------------------------------------------------------------
    """

    """
        class HumanPlayer

        This class is used when the user choices to play multiplayer.
        
    """


class HumanPlayer(showBoard):
    def __init__(self, xstate, zstate, name1, name2):
        showBoard.__init__(self, xstate, zstate)
        self.name1 = name1
        self.name2 = name2

    def win(self, xstate, zstate, name1, name2):
        """game winning logic

        Returns:
                Which player won the match by adding the number of one's in the xstate and zstate 
                corresponding to the number of X and O in the board from 0 to 8
        """
        lst = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        """lst

        The above list gives us the number of ways of winning the game.
        
        """

        for i in lst:

            if (xstate[i[0]] + xstate[i[1]] + xstate[i[2]]) == 3:
                print("-"*50)
                print("FINAL SCORE")
                print(showBoard.board(self, xstate, zstate))
                print()
                print("-"*50)
                print("{} wons the game".format(name1))
                print("-"*50)
                return 1

            if (zstate[i[0]] + zstate[i[1]] + zstate[i[2]]) == 3:
                print("-"*50)
                print("FINAL SCORE")
                print(showBoard.board(self, xstate, zstate))
                print()
                print("-"*50)
                print("{} wons the game".format(name2))
                print("-"*50)
                return 0

    def human_player(self, xstate, zstate, name1, name2):
        """
        This function will sets the values to the board if two players are playing.
        """
        chance = 1
        while True:

            print(showBoard.board(self, xstate, zstate))

            if chance == 1:
                print("{} chance".format(name1))
                value = int(input(
                    "{} Please Enter the position from 0 to 8 in which you want to place X".format(name1)))
                if value >= 0 and value <= 8:
                    print("-"*50)
                    print("Valid Entry")
                    print("-"*50)
                    print()
                    time.sleep(1)
                    xstate[value] = 1
                else:
                    chance = 0
                    print("-"*50)
                    print(
                        "Invalid Entry!!!Please enter the position from 0 to 8 in which you want to place")
                    print("-"*50)
                    print()
            else:
                print("{} chance".format(name2))
                value = int(input(
                    "{} Please Enter the position from 0 to 8 in which you want to place O".format(name2)))
                if value >= 0 and value <= 8:
                    print("-"*50)
                    print("Valid Entry")
                    print("-"*50)
                    print()
                    time.sleep(1)
                    zstate[value] = 1
                else:
                    chance = 1
                    print("-"*50)
                    print(
                        "Invalid Entry!!!Please enter the position from 0 to 8 in which you want to place")
                    print("-"*50)
                    print()

            check = self.win(xstate, zstate, name1, name2)

            """
        The check will store the value of the win function defined above for the next operation
            """

            if check == 1 or check == 0:

                break

            """
            Condition for the draw 
            """

            if xstate.count(1) == 5 and zstate.count(1) == 4:
                print("-"*50)
                print("FINAL SCORE")
                print(showBoard.board(self, xstate, zstate))
                print("Game is Draw and no one wins the match")
                break

            chance = 1 - chance

        """
----------------------------------------------------------------------------------------------------------------
        """

        """
        class ComputerPlayer

        This class is used when the user choices to play multiplayer.
        
        """


class ComputerPlayer(HumanPlayer):

    def __init__(self, xstate, zstate, name1, name2):
        HumanPlayer.__init__(self, xstate, zstate, name1, name2)

    def computer_player(self, xstate, zstate, name1, name2):
        chance = 1
        lst = []
        while(True):
            print(showBoard.board(self, xstate, zstate))

            if chance == 1:

                """
                Player1 chance
                """
                print("{}'s chance".format(name1))
                value = int(input(
                    "{} Please Enter the position from 0 to 8 in which you want to place X".format(name1)))
                if value >= 0 and value <= 8:
                    print("-"*50)
                    print("Valid Entry")
                    print("-"*50)
                    print()
                    time.sleep(1)
                    xstate[value] = 1
                else:
                    chance = 0
                    print("-"*50)
                    print(
                        "Invalid Entry!!!Please enter the position from 0 to 8 in which you want to place")
                    print("-"*50)
                    print()

            else:
                """
                Computer chance
                """
                print("{}'s chance and places O".format("Computer's"))

                flag = 1
                while(flag == 1):

                    """
                random module is used to generate random number or random position for placing O
                    """

                    value = random.randint(0, 8)

                    if value not in lst:

                        """
                This condition will check whether the random number is present in the list or not 
                if its not present then append it to the list and also update the zstate list with value 1 to determine
                that this place for O is already done
                        """

                        lst.append(value)
                        zstate[value] = 1
                        if xstate[value] != zstate[value]:

                            """
                            This condition is used to check that the X and O will not have placed at same place in the board
                            so to avoid that we update the value of flag.
                            """
                            flag = 0

                        else:
                            flag = 1

                    else:
                        flag = 1
                    # print(lst,xstate,zstate)
            check = self.win(xstate, zstate, name1, name2)

            """
        The check will store the value of the win function defined above for the next operation
            """

            if check == 1 or check == 0:
                break

            """
            Condition for the draw 
            """

            if xstate.count(1) == 5 and zstate.count(1) == 4:
                print("-"*50)
                print("Game is Draw and no one wins the match")
                print("-"*50)
                print()
                break

            chance = 1-chance

        """
----------------------------------------------------------------------------------------------------------------
        """

        """
        START OF THE GAME BEGINS FROM HERE
        """
        """
Introduction:-
 
Tic-Tac-Toe is a very simple two-player game. So only two players can play at a time. This game is also known as Noughts and Crosses or Xs and Os game. One player plays with X and the other player plays with O. In this game we have a board consisting of a 3X3 grid.

Game Rules:- 

1.	Traditionally the first player plays with "X". So you can decide who wants to go with "X" and who wants to go with "O".

2.	Only one player can play at a time.

3.	If any of the players have filled a square then the other player and the same player cannot override that square.

4.	There are only two conditions that may match will be a draw or may win.

5.	The player that succeeds in placing three respective marks (X or O) in a horizontal, vertical, or diagonal row wins the game.

Winning condition:-
 
Whoever places three respective marks (X or O) horizontally, vertically, or diagonally will be the winner.

        """


"""
Here flag is used to check when the game is over and if the user wants to restart the game.
"""


flag = 1
while flag == 1:
    print("Welcome to the tic tac toe game X/O")
    print("-"*100)
    print("There will be a 3X3 grid containing the positions where the players have to place their respective Xs and Os")
    print("-"*100)

    "Whoever places three respective marks (X or O) horizontally, vertically, or diagonally will be the winner."

    "If user chooses multiplayer then player1 will have to place Xs in the respective places and player 2 have to place O;s"

    choice = input("Multiplayer or Singleplayer")

    print("You have selected ", choice)

    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if choice == "Multiplayer":

        name1 = input("Please enter your name player 1")
        name2 = input("Please enter your name player 2")

        print("Hey {} and  {} ".format(name1, name2))
        print("Game starts between {} and {}:".format(name1, name2))

        count = 5
        while count:

            print("GAME BEGINS IN: {}".format(count))
            print("-"*10)
            count -= 1
            time.sleep(1)

        print("GAME BEGINS NOW!")

        test = HumanPlayer(xstate, zstate, name1, name2)
        test.human_player(xstate, zstate, name1, name2)

    """
        If we choose a singleplayer then we have to play with computer
        and for that we have to use random module
    """

    if choice == "Singleplayer":
        name1 = input("Please enter your name player 1")

        print("Hey {} ".format(name1))
        print("Game starts between {} and {}:".format(name1, "Computer"))

        count = 5
        while count:
            print("GAME BEGINS IN: {}".format(count))
            print("-"*10)
            count -= 1
            time.sleep(1)

        print("GAME BEGINS NOW!")

        test = ComputerPlayer(xstate, zstate, name1, "Computer")
        test.computer_player(xstate, zstate, name1, "Computer")

    game = input("Do you wanna restart the game? [yes/no]:")

    """
    Condition to restart the game by using flag
    """

    if flag == 1 and game == "yes":
        flag = 1

    else:
        flag = 0
