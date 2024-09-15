import sys
import math

with open(sys.argv[1]) as f:
    line_list = [line.strip().split(',') for line in f]

feature_dict = dict()
for index, feature in enumerate(line_list[0]):
    feature_dict[feature] = list()
    for vector in line_list[1:]:
        feature_dict[feature].append(vector[index])


decision_tree = dict()

def start_entropy(input):
    starting_entropy = 0
    output_occurence_dict = dict()
    for decision in input:
        if decision not in output_occurence_dict.keys():
            output_occurence_dict[decision] = 0
        output_occurence_dict[decision] += 1
    total_possibiliites = sum(list(output_occurence_dict.values()))
    for decision, occurences in output_occurence_dict.items(): 
        starting_entropy += (occurences/total_possibiliites) * math.log((occurences/total_possibiliites), 2)
    return -1 * starting_entropy

def calc_data_entropy(feature_vector, output_vector):
    entropy = 0
    total_options = len(feature_vector)
    occurence_dict = dict()
    outcome_dict = dict()
    for i, val in enumerate(feature_vector):
        if val not in occurence_dict.keys():
            occurence_dict[val] = 0
        occurence_dict[val] += 1
        if val not in outcome_dict.keys():
            outcome_dict[val] = dict()
        outcome = output_vector[i]
        if outcome not in outcome_dict[val].keys():
            outcome_dict[val][outcome] = 0
        outcome_dict[val][outcome] += 1
    for possibility, occurences in occurence_dict.items():
        decision_odds = (occurences/total_options)
        sub_entropy = 0
        sub_total_options = sum(list(outcome_dict[possibility].values()))
        for outcome, count in outcome_dict[possibility].items():
            sub_entropy += (count/sub_total_options) * math.log((count/sub_total_options), 2)
        entropy += (decision_odds * (sub_entropy * -1))
    return entropy

# print(start_entropy(feature_dict["Play?"]))
#print(calc_data_entropy(feature_dict["Play?"], feature_dict["Play?"]))
#print(start_entropy(feature_dict["Play?"])-calc_data_entropy(feature_dict["Play?"], feature_dict["Play?"]))

def split_dataset(dataset, feature):
    list_of_splits = list()
    values = set()
    for value in dataset[feature]:
        values.add(value)
    for value in values: 
        split_dict = dict()
        for key in dataset.keys():
            split_dict[key] = list()
        for index, possibility in enumerate(dataset[feature]):
            if value == possibility:
                for key in split_dict.keys():
                    split_dict[key].append(dataset[key][index])
        list_of_splits.append(split_dict)
    return list_of_splits

#print(split_dataset(feature_dict, "Outlook"))


def dtify(input, final_tree):
    outcome_feature = list(input.keys())[-1]
    outcome_vector = input[list(input.keys())[-1]]
    starting_entropy = start_entropy(outcome_vector)
    if starting_entropy == 0: 
        return outcome_vector[0]
    best_feature = None
    max_gain = 0
    for feature, values in input.items():
        if feature == outcome_feature:
            break
        info_gain = starting_entropy - calc_data_entropy(values, outcome_vector)
        if info_gain > max_gain:
            best_feature = feature
            max_gain = info_gain
    final_tree[best_feature] = dict()
    split_sets = split_dataset(input, best_feature)
    for split_set in split_sets:
        best_feature_option = split_set[best_feature][0]
        final_tree[best_feature][best_feature_option] = dict()
        final_tree[best_feature][best_feature_option] = dtify(split_set, final_tree[best_feature][best_feature_option])
    return final_tree

def format(input, depth):
    for key, value in input.items():
        f.write(("\t" * depth) + " * " + str(key))
        if type(value) != dict: 
            f.write(" - - > " + str(value +  "\n"))
        else: f.write("\n"); format(value, depth + 1)

with open("treeout.txt", "w+") as f: format(dtify(feature_dict, dict()), 0)
