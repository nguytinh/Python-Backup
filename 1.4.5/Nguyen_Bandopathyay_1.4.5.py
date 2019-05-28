'''Procedure'''
# 1-4. N/A

# 5. The 3 functions:
#    round_corners_one_image()
#    get_images()
#    round_corners_of_all_images()

# 6. The images were copied into the modified folder and then the corners were 
#    rounded. Also, when running this file in ipython, it outputted numbers 
#    until 40.

# 7a. Each argument is an instance variable of PIL. result is the returned 
#     variable. Argument 1: original_image; Argument 2: percent_of_side=.3; 
#     Return Value: result
# 7b. The color in line 26 is purple.
# 7c. Object created in line 26: rounded_mask
#     Object created in line 27: drawing_layer
# 7d. The alpha value that we would want in the corners of the images would be 
#     255, since we want the corners to be completely transparent.
# 7e. Lines 33-38 give you the second image, lines 40-48 give you the second 
#     image.
# 7f. The color on line 54 is black.
# 7g. The color values in the corners are the colors of the corners of the 
#     image, but technically it is no color because it is transparent with an 
#     alpha value of 0.

# 8a. Because a default value is specified for directory, that argument is 
#     optional, so get_images() can be passed either 1 or 2 arguments.
# 8b. There are two objects being returned in the function get_images(). Those 
#     objects are tuples. 
# 8c. The three calls to the os module used in the code are the three functions 
#     below:
#     os.getcwd() 
#     os.listdir()
#     os.path.join() 
# 8d. os.getcwd() - Return a string representing the current working directory.
#     os.listdir() - Return a list containing the names of the entries in the 
#     directory given by path. The list is in arbitrary order, and does not 
#     include the special entries '.' and '..' even if they are present in the
#     directory.
#     os.path.join() - Join one or more path components intelligently.
# 8e. This program uses a try-except structure to open all images in a directory
#     so that errors are caught easier and so that the program isn't halted. 
#     Some of the advantages/disadvantages of using a try-except structure are 
#     that if the error doesn't match the except statement, then the program 
#     will still be halted. The advantage of using a try-except structure is 
#     that if there is an actual error, then you are able to easily figure out 
#     the error when the except statement is executed.
# 8f. On line 80, if the error in the try statement is an IOError, then "pass" 
#     which pretty much just does nothing. The except statement can only be 
#     called if the error matches, else, the program is halted. Also if there is
#     no error, then the except statement isn't called.
# 9a. I think that this function call needed to be embedded in a try-except 
#     structure just incase the directory already existed, so that if the 
#     directory.
# 9b. In line 106 len(image_list) represents the number of rows in the image.
# 9c. The role being played by n in lines 106, 108,, 109 and 112 are the pixels 
#     of the image.

# Conclusion 1: Seeing through the desktop behind the irregular edges of the 
#               icons are accomplished by modifying the icons so that certain 
#               areas that they want transparent have an alpha value of zero.
# Conclusion 2: I think that dividing the code into three functions made the 
#               code reuse easier because if it executed all of these functions
#               in one single function, then the code would take longer to 
#               finish running, especially if you have a lot of complex 
#               modifications. 
# Conclusion 3: The term modified image can be different for everyone. It just 
#               depends on how you define an original image. For example, if an 
#               image of Ronald Reagan is the "original" one, then if you 
#               manipulate it by resizing, drawing, or pasting something, than 
#               it can be considered as a manipulated image. This is my 
#               understanding of what a manipulated image is, but I would agree 
#               more with Alice because every image is technically a manipulated 
#               image. When you take a picture with a camera, there is a bunch 
#               of code being executed in order for you to have the picture 
#               taken which is in a way manipulating the image.
# Conclusion 4: Under any circumstance is an image yours to use unless the image 
#               was stolen and/or private to a specific person. You can 
#               distribute and sell images under any circumstances unless it is 
#               illegal. You can download or take any pictures you want as long 
#               as it is not illegal, and if it is illegal, then you will get in
#               trouble.
# Conclusion 5: My partner Ayush, and I are always on task in class, constantly 
#               trying our best on assignments, helping each other when needed 
#               and sharing ideas with each other until we agree on one. We can 
#               improve on staying on the same question so that we can get more 
#               detailed and defined answers. The thing we can do to improve, is
#               to get better communication in class, out of class, and even on 
#               weekends, by getting each others phone numbers and knowing each 
#               others schedules.

from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw            

def round_corners_one_image(original_image, percent_of_side=.3):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))
                         
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def round_corners_of_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = round_corners_one_image(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    
  
round_corners_of_all_images()