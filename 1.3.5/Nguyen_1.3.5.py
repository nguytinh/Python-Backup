# 1-4 N/A
# 5. int can represent the number six million but if the number six million has
#    a decimal it can be represented by float. 
#    It would be a str if there are quotation marks around the number. 
# 6. type('tr' + 5) would result in the error because you cannot concatenate a 
#    string and an integer
# 7. In a string the first letter or character is 0. So slogan[0] would be the 
#first character. In this 
#    case M is the first character. That's why slogan[2] is the third character. 
#    slogan[26] is the 27th 
#    character but the string doesn't have a 27th character. slogan[-7] is the 
#    seventh to last character 
#    since slogan[-2] is the second to last character.

# 8. Slicing Code:
slogan = "My school is the best"
sliced_slogan = slogan[-4:]

# 9. Code:
new_slogan = "I am " + slogan[-8:]

# 10a. len(activity) would output 7 because that is how many elements that are 
#      in the variable activity.
# 10b. activity[0 : len(activity)-1] would output 'heater' because 7-1 is 6, and
#      the code outputs 0:6 which is heater.
# 11. The boolean came out true because true goo was part of the actual string.
# 12. Code:


def how_eligible(essay): 
    '''Code that rates your writing seeing if it is eligible or not'''
    
    score = 0
    
    if "?" in essay:
        score += 1

    if '"' in essay:
        score += 1

    if "," in essay:
        score += 1
        
    if "!" in essay:
        score += 1
        
    return score    
    
#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))

#Assignment check: based on my result of 4 for the fisrt print statement and 1 
#                  for the second one, I 
#                  believe that I have successfully completed this assignment