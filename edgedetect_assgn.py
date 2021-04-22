from helper_functions import *

#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = "C:/Users/spj/workspace-python/teaching-material/assgn1code/images/"
imgpath = datafolder + "1.jpg" 
#----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to grayscale and returns the grayscale pixels 
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
#----------------------------------------WRITE YOUR CODE HERE----------------------------------------
# Create a data structure to store updated pixel information
temp = [0] * numb_colns
new_pixel_values = [temp] * numb_rows
# Define the 3 x 3 mask as a tuple of tuples
mask = [[0,0,0], [0,1,0], [0,0,0]]

# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list():
    return []

# Implement a function to flatten a 2D list or a 2D tuple
def flatten():
    return []

# For each of the pixel values, excluding the boundary values
    # Create little local 3x3 box using list slicing
    neighbour_pixels = get_slice_2d_list()
    # Apply the mask
    mult_result = map(None, None, None)        
    # Sum all the multiplied values and set the new pixel value
#        
#----------------------------------------END YOUR CODE HERE----------------------------------------
# Verify your result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)