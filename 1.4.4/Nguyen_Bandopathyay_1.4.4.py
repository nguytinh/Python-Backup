'''Procedure'''
# 9-12. N/A
# 13. matplotlib.pyplot - A library that is used to create figures, and plots
#     numpy - A library that uses tools to work with arrays. It also provides 
#             many funtions to create arrays.
#     PIL - A library that is used to manipulate or change images by using the 
#     methods and modules that are provided with the library

# 14. N/A

# 15a. Line 19 calls the function subplots() from the matplotlib.pyplot library.
#      The function is being called with 2 arguments: 1 and 2. The function 
#      returns two objects, which are being assigned to fid and ax. 

# 15b. Line 20 calls __imshow()_ on ___ax[0]____
#      Line 23 calls __imshow()_ on ___ax[1]____
#      Line 24 calls set_xticks() on ax[1]
#      Line 25 calls set_xlim(1050, 1400) on ax[1]
#      Line 26 calls set_ylim(1100, 850) on ax[1]
#      Line 27 calls save.fig on ___fig___

# 15c. The (x, y) coordinates of the upper left corner of the bounding box is 
#      (1162, 966). The upper left corner of the bounding box is (1253, 966).

# 16. Upper Left: (707, 942) Upper Right: (791, 942) Lower Left: (707, 1012) 
#     Lower Right: (791, 1012) Width of iris: 84 Length of iris: 70

# 17a. Line 30 uses the join() method from the os.path module. It is being 
#      passed 2 arguments. The value it returns is being assigned to the 
#      variable earth_file.  
# 17b. In line 31 the open() function of the PIL.Image module returns a new 
#      PIL.Image object, which is being assigned to the variable earth_img. 
# 17c. In line 32 the resize() method takes only one argument: a 2-tuple. There 
#      are two sets of parentheses in this line because since the values are the
#      x and y value, they need extra parentheses.
# 17d. The purpose of the (89, 87) argument in line 32 is to resize the earth 
#      image to fit the bounding box of the girl's iris.
# 17e. Line 33 calls the function subplots from the matplotlib.pyplot library 
#      with 2 argument(s): (1, 2). The function returns 2 object(s), 
#      which is/are being assigned to fig2 and axes2.
#      Line 34 calls the method imshow() on the object axes2 
#      with 1 argument: earth_img. 
#      Line 35 calls the method imshow() on the object axes2 with 1 
#      argument: earth_small. 
#      Line 36 calls the method savefig() on the object fig2 with 1 
#      argument: 'resize_earth'. 
# 17f. An additional argument that can be passed to the resize() method is size 
#      or filter = none.
#      The default value of filter is NEAREST
#      The ANITALIAS value of the argument filter is recommended for 
#      downsampling
# 17g. The size attribute gives the recommended size for the image in pixels as 
#      a 2-tuple. Ex. (width, height)
# 17h. After running earthEyes.py again, (479, 475), (89, 87), and 475 was 
#      printed. (479, 475) represents the height and width of the image before 
#      it was shrunk. While (89, 87) represents the the width and height of the
#      image after it has been shrunk.
# 17i. You can tell that the right image has a smaller amount of pixels because 
#      of the plot, and because of how pixelated it looks. The eadges of the
#      earth are not smooth, and you can tell that the pixels are bigger.
# 18. I believe that the algorithm resize() might be using is that it takes a 
#     group of pixels, and then it averages all of the rgb values, and then it
#     turns that group of pixels into one single pixel. For example, it can take
#     9 pixels at a time and it turns those 9 pixels into one single pixel with 
#     the rgb value average of the 9 pixels.
# 19a. There are 3,367,476 bytes in the student_img image.
#      There are 30,972 bytes in the earth_img image.
# 19b. Saveed earth_small.png with the following code in the iPython session.
# 19c. smallEarth.png = 18300 bytes; student.jpg = 206000 bytes
# 19d. In step B, it said that there were about 3.5 million bytes in the image,
#      but when we download the image and then see how large it is, it said that
#      it only had 206,000 bytes.
# 19e. If color is used for the first argument of paste, then it fills the area
#      with one single color rather than pasting the actual image.
# 19f. According to the documentation, if the modes of two images in step 19b 
#      are different from each other, then one image would not have an alpha and
#      the other one will. If both images didn't have an alpha or do have an 
#      alpha at the same time, then they would have the same mode.
# 19g. The earth_small image will be pasted onto the student_img image, 
#      (1162, 966) this will be the size of the image,  mask=earth_small just 
#      makes the variable mask equal to the image earth_small.

# 20. Directions: Add lines of code in the code editor to paste the Earth image 
#     onto the girl’s other iris. Save the new image as earths_as_eyes.png. The 
#     new image should show the full size student image with the close up of the 
#     eyes where the girl now has both eyes with earth images.

# Conclusion #1: The code in this lesson is mainly based off of the Image 
#                Module. Many methods were used, like resize() and paste(), 
#                which contained arguments like image and size. Instances of the
#                Image class have many attributes such as format, mode, size 
#                etc. 
# Conclusion #2: The abstraction I used from the PIL library that helped me 
#                perform this task were the methods from the Image module of the
#                PIL library. For example, I used the paste() method to paste 
#                the resized earth onto the student image picture instead of 
#                coding a complex piece of code. I also used the resize() method
#                to resize the earth image to fit the eyeball of the student, 
#                rather than coding a lot of complex code.