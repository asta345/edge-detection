from helper_functions import *

#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = "images/"
imgpath= datafolder + "1.jpg" 
#----------------------------------------STARTER CODE----------------------------------------
#Convert the color image to grayscale and returns the grayscale pixels 
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
#----------------------------------------WRITE YOUR CODE HERE----------------------------------------
# Create a data structure to store updated pixel information
#temp = [0] * numb_colns
new_pixel_values = [[0 for i in range(numb_colns)] for j in range(numb_rows)]
# Define the 3 x 3 mask as a tuple of tuples
mask = ((-1,-1,-1),(-1,8,-1),(-1,-1,-1))
# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list(a,b):
     return [pixel_values[row][b-1:b+2] for row in range (a-1,a+2)]
# Implement a function to flatten a 2D list or a 2D tuple
def flatten(x):
     y = [pixel for row in x for pixel in row]
     return y
# For each of the pixel values, excluding the boundary values
# Create little local 3x3 box using list slicing
# Apply the mask
# Sum all the multiplied values and set the new pixel value
for a in range(1, numb_rows+1):
     for b in range(1, numb_colns+1):
          neighbour_pixels = get_slice_2d_list(a,b)
          neighbour_pixels = flatten(neighbour_pixels)
          mult_result = map(lambda x,y:  x*y, neighbour_pixels, flatten(mask))
          new_pixel_values[a-1][b-1] = sum(list(mult_result))
        #----------------------------------------END YOUR CODE HERE----------------------------------------
# Verify your result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)