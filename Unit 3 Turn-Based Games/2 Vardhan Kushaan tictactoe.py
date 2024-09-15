import random
import sys


def print_board(board):
    return board[0:3] + "\n" + board[3:6] + "\n" + board[6:9]

def game_over(board):
    if "." not in board:
        return True
    for row_num in range(3):
        possible_winner = board[3*row_num: (3*row_num)+ 3]
        if possible_winner == "XXX" or possible_winner == "OOO":
            return True
    for col_num in range(3):
        possible_winner = board[col_num: col_num+7: 3]
        if possible_winner == "XXX" or possible_winner == "OOO":
            return True
    possible_winner = "" + board[0] + board[4] + board[8]
    if possible_winner == "XXX" or possible_winner == "OOO":
        return True
    possible_winner = "" + board[2] + board[4] + board[6]
    if possible_winner == "XXX" or possible_winner == "OOO":
        return True
    return False

def score(board):
    for row_num in range(3):
        possible_winner = board[3*row_num: (3*row_num)+3]
        if possible_winner == "XXX":
            return 1 
        if possible_winner == "OOO":
            return -1
    for col_num in range(3):
        possible_winner = board[col_num: col_num+7: 3]
        if possible_winner == "XXX":
            return 1 
        if possible_winner == "OOO":
            return -1
    possible_winner = "" + board[0] + board[4] + board[8]
    if possible_winner == "XXX":
        return 1
    if possible_winner == "OOO":
        return -1
    possible_winner = "" + board[2] + board[4] + board[6]
    if possible_winner == "XXX":
        return 1
    if possible_winner == "OOO":
        return -1
    if "." not in board:
        return 0
    
def score_words(score):
    if score == 0:
        return "tie"
    elif score == 1:
        return "X win"
    elif score == -1: 
        return "O win"

def possible_moves(board):
    possible_move_list = list()
    for ind, val in enumerate(board):
        if val == ".":
            possible_move_list.append(ind)
    return possible_move_list


def max_step(board):
    if game_over(board):
        return score(board)
    results = list()
    for ind in possible_moves(board):
        new_board = board[0:ind] + "X" + board[ind+1:]
        results.append(min_step(new_board))
    return max(results)

def min_step(board):
    if game_over(board):
        return score(board)
    results = list()
    for ind in possible_moves(board):
        new_board = board[0:ind] + "O" + board[ind+1:]
        results.append(max_step(new_board))
    return min(results)

def max_move(board):
    if game_over(board):
        return score(board)
    results = dict()
    for ind in possible_moves(board):
        new_board = board[0:ind] + "X" + board[ind+1:]
        results[ind] = min_step(new_board)
    return results

def min_move(board):
    if game_over(board):
        return score(board)
    results = dict()
    for ind in possible_moves(board):
        new_board = board[0:ind] + "O" + board[ind+1:]
        results[ind] = max_step(new_board)
    return results



initial_board = sys.argv[1]

if initial_board == ".........":
    print("Should I be X or O?")
    choice = input()
    print()
    print("Current Board:")
    print(print_board(initial_board))
    print()
    print(print_board("012345678"))
    print()
    if choice == "X":
        while(not game_over(initial_board)):
            possible_boards = max_move(initial_board)
            for result in possible_boards.keys():
                print("Moving at " + str(result) +" results in a " + str(score_words(possible_boards[result])))
            print()
            for key,value in possible_boards.items():
                if int(value) == max(list(possible_boards.values())):
                    myKey = key
                    break
            print("I choose " + str(myKey))
            initial_board = initial_board[0:myKey] + "X" + initial_board[myKey+1:]
            print("Current Board:")
            print(print_board(initial_board))
            print(print_board("012345678"))
            print()
            if game_over(initial_board):
                print("It's an " + str(score_words(score(initial_board))))
                break
            print("You can move to any of these spaces: " + ", ".join(x := [str(i) for i in possible_moves(initial_board)]))
            print("Your choice?")
            user_choice = input()
            initial_board = initial_board[0:int(user_choice)] + "O" + initial_board[int(user_choice)+1:]
            print("Current Board:")
            print(print_board(initial_board))
            print(print_board("012345678"))
            print()
            if game_over(initial_board):
                print("It's an " + str(score_words(score(initial_board))))
                break
    if choice == "O":
        while(not game_over(initial_board)):
            print("You can move to any of these spaces: " + ", ".join(x := [str(i) for i in possible_moves(initial_board)]))
            print("Your choice?")
            user_choice = input()
            initial_board = initial_board[0:int(user_choice)] + "X" + initial_board[int(user_choice)+1:]
            print("Current Board:")
            print(print_board(initial_board))
            print(print_board("012345678"))
            print()
            if game_over(initial_board):
                print("It's an " + str(score_words(score(initial_board))))
                break
            possible_boards = min_move(initial_board)
            for result in possible_boards.keys():
                print("Moving at " + str(result) +" results in a " + str(score_words(possible_boards[result])))
            print()
            for key,value in possible_boards.items():
                if int(value) == min(list(possible_boards.values())):
                    myKey = key
                    break
            print("I choose " + str(myKey))
            initial_board = initial_board[0:myKey] + "O" + initial_board[myKey+1:]
            print("Current Board:")
            print(print_board(initial_board))
            print(print_board("012345678"))
            print()
            if game_over(initial_board):
                print("It's an " + str(score_words(score(initial_board))))
                break
else:
    print("Current Board:")
    print(print_board(initial_board))
    print()
    print(print_board("012345678"))
    print()
    if initial_board.count("X") == initial_board.count("O"):
        while(not game_over(initial_board)):
            possible_boards = max_move(initial_board)
            for result in possible_boards.keys():
                print("Moving at " + str(result) +" results in a " + str(score_words(possible_boards[result])))
            print()
            for key,value in possible_boards.items():
                if int(value) == max(list(possible_boards.values())):
                    myKey = key
                    break
            print("I choose " + str(myKey))
            initial_board = initial_board[0:myKey] + "X" + initial_board[myKey+1:]
            print("Current Board:")
            print(print_board(initial_board))
            print(print_board("012345678"))
            print()
            if game_over(initial_board):
                print("It's an " + str(score_words(score(initial_board))))
                break
            print("You can move to any of these spaces: " + ", ".join(x := [str(i) for i in possible_moves(initial_board)]))
            print("Your choice?")
            user_choice = input()
            initial_board = initial_board[0:int(user_choice)] + "O" + initial_board[int(user_choice)+1:]
            print("Current Board:")
            print(print_board(initial_board))
            print(print_board("012345678"))
            print()
            if game_over(initial_board):
                print("It's an " + str(score_words(score(initial_board))))
                break
    if initial_board.count("X") > initial_board.count("O"):
        while(not game_over(initial_board)):
            possible_boards = min_move(initial_board)
            for result in possible_boards.keys():
                print("Moving at " + str(result) +" results in a " + str(score_words(possible_boards[result])))
            print()
            for key,value in possible_boards.items():
                if int(value) == min(list(possible_boards.values())):
                    myKey = key
                    break
            print("I choose " + str(myKey))
            initial_board = initial_board[0:myKey] + "O" + initial_board[myKey+1:]
            print("Current Board:")
            print(print_board(initial_board))
            print(print_board("012345678"))
            print()
            if game_over(initial_board):
                print("It's an " + str(score_words(score(initial_board))))
                break
            print("You can move to any of these spaces: " + ", ".join(x := [str(i) for i in possible_moves(initial_board)]))
            print("Your choice?")
            user_choice = input()
            initial_board = initial_board[0:int(user_choice)] + "X" + initial_board[int(user_choice)+1:]
            print("Current Board:")
            print(print_board(initial_board))
            print(print_board("012345678"))
            print()
            if game_over(initial_board):
                print("It's an " + str(score_words(score(initial_board))))
                break


  

        





        

    




    

