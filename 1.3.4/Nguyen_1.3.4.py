from __future__ import print_function # use Python 3.0 printing
import random

'''Part 1: Nested if structures and testing'''
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
            
# 1a. The return value result was from line 18
# 1b. food_id('orange') is the input that will cause line 15 or int htis case 16 to be executed;
#     food_id('banana') that will get you line 18; food_id('potato') will execute line 21;
#     food_id('hello') will execute line 22;
# 1c. Line 21 will never report bananas as starchy because bananas are part of the fruits list

def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

# 2. I debugged the code. It has Liid instead of id so I changed it into id

# 3. Code

def f(n):
    '''Code using f(n) function to see if number is an integer, even or odd, and divisible by 6'''
    if int(n) == n:
        if n % 2 == 0:
            if n % 3 == 0:
                return "n is a multiple of 6"
            else:
                return "n is an even number"
        else:
            return "n is an odd number"
    else:
        return "n is not an integer"
        
# 4. The set of test cases that you could use to visit all of the code is a test suite called test-driven design
# 5. Code:

def f_test():
    '''Test Suite for code in #3'''
    works = True
    if f(6) != "n is a multiple of 6":
        works = 'There is a bug in f(n) function'
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

'''Part II: The raw_input() function, type casting, and print() from Python 3'''
# 7. The + sign used in concatenation creates a string with all of the variables and strings concatenated together. 
# The + sign used as numeric addition just adds numbers together, resulting in an integer or float.

# 8a. Line 95 works by using lines 93 and 91 as a template because is a number is not higher or lower, then 
#     it is the exact number. The else line just tells you what will happen if any of the elifs or if happer   

# 8b. 

def guess_once():
    '''Number guessing program with user interaction'''
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess > secret:
        print('Wrong! You guessed too high, my number is ', secret, '.', sep='')
    elif guess < secret:
        print('Wrong! You guessed too low, my number is ', secret, '.', sep='')
    else:
        print("Right On! My number is", guess, end='!\n')
    
# 9. code:

def quiz_decimal(low, high):
    '''Number guessing program with user interaction but using decimals'''
    print('Type a number between', low, 'and', high, ':')
    guess = float(raw_input('Guess: '))
    if guess > high:
        print('Wrong! You guessed too high. ', guess, ' is greater than ', high, '.', sep='')
    elif guess < low:
        print('Wrong! You guessed too low. ', guess, ' is lower than ', low, '.', sep='')
    else:
        print("Right On!", low, '<', guess, '<', high, end='!\n')
    
        
        
# Conclusion 1: The difference between if-structures and glass box testing is that if-structures indentation tells the python
#               interpreter what blocks of code should be skipped under what conditions while the glass box testing tests for 
#               all bugs in your code, checking if there are eny bugs in it.

# Conclusion 2: Nested if-structures several blocks of code are executed, but only 1 block of code might be executed in a normal 
#               if elif else structure.
# Conclusion 3: A test suite uses it's own arguments to see if the code is working properly.
# Conclusion 4: Yes, you make a function for each output case in the flow chart in number 3. Go back to the code in number 3 to see the modifications.

#CHALLENGE

def f_chalenge(n):
    '''Challenge test'''
    works = True
    if f(6) != "n is a multiple of 6":
        works = 'There is a bug in f(n) function'
    if f(2) != "n is an even number":
        works = 'There is a bug in f(n) function'
    if f(3) != "n is an odd number":
        works = 'There is a bug in f(n) function'
    if f(0.01) != "n is not an integer":
        works = 'There is a bug in f(n) function'
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

def not_int(n):
    '''function for not integer'''
    print(n, 'is not an integer')
    
def odd_int(n):
    '''function for odd integer'''
    print(n, "is an odd number")
    
def even_int(n):
    '''function for even integer'''
    print(n, "is an even number")
    
def multiple_six(n):
    '''function is a multiple of six'''
    print(n, "is a multiple of 6")


def f_challenge(n):
    '''Challenge that returns all possible results from the flow chart provided in question 3 from the activity'''
    if int(n) != n:
        not_int(n)
    elif n % 2 != 0:
        odd_int(n)
    elif n % 3 != 0:
        even_int(n)
    else:
        multiple_six(n)
        
#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)
        

# Assignment testing: Everything works perfectly. My results are NOT Citrus, Fruit; All good!; All good!; 
#                     I have a number between 1 and 4.; Then a user interactive Guess: ; Then another user
#                     interactive Guess: ; Then another 2 user interactive Guess: (but with decimals); And 
#                     then it prints All good! 4 times 