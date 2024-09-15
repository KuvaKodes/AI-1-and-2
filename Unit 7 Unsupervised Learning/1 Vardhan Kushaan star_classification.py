import sys 
import math
import ast
import random

with open("star_data.csv") as f: 
    line_list = [line.strip().split(',') for line in f]
line_list = line_list[1:]

star_dict = dict()
for line_array in line_list:
    new_array = list()
    for index in range(0,3):
        new_array.append(math.log(ast.literal_eval(line_array[index])))
    new_array.append(ast.literal_eval(line_array[3]))
    new_tuple = tuple(new_array)
    star_dict[new_tuple] = line_array[4]


# initial_dict = dict()


# for mean in means: 
#     initial_dict[mean] = {mean, }
# for input_vector in input_vectors:
#     d_min = 1000000000000
#     mean_of_d_min = None 
#     for mean in means: 
#         d_mean = (((input_vector[0]-mean[0])**2) + ((input_vector[1]-mean[1])**2) + ((input_vector[2]-mean[2])**2) + ((input_vector[3]-mean[3])**2)) ** 0.5 
#         if d_mean < d_min:
#             d_min = d_mean
#             mean_of_d_min = mean
#     initial_dict[mean_of_d_min].add(input_vector)
# new_dict = dict()
# for mean in means: 
#     set_to_average = initial_dict[mean]
#     temp_sum, lum_sum, rad_sum, avm_sum = 0, 0, 0, 0
#     for vector in set_to_average: 
#         temp_sum += vector[0]
#         lum_sum += vector[1]
#         rad_sum += vector[2]
#         avm_sum += vector[3]
#     new_mean = (temp_sum/len(set_to_average), lum_sum/len(set_to_average), rad_sum/len(set_to_average), avm_sum/len(set_to_average))
#     new_dict[new_mean] = {new_mean,}

k = 6
input_vectors = list(star_dict.keys())
means = random.sample(input_vectors, k)
prev_dict = dict()
mean_dict = dict()
for mean in means: 
    mean_dict[mean] = {mean, }
for input_vector in input_vectors:
    d_min = 1000000000000
    mean_of_d_min = None 
    for mean in mean_dict.keys(): 
        d_mean = (((input_vector[0]-mean[0])**2) + ((input_vector[1]-mean[1])**2) + ((input_vector[2]-mean[2])**2) + ((input_vector[3]-mean[3])**2)) ** 0.5 
        if d_mean < d_min:
            d_min = d_mean
            mean_of_d_min = mean
    mean_dict[mean_of_d_min].add(input_vector)

iteration = 0
while prev_dict != mean_dict:
    prev_dict = dict()
    for mean in mean_dict.keys():
        prev_dict[mean] = mean_dict[mean].copy()
    mean_dict = dict()
    for mean in prev_dict.keys():
        set_to_average = prev_dict[mean]
        temp_sum, lum_sum, rad_sum, avm_sum = 0, 0, 0, 0
        for vector in set_to_average: 
            temp_sum += vector[0]
            lum_sum += vector[1]
            rad_sum += vector[2]
            avm_sum += vector[3]
        new_mean = (temp_sum/len(set_to_average), lum_sum/len(set_to_average), rad_sum/len(set_to_average), avm_sum/len(set_to_average))
        mean_dict[new_mean] = set()
    for input_vector in input_vectors:
        d_min = 1000000000000
        mean_of_d_min = None 
        for mean in mean_dict.keys(): 
            d_mean = (((input_vector[0]-mean[0])**2) + ((input_vector[1]-mean[1])**2) + ((input_vector[2]-mean[2])**2) + ((input_vector[3]-mean[3])**2)) ** 0.5 
            if d_mean < d_min:
                d_min = d_mean
                mean_of_d_min = mean
        mean_dict[mean_of_d_min].add(input_vector)
    iteration += 1

for val, key in enumerate(list(mean_dict.keys())):
    list_of_star_types = list()
    for star_vector in mean_dict[key]:
        list_of_star_types.append(star_dict[star_vector])
    print(list_of_star_types)
    print()