from __future__ import print_function
import matplotlib
matplotlib.use('')
import matplotlib.pyplot as plt
import random
# 1-3. N/A
# 4. Code:
def days():
    ''' for loop that tells what day in september it is from a range of 5 and 8
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')

# 5. Code:
def picks():
    '''Function that makes a histogram'''
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('1.3.7/picks')
    
# 6a. Code:
def roll_hundred_pair():
    '''Function that produces a histogram of the results of 100 rolls of two 
    6-sided dice'''
    individual_roll = [] 
    for choices in range(101):
        individual_roll += [random.choice([1, 2, 3, 4, 5, 6]) + \
        random.choice([1, 2, 3, 4, 5, 6])]

    plt.hist(individual_roll)
    plt.savefig('1.3.7/dice')
    
# 6b. Code:
def dice(n):
    '''Function that returns the sum of a random roll of n 6-sided dice'''
    total = 0
    for i in range(0,n):
        total += random.randint(1, 6)
    print (total)

# 7. Line 55 is necessary because without it, any line with the variable guess 
#    will not work. If you change the 1 to an a, then the code will break as well. 
def validate():
    '''Function that tells you if theletter you type is in the string 
    hangman word'''
    guess = '1' # initialization with a bad guess
    answer = ('hangman word')
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')

# 8. Code:

def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''Function that tells you to guess who won the lottery
    If you don't guess right, you have to guess again. If you guess right,
    tells you that you have guessed right, and then tells you how many 
    tries it took
    '''
    winner = random.choice(players) 

    ####
    # Prints raw_input and then prints the names of contestants
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # p are the people in the list and end is
                                       # used to put a spaces in the names.
        print(p+', ', end='')
    print(players[len(players)-1]) # The input is on the next line

    ####
    # If the answer isn't correct, you have to guesss again but if you got 
    #it correct, then it tells you how many guesses it took you
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    

# 9. Code:
def goguess():
    '''You guess a number from 1 to 20. This function tells you if you 
    answered too high or low'''
    print ("I have a number between 1 and 20 inclusive.")
    num = str(random.randint(1,20))
    guess_num = raw_input("Guess: ")
    tries = 1
    while guess_num not in num:
        if guess_num > num:
            print (guess_num, 'is too high')
            tries += 1
            guess_num = raw_input('Guess: ')
        else:
            print (guess_num, 'is too low')
            tries += 1
            guess_num = raw_input('Guess: ')
    print ('Right! My number is',guess_num,'! You guessed in',tries,'tries')
    return tries

# 10. If you are extremely unluck, then it will take you at most 6000 tries to 
#     get the answer correct, but if you are extremely luck, then you would be 
#     able to get the right answer in at least 1 try     

# 11a. Code:
def matches(ticket, winners):
    '''Funtion that tells you what numbers are in common between 2 lists'''
    match = 0
    for n in winners:
        if n in ticket:
            match += 1
    return match

# 11b. Code:
def report(guess, secret):
    '''Function that takes two lists and tells you what is out of place in the
    second list compared to the first list, and what is in place'''
    in_place = 0
    out_place = 0
    index = 0
    for n in guess:
        if n == secret[index]:
            in_place += 1
        elif n in secret and not guess.index(n) == secret.index(n):
            out_place += 1
        index += 1
    return [in_place, out_place]

    
# Conclusion #1: The disadvantages of developing a program this way is that your
#                code becomes much longer than it is, and also things are less 
#                organized.
# Conclusion #2: The relationship between an iteration and analysis of a large 
#                set of data is that an iteration iterates over the code while 
#                the analysis compares the information or looks for what has 
#                to be executed
# Conclusion #3: A while loop work with conditionals, where if the conditional 
#                is true, then it runs, but a for loop doesn't need a 
#                conditional to run
# Conclusion #4: My partner and I didn't work together very well in this 
#                assignment. We worked together on the first few problems, but 
#                after that, we didn't have too much time to work on it 
#                together, mainly because of the 3 day weekend. We could have 
#                definately had better communication, and we could have improved 
#                it by working on this assignment at each other's house. Our 
#                strengths were that we could logically explain how to make 
#                functions together. 

#1.3.7 Function Test
print (days())
print (dice(4))
print (validate())
print (guess_winner())
print (goguess())
print (matches([11, 12, 13, 14, 15], [3, 8, 12, 13, 17]))
guess = ['red','red','red','green','yellow']
secret = ['red','red','yellow','yellow','black']
print (report(guess, secret))

# Based on my results, I believe that I have done this assignment successfully



    