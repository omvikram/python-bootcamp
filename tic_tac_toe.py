## TIC TAC TOE PROGRAM

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
            print("inside row1")            
            index1 = row1.index(position)
            board1[index1] = choice
        elif(position in row2):
            print("inside row2")
            index2 = row2.index(position)
            board2[index2] = choice
        elif(position in row3):
            print("inside row3")
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
    while(is_valid_choice == False):
        try:
            choice = int(input("Please choose your sign -> 0 or 1 : "))
            if(choice in choices):
                is_valid_choice = True
                break
        except:
            pass
    return choice


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

display_board()
choice = ask_choice()
pos = ask_position()
display_board(pos, choice)