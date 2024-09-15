import sys
import re


with open(sys.argv[1]) as f: 
    line_list = [line.strip().lower() for line in f]

#Problem 1
min = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
matchlist = list()
for word in line_list: 
     m = re.match(r'^(?=.*a)(?=.*e)(?=.*i)(?=.*o)(?=.*u).*$', word)
     if m: 
          if len(m[0]) < min:
               min = len(m[0])
          matchlist.append(m[0])
shortest_match_list = list()
for match in matchlist:  
    if len(match) == min:
         shortest_match_list.append(match)
print("#1: %s" % r'/^(?=.*a)(?=.*e)(?=.*i)(?=.*o)(?=.*u).*$/')
print("%s total matches" % len(shortest_match_list))
for word in shortest_match_list[0:5]:
     print(word)
print()
        
#Problem 2
max_1 = 0 
matchlist_2 = list()
for word in line_list:
     m2 = re.match(r'^(?=(\w*?[aeiou]){5}\w*$)(?!(\w*?[aeiou]){6})\w+$', word)
     if m2:
          if len(m2[0]) > max_1:
               max_1 = len(m2[0])
          matchlist_2.append(m2[0])
longest_match_list = list()
for match in matchlist_2:
     if len(match) == max_1:
          longest_match_list.append(match)
print("#2: %s" % r'/^(?=(\w*?[aeiou]){5}\w*$)(?!(\w*?[aeiou]){6})\w+$/')
print("%s total matches" % len(longest_match_list))
for word in longest_match_list[0:5]:
     print(word)
print()

#Problem 3
max_2 = 0
matchlist_3 = list()
for word in line_list:
     m3 = re.match(r'^(\w)(?!.*\1\w).*\1$', word)
     if m3: 
          if len(m3[0]) > max_2:
               max_2 = len(m3[0])
          matchlist_3.append(m3[0])
longest_match_list_2 = list()
for match in matchlist_3:
     if len(match) == max_2:
          longest_match_list_2.append(match)
print("#3: %s" % r'/^(\w)(?!.*\1\w).*\1$/')
print("%s total matches" % len(longest_match_list_2))
for word in longest_match_list_2[0:5]:
     print(word)
print()

#Problem 4
matchlist_4 = list()
for word in line_list:
     m5 = re.match(r'^(\w)(\w)(\w)\w*\3\2\1$|^(\w)\w\4$|^(\w)(\w)\6\5$|^(\w)(\w)\w\8\7$', word)
     if m5:
          matchlist_4.append(m5[0])
print("#4: %s" % r'/^(\w)(\w)(\w)\w*\3\2\1$|^(\w)\w\4$|^(\w)(\w)\6\5$|^(\w)(\w)\w\8\7$/')
print("%s total matches" % len(matchlist_4))
for word in matchlist_4[0:5]:
     print(word)
print()

#Problem 5
matchlist_5 = list()
for word in line_list:
     m4 = re.match(r'^(?!.*b.*b)(?!.*t.*t).*[bt][bt].*$', word)
     if m4:
          matchlist_5.append(m4[0])
print("#5: %s" % r'/^(?!.*b.*b)(?!.*t.*t).*[bt][bt].*$/')
print("%s total matches" % len(matchlist_5))
for word in matchlist_5[0:5]:
     print(word)
print()

#Problem 6
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# longest_streak = 0
# contigous_dict = dict()
# for letter in alphabet: 
#      pattern = re.compile(f"{letter}+")
#      for word in line_list:
#           m6 = re.search(pattern, word)
#           if m6:
#             length_of_contigousness = len(m6[0])
#             if length_of_contigousness not in contigous_dict.keys():
#                 contigous_dict[length_of_contigousness] = [word,]
#             else:
#                 contigous_dict[length_of_contigousness].append(word)
#             if len(m6[0]) > longest_streak:
#                 longest_streak = len(m6[0])
# output_list_0 = sorted(list(contigous_dict[longest_streak]))
# print("#6: %s" % r'/{letter}+/')
# print("%s total matches" % len(output_list_0))
# for word in output_list_0[:5]:
#      print(word)
# print()
     
longest_streak = 0
contigous_dict = dict()
pattern = re.compile(r'(\w)(\1)+')
for word in line_list:
     word_streak = 0
     for i in range(len(word)):
          mini_word = word[i:]
          m6 = re.match(pattern, mini_word)
          if m6:
               length_of_contigousness = len(m6[0])
               if length_of_contigousness > word_streak: 
                    word_streak  = length_of_contigousness
     if word_streak not in contigous_dict.keys():
          contigous_dict[word_streak] = [word,]
     else:
          contigous_dict[word_streak].append(word)
     if word_streak > longest_streak: 
          longest_streak = word_streak                              
output_list_0 = sorted(list(contigous_dict[longest_streak]))
print("#6: %s" % r'/(\w)(\1)+/')
print("%s total matches" % len(output_list_0))
for word in output_list_0[:5]:
     print(word)
print()

#Problem 7
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# most_repetitions = 0
# repetition_dict = dict()
# for letter in alphabet:
#      pattern = re.compile(f"{letter}")
#      for word in line_list:
#           m7 = re.findall(pattern, word)
#           if m7:
#                repetitions = len(m7)
#                if repetitions not in repetition_dict.keys(): 
#                     repetition_dict[repetitions] = set()
#                repetition_dict[repetitions].add(word)
#                if repetitions > most_repetitions:
#                     most_repetitions = repetitions
# output_list = sorted(list(repetition_dict[most_repetitions]))
# print("#7: %s" % r'/{letter}/')
# print("%s total matches" % len(output_list))
# for word in output_list[0:5]:
#      print(word)
# print()

most_repetitions = 0
repetition_dict = dict()
pattern = re.compile(r'(\w)')
for word in line_list:
     word_repetitions = 0
     m7 = re.findall(pattern, word)
     word_breakdown_dict = dict()
     if m7:
          for match in m7: 
               if match[0] not in word_breakdown_dict.keys():
                    word_breakdown_dict[match[0]] = 1
               else: 
                    word_breakdown_dict[match[0]] = word_breakdown_dict[match[0]] + 1
          for key in word_breakdown_dict.keys():
               if word_breakdown_dict[key] > word_repetitions:
                    word_repetitions = word_breakdown_dict[key]
     if word_repetitions not in repetition_dict.keys():
          repetition_dict[word_repetitions] = set()
     repetition_dict[word_repetitions].add(word)
     if word_repetitions > most_repetitions: 
          most_repetitions = word_repetitions
output_list = sorted(list(repetition_dict[most_repetitions]))
print("#7: %s" % r'/(\w)/')
print("%s total matches" % len(output_list))
for word in output_list[0:5]:
     print(word)
print()

#Problem 8
doubles_dict = dict()
for word in line_list:
     max_doubles = 0 
     for i in range(0, len(word)-1):
          two_letter = word[i:i+2]
          m8 = re.findall(f"{two_letter}", word)
          if len(m8) > max_doubles:
               max_doubles = len(m8)
     if max_doubles not in doubles_dict.keys():
          doubles_dict[max_doubles] = list()
     doubles_dict[max_doubles].append(word)
most_doubles = max(doubles_dict.keys())
print("#8: %s" % r'/(\w)(\w)/')
print("%s total matches" % len(doubles_dict[most_doubles]))
for word in doubles_dict[most_doubles][0:5]:
     print(word)
print()

# doubles_dict = dict()
# pattern = re.compile(r'(\w)(\w)')
# for word in line_list:
#      word_doubles = 0
#      m8 = re.findall(pattern, word)
#      doubles_breakdown_dict = dict()
#      if m8:
#           for match in m8: 
#                if match not in doubles_breakdown_dict.keys():
#                     doubles_breakdown_dict[match] = 1
#                else: 
#                     doubles_breakdown_dict[match] = doubles_breakdown_dict[match] + 1
#           for key in doubles_breakdown_dict.keys():
#                if doubles_breakdown_dict[key] > word_doubles:
#                     word_doubles = doubles_breakdown_dict[key]
#      if word_doubles not in doubles_dict.keys():
#           doubles_dict[word_doubles] = list()
#      doubles_dict[word_doubles].append(word)
# most_doubles = max(doubles_dict.keys())
# print("#8: %s" % r'/(\w)(\w)/')
# print("%s total matches" % len(doubles_dict[most_doubles]))
# for word in doubles_dict[most_doubles][0:5]:
#      print(word)
# print()

#Problem 9
most_cosonants = 0
consonant_dict = dict()
pattern = re.compile(r"[bcdfghjklmnpqrstvwxyz]")
for word in line_list:
    m9 = re.findall(pattern, word)
    if m9:
        consonants = len(m9)
        if consonants not in consonant_dict.keys(): 
            consonant_dict[consonants] = set()
        consonant_dict[consonants].add(word)
        if consonants > most_cosonants:
            most_cosonants = consonants
output_list_2 = sorted(list(consonant_dict[most_cosonants]))
print("#9: %s" % r'/[bcdfghjklmnpqrstvwxyz]/')
print("%s total matches" % len(output_list_2))
for word in output_list_2[0:5]:
     print(word)
print()

#Problem 10
longest_length = 0
matchlist_10 = list()
pattern = re.compile(r'(\w)')
for word in line_list:
     is_valid_word = True
     m10 = re.findall(pattern, word)
     count_breakdown = dict()
     if m10: 
          for match in m10:
               if match not in count_breakdown.keys():
                    count_breakdown[match] = 1
               else: 
                    count_breakdown[match] = count_breakdown[match] + 1
          for key in count_breakdown.keys(): 
               if count_breakdown[key] >= 3:
                    is_valid_word = False
     if is_valid_word:
          matchlist_10.append(word)
          if len(word) > longest_length:
               longest_length = len(word)
longest_length_words = list()
for match in matchlist_10:
     if len(match) == longest_length:
          longest_length_words.append(match)
print("#10: %s" % r'/(?:(\w)(?!.*\1))+/')
print("%s total matches" % len(longest_length_words))
for word in longest_length_words[0:5]:
     print(word)
print()

