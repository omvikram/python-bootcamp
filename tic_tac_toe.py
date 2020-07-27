## TIC TAC TOE PROGRAM
stop_game = False
positions = range(1,10)
row1 = range(1,4)
row2 = range(4,7)
row3 = range(7,10)
board1 = ["","",""]
board2 = ["","",""]
board3 = ["","",""]

def display_board(position = 0, choice = 0):
    if(position > 0):
        print(row1)
        print(row2)
        print(row3)
    if(position in positions):
        if(position in row1):
            #print("inside row1")            
            index1 = row1.index(position)
            board1[index1] = choice
        elif(position in row2):
            #print("inside row2")
            index2 = row2.index(position)
            board2[index2] = choice
        elif(position in row3):
            #print("inside row3")
            index3 = row3.index(position)
            board3[index3] = choice
                            
        print(board1)
        print(board2)
        print(board3)
    else:
        print(board3)
        print(board2)
        print(board1)

def ask_choice():
    is_valid_choice = False
    choices = [0,1]
    choice1 = choice2 = 0
    while(is_valid_choice == False):
        try:
            choice1 = int(input("Please choose your sign -> 0 or 1 : "))
            if(choice1 == 0):
                choice2 = 1
            
            if((choice1 in choices) and (choice2 in choices)):
                is_valid_choice = True
                break
        except:
            pass
    return choice1, choice2


def ask_position():
    is_valid_position = False
    position = 0
    while(is_valid_position == False):
        try:
            position = int(input("Please choose your position : "))
            if(position in positions):
                is_valid_position = True
                break
        except:
            pass
    return position

def check_game_won(choice):
    if((board1[0] == board1[1] == board1[2] == choice) or
    (board2[0] == board2[1] == board2[2] == choice) or
    (board3[0] == board3[1] == board3[2] == choice) or
    (board1[0] == board2[0] == board3[0] == choice) or
    (board1[1] == board2[1] == board3[1] == choice) or
    (board1[2] == board2[2] == board3[2] == choice) or
    (board1[0] == board2[1] == board3[2] == choice) or
    (board1[2] == board2[1] == board3[0] == choice)):
        return True
    else:
        return False


def check_game_tie():
    if("" not in board1 and "" not in board2 and "" not in board3):
        return True
    else:
        return False

display_board()
choice1, choice2 = ask_choice()
while(stop_game != True):
    #Player 1 Plays
    pos = ask_position()
    display_board(pos, choice1)
    #Check Game Won or Tie
    if(check_game_won(choice1)):
        stop_game = True
        print("Game is won by Player 1")
        break
    if(check_game_tie()):
        stop_game = True
        print("Game is TIE")
        break
    else:
        pass
    #Player 2 Plays
    pos = ask_position()
    display_board(pos, choice2)
    #Check Game Won or Tie
    if(check_game_won(choice2)):
        stop_game = True
        print("Game is won by Player 2")
        break
    if(check_game_tie()):
        stop_game = True
        print("Game is TIE")
        break
