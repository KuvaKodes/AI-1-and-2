from PIL import Image
import sys
import math
import ast
import random

def naive_quantization_eight(image_name):
    img = Image.open(image_name)
    width, height = img.size
    new_img = Image.new("RGB", (width, height+80), 0)
    pix = img.load()
    pix2 = new_img.load()
    final_colors = set()
    for x in range(width):
        for y in range(height):
            new_colors = list()
            for color in pix[x,y]: 
                if color < 128: 
                    new_colors.append(0)
                else:
                    new_colors.append(255)
            pix2[x,y] = tuple(new_colors)
            final_colors.add(tuple(new_colors))
    final_colors = list(final_colors)
    for val, color in enumerate(final_colors): 
        for x in range(val * (width//8), (val+1) * (width//8)):
            for y in range(height, new_img.size[1]):
                pix2[x,y] = color
    new_img.show()
    new_img.save("Naive_Eight_RED.png")
    return

def naive_quantization_eight_dither(image_name):
    img = Image.open(image_name)
    width, height = img.size
    new_img = Image.new("RGB", (width, height+80), 0)
    pix = img.load()
    pix2 = new_img.load()
    final_colors = set()
    for x in range(width):
        for y in range(height):
            new_colors = list()
            differences = list()
            for color in pix[x,y]: 
                if color < 128: 
                    new_colors.append(0)
                    differences.append(color - 0)
                else:
                    new_colors.append(255)
                    differences.append(color-255)
            pix2[x,y] = tuple(new_colors)
            #differences = [i ** 2 for i in differences]
            if x + 1 != width: 
                pix[x+1, y] = (pix[x+1, y][0] + (differences[0] * 7//16), pix[x+1, y][1] + (differences[1] * 7//16), pix[x+1, y][2] + (differences[2] * 7//16))
                if y + 1 != height: 
                    pix[x+1, y+1] = (pix[x+1, y+1][0] + (differences[0] * 1//16), pix[x+1, y+1][1] + (differences[1] * 1//16), pix[x+1, y+1][2] + (differences[2] * 1//16))
            if y + 1 != height:
                pix[x, y+1] = (pix[x, y+1][0] + (differences[0] * 5//16), pix[x, y+1][1] + (differences[1] * 5//16), pix[x, y+1][2] + (differences[2] * 5//16))
                if x - 1 != -1:       
                    pix[x-1, y+1] = (pix[x-1, y+1][0] + (differences[0] * 3//16), pix[x-1, y+1][1] + (differences[1] * 3//16), pix[x-1, y+1][2] + (differences[2] * 3//16))
            final_colors.add(tuple(new_colors))
    final_colors = list(final_colors)
    for val, color in enumerate(final_colors): 
        for x in range(val * (width//8), (val+1) * (width//8)):
            for y in range(height, new_img.size[1]):
                pix2[x,y] = color
    new_img.show()
    new_img.save("Naive_Eight_Dithering_RED.png")
    return

def naive_quantization_twenty_seven(image_name):
    img = Image.open(image_name)
    width, height = img.size
    new_img = Image.new("RGB", (width, height+80), 0)
    pix = img.load()
    pix2 = new_img.load()
    final_colors = set()
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
            pix2[x,y] = tuple(new_colors)
            final_colors.add(tuple(new_colors))
    final_colors = list(final_colors)
    for val, color in enumerate(final_colors): 
        for x in range(val * (width//27), (val+1) * (width//27)):
            for y in range(height, new_img.size[1]):
                pix2[x,y] = color
    new_img.show()
    new_img.save("Naive_TwoSeven_RED.png")
    return

def naive_quantization_twenty_seven_dither(image_name):
    img = Image.open(image_name)
    width, height = img.size
    new_img = Image.new("RGB", (width, height+80), 0)
    pix = img.load()
    pix2 = new_img.load()
    final_colors = set()
    for x in range(width):
        for y in range(height):
            new_colors = list()
            differences = list()
            for color in pix[x,y]: 
                if color < (255//3): 
                    new_colors.append(0)
                    differences.append(color-0)
                elif color > (510 // 3):
                    new_colors.append(255)
                    differences.append(color-255)
                else: 
                    new_colors.append(127)
                    differences.append(color-127)
            pix2[x,y] = tuple(new_colors)
            if x + 1 != width: 
                pix[x+1, y] = (pix[x+1, y][0] + (differences[0] * 7//16), pix[x+1, y][1] + (differences[1] * 7//16), pix[x+1, y][2] + (differences[2] * 7//16))
                if y + 1 != height: 
                    pix[x+1, y+1] = (pix[x+1, y+1][0] + (differences[0] * 1//16), pix[x+1, y+1][1] + (differences[1] * 1//16), pix[x+1, y+1][2] + (differences[2] * 1//16))
            if y + 1 != height:
                pix[x, y+1] = (pix[x, y+1][0] + (differences[0] * 5//16), pix[x, y+1][1] + (differences[1] * 5//16), pix[x, y+1][2] + (differences[2] * 5//16))
                if x - 1 != -1:       
                    pix[x-1, y+1] = (pix[x-1, y+1][0] + (differences[0] * 3//16), pix[x-1, y+1][1] + (differences[1] * 3//16), pix[x-1, y+1][2] + (differences[2] * 3//16))
            final_colors.add(tuple(new_colors))
    final_colors = list(final_colors)
    for val, color in enumerate(final_colors): 
        for x in range(val * (width//27), (val+1) * (width//27)):
            for y in range(height, new_img.size[1]):
                pix2[x,y] = color
    new_img.show()
    new_img.save("Naive_TwoSeven_Dither_RED.png")
    return

def k_means(image_name, k): 
    img = Image.open(image_name)
    width, height = img.size
    new_img = Image.new("RGB", (width, height+80), 0)
    pix = img.load()
    pix2 = new_img.load()
    RGB_dict = dict()
    for x in range(width): 
        for y in range(height):
            point = pix[x,y]
            if point not in RGB_dict.keys():
                RGB_dict[point] = 1
            else:
                RGB_dict[point] += 1 
    means = k_plus(list(RGB_dict.keys()), k)
    #means = random.sample(list(RGB_dict.keys()), k)
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
            pix2[x,y] = (round(mean_of_d_min[0]), round(mean_of_d_min[1]), round(mean_of_d_min[2]))
    for val, mean in enumerate(list(curr_dict.keys())): 
        for x in range(val * (width//len(list(curr_dict.keys()))), (val+1) * (width//len(list(curr_dict.keys())))):
            for y in range(height, new_img.size[1]):
                pix2[x,y] = (round(mean[0]), round(mean[1]), round(mean[2]))

    new_img.show()
    new_img.save("kmeansout.png")
    return

def k_plus(data_set, k):
    centroids = random.sample(data_set, 1)
    for remaing_centroids  in range(k-1): 
        dist = dict()
        for point in data_set: 
             d_min = float('inf')
             for current_centroid in centroids: 
                 d_closest_mean = (((point[0]-current_centroid[0])**2) + ((point[1]-current_centroid[1])**2) + ((point[2]-current_centroid[2])**2)) ** 0.5
                 if d_closest_mean < d_min:
                    d_min = d_closest_mean
             dist[d_min] = point
        centroids.append(dist[max(list(dist.keys()))])
    return centroids

def dithering_kmeans(image_name, k):
    img = Image.open(image_name)
    width, height = img.size
    new_img = Image.new("RGB", (width, height+80), 0)
    pix = img.load()
    pix2 = new_img.load()
    RGB_dict = dict()
    for x in range(width): 
        for y in range(height):
            point = pix[x,y]
            if point not in RGB_dict.keys():
                RGB_dict[point] = 1
            else:
                RGB_dict[point] += 1 
    means = k_plus(list(RGB_dict.keys()), k)
    #means = random.sample(list(RGB_dict.keys()), k)
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
    for y in range(height):
        for x in range(width): 
            point = pix[x,y]
            #print(point)
            d_min = 10000000000000000
            mean_of_d_min = None
            for mean in curr_dict.keys(): 
                d_mean = (((point[0]-mean[0])**2) + ((point[1]-mean[1])**2) + ((point[2]-mean[2])**2)) ** 0.5
                if d_mean < d_min:
                    d_min = d_mean
                    mean_of_d_min = mean
            pix2[x,y] = (round(mean_of_d_min[0]), round(mean_of_d_min[1]), round(mean_of_d_min[2]))
            differences = [point[i] - pix2[x,y][i] for i in range(0,3)]
            #print(round(d_min), pix[x+1, y], pix[x+1, y+1], pix[x-1, y+1], pix[x, y+1])
            if x + 1 != width: #
                pix[x+1, y] = (pix[x+1, y][0] + (differences[0] * 7//16), pix[x+1, y][1] + (differences[1] * 7//16), pix[x+1, y][2] + (differences[2] * 7//16))
                if y + 1 != height: 
                    pix[x+1, y+1] = (pix[x+1, y+1][0] + (differences[0] * 1//16), pix[x+1, y+1][1] + (differences[1] * 1//16), pix[x+1, y+1][2] + (differences[2] * 1//16))
            if y + 1 != height:
                pix[x, y+1] = (pix[x, y+1][0] + (differences[0] * 5//16), pix[x, y+1][1] + (differences[1] * 5//16), pix[x, y+1][2] + (differences[2] * 5//16))
                if x - 1 != -1:       
                    pix[x-1, y+1] = (pix[x-1, y+1][0] + (differences[0] * 3//16), pix[x-1, y+1][1] + (differences[1] * 3//16), pix[x-1, y+1][2] + (differences[2] * 3//16))
            #print(round(d_min), pix[x+1, y], pix[x+1, y+1], pix[x-1, y+1], pix[x, y+1])
            #input()
       
    for val, mean in enumerate(list(curr_dict.keys())): 
        for x in range(val * (width//len(list(curr_dict.keys()))), (val+1) * (width//len(list(curr_dict.keys())))):
            for y in range(height, new_img.size[1]):
                pix2[x,y] = (round(mean[0]), round(mean[1]), round(mean[2]))
    new_img.show()
    new_img.save("kmeansout.png")
    return




# naive_quantization_eight("harambe.jpg")
# naive_quantization_eight_dither("harambe.jpg")
# naive_quantization_twenty_seven("harambe.jpg")
# naive_quantization_twenty_seven_dither("harambe.jpg")
#k_means("rodgers.jpeg", 8)
#dithering_kmeans("rodgers.jpeg", 8)
dithering_kmeans(sys.argv[1], ast.literal_eval(sys.argv[2]))