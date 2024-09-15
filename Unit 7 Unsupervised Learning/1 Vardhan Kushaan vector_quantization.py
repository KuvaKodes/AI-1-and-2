from PIL import Image
import sys
import math
import ast
import random

def naive_quantization_eight(image_name):
    img = Image.open(image_name)
    pix = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            new_colors = list()
            for color in pix[x,y]: 
                if color < 128: 
                    new_colors.append(0)
                else:
                    new_colors.append(255)
            pix[x,y] = tuple(new_colors)
    img.show()
    img.save("Naive_Eight_Blue.png")
    return

def naive_quantization_twenty_seven(image_name):
    img = Image.open(image_name)
    pix = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            new_colors = list()
            for color in pix[x,y]: 
                if color < (255//3): 
                    new_colors.append(0)
                elif color > (510 // 3):
                    new_colors.append(255)
                else: 
                    new_colors.append(127)
            pix[x,y] = tuple(new_colors)
    img.show()
    img.save("Naive_Eight_Twenty_Seven.png")
    return

def k_means(image_name, k): 
    img = Image.open(image_name)
    pix = img.load()
    width, height = img.size
    RGB_dict = dict()
    for x in range(width): 
        for y in range(height):
            point = pix[x,y]
            if point not in RGB_dict.keys():
                RGB_dict[point] = 1
            else:
                RGB_dict[point] += 1 
    means = random.sample(list(RGB_dict.keys()), k)
    prev_dict = dict()
    curr_dict = dict()
    for mean in means: 
        curr_dict[mean] = [mean, ]
    for point in RGB_dict.keys(): 
            d_min = float('inf')
            mean_of_d_min = None
            for mean in curr_dict.keys(): 
                d_mean = (((point[0]-mean[0])**2) + ((point[1]-mean[1])**2) + ((point[2]-mean[2])**2)) ** 0.5
                if d_mean < d_min:
                    d_min = d_mean
                    mean_of_d_min = mean
            for i in range(RGB_dict[point]):
                curr_dict[mean_of_d_min].append(point)
    iteration = 0
    while prev_dict != curr_dict:
        prev_dict = dict()
        for mean in curr_dict.keys():
            prev_dict[mean] = curr_dict[mean].copy()
        curr_dict = dict()
        for mean in prev_dict.keys():
            set_to_average = prev_dict[mean]
            R_sum, G_sum, B_sum = 0, 0, 0
            for vector in set_to_average: 
                R_sum += vector[0]
                G_sum += vector[1]
                B_sum += vector[2]
            new_mean = (R_sum/len(set_to_average), G_sum/len(set_to_average), B_sum/len(set_to_average))
            curr_dict[new_mean] = list()
        for point in RGB_dict.keys():
            d_min = float('inf')
            mean_of_d_min = None
            for mean in curr_dict.keys(): 
                d_mean = (((point[0]-mean[0])**2) + ((point[1]-mean[1])**2) + ((point[2]-mean[2])**2)) ** 0.5
                if d_mean < d_min:
                    d_min = d_mean
                    mean_of_d_min = mean
            for i in range(RGB_dict[point]):
                curr_dict[mean_of_d_min].append(point)
        differences_list = list()
        prev_values = list()
        for mean in prev_dict.keys():
            prev_values.append(len(prev_dict[mean]))
        for ind, mean in enumerate(list(curr_dict.keys())):
            differences_list.append(len(curr_dict[mean]) - prev_values[ind])
        print(iteration, differences_list)
        iteration += 1
    for x in range(width):
        for y in range(height): 
            point = pix[x,y]
            d_min = 10000000000000000
            mean_of_d_min = None
            for mean in curr_dict.keys(): 
                d_mean = (((point[0]-mean[0])**2) + ((point[1]-mean[1])**2) + ((point[2]-mean[2])**2)) ** 0.5
                if d_mean < d_min:
                    d_min = d_mean
                    mean_of_d_min = mean
            pix[x,y] = (round(mean_of_d_min[0]), round(mean_of_d_min[1]), round(mean_of_d_min[2]))
    img.show()
    img.save("kmeansout.png")
    return

#naive_quantization_eight("harambe.jpg")
#naive_quantization_twenty_seven("harambe.jpg")
k_means(sys.argv[1], ast.literal_eval(sys.argv[2]))
