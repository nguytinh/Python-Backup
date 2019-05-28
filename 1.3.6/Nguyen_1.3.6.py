import random
# 1-3. N?A
'''Part I: Tuples, Syntax'''
# 4. (3,7,0,1,3) is another tuple
# 5. Mr. Brown kind of has a convention rule for indentatio in HTML even though 
#    you don't actually have to indent.
#    Mr. Brown does have a convention for us to follow in python where we have 
#    to have our answers in a certain format
# 6a. the output is 'a' because the 'a' is in the number 0 index. the second 
#     output is 3 because 3 is in the number 2 index.
#     some_values[1] would output 'b' because 'b' is in the number 1 index.
# 6b. the output will be ('a', 'b') because it was sliced from 0:2 which means 
#     that it includes the 0 and 1 index but not the 2 index
# 7. I predict that if you type b as an input, (9, 10, 11) will be the output 
#    because a is equal to 10
a = 10
b = (9, a, 11)

'''Part II: Lists '''
# 8. I predict that the output will be ['b', 3] because [1:] means that it will 
#    output the 1 index and every index after.
values = ['a', 'b', 3]
# values[1:]
# 9. The output is false because values[2] is equal to the string '3' not the integer 3.
values[2] = '3' # Note the quotes!
values[2] == 3
# 10a. The output will be ['a', 'b', 3, 4, 5] because the code adds [4, 5] onto 
#      the current list containing ['a', 'b', 3]
# 10b. The output will be ['a', 'b', 3, 4, 5, [6, 7]] because the code appends 
#      [6, 7] onto the end of the list, and there
#      are still brakets because you append it not add
# 11. values = values + 5 will not work because values is a list not an intger. 
#     If you wanted to add 5 into the list you 
#     have to change 5 to [5]
# 12. The output of a is 18 because *= multiplies a with 3.
a = 6
a *= 3

'''Part III: Lists and the random module '''
# 13. Imported the random module
#random.choice(values) # choose from a list
#random.randint(5,8) # choose int from [5,6,7,8]
#random.uniform(5,8) # choose float between 5 and 8

# 14. Code:
def roll_two_dice():
    return random.randint(1,12)
    
# Conclusion 1. The differences are that variable a is a string, the variable b 
#               is a tuple, and the variable c is a list of characters.
# Conclusion 2. Computer programming languages almost always have a variety of 
#                variable types so that there is more flexibility in the
#               programming language. If you could only use integers, then how 
#               will you be able to assign text or strings to a variable?
#               Not everything can be represented by an integer because making 
#            a game or program doesn't just need numbers, you need text as well.
# Conclusion 3. Summary of 1.3.2 - 1.3.6: Python is a programming language with 
#                 a variety of tools. Functions are one of them, they help you 
#                 shorten, simplify, and make your program better. Booleans and 
#               arithmetics are also very important in python and are essential 
#               to programming. If else statements are also useful to help you 
#            create programs with multiple outcomes. Strings, tuples, and lists
#               are important when incorporating any type of character into your 
#                 code and assigning values to variables. These are the things 
#               that I learned about from 1.3.2 to 1.3.6

#1.3.6 Function Test
print(roll_two_dice())