from PIL import Image
from matplotlib import image as im
import numpy as np
import math
import cv2
import sys


image = cv2.imread(sys.argv[1])
image = cv2.resize(image,(350,120),interpolation=cv2.INTER_AREA)



print("Successfully Loaded Image!")
print(f"Image size: {image.shape[1]} x {image.shape[0]}")

print(image.shape)
brightness_matrix = np.zeros((image.shape[0],image.shape[1]))

for row in range(image.shape[0]):
    for col in range(image.shape[1]):
        average_value = np.sum(image[row][col])// 3
        brightness_matrix[row][col] = average_value


ascii_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


ascii_string_length = len(ascii_string)


amount_of_brightness_values_per_pixel = math.ceil(255/ascii_string_length)


mapping = {i: ascii_string[i//amount_of_brightness_values_per_pixel] for i in range(0,257,amount_of_brightness_values_per_pixel)}

values = []
for row in range(brightness_matrix.shape[0]):
    r= []
    for col in range(brightness_matrix.shape[1]):
        r.append(mapping[brightness_matrix[row][col]//amount_of_brightness_values_per_pixel * amount_of_brightness_values_per_pixel])

    values.append(r)


for row in values:
    print(''.join(row))










