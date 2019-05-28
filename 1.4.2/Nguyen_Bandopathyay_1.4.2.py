# 1-3. N/A
'''Part I: Working with a Filesystem'''
# 4. The absolute filename of nice.jpg is C:/Users/Student login/Desktop/nice.jpg
# 5. The  admin/../Users/Student login/Desktop/nice.jpg
# 6. When you use pwd the file and C:\\Windows\\Cursors\\cursor1.png is returned
# it is an absolute filename because it doesn't have the special symbol .. 
# You have to be in a particular working directory for this filename to make 
# sense, and it is the C: directory. These commands are different than the ones 
# in Cloud 9 because back slashes are being used than a normal slash.
# 7. One Subplot
# The 1st example of code didn't work at all. There was a display error.
# But, the modified code below worked. If I didn't refresh the terminal, then 
# the code would have still not worked

# 7a. The coordinate pair of the her nose is (300, 400).
# 7b. *Modify the code to show cat* The coordinate pair of the cat's nose 
#     is (60, 40).

'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 1)
# Show the image data in the first subplot
ax.imshow(img, interpolation='none') # Override the default
ax.plot(36, 47, 'ro')
ax.plot(117, 43, 'ro')
ax.plot(140, 43, 'ro')

# Show the figure on the screen
# fig.show()
fig.savefig('crazy_mice')


'''Part III: Objects and Methods'''

# 8a. fig is an instance of the class Figure which is an instance of the class 
# figure which is an instance of the module matplotlib.  
# ax is an instance of the class AxesSubplot which is an instance of the class 
# axes which is an instance of the module matplotlib

# 8b. Similarly, in line 25, the method savefig is being called on the object 
# fig. That method is being given two arguments. That method is a method of the 
# class Figure.

# 8c. The comments on line 11 explains the code in line 12. The comments on line
#     13 explains the code in line 14. The comments on line 15 explains the code
#     in line 16. The comments on line 19 explains the code in line 20. The 
#     comments on line 21 explains the code in line 22. The comments on line 23 
#     and 24 explains the code in line 25.    

'''Part IV: Arrays of Objects'''
# 9a. The method imshow is being called on the object ax
# 9b. I made 5 cats and 2 women from the image of 1 cat and 1 woman by modifying
#     the code. 

'''Part V: Keyword = Value Pairs'''
# 10. There is interpolation in the second image but there isn't interpolation 
#     in the first image, so the interpolation argument makes the pixels merge. 

# 11a. I modified the code with methods from the chart.
# 11b. I used the methods above to create three close-ups of an image in a 
#      single Figure.

# 12. One additional method of an AxesSubplot is the step() method. One of the 
#     optional arguments in that method is data. Its' default value is none.

# 13. I marked the eyes of the mice with red circles using plot(). I saved it as 
#     crazy_mice.png

#Conclusion 1: A relative filename is one where the file location starts at the 
#              current working directory. It doesn’t start with the root / or  
#              C:\ while an absolute filename does start with the root / or C:\.
#Conclusion 2: An object is an instance of a class, for example, the object fig 
#              is an instance of the class Figure which is an instance of the 
#              class figure. 
#Conclusion 3: A method is a function that can be called, and is part of an 
#              object. Properties are variables with specific values and is a 
#              part of an object. 
#Conclusion 4: When you call a method on an object then the method gets executed 
#              based on it’s code. The object also gets modified depending on 
#              what the code does.
