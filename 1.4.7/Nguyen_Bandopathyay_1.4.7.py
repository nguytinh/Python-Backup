from __future__ import print_function
import time
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL.ImageDraw            
from PIL import Image, ImageOps 
import numpy
import ImageDraw

def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs; list of images
    file_list = [] #list of files
    
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
    
############################## Border Modification #############################

def border_one(original_image):
    """There are two parameters, original_image represents the image before it 
    is modified, and percent_of_side is set to .3. There is a border that is 
    made with masks that are transparent so that you can see the brown canvas 
    behind the image. Our logo of the image is then pasted onto the bordered 
    image, and then it is returned"""
    width, height = original_image.size #width and height can now be used as the
                                        #width and height in images.
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    border_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(border_mask)
    
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw four rectangles to make a border that is 30px in the image.
    # The alpha value of the rectangles are low so that you see the brown 
    # canvas, making the image seem like it has a border
    drawing_layer.polygon([(0,0),(width, 0),
                            (width, height),(0,height)],
                            fill=(127,0,127,150))
                            
    drawing_layer.polygon([(0,30),(30, 0),
                  (30, height),(0,height-30)],
                  fill=(0,0,255,0),outline=(0,255,0,1))      
    drawing_layer.polygon([(width, 30),(width-30,0),
                  (width-30, height),(width,height-30)],
                  fill=(0,0,255,0),outline=(0,255,0,1))     
    drawing_layer.polygon([(0, 30),(30,0),
                  (width-30,0),(width, 30)],
                  fill=(0,0,255,0),outline=(0,255,0,1))
    drawing_layer.polygon([(0, height-30),(width,height-30),
                  (width-30,height),(30, height)],
                  fill=(0,0,255,0),outline=(0,255,0,1))
                  
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (136,39,16,255))
    result.paste(original_image, (0,0), mask=border_mask)
    
    drawing_layer = PIL.ImageDraw.Draw(result)
    #Makes transparent triangles in the corners              
    drawing_layer.polygon([(0,0),(30,0),
                  (0,30)],
                  fill=(0,0,255,0))  
    drawing_layer.polygon([(width-30,0),(width,0),
                  (width,30)],
                  fill=(0,0,255,0)) 
    drawing_layer.polygon([(0,height-30),(30,height),
                  (0,height)],
                  fill=(0,0,255,0))
    drawing_layer.polygon([(width,height-30),(width-30,height),
                  (width,height)],
                  fill=(0,0,255,0)) 
                  
    img = Image.open('ourlogo.png') # The logo is opened
    logo_small = img.resize((85,93)) # logo is resized
    result.paste(logo_small, (width-130,40), mask = logo_small) #The logo is 
                                                          #pasted onto the image
    
    return result 
    
def border_oneIMG(directory=None):
    """ Saves a modified version of each image in directory.
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have a border and a pasted image onto 
    it."""
    
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
        
        # Give the images a border and a pasted logo
        curr_image = image_list[n]
        new_image = border_one(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)       
    

############################# Grayscale modification ###########################
    
    
def gray_scale(original, new):
    '''There are two parameters. Original is the original image that has yet to 
    be modified. New is the image after it has been modified. First, we open the
    images that aren't modified yet, and then, we open the logo. We use imageOps 
    to change the image into grayscale and then we paste the logo onto the 
    image. We don't set the logo equal to the mask because we want the logo to 
    have a black background. After the logo is pasted, we return the image with 
    the pasted logo and grayscale'''
    image_file = Image.open(original) # opens image
    img = Image.open('ourlogo.png') # logo is opened
    grayscale = ImageOps.grayscale(image_file) # imageops grayscales it
    
    width, height = grayscale.size
    logo_small = img.resize((78,86))  
    grayscale.paste(logo_small, (width-90,5)) #logo is pasted and resized with a
                                              #black background

    return grayscale
    
def gray_scaledIMG(directory=None):
    """ Saves a modfied version of each image in directory.
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and are grayscaled as well as have a pasted 
    image on them."""
    
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
        
        # Grayscales the image and pastes the logo onto it
        curr_image = image_list[n]
        new_image = gray_scale(file_list[n], curr_image)
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename) 
        

############################# Distorted Modification ###########################   
        
    
def distorted_colored(original, new):
    '''There are two parameters. Original is the original image that has yet to 
    be modified. New is the image after it has been modified. First the image is
    opened, and then, with ImageOps, and assigning variables specific colors, we
    are able to colorize the image into a red and blue image that makes it have 
    some wierd and distorted colors. The red and blue colored image is 
    returned'''
    image_file = Image.open(original) # open colour image
    grayscale = ImageOps.grayscale(image_file) #imageops grayscales it
    BLUE = "#0000FF" #sets variables for the colors blue and red
    RED = "#FF0000"
    distorted_pic = ImageOps.colorize(grayscale, RED, BLUE) #The image is 
                                #colorized to become blue and red using imageops

    return distorted_pic   
    
def distorted_coloredIMG(directory=None):
    """ Saves a modfied version of each image in directory.
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG are recolored as red and blue.
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
        
        # The image is colored to be blue and red to create a cool effect
        curr_image = image_list[n]
        new_image = distorted_colored(file_list[n], curr_image)
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)        
    

########################### Multi-Border Modification ##########################   
    
    
def multi_border(original, new):
    '''There are two parameters. Original is the original image that has yet to 
    be modified. New is the image after it has been modified. First, the 
    function upens the image, and then wit ImageOps, three borders are made by 
    adding a border around the image three times. One is red, one is blue and 
    one is white. Then, the logo image is opened and it is pasted onto the image 
    with three borders after it is resized to a smaller scale. The mask is set 
    to the logo because if it isn't, the png would have a black background'''
    img = Image.open(original) #opens original image
    #adds three borders to the original image with imageops
    img_with_border1 = ImageOps.expand(img, border=30, fill='blue')
    img_with_border2 = ImageOps.expand(img_with_border1, border=30,fill='white')
    img_with_border3 = ImageOps.expand(img_with_border2, border=30, fill='red')
    
    width, height = img_with_border3.size
    #the logo is pasted onto the image and resized
    img = Image.open('ourlogo.png')
    logo_small = img.resize((78,86))
    img_with_border3.paste(logo_small, (width-190,90), mask = logo_small)
    
    return img_with_border3    
        

def multi_borderIMG(directory=None):
    """ Saves a modfied version of each image in directory.
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have three borders as well as a pasted 
    logo/watermark."""
    
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
        
        # Adds three different colored borders around the image
        curr_image = image_list[n]
        new_image = multi_border(file_list[n],curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    
    
########################### Customizable Modification ##########################        
def usercolorIMG(directory=None):
    """There is one parameter which sets the directory to none. Uses current 
    directory if no directory is specified. The code then asks the user what 
    values they want for the color and thickness of the border. Saves a modfied
    version of each image in directory. Places images in subdirectory 
    'modified', creating it if it does not exist. New image files are of type 
    PNG and have a customized border.
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
    
    #raw input used to ask the user what values they want for color and 
    #thickness
    color = raw_input('What color would you like the border to be?: \n')
    thickness = raw_input('What width(in pixels) would you like the border to \
be?: \n')
    print("If any values are invalid, the images will get a default blue and \
30px wide border...")
    time.sleep(1)
    
    # Go through the images and save modified versions
    for n in range(len(image_list)):
        
        print(n)
    
        filename, filetype = os.path.splitext(file_list[n])
        
        curr_image = image_list[n]
        #try and except used for when user inputs an invalid value
        #code makes the actual modifications to the images.
        try:
            img_with_border = ImageOps.expand(curr_image, border=int(thickness)\
            ,fill=str(color))
        except ValueError:
            img_with_border = ImageOps.expand(curr_image, border=int(30),\
            fill=str("blue"))        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        img_with_border.save(new_image_filename)  
        

############################## Intro to our program ############################
        
        
print('Welcome to the Freshman Cars INC. image modifier!')  
time.sleep(1)
pic_option = raw_input('What modification would you like? grayscale(1), \
border(2), multi border(3), distorted(4) or Custom Border(5) (type the numbers \
that correspond with the specific modification): ')

if pic_option == "1": #calls certain functions when the user wants a specific 
                      #modification
    gray_scaledIMG()
elif pic_option == "2":
    border_oneIMG()
elif pic_option == "3":
    multi_borderIMG() 
elif pic_option == "4":
    distorted_coloredIMG()  
elif pic_option == "5":
    usercolorIMG()
else:
    print('Sorry, that is not a valid answer... Please run the code again and \
type in a valid answer') #this is printed when they enter an invalid option
