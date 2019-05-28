import random
import time
print '''

 _    _                                            _____                      
| |  | |                                          / ____|                     
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __   | |  __  __ _ _ __ ___   ___
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | | |_ |/ _` | '_ ` _ \ / _ |
| |  | | (_| | | | | (_| | | | | | | (_| | | | | | |__| | (_| | | | | | |  __/
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  \_____|\__,_|_| |_| |_|\___|
                     __/ |                                                    
                    |___/     
                    
      /| ________________
O|===|* >________________>
      \|                    
                     
      '''
def hangman():
    """Function that contains a game of Hangman. There are no parameters, no 
    arguments need to be entered. Many words are contained in a list and one is 
    chosen by random. The user has to guess a letter from that word until the 
    entire word is guessed. You only have 7 lives so guess wisely. The letters 
    that already have been guessed will display. If your input is more than 1 
    letter, not a letter at all, or already guessed, then you have to lose a 
    life and you have to guess a valid guess. If your input is a correct letter, 
    then the hyphen will be replaced by the correct letter. You must guess all 
    of the letters in the word until you run out of tries. When you run out of 
    tries, then you lose. If you guess the word before your tries run out, then 
    you win."""
    
    
    ASCII_ART = [
    '''
         _____
     |/      
     |      
     |      
     |      
     |      
     |
 ____|___
    '''
    ,
    '''
        ______
     |/      |
     |      (_)
     |      
     |      
     |      
     |
 ____|___
    '''
    ,
    '''
        ______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
 ____|___
    '''
    ,
    '''
        ______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
 ____|___
    '''
    ,
    '''
        ______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 ____|___
    '''
    ,
    '''
        ______
     |/      |
     |      (_)
     |      \|/
     |       |
     |     _/ 
     |
 ____|___
    '''
    ,
    '''
         ______
     |/      |
     |      (_)
     |     --|--
     |       |
     |     _/ \_
     |
 ____|___
    '''
    ,
    '''
         ______
     |/      |
     |      (_)
     |    ---|---
     |       |
     |     _/ \_
     |
 ____|___
    '''
    ,
    '''
         ______
     |/      |
     |      (_)
     |     \_|_/
     |       | 
     |     _/ \_
     |
 ____|___
    '''
    ]
    
    
    secret_words = ['MINECRAFT', 'ENDERDRAGON', 'ZOMBIE', 'ANIMAL', 'DIAMONDS', 
                    'HEROBRINE', 'APPLES', 'WOODEN', 'PIG', 'PICKAXE',
                    'GOLD', 'IRON', 'HOUSE', 'SWORD', 'CHICKEN', 
                    'BLOCKS', 'CREEPER', 'ENCHANT', 'WORLD',
                    'NETHERWORLD', 'VILLAGER', 'NOTCH', 'DANTDM', 'FURNACE', 
                    'CRAFTING', 'ENDERMAN', 'ARMOR', 'BUILDING']     
    #The words that the user tries to guess                
    picked_word = random.choice(secret_words)#picks random word from secret_words   
    guessed_letters = [] #holds letters that are already guessed
    hidden_letters = '-' * len(picked_word) #letters are displayed as hyphens
    lives = 0 #number of lives you have
    full_hangman = 9
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    intro = '''Welcome to the game of Hangman! A random word will be chosen.
You have to try to guess the word correctly by inputing letters
If you run out of attempts, then you lose! Remember this game is Minecraft 
Themed'''
              
    print intro
    print ''
    time.sleep(1)
    print 'PLEASE TURN ON CAPSLOCK BEFORE YOU START'
    print ''
    time.sleep(1)
    
    while lives != full_hangman and hidden_letters != picked_word: #holds entire game and 
        #continues running until you lose all lives, or you find all letters
        print ASCII_ART[lives]
        print ''
        print 'Word: ' + hidden_letters
        print 'Characters used: ' + str(guessed_letters)
        guess = raw_input("Guess a letter: ")
        
        while guess in guessed_letters: #while loop that runs when user inputs 
                                        #letter that they already have inputted
            print "Sorry... That letter has already been used"
            guess = raw_input("Guess a letter: ")
        guessed_letters.append(guess)
        
        if guess not in alphabet: #If input is not a letter or 
                                   #more than 1 letter this if statement runs
            print "That is not a valid letter or that is more than 1 letter..."
            print ""
            guess = raw_input("Guess a letter: ")
        
        
        if guess in picked_word: #Runs when the guessed letter is correct
            print "YAY! You guessed correctly!"
            correct = ""
            for char in range(len(picked_word)):
                if guess == picked_word[char]: 
                    correct += guess #empty sting is added to the user's input
                else:
                    correct += hidden_letters[char] 
            hidden_letters = correct #the variable hidden letters now holds the
                                     #user's correct input
        elif guess not in picked_word:
            print "WRONG! Guess again..."
            lives += 1 #you lose a life if you guess wrong
    if "-" not in hidden_letters: #this happens if you win(all hyphens are gone)
        print "CONGRATS! You won! The word was " + picked_word 
        print "YOU ARE A TRUE MINECRAFTER"
    
    elif lives == full_hangman: #you lose
        print "calculating..."
        time.sleep(1)
        print "You can't guess anymore. You Lost. The word was " + picked_word
        time.sleep(2)
        print '''
          _____       
         /  +  \     
         | ~~~ |   
         |R.I.P|   
         |_____|
        '''
    
    play_again = raw_input("Do you want to play again?(YES, NO): ")
    
    if play_again == "YES": #you want to play again, so the function hangman() 
                            #is called
        hangman()
    else: #you don't want to play again, so the game ends
        end_game()
        
def end_game():
    '''No parameters and no arguments needed to be entered. Function is called 
    when user doesn't want to play again. Function simply prints a string'''
    print "The end"
    
hangman()