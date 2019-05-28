from __future__ import print_function # use Python 3.0 printing
'''Procedure'''
# 1-5 N/A
'''Part 1: Conditionals'''
# 6a. Prediction: I think that the output would be True.
# My prediciton was correct.

# 6b. Prediction: I think that the output will be True.
# My prediction was correct again.

# 7. I made a compound conditional in Ipython
# 8. I made another compound conditional in Ipython with different values.
'''Part 2: If-else Structures and the print() Function!!!'''

# 9a. Predictions: If you type age_limit_output(10), then it will print 10 is below the age limit. 
#If you type age_limit_output(16), then it will print 16 is old enough.
def age_limit_output(age):
    '''Step 9a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT) 

# 9b 
def report_grade(percent): 
    '''Step 9b if-else'''
    MASTERY = 90 
    if percent < MASTERY:
        print(' A grade of ', percent, ' does not indicate mastery ')
    else:
        print(' A grade of ', percent, ' does indicate mastery ')
    print('Keep up the good work!')
     
'''Part 3. The in operator and an introduction to collections'''
# 10 prediction: the "in" element just tells you if the letter,float, or integer is in the string or list. 
#If you do 3 in [1,2,3] it will be true, but '3' in [1,2,3] will be false 

# 11 code
def letter_in_word(guess, word):
    '''Step 11 using the in operator'''
    if guess in word:
        return True
    else:
        return False

# 12 code    
def hint(color, secret):
    '''Step 12 code using lists and functions'''
    if color in secret:
        print(' The color ', color, ' IS in the sequence of colors ')
    else:
        print(' The color ', color, ' IS NOT in the sequence of colors ')

# Conclusion 1: Anything indented once after the if, elif, or else statement 
#               will be a part of that statement.
# Conclusion 2: The operator that I learned about that can be used to create Boolean expressions 
#               is the in operator. An operator online that can be used to create a Boolean expression is , 
#               the not in operator and the is operator. 
# Conclusion 3: I think that Ira's answer is somewhere in between because she is right about the print 
#               statement happening no matter what, but she is wrong about the part that the program will run slower. 
#               I think that Jayla is correct because since the piece of code is printing the same thing no matter what,
#               because when editing one of the print staetments, you will have to edit the other one too which will 
#               take more time. I believe that Kendra is right as well, because the print statement will print no matter what, 
#               and the 2 statements will take up more memory than only 1 print statement.

#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)

# Assignment Check: My result was:  10 is below the age limit. Minimum age is  13 16 is old enough. 
#                                   Minimum age is  13 A grade of  79  does not indicate mastery Keep up the good work! A grade of  
#                                   85 does not indicate mastery Keep up the good work! True The color  red  IS in the sequence of colors 
# Based on my result I think that I have successfully completed the assignment.