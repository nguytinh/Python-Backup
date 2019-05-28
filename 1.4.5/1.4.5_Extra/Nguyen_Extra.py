from __future__ import print_function
import time
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL as Image
import PIL.ImageDraw            
from PIL import Image, ImageOps 
import numpy 

def border_one(original_image, percent_of_side=.3):
    """ Rounds the corner of a PIL.Image
        original_image must be a PIL.Image
        Returns a new PIL.Image with rounded corners, where
        0 < percent_of_side < 1 is the corner radius as a portion of the shorter 
        dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    border_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(border_mask)
    
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
       # Draw two rectangles to fill interior with opaqueness
    if width >= 300 or height >= 300:   
        drawing_layer.polygon([(0,0),(width, 0),
                                (width, height),(0,height)],
                                fill=(127,0,127,170))
                                
        drawing_layer.polygon([(0,0),(30, 0),
                      (30, height),(0,height)],
                      fill=(0,0,255,0),outline=(0,255,0,1))      
        drawing_layer.polygon([(width, 0),(width-30,0),
                      (width-30, height),(width,height)],
                      fill=(0,0,255,0),outline=(0,255,0,1))     
        drawing_layer.polygon([(0, 0),(width,0),
                      (width,30),(0, 30)],
                      fill=(0,0,255,0),outline=(0,255,0,1))
        drawing_layer.polygon([(0, height),(width,height),
                      (width,height-30),(0, height-30)],
                      fill=(0,0,255,0),outline=(0,255,0,1))       
    
    
        
        
        # Make the new image, starting with all transparent
        result = PIL.Image.new('RGBA', original_image.size, (136,39,16,255))
        result.paste(original_image, (0,0), mask=border_mask)
        
        img = Image.open('ourlogo_test.png')
        logo_small = img.resize((85,93))
        result.paste(logo_small, (width-130,40), mask = logo_small)
        
        return result
        
    elif width <= 300 and height <= 300:
        
        original_image.size = 500, 500
        
        drawing_layer.polygon([(0,0),(width, 0),
                                (width, height),(0,height)],
                                fill=(127,0,127,170))
                                
        drawing_layer.polygon([(0,0),(20, 0),
                      (20, height),(0,height)],
                      fill=(0,0,255,0),outline=(0,255,0,1))      
        drawing_layer.polygon([(width, 0),(width-20,0),
                      (width-20, height),(width,height)],
                      fill=(0,0,255,0),outline=(0,255,0,1))     
        drawing_layer.polygon([(0, 0),(width,0),
                      (width,20),(0, 20)],
                      fill=(0,0,255,0),outline=(0,255,0,1))
        drawing_layer.polygon([(0, height),(width,height),
                      (width,height-30),(0, height-30)],
                      fill=(0,0,255,0),outline=(0,255,0,1))       
    
    
        
        
        # Make the new image, starting with all transparent
        result = PIL.Image.new('RGBA', original_image.size, (136,39,16,255))
        result.paste(original_image, (0,0), mask=border_mask)
        
        img = Image.open('ourlogo_test.png')
        logo_small = img.resize((10,23))
        result.paste(logo_small, (width-130,40), mask = logo_small)
        
        return result
        
        
def multi_border(originalimg, new):
    ''' Module for adding borders to images in folders '''
    
    img = Image.open(originalimg) #opens original image
    #adds border to original
    img_with_border1 = ImageOps.expand(img, border=30, fill='blue')
    img_with_border2 = ImageOps.expand(img_with_border1, border=30,fill='white')
    img_with_border3 = ImageOps.expand(img_with_border2, border=30, fill='red')
    
    return img_with_border3
    
def user_color(original, new):
    '''allows user to change border colors from set options'''
    img = Image.open(original) #opens original image
    #adds border to original
    color = raw_input('What color would you like the border to be?(Prompt \
will appear until all images are have a chosen color.): \n')
    time.sleep(1)
    thic = raw_input('What width would you like the border to be?(Prompt \
will appear until all images are have a chosen width.): \n')
    try:
        img_with_border = ImageOps.expand(img, border=int(thic), fill=str(color))
    except ValueError:
        img_with_border = ImageOps.expand(img, border=30, fill=str("blue"))
    try:
        img_with_border = ImageOps.expand(img, border=int(thic), fill=str(color))
    except TypeError:
        img_with_border = ImageOps.expand(img, border=30, fill=str("blue"))    
    
    
    return img_with_border    
        
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

def usercolorIMG(directory=None):
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
        new_image = user_color(file_list[n],curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    

print('Welcome to the Freshman Cars INC. image modifier!')  
time.sleep(1)
pic_option = raw_input('What modification would you like? grayscale(1), \
border(2), multi border(3), distorted(4) or coolmask(5) *type the numbers that \
correlate with the specific modification*: ')

if pic_option == "1":
    usercolorIMG()