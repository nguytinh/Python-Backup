from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations
import PIL

# 1-3. N/A

'''Part I: Using Arrays of Pixels'''

# 4. Arrays and lists are similar when it comes to accessing to an element of a 
#    list. The differences are that an array is an actual variable that can hold
#    multiple values at a time while the list is a group of items in brackets. 




# 5. Code:

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman (1).jpg')
filename = os.path.join(directory, 'mask.png')
# Read the image data into an array
img = plt.imread('woman (1).jpg')
img2 = plt.imread('mask.png')

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
###
# Make a rectangle of pixels yellow
###

height = len(img)
width = len(img[0])
for r in range(420, 467):
    for c in range(135, 160):
        if sum(img[r][c])>310: 
            img[r][c]=[0,0,255] # Blue
        
height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
        
        
# Show the image data in a subplot
 
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img2, interpolation='none')
# Saves the figure
fig.savefig('women_and_mask.png')        


# Answers: the image height = the number of rows of pixels = 584px
#  the image width = the number of columns = 960px
#  the green intensity at (5,9) = img[5][9][1] = 94
#  the red intensity at (4,10) = 62
#  the red intensity of the 25th pixel in the 50th row = 79

'''Part II: Manipulating Pixels'''

# 6. *Modified the code above to make a green block cover the green earing*

# 7a. In lines 28 through 31; if the sum of the rows and columns of the image is
#     less than 500, than the pixel turns into magenta
# 7b. I modified the code to make the background purple.
# 7c. I saved it as women_sky_earing.png

# 8. I modified the make_mask.py file to create a different pattern.
# 9. I successfullly put the mask and the woman side by side.

# Conclusion Questions:
# 1.  The data in a digital image contains many arrays. Those arrays carry 
#     certain rgb values that make certain colors. Images are just made up from
#     many small pixels. A digital image is altered when any of it's pixels or 
#     arrays are changed to carry different colors
# 2.  A photograph taken with light-sensitive film can have better quality, 
#     while a photograph taken with a digital camera can have worst quality. 
#     They are the same in many ways, for example they are both made of small 
#     pixels that can carry different rgb values.
# 3a. These 6 bits are of least significance in the image representation because
#     6 bits changing will not even effect the millions or billions of bits that
#     create the actual image, so 6 bits won't really change what a human eye can
#     see in an image.
# 3b. 6 bits are enough to encode 0 to 63 because it stores 4 bits three times, 
#     and 4^3 equals 64 which is in range of 0 to 63 when it comes to indexing.
# 3c.This could make the image look less detailed.
# 4. I think that such an algorithm might acquire this information from the RGB
#    pixel values because it will be able to find areas of color with a lot of 
#    contrast and it will find patterns. It can use those patterns to see if 
#    there are two separate objects. For example, an orange in a black 
#    background, and an apple in a black background. The algorithm can see the 
#    differences in color of the pixels and it can find the two separate 
#    objects.


