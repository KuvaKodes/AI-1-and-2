import sys

f1 = sys.argv[1]
min_length = int(sys.argv[2])
if len(sys.argv) == 4:
    starting_board = sys.argv[3]
else:
    starting_board = ""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
possible_scores = [-1, 1]

with open(f1) as f:
    move_dict = dict()
    move_dict_keyset = set()
    for line in f:
        word = line.strip()
        word = word.upper()
        if len(word) >= min_length and word.isalpha():
             for i in range(1,len((word))+1):
                 sub_key = word[0:i]
                 if sub_key not in move_dict_keyset:
                     move_dict[sub_key] = [word, ]
                     move_dict_keyset.add(sub_key)
                 else: 
                     move_dict[sub_key].append(word)


def possible_moves(state):
    if state == "":
        return [str(i) for i in alphabet]
    else:
        return move_dict[state]
    
def game_over(state):
    if state in possible_moves(state):
        return True
    return False


def max_move(board):
    if game_over(board):
        return max(possible_scores)
    results = {-1: list(), 1: list()}
    tried_set = set()
    for wordy in possible_moves(board):
        new_word = wordy[0:len(board)+1]
        if new_word not in tried_set:
            tried_set.add(new_word)
            val = min_step(new_word)
            results[val].append(wordy)
    return results[max(results.keys())]

def max_step(board):
    if game_over(board):
        return max(possible_scores)
    results = list()
    tried_set = set()
    for wordy in possible_moves(board):
        new_word = wordy[0:len(board)+1]
        if new_word not in tried_set:
            tried_set.add(new_word)
            results.append(min_step(new_word))
    return max(results)

def min_step(board):
    if game_over(board):
        return min(possible_scores)
    results = list()
    tried_set = set()
    for wordy in possible_moves(board):
        new_word = wordy[0:len(board)+1]
        if new_word not in tried_set:
            tried_set.add(new_word)
            results.append(max_step(new_word))
    return min(results)

def run_game(starting_board):
    list_of_letters = set()
    winning_words = max_move(starting_board)
    if len(winning_words) == 0:
        print("Next Player Will Lose!")
    else:
        for word in winning_words:
            list_of_letters.add(word[len(starting_board): len(starting_board)+1])
        print("Next player can guarantee victory by playing any of these letters: " + str(list_of_letters))

run_game(starting_board)
        


