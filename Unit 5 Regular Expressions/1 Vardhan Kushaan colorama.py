from colorama import init, Back, Fore  # Note I have imported specific things here
import re
import sys

init()

s = "While inside they wined and dined, safe from the howling wind.\nAnd she whined, it seemed, for the 100th time, into the ear of her friend,\nWhy indeed should I wind the clocks up, if they all run down in the end?"
input = r'{}'.format(sys.argv[1])
broken_input = input.split("/")
flags = broken_input[2]


match len(flags):
    case 1:
        match flags:
            case "i": 
                exp = re.compile(r'{}'.format(broken_input[1]), re.I)
            case "s":
                exp = re.compile(r'{}'.format(broken_input[1]), re.S)
            case "m":
                exp = re.compile(r'{}'.format(broken_input[1]), re.M)
    case 2:
        if "i" in flags and "s" in flags:
            exp = re.compile(r'{}'.format(broken_input[1]), re.I | re.S)
        elif "m" in flags and "s" in flags:
            exp = re.compile(r'{}'.format(broken_input[1]), re.M | re.S)
        elif "i" in flags and "s" in flags:
            exp = re.compile(r'{}'.format(broken_input[1]), re.I | re.M)
    case 3:
        exp = re.compile(r'{}'.format(broken_input[1]), re.I | re.M | re.S)
    case _: 
        exp = re.compile(r'{}'.format(broken_input[1]))

matchified_string = list()
next_start = 0
match_indices = set()

for result in exp.finditer(s):
    matchified_string.append(s[next_start:int(result.start())])
    matchified_string.append(s[int(result.start()):int(result.end())])
    if "" in matchified_string:
        matchified_string.remove("")
    for key, val in enumerate(matchified_string):
        if val == result[0]:
            match_indices.add(key)
    next_start = int(result.end())
matchified_string.append(s[next_start:])

final_string = str()
dos_matches = True
for key, val in enumerate(matchified_string):
    if key in match_indices:
        if key-1 in match_indices:
            if dos_matches:
                final_string = final_string + Back.CYAN + val + Back.RESET
                dos_matches = False
            else:
                final_string = final_string + Back.YELLOW + val + Back.RESET
                dos_matches = True
        else:
            final_string = final_string + Back.YELLOW + val + Back.RESET
            dos_matches = True    
    else:
        final_string = final_string + val

print(final_string)

 