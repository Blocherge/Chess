from tkinter import *

top = Tk()

screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()

top.geometry('1000x1000')

c = Canvas(top, bg="white", height='1000', width=1000)

letter_values = ["a", "b", "c", "d", "e", "f", "g", "h"]

#creates the outline of the board
arc = c.create_rectangle((0, 0, 800, 800), outline="black", fill="white")

def create_pawn(x, y, color):
    c.create_oval(x, y, x+20, y+20, outline='black', fill=color)
    c.create_oval(x-5, y+15, x+25, y+45, outline='black', fill=color)
    c.create_arc(x-10, y+40, x+30, y+70, start=0, extent=180, outline='black', fill=color)


def create_rook(x, y, color):
    c.create_rectangle(x-12.5, y-12.5, x+12.5, y+12.5, outline='black', fill=color)
    c.create_polygon(x+12.5, y-12.5, x-12.5, y-12.5, x-18, y-18, x+18, y-18, outline='black', fill=color)
    c.create_rectangle(x-18, y-18, x+18, y-20, outline='black', fill=color)
    c.create_rectangle(x-18, y-20, x-12, y-28, outline='black', fill=color)
    c.create_rectangle(x+18, y-20, x+12, y-28, outline='black', fill=color)
    c.create_rectangle(x-3, y-20, x+3, y-28, outline='black', fill=color)
    c.create_polygon(x-12.5, y+12.5, x+12.5, y+12.5, x+18, y+18, x-18, y+18, outline='black', fill=color)
    c.create_rectangle(x-18, y+18, x+18, y+22, outline='black', fill=color)

#places all the board elements
for i in range(8):
    if i % 2 == 0:
        arc = c.create_rectangle((100, 100*i, 200, 100+100*i), outline="black", fill="grey")
        arc = c.create_rectangle((300, 100*i, 400, 100+100*i), outline='black', fill='grey')
        arc = c.create_rectangle((500, 100*i, 600, 100+100*i), outline='black', fill='grey')
        arc = c.create_rectangle((700, 100*i, 800, 100+100*i), outline='black', fill='grey')
    elif i % 2 == 1:
        arc = c.create_rectangle((0, 100*i, 100, 100*i+100), outline='black', fill='grey')
        arc = c.create_rectangle((200, 100*i, 300, 100*i+100), outline='black', fill='grey')
        arc = c.create_rectangle((400, 100*i, 500, 100*i+100), outline='black', fill='grey')
        arc = c.create_rectangle((600, 100*i, 700, 100*i+100), outline='black', fill='grey')

#creates the rooks
arc = create_rook(50, 50, 'black')
arc = create_rook(50, 750, 'white')
arc = create_rook(750, 50, "black")
arc = create_rook(750, 750, 'white')

#creates the pawns
for i in range(8):
    arc = create_pawn(40+(i*100), 125, 'black')
    arc = create_pawn(40+(i*100), 625, 'white')

#creates the board positions
for i in range(8):
    arc = c.create_text(825, 62.5+(100*i), fill='black', font='Times 20', text=str(i+1))
    arc = c.create_text(62.5+(i*100), 825, fill='black', font='Times 20', text=letter_values[i])


c.pack()

top.mainloop()

#lists for data storage
piece_locations_white = ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
                         "a1", "h1", "b1", "g1", "c1", "f1", "d1", "e1"]
pieces_types_white = ["pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn",
                      "rook", "rook", "knight", "knight", "bishop", "bishop", "queen", "king"]
piece_moved_white = [False, False, False, False, False, False, False, False,
                     False, False, False, False, False, False, False, False]
destroyed_pieces_white = []
white_num_queens = 1
piece_locations_black = ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
                         "a8", "h8", "b8", "g8", "c8", "f8", "d8", "e8"]
pieces_types_black = ["pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "rook", "rook",
                      "knight", "knight", "bishop", "bishop", "queen", "king"]
piece_moved_black = [False, False, False, False, False, False, False, False,
                     False, False, False, False, False, False, False, False]
destroyed_pieces_black = []
black_num_queens = 1
board_locations = [["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"],
                   ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
                   ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
                   ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
                   ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
                   ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
                   ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
                   ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"]]

#stores the turn value for color changing and stuff
turn = "white"
winner = False

def piece_destroyed(pos, color, wnq, bnq):
    print("this is being run")
    print(color)
    if color == "white":
        print("This is also being run")
        ind = piece_locations_black.index(pos)
        tip = pieces_types_black[ind]
        destroyed_pieces_black.append(tip)
        piece_locations_black.pop(ind)
        pieces_types_black.pop(ind)
        piece_moved_black.pop(ind)
    elif color == "black":
        ind = piece_locations_white.index(pos)
        tip = pieces_types_white[ind]
        destroyed_pieces_white.append(tip)
        piece_locations_white.pop(ind)
        pieces_types_white.pop(ind)
        piece_moved_white.pop(ind)


def pawn_movement(current_location, move_to, has_moved, color, w_l, b_l, p_l, board, hope):
    can_move = False
    indexing = letter_values.index(current_location[0])
    if move_to in str(board):
        if move_to != current_location:
            if hope:
                if not has_moved:
                    if color == "white":
                        if move_to[0] == current_location[0]:
                            if int(move_to[1]) == int(current_location[1])+1 or int(move_to[1]) == \
                                    int(current_location[1])+2:
                                if move_to in b_l:
                                    print("There is already a piece there")
                                elif move_to not in b_l:
                                    if int(move_to[1]) == int(current_location[1])+2:
                                        if move_to[0] + str(int(move_to[1])-1) not in p_l and move_to[0] + \
                                                str(int(move_to[1])-1) not in b_l:
                                            can_move = True
                                    else:
                                        can_move = True
                                        print(move_to[0])
                                        print(current_location[0])
                                else:
                                    print("there is already a piece there")
                        elif move_to[0] == letter_values[indexing+1] or move_to[0] == letter_values[indexing-1] and \
                                int(move_to[1]) == int(current_location[1])+1:
                            if move_to in b_l:
                                piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                                can_move = True
                            elif move_to not in b_l:
                                print("You can't make that move")
                    elif color == "black":
                        if move_to[0] == current_location[0]:
                            if int(move_to[1]) == int(current_location[1]) - 1 or int(move_to[1]) == \
                                    int(current_location[1]) - 2:
                                if move_to in w_l:
                                    print("There is already a piece there")
                                elif move_to not in w_l:
                                    if int(move_to[1]) == int(current_location[1]) - 2:
                                        if move_to[0] + str(int(move_to[1]) + 1) not in p_l and move_to[0] + \
                                                str(int(move_to[1]) + 1) not in w_l:
                                            can_move = True
                                    else:
                                        can_move = True
                                        print(move_to[0])
                                        print(current_location[0])
                                else:
                                    print("there is already a piece there")
                        elif move_to[0] == letter_values[indexing + 1] or move_to[0] == letter_values[indexing - 1] and\
                                 int(move_to[1]) == int(current_location[1]) - 1:
                            if move_to in w_l:
                                piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                                can_move = True
                            elif move_to not in w_l:
                                print("You can't make that move")
                elif has_moved:
                    if color == "white":
                        if move_to[0] == current_location[0] and int(move_to[1]) == int(current_location[1])+1:
                            if move_to not in b_l:
                                can_move = True
                            elif move_to in b_l:
                                print("There is a piece in the way")
                        elif move_to[0] == letter_values[indexing+1] or move_to[0] == letter_values[indexing-1] and \
                                int(move_to[1]) == int(current_location[1])+1:
                            if move_to in b_l:
                                can_move = True
                                piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            elif move_to not in b_l:
                                print("That is not an accepted move with that piece")
                    elif color == "black":
                        if move_to[0] == current_location[0] and int(move_to[1]) == int(current_location[1]) - 1:
                            if move_to not in w_l:
                                can_move = True
                            elif move_to in w_l:
                                print("There is a piece in the way")
                        elif move_to[0] == letter_values[indexing + 1] or move_to[0] == letter_values[indexing - 1] and\
                                int(move_to[1]) == int(current_location[1]) - 1:
                            if move_to in w_l:
                                can_move = True
                                piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            elif move_to not in w_l:
                                print("That is not an accepted move with that piece")
            else:
                print("You have a piece already at that location")
        else:
            print("The piece must move away from the current location")
    else:
        print("That location is not on the board")
    print(can_move)
    if can_move:
        if color == "white":
            ind = w_l.index(current_location)
            p_l[ind] = move_to
            piece_moved_white[ind] = True
        elif color == "black":
            ind = b_l.index(current_location)
            b_l[ind] = str(move_to)
            piece_moved_black[ind] = True


def knight_movement(current_location, move_to, p_l, letters, np_l, p_pm, hope, color):
    can_move = False
    continuation = False
    location = letters.index(str(current_location[0]))
    if move_to in str(board_locations):
        if move_to != current_location:
            if hope:
                if move_to[1] == int(current_location[1])+1:
                    print("darn")
                try:
                    if move_to[0] == letters[location+2] or move_to[0] == letters[location-2]:
                        if int(move_to[1]) == int(current_location[1])-1 or int(move_to[1]) == \
                                int(current_location[1])+1:
                            if move_to in np_l:
                                piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                                can_move = True
                                print("It is running through #1")
                            elif move_to not in np_l:
                                can_move = True
                                print("It is running through #2")
                            else:
                                print("That is not an accepted move with that piece")
                        else:
                            print("That is not an accepted move with that piece")
                    else:
                        continuation = True
                except IndexError:
                    if move_to[0] == letters[location+1] or move_to[0] == letters[location-1] and int(move_to[1]) == \
                            int(current_location[1])+2 or int(move_to[1]) == int(current_location[1])-2:
                        if move_to in np_l:
                            piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            can_move = True
                            print("It is running through #3")
                        elif move_to not in np_l:
                            can_move = True
                            print("It is running through #4")
                        else:
                            print("That is not an accepted move with that piece")
                if continuation:
                    if move_to[0] == letters[location+1] or move_to[0] == letters[location-1] and int(move_to[1]) == \
                            int(current_location[1])+2 or int(move_to[1]) == int(current_location[1])-2:
                        if move_to in np_l:
                            piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            can_move = True
                            print("It is running through #5")
                        elif move_to not in np_l:
                            can_move = True
                            print("It is running through #6")
                        else:
                            print("That is not a legal move with that piece")
            else:
                print("You already have a piece at that location")
        else:
            print("The piece must move away from it's current location")
    else:
        print("That location is not on the board")
    print(can_move)
    if can_move:
        ind = p_l.index(current_location)
        p_l[ind] = str(move_to)
        p_pm[ind] = True


def bishop_movement(current_location, move_to, p_l, np_l, p_pm, letters, hope, color):
    can_move = False
    location = letters.index(str(current_location[0]))
    if move_to in str(board_locations):
        if move_to != current_location:
            if hope:
                for i in range(location):
                    print(i)
                    if move_to[0] == letters[i] and int(move_to[1]) == int(current_location[1])+1+i or \
                            int(move_to[1]) == int(current_location[1])-1-i:
                        print("passing")
                        if move_to in np_l:
                            piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            can_move = True
                        if move_to not in np_l:
                            can_move = True
                for i in range(location):
                    if move_to[0] == letters[i] and int(move_to[1]) == int(current_location[1])+1 or \
                            int(move_to[1]) == int(current_location[1])-1:
                        if move_to in np_l:
                            piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            can_move = True
                        if move_to not in np_l:
                            can_move = True
            else:
                print("You already have a piece at that location")
        else:
            print("The piece has to move away from it's current location")
    else:
        print("That location is not on the board")
    if not can_move:
        print("That is not an acceptable move with that piece")
    elif can_move:
        ind = p_l.index(current_location)
        p_l[ind] = str(move_to)
        p_pm[ind] = True


def rook_movement(current_location, move_to, p_l, np_l, p_pm, letters, hope, color):
    can_move = False
    ending = True
    location = letters.index(str(move_to[0]))
    if move_to not in board_locations:
        if move_to != current_location:
            if hope:
                for i in range(len(letters)-location):
                    if move_to[0] == letters[location+i] and int(move_to[1]) == int(current_location[1]):
                        for j in range(abs(int(move_to[1])-int(current_location[1]))):
                            if int(move_to[1]) - (j+1) not in p_l:
                                if move_to in np_l:
                                    piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                                    can_move = True
                                    print("It is the first one")
                                if move_to not in np_l:
                                    can_move = True
                                    print("It is this one")
                for i in range(location):
                    if move_to[0] == letters[i] and int(move_to[1]) == int(current_location[1]):
                        if move_to in np_l:
                            piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            can_move = True
                            print("it is the third one")
                        if move_to not in np_l:
                            can_move = True
                            print("It is the fourth one")
                for i in range(1, 9-int(current_location[1]), 1):
                    if int(move_to[1]) == int(current_location[1]) + i and move_to[0] == current_location[0]:
                        if move_to in np_l:
                            piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            can_move = True
                            print("it is the fifth one")
                        elif move_to not in np_l:
                            can_move = True
                            print("It is the sixth one")
                for i in range(int(current_location[1])):
                    if int(move_to[1]) == i and move_to[0] == current_location[0]:
                        if move_to in np_l:
                            piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            can_move = True
                            print("It is the seventh one")
                        if move_to not in np_l:
                            can_move = True
                            print("it is the eighth one")
            else:
                print("You already have a piece there")
        else:
            print("The piece has to move from it's current location")
    else:
        print("That location is not on the board")
    if can_move:
        ind = p_l.index(current_location)
        p_l[ind] = move_to
        p_pm[ind] = True
    else:
        print("That is not a valid move")


def queen_movement(current_location, move_to, p_l, np_l, p_pm, letters, hope, color):
    can_move = False
    location = letters.index(str(move_to[0]))
    if move_to in board_locations:
        if move_to != current_location:
            if hope:
                for i in range(len(letters)-location):
                    if move_to[0] == letters[location+i] and int(move_to[1]) == int(current_location[1]):
                        if move_to in np_l:
                            piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            can_move = True
                        if move_to not in np_l:
                            can_move = True
                for i in range(letters.index(location)):
                    if move_to[0] == letters[i] and int(move_to[1]) == int(current_location[1]):
                        if move_to in np_l:
                            piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            can_move = True
                        if move_to not in np_l:
                            can_move = True
                for i in range(1, 9-int(current_location[1]), 1):
                    if int(move_to[1]) == int(current_location[1]) + i and move_to[0] == current_location[0]:
                        if move_to in np_l:
                            piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            can_move = True
                        elif move_to not in np_l:
                            can_move = True
                for i in range(int(current_location[1])):
                    if int(move_to[1]) == i and move_to[0] == current_location[0]:
                        if move_to in np_l:
                            piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            can_move = True
                        if move_to not in np_l:
                            can_move = True
                for i in range(len(letters)-location):
                    if move_to[0] == letters[i] and int(move_to[1]) == int(current_location[1])+1 or \
                            int(move_to[1]) == int(current_location[1])-1:
                        if move_to in np_l:
                            piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            can_move = True
                        if move_to not in np_l:
                            can_move = True
                for i in range(location):
                    if move_to[0] == letters[i] and int(move_to[1]) == int(current_location[1])+1 or \
                            int(move_to[1]) == int(current_location[1])-1:
                        if move_to in np_l:
                            piece_destroyed(move_to, color, white_num_queens, black_num_queens)
                            can_move = True
                        if move_to not in np_l:
                            can_move = True
            else:
                print("You already have a piece there")
        else:
            print("The piece has to move from it's current location")
    else:
        print("That location is not on the board")
    if can_move:
        ind = p_l.index(current_location)
        p_l[ind] = move_to
        p_pm[ind] = True


def in_pawn_range(move_to, pawn_location, letters, color):
    in_range = False
    location = letters.index(pawn_location[0])
    if color == "white":
        if int(move_to[1]) == int(pawn_location[1])-1:
            if move_to[0] == letters[location+1]:
                in_range = True
            elif move_to[0] == letters[location-1]:
                in_range = True
    elif color == "black":
        if int(move_to[1]) == int(pawn_location[1])+1:
            if move_to[0] == letters[location+1]:
                in_range = True
            elif move_to[0] == letters[location-1]:
                in_range = True
    return in_range


def in_knight_range(move_to, knight_location, letters):
    in_range = False
    location = letters.index(knight_location[0])
    if move_to[0] == letters[location+1] and int(move_to[1]) == int(knight_location[1])+2 or int(move_to[1]) == \
            int(knight_location[1])-2:
        in_range = True
    elif move_to[0] == letters[location-1] and int(move_to[1]) == int(knight_location[1])+2 or int(move_to[1]) == \
            int(knight_location[1])-2:
        in_range = True
    elif move_to[0] == letters[location+2] and int(move_to[1]) == int(knight_location[1])+1 or int(move_to[1]) == \
            int(knight_location[1])-1:
        in_range = True
    elif move_to[0] == letters[location-2] and int(move_to[1]) == int(knight_location[1])+1 or int(move_to[1]) == \
            int(knight_location[1])-1:
        in_range = True
    return in_range


def in_bishop_range(move_to, bishop_location, letters):
    continuation = False
    in_range = False
    location = letters.index[bishop_location[0]]
    for i in range(location):
        if move_to[0] == letters[location-(1+i)] and int(move_to[1]) == int(bishop_location[1])-(i+1):
            in_range = True
        elif move_to[0] == letters[location-(1+i)] and int(move_to[1]) == int(bishop_location[1])+(i+1):
            in_range = True
        else:
            continuation = True
    if continuation:
        for i in range(8-location):
            if move_to[0] == letters[location+(1+i)] and int(move_to[1]) == int(bishop_location[1])-(i+1):
                in_range = True
            elif move_to[0] == letters[location+(1+i)] and int(move_to[1]) == int(bishop_location[1])+(i+1):
                in_range = True
    return in_range


def in_rook_range(move_to, rook_location, letters):
    in_range = False
    return in_range
    location = letters.index(rook_location[0])
    try:
        if move_to[0] == letters[location + 2] and int(move_to[1]) == int(rook_location[1]) + 1 or int(move_to[1]) \
                == int(rook_location[1])-1:
            in_range = True
    except ValueError:
        print("Weird")
    try:
        if move_to[0] == letters[location-2] and int(move_to[1]) == int(rook_location[1])+1 or int(move_to[1]) == \
                int(rook_location[1])-1:
            in_range = True
    except ValueError:
        print("Weird")
    try:
        if move_to[0] == letters[location+1] and int(move_to[1]) == int(rook_location[1])+2 or int(move_to[1]) == \
                int(rook_location[1])-2:
            in_range = True
    except ValueError:
        print("Weird")
    try:
        if move_to[0] == letters[location-1] and int(move_to[1]) == int(rook_location[1])-2 or int(move_to[1]) == \
                int(rook_location[1])+2:
            in_range = True
    except ValueError:
        print("Weird")
    return in_range


def in_queen_range(move_to, queen_location, letters):
    in_range = False
    location = letters.index(queen_location[0])
    for i in range(1, 7-int(move_to[1]), 1):
        if move_to[0] == queen_location[0] and int(move_to[1])+i == int(queen_location[1]):
            in_range = True
    for i in range(1, int(move_to[1]), 1):
        if move_to[0] == queen_location[0] and int(move_to[1])-i == int(queen_location[1]):
            in_range = True


def in_king_range(move_to, king_location, letters):
    in_range = False
    location = letters.index(king_location[0])
    if move_to[0] == king_location[0] and int(move_to[1])+1 == int(king_location[1]):
        in_range = True
    if move_to[0] == king_location[0] and int(move_to[1])-1 == int(king_location[1]):
        in_range = True
    if move_to[0] == letters[location+1] and int(move_to[1]) == int(king_location[1]):
        in_range = True
    if move_to[0] == letters[location-1] and int(move_to[1]) == int(king_location[1]):
        in_range = True
    if move_to[0] == letters[location+1] and int(move_to[1]) == int(king_location[1])+1:
        in_range = True
    if move_to[0] == letters[location+1] and int(move_to[1]) == int(king_location[1])-1:
        in_range = True
    if move_to[0] == letters[location-1] and int(move_to[1]) == int(king_location[1])+1:
        in_range = True
    if move_to[0] == letters[location-1] and int(move_to[1]) == int(king_location[1])-1:
        in_range = True
    return in_range


def king_movement(current_location, move_to, p_l, p_t, np_l, np_t, p_pm, np_pm, letters):
    potato = ""
    pawns_alive = -1
    knight_indexes = []
    rook_indexes = []
    bishop_indexes = []
    queen_indexes = []
    king_location = np_t.index("king")
    king_index = p_t.index("king")
    can_move = True
    random_var = False
    color = str(p_l[17:])
    location = letters.index(str(current_location[0]))
    if move_to in board_locations:
        if move_to != current_location:
            for i in range(len(np_l)):
                if np_t[i] == "pawn":
                    pawns_alive = i
                elif np_t[i] == "knight":
                    knight_indexes.append(i)
                elif np_t[i] == "rook":
                    rook_indexes.append(i)
                elif np_t[i] == "bishop":
                    bishop_indexes.append(i)
                elif np_t[i] == "queen":
                    queen_indexes.append(i)
            for i in range(pawns_alive):
                if not in_pawn_range(move_to, np_l[i], letters, color):
                    print("Passed 1")
                else:
                    can_move = False
                    print("You can't move there because you would be killing your king")
            for i in range(len(knight_indexes)):
                if in_knight_range(move_to, np_l[knight_indexes[i]], letters):
                    can_move = False
                    print("You can't move there because you would be killing your king")
            for i in range(len(bishop_indexes)):
                if in_bishop_range(move_to, np_l[bishop_indexes[i]], letters):
                    can_move = False
                    print("You can't move there because you would be killing your king")
            for i in range(len(rook_indexes)):
                if in_rook_range(move_to, np_l[rook_indexes[i]], letters):
                    can_move = False
            for i in range(len(queen_indexes)):
                if in_queen_range(move_to, np_l[queen_indexes[i]], letters):
                    can_move = False
                    print("You can't move there because you would be killing your king")
            if in_king_range(move_to, np_l[king_location], letters):
                can_move = False
                print("you can't move there because you would be killing you king")
            try:
                if move_to[0] == letters[location+1] and int(move_to[1]) == int(current_location[1]) or int(move_to[1])\
                        == int(current_location[1])+1 or int(move_to[1]) == int(current_location[1])-1:
                    random_var = True
            except TypeError:
                print("This really shouldn't happen so if it did whoever caused it loses")
            try:
                if move_to[0] == letters[location-1] and int(move_to[1]) == int(current_location[1]) or int(move_to[1])\
                        == int(current_location[1])+1 or int(move_to[1]) == int(current_location[1])-1:
                    random_var = True
            except TypeError:
                print("If you got this there is something seriously wrong")
            if move_to[0] == current_location[0] and int(move_to[1]) == int(current_location[1])+1 or int(move_to[1]) \
                    == int(current_location[1])-1:
                random_var = True
            if not random_var:
                can_move = False
            if can_move:
                if move_to in np_l:
                    potato = np_l.index(move_to)
                    np_l.pop(potato)
                    np_t.pop(potato)
                    np_pm.pop(potato)
                p_l[potato] = move_to
                p_pm[potato] = True


def castle(current_location, p_pm, p_l, np_l, p_t, color):
    can_move = False
    location_rook = p_l.index(current_location)
    location_king = p_t.index("king")
    has_moved_rook = p_pm[location_rook]
    has_moved_king = p_pm[location_king]
    if not has_moved_rook:
        if not has_moved_king:
            if color == "white":
                if current_location == "a1":
                    if "b1" not in p_l and "b1" not in np_l and "c1" not in p_l and "c1" not in np_l and "d1" not in \
                            p_l and "d1" not in np_l:
                        can_move = True
                        p_l[location_rook] = "d1"
                        p_l[location_king] = "c1"
                        piece_moved_white[location_rook] = True
                        piece_moved_white[location_king] = True
                    else:
                        print("There is another piece in the way you cannot castle")
                elif current_location == "h1":
                    if "f1" not in p_l and "f1" not in np_l and "g1" not in p_l and "g1" not in np_l:
                        can_move = True
                        p_l[location_rook] = "f1"
                        p_l[location_king] = "g1"
                        piece_moved_white[location_rook] = True
                        piece_moved_white[location_king] = True
                    else:
                        print("There is another piece in the way you cannot castle")
                else:
                    print("the location you input is not the location of one of the starting positions of the rooks")
            elif color == "black":
                if current_location == "a8":
                    if "b8" not in p_l and "b8" not in np_l and "c8" not in p_l and "c8" not in np_l and "d8" not in \
                            p_l and "d8" not in np_l:
                        can_move = True
                        p_l[location_rook] = "d8"
                        p_l[location_king] = "c8"
                        piece_moved_black[location_rook] = True
                        piece_moved_black[location_king] = True
                    else:
                        print("There is another piece in the way you cannot castle")
                elif current_location == "h8":
                    if "g8" not in p_l and "g8" not in np_l and "f8" not in p_l and "f8" not in np_l:
                        can_move = True
                        p_l[location_rook] = "f8"
                        p_l[location_king] = "g8"
                        piece_moved_black[location_rook] = True
                        piece_moved_black[location_king] = True
                    else:
                        print("There is another piece in the way you cannot castle")
                else:
                    print("The location you input is not the location of one of the starting positions of the rooks")
        else:
            print("The king has moved you can no longer castle")
    else:
        print("the rook has already moved you can no longer castle with that piece")
    return can_move


def pawn_change(current_location, move_to, color, p_l, p_t, can_move):
    queens_color = ""
    need_switch = False
    type_index = p_t.index(p_l.index(current_location))
    if color == "white":
        if can_move and int(move_to[1]) == 8:
            need_switch = True
        queens_color = white_num_queens
    elif color == "black":
        if can_move and int(move_to[1]) == 1:
            need_switch = True
        queens_color = black_num_queens
    if need_switch:
        while True:
            switch_to = input("What would you like to switch the pawn to: ")
            if switch_to == "knight" or switch_to == "bishop" or switch_to == "rook":
                p_t[type_index] = switch_to
                break
            elif switch_to == "queen" and queens_color < 2:
                p_t[type_index] = switch_to
                break
            else:
                print("That is not an accepted option, choices: knight, bishop, rook, queen")


def checkmate(p_l, p_t, np_l, np_t, letters, color):
    checkmated = False
    long = False
    king_location = p_l[p_t.index("king")]
    pawn_indexes = []
    rook_indexes = []
    bishop_indexes = []
    knight_indexes = []
    queen_indexes = []
    enemy_king = np_t.index("king")
    letter_location = letters[king_location[0]]
    if king_location[0] == "a":
        king_move_to = [king_location[0] + str(int(king_location[1])+1), letters[letter_location+1] +
                        str(int(king_location[1])+1), letters[letter_location+1] + king_location[1],
                        letters[letter_location+1] + str(int(king_location[1])-1), king_location[0] +
                        str(int(king_location[1])-1)]
        all_checkmate_values = [False, False, False, False, False, False]
    elif king_location[0] == "h":
        king_move_to = [king_location[0] + str(int(king_location[1])+1), letters[letter_location-1] +
                        str(int(king_location[1])+1), letters[letter_location-1] + king_location[1],
                        letters[letter_location-1] + str(int(king_location[1])-1), king_location[0] +
                        str(int(king_location[1])-1)]
        all_checkmate_values = [False, False, False, False, False, False]
    else:
        king_move_to = [king_location[0] + str(int(king_location[1])+1), letters[letter_location+1] +
                        str(int(king_location[1])+1), letters[letter_location+1] + king_location[1],
                        letters[letter_location+1] + str(int(king_location[1])-1), king_location[0] +
                        str(int(king_location[1])-1), letters[letter_location-1] + str(int(king_location[1])-1),
                        letters[letter_location-1] + king_location[1], letters[letter_location-1] +
                        str(int(king_location[1])+1)]
        all_checkmate_values = [False, False, False, False, False, False, False, False, False]
        long = True
    for i in range(len(np_t)):
        if np_t[i] == "pawn":
            pawn_indexes.append(i)
        elif np_t[i] == "rook":
            rook_indexes.append(i)
        elif np_t[i] == "bishop":
            bishop_indexes.append(i)
        elif np_t[i] == "knight":
            knight_indexes.append(i)
        elif np_t[i] == "queen":
            queen_indexes.append(i)
    for i in range(len(pawn_indexes)):
        if in_pawn_range(king_location, np_l[pawn_indexes[i]], letters, color):
            all_checkmate_values[0] = True
    for i in range(len(rook_indexes)):
        if in_rook_range(king_location, np_l[rook_indexes[i]], letters):
            all_checkmate_values[0] = True
    for i in range(len(bishop_indexes)):
        if in_bishop_range(king_location, np_l[knight_indexes[i]], letters):
            all_checkmate_values[0] = True
    for i in range(len(knight_indexes)):
        if in_knight_range(king_location, np_l[bishop_indexes[i]], letters):
            all_checkmate_values[0] = True
    for i in range(len(queen_indexes)):
        if in_queen_range(king_location, np_l[queen_indexes[i]], letters):
            all_checkmate_values[0] = True
    if in_king_range(king_location, np_l[enemy_king], letters):
        all_checkmate_values[0] = True
    for i in range(len(king_move_to)):
        if king_move_to[i] in board_locations:
            for j in range(len(pawn_indexes)):
                if in_pawn_range(king_move_to[i], np_l[pawn_indexes[j]], letters, color):
                    all_checkmate_values[1+i] = True
            for j in range(len(bishop_indexes)):
                if in_bishop_range(king_move_to[i], np_l[bishop_indexes[j]], letters):
                    all_checkmate_values[1+i] = True
            for j in range(len(rook_indexes)):
                if in_rook_range(king_move_to[i], np_l[rook_indexes[j]], letters):
                    all_checkmate_values[1+i] = True
            for j in range(len(knight_indexes)):
                if in_knight_range(king_move_to[i], np_l[knight_indexes[j]], letters):
                    all_checkmate_values[1+i] = True
            for j in range(len(queen_indexes)):
                if in_queen_range(king_move_to[i], np_l[queen_indexes[j]], letters):
                    all_checkmate_values[1+i] = True
            if in_king_range(king_move_to[i], np_l[enemy_king], letters):
                all_checkmate_values[1+i] = True
            if king_move_to[i] in p_l:
                all_checkmate_values[1+i] = True
    if long:
        if all_checkmate_values[0] and all_checkmate_values[1] and all_checkmate_values[2] and all_checkmate_values[3]\
                and all_checkmate_values[4] and all_checkmate_values[5] and all_checkmate_values[6] and\
                all_checkmate_values[7] and all_checkmate_values[8]:
            checkmated = True
    else:
        if all_checkmate_values[0] and all_checkmate_values[1] and all_checkmate_values[2] and all_checkmate_values[3] \
                and all_checkmate_values[4] and all_checkmate_values[5]:
            checkmated = True
    return checkmated


def check(p_l, p_t, np_l, np_t, letters, color):
    in_check = False
    king_location = p_l[p_t.index("king")]
    pawn_indexes = []
    rook_indexes = []
    bishop_indexes = []
    knight_indexes = []
    queen_indexes = []
    enemy_king = np_t.index("king")
    for i in range(len(np_t)):
        if np_t[i] == "pawn":
            pawn_indexes.append(i)
        elif np_t[i] == "rook":
            rook_indexes.append(i)
        elif np_t[i] == "bishop":
            bishop_indexes.append(i)
        elif np_t[i] == "knight":
            knight_indexes.append(i)
        elif np_t[i] == "queen":
            queen_indexes.append(i)
    for i in range(len(pawn_indexes)):
        if in_pawn_range(king_location, np_l[pawn_indexes[i]], letters, color):
            in_check = True
    for i in range(len(rook_indexes)):
        if in_rook_range(king_location, np_l[rook_indexes[i]], letters):
            in_check = True
    for i in range(len(bishop_indexes)):
        if in_bishop_range(king_location, np_l[knight_indexes[i]], letters):
            in_check = True
    for i in range(len(knight_indexes)):
        if in_knight_range(king_location, np_l[bishop_indexes[i]], letters):
            in_check = True
    for i in range(len(queen_indexes)):
        if in_queen_range(king_location, np_l[queen_indexes[i]], letters):
            in_check = True
    if in_king_range(king_location, np_l[enemy_king], letters):
        in_check = True
    return in_check


def piece_movement(p_l, p_t, p_m, np_l, color):
    hope = False
    print("it is " + str(turn) + "'s turn")
    current_location = str(input("where on the board is the piece that you want to move: "))
    if current_location in p_l:
        move_to = input("where do you want to move it: ")
        location = p_l.index(current_location)
        if move_to not in p_l:
            hope = True
        print("you moved the piece at " + str(current_location) + " to " + str(move_to))
        if current_location in str(p_l):
            if move_to == "castle":
                castle(current_location, p_m, p_l, np_l, p_t, color)
            elif str(p_t[location]) == "pawn":
                pawn_movement(current_location, move_to, p_m[location], turn, piece_locations_white,
                              piece_locations_black, p_l, board_locations, hope)
            elif str(p_t[location]) == "knight":
                knight_movement(current_location, move_to, p_l, letter_values, np_l, p_m, hope, color)
            elif str(p_t[location]) == "bishop":
                bishop_movement(current_location, move_to, p_l, np_l, p_m, letter_values, hope, color)
            elif str(p_t[location]) == "rook":
                rook_movement(current_location, move_to, p_l, np_l, p_m, letter_values, hope, color)
            elif str(p_t[location]) == "queen":
                queen_movement(current_location, move_to, p_l, np_l, p_m, letter_values, hope, color)
        else:
            print("You have no piece at that location")
    else:
        print("That is not an accepted input")


while not winner:
    if turn == "white":
        print(piece_locations_white)
        print(pieces_types_white)
        print(piece_locations_black)
        print(pieces_types_black)
        piece_movement(piece_locations_white, pieces_types_white, piece_moved_white, piece_locations_black, "white")
        turn = "black"
    elif turn == "black":
        print(piece_locations_white)
        print(pieces_types_white)
        print(piece_locations_black)
        print(pieces_types_black)
        piece_movement(piece_locations_black, pieces_types_black, piece_moved_black, piece_locations_white, "black")
        turn = "white"
