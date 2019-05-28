import time
names = raw_input("To start the game, enter your name: ")
def intro():
    '''Intro to Text Adventure Story telling you the name of the game 
    and goal of the game'''
    print "Hello " + names #start of introduction
    time.sleep(1)
    print "Welcome to The Game Of Fortnite" #introduction to the game/explaining 
#                                            how this game works 
    time.sleep(2)
    print "You will soon be trapped on an island with multiple cities and towns"
    time.sleep(2)
    print "there are 99 other players on this island, and you must be..."
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "THE LAST ONE TO SURVIVE!"
    time.sleep(1)
    print "BOOM..."
    time.sleep(1)
    print "BOOOOOOOOOOM..."
    time.sleep(2.5)
    print "Welcome to... The Game of Fortnite" #the name of this game is 
#                                                             "Fortnite"
    time.sleep(1)
    print "*You are spawned on an island*" 
    crossroads()

    
    
def crossroads():
    '''User needs to make their first decision, to go right, left or forward'''
    time.sleep(2)
    print "You are a player named " + names + """ and you are walking through 
the town pleasant park... until you run into a crossroads""" #command to insert 
                               #your username and starting location of this game 
    time.sleep(1)
    way = raw_input('Which direction do you follow?(left, right or straight): ')
    time.sleep(1)
    if (way == "left"):
        left()
    elif (way == "right"):
        right()
    elif (way == "straight"):
        straight()
    else: 
        print "sorry, that was not a valid answer" #if they don't choose left 
#                                           right or straight it is not valid
        crossroads()
  
    
def left(): 
    '''Function is called when the person decides to go left, but leads
    them back to the crossroads again'''
    print "You go left and see a dead end..." #You go left, but have to travel 
                                              #back to where you were before
    time.sleep(1)
    print "you walk back to where you were before"
    time.sleep(1)
    way = raw_input('Which direction do you follow?(left, right or straight): ')
    if (way == "left"):
        left()
    elif (way == "right"):
        right()
    elif (way == "straight"):
        straight()
    else:
        print "sorry, that was not a valid answer" #if they don't choose left 
#                                            right or straight it is not valid
        left()
  

def right():
    '''Function is called when the person decides to go right, and going right
    gives you a different story line than going straight'''
    print "You turn right" #You choose to turn right
    time.sleep(1)
    print "You see a sniper on the floor... "
    time.sleep(1)
    print "*Sniper added to Inventory*" #the first weapon you can achieve if 
                                        #you go right 
    time.sleep(1)
    print "You keep walking the same direction, and you see a PLANE!" 
#   a way of transportation inside the game, the plane leads you to many places 
    plane = raw_input('Do you fly the plane?(yes, no): ')
    if (plane == "yes"):
        fly_plane()
    elif (plane == "no"):
        no_plane()
    else:
        print "sorry, that was not a valid answer"
        right()
        

def no_plane():
    '''Function is called when the person doesn't want to fly the plane. 
    When choosing this, the user ends up dying'''
    time.sleep(1)
    print "You leave the plane alone, but it randomly starts flying towards you" 
#   in order to win the game you MUST get on the plane or else it kills you
    print "*You have been run over by the plane*" #plane kills you
    time.sleep(2)
    print "You killed yourself. You placed 50h place." #tells you what place you 
#                                                       have placed
    ending()    

        
def fly_plane():
    '''Function is called when the user decides to fly the plane into the air'''
    print "You have entered the plane..."
    time.sleep(1)
    print "You start to fly the plane into the air" 
    print "As you keep on flying..."
    time.sleep(1)
    print "and flying..."
    time.sleep(2)
    print "and flying..." #You fly for a long time, not really doing anything
    time.sleep(2)
    print "much time passes, and only 30 people remain"
    time.sleep(1)
    print """As you fly past the city Tilted Towers you finally 
see another player!""" #the plane helps you survive from 20 more people
    time.sleep(2)
    kill = raw_input('Do you try to eliminate the player?(yes, no): ')
    if (kill == "yes"):
        kill_player()
    elif (kill == "no"):
        leave_player()
    else:
        print "sorry, that was not a valid answer"
        fly_plane()


def leave_player():
    '''Function is called when the person doesn't want to fight the player'''
    print "You fly away from the player, but then, your plane explodes..." 
#   you must go and attack the player or else this game will not continue 
    time.sleep(2)
    print "You killed yourself with a plane... You placed 20th place."
#   You die and you lose the game
    time.sleep(2) 
    ending()
    

def kill_player():
    '''Function is called when the user wants to attack the player'''
    time.sleep(1)
    print "You fly towards the player and you run them over with the plane"
    time.sleep(1)
    print "*You have eliminated TSM_Myth*" #This is your first elimination
    time.sleep(2)
    print "As you continue to fly around, you start to get more bored..." #You
#                                                        thirsty for more kills  
    time.sleep(2)
    find = raw_input('Do you try to find more people to eliminate?(yes, no): ')
    if (find == "yes"):
        find_player()
    elif (find == "no"):
        nofind_player()
    else:
        print "sorry, that was not a valid answer"
        kill_player()
    

def find_player():
    '''Function is called when user wants to find a player'''
    print "You see an enemy, so you rush at them with your plane..." #you must 
            #avoid this player to continue on with the game (you must choose no)
    time.sleep(2)
    print "but then... they shoot your plane and it EXPLODES!"
    time.sleep(1)
    print "You have been eliminated by PlaneDestroyer123" #You die here 
    time.sleep(1)
    print "You placed 15th place"
    time.sleep(1)
    ending()
    
    
def nofind_player():    
    '''function is called when the user doesn't want to find a player'''
    print "You see an enemy, but you choose to not engage in any battle"
    time.sleep(1)
    print "You keep on flying around..."
    time.sleep(1)
    print "Much..."
    time.sleep(2)
    print "Much..."
    time.sleep(2)
    print "much!" 
    time.sleep(2)
    print "time passes as you hide in your plane, and only 5 people remain..."
    time.sleep(1)
    print "There is a huge battle in Greasy Groves" 
    time.sleep(1)
    print "but you decide to keep on staying in your plane..."
    time.sleep(1)
    print "more time passes..."
    time.sleep(1)
    time.sleep(2.5)
    print "NOW ONLY ONE PERSON REMAINS!" #You camp around until there is only 
                                         #one person left. Now is your chance to
                                         #win
    time.sleep(1)
    attack = raw_input('You see the last player... Attack him?(yes, no): ')
    if (attack == "yes"):
        attack_player()
    elif (attack == "no"):
        noattack_player()
    else:
        print "sorry, that was not a valid answer"
        nofind_player()
        
        
def noattack_player():
    '''User chooses to not attack the player'''
    print "You don't attack the player..."
    time.sleep(2.5)
    print "your plane weirdly stops working, making you drop to the floor"
    time.sleep(1)
    print "You eliminated yourself" 
    time.sleep(2)
    print "You placed 2nd place... ProPlayer123 WON THE GAME!" #in order to win 
#                               the game you must attack the player and not run 
    time.sleep(1)
    ending()


def attack_player():
    '''User decides to attack the player'''
    print "You pull out your sniper..." #to win you must pull out your gun and 
#                                        attack your final opponent 
    time.sleep(1)
    print "You scope onto the last player..."
    time.sleep(2)
    print "POW!"
    time.sleep(2.5)
    print "..."
    time.sleep(2.5)
    print "..."
    time.sleep(1)
    print "You have eliminated noob902" #You kill the last player remaining
    time.sleep(2)
    print "#1 Victory Royale!!!!" #You finally win the game
    time.sleep(1)
    print names + " has won the game" 
    ending()


def straight():
    '''User chooses to go straight in the crossroads'''
#   Completely different scenario where you turn right
    print "You go straight and encounter a glowing chest..."
    time.sleep(1)
    print "You slowly walk around it and hear a heavenly noise"
    time.sleep(2)
    open = raw_input('Do you open the chest?(yes, no): ') 
#   you find your first chest
    if (open == "yes"):
        open_chest()
    elif (open == "no"):
        leave_chest()
    else:
        print "sorry, that was not a valid answer"
        straight()
        

def leave_chest(): 
    '''User doesn't open the chest and ends up dying as they choose 
    the wrong choice'''
    print "You walk away from the chest" 
    time.sleep(1)
    print "but all of a sudden... you get sniped from a hunting rifle"
#   You die after not opening the chest
    time.sleep(1)
    print "You have been killed by player1234. You placed 67th place"
    time.sleep(1)
    ending()        
        

def open_chest():
    '''User opens the chest and gets weapons to help them continue 
    in the story'''
    print "You open the chest and get mini shields and a golden assault rifle"
#   You get really good loot after opening the chest
    time.sleep(2)
    print "*scar and mini shields added to inventory*"
    time.sleep(1)
    print "You drink the shields and gain 50 shield"
#   You get shield, which is pretty much more health
    time.sleep(1)
    print "You are happy with what you got out of the chest!"
    time.sleep(2)
    dance = raw_input('Do you want to start dancing?(yes, no): ')
    if (dance == "no"):
        no_dance()
    elif (open == "yes"):
        yes_dance()
    else:
        print "sorry, that was not a valid answer"
        open_chest()
       
        
def yes_dance(): 
    '''User decides to dance but then ends up dying because of 
    their obliviousness'''
    print "You start dancing... *harmonizing melody starts playing*" 
    time.sleep(2.5)
    print "but... all of sudden,"
    time.sleep(1)
    print "a player runs up to you and eliminates you with an LMG"
    time.sleep(2)
#   You start to dance, but then you get killed by a player who hates you
    print "You have been killed by I_HATE_" + names + "123"
    time.sleep(2)
    print "You placed 57th place"
    time.sleep(1)
    ending()        
        

def no_dance():
    '''User decides to not dance and continues to live in the story'''
    time.sleep(1)
    print """You don't dance because you know that it might be dangerous 
to dance in the open"""
#   You are wise and make the right decision, making you survive longer
    time.sleep(1)
    print "Time passes..." 
    time.sleep(2)
    print "..."
    time.sleep(2)
    print "..."  # a lot of time passes
    time.sleep(2)
    print "Only 30 players remaining"
    time.sleep(1)
    print "You explore around" 
    time.sleep(1)
    print "You spot a large hill, but people are fighting each other on it."
    time.sleep(1)
    hill = raw_input('Do you go up the hill?(yes, no): ')
    time.sleep(1)
    if (hill == "no"):
        no_hill()
    elif (hill == "yes"):
        yes_hill()
    else:
        print "sorry, that was not a valid answer"
        no_dance()
        
        
def yes_hill():
    '''User decides to climb the hill'''
    time.sleep(1)
    print "You climb up the hill, and you see the players fighting..."
    time.sleep(1)
    print "*Boom* *Bang*"
    time.sleep(2.5)
    print "you slowly approach the players, but then, they kill themselves"
#   As you approach the fighting enemies, they kill each other
    time.sleep(1)
    print """You walk towards the dead bodies , but there is a spike trap on 
    the floor and it kills you"""
#   You walk towards a spike trap which kills you
    time.sleep(2)
    print "You killed yourself" 
    time.sleep(1)
    print "You placed 15th place..." #Shows your placing in the game
    time.sleep(1)
    ending()
    

def no_hill():
    '''User doesn't go on the hill'''
    time.sleep(1)
    print "You stay under the hill..." #You stay under the hill, trying to play
#                                       smart
    time.sleep(1)
    print "but randomly, a player comes out of nowhere and tries to kill YOU!!!"
#   all of a sudden, the enemy attacks you
    time.sleep(1)
    runs = raw_input('Do you "run" away or "shoot" the player?(run, shoot): ')
    time.sleep(1)
    if (runs == "shoot"):
        shoot_player()
    elif (runs == "run"):
        no_shoot()
    else:
        print "sorry, that was not a valid answer"
        no_hill()
        

def no_shoot():
    '''You try to run away but the other player kills you'''
    print "You attempt to run away, but..."
    time.sleep(1)
    print "YOU GET KILLED BY A HEAVY Assault Rifle" #You are eliminated by
#                                                    an extremely strong gun
    time.sleep(1)
    print "You have been killed by NinjaFan123"
    time.sleep(1)
    print "You placed 12th place" #shows you placing in the game
    ending()
    
    
def shoot_player():
    '''User chooses to shoot the other player and eliminates them'''
    print "You start shooting the player with your assault rifle"
    time.sleep(1.5)
    print "POW!" 
    time.sleep(1.5)
    print "BANG!"
    time.sleep(1.5)
    print "ZAP!"
    time.sleep(1.5)
    print "...you eliminate him" #You kill the player
    time.sleep(1)
    print "You have eliminated NinjaFan123, but he has done 100 damage to you"
    time.sleep(1)
    print "You are getting kind of weak" #but you are low on HP or health
    time.sleep(1)
    print """After eliminating the other player, all of their guns 
drop to the floor"""
    time.sleep(1)
    print "There is a legendary heavy shotgun and a legendary pump"
    time.sleep(1)
    winner = raw_input('Pick the "heavy" or "pump" shotgun?(heavy, pump): ')
    if (winner == "heavy"):
        take_heavy()
    elif (winner == "pump"):
        take_pump()
    else:
        print "sorry, that was not a valid answer"
        shoot_player()


def take_heavy():  
    '''User takes the Heavy Shotgun over the pump, leading to different 
    scenario, which is the death scenario'''
    time.sleep(1)
    print "*Heavy shotgun added to inventory*" #you take the heavy shotgun which
#                                               is weaker than the pump
    time.sleep(1)
    print "Time passes..."
    time.sleep(2.5)
    print "Only 7 players remaining" #you are so close to winning the game
    time.sleep(1)
    print "Now that you are safe you go around trying to find somewhere to hide"
    time.sleep(1)
    print "You start scanning the area around to see if there are any enemies"
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "YOU SEE A PLAYER!" 
    scout = raw_input('Do you "attack" them or "leave" them?(attack, leave): ')
    #you have to think carefully, as you try to win the game
    if (scout == "attack"):
        kill_lose()
    elif (scout == "leave"):
        leave_lose()
    else:
        print "sorry, that was not a valid answer"
        take_heavy()
        

def kill_lose():
    '''You attempt to kill other player, but then you lose the game'''
    print """You rush towards the player and try to shoot them with your 
legendary heavy shotgun""" 
    time.sleep(2)
    print "But then... they look at you and *BOOM* snipe you in the face"
#   You are eliminated from a sniper as you play too aggressively
    time.sleep(2)
    print "You have been killed by fortnitegod123" 
    time.sleep(1)
    print "You placed 6th place"
    time.sleep(1)
    ending()
    

def leave_lose():    
    '''You leave the player alone but die and lose the game because
    you were out-skilled'''
    print "You leave the player alone..." #you continue to hide
    time.sleep(2)
    print "But then... they look at you and *BOOM* snipe you in the face"
    time.sleep(1)
    print "You have been killed by fortnitegod123" #you still die
    time.sleep(1)
    print "You placed 5th place"
    time.sleep(1)
    ending()

def take_pump():
    '''User takes the pump shotgun leading into a different scenario'''
    print "*Pump shotgun added to inventory*"
    time.sleep(1)
    print "Time passes..."
    time.sleep(1)
    print "Only 7 players remaining"
    time.sleep(1)
    print "Now that you are safe you go around trying to find somewhere to hide"
    time.sleep(2)
    print "You start scouting the area for enemies around"
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "YOU SEE A PLAYER!" #Instead of having a heavy shotgun you have a pump
    time.sleep(2)
    look = raw_input('Do you "attack" them or "leave" them?(attack, leave): ')
    if (look == "attack"):
        kill_win()
    elif (look == "leave"):
        nokill_lose()
    else:
        print "sorry, that was not a valid answer"
        take_pump()
        
        
def nokill_lose():
    '''You don't kill the other player and lose the game'''
    print "You attempt to run from the player but randomly..." 
    time.sleep(2)
    print "a meteorite rushes down and explodes you into pieces" #A random 
#                      meteorite unfortunately kills you as you run away
    time.sleep(1)
    print "You have been killed by A STRANGE METEOR..." 
    time.sleep(1)
    print "You placed 5th place"
    time.sleep(1)
    ending()
   
   
def kill_win():
    '''User kills the player and gets shield that will help them advance 
    in the game'''
    time.sleep(1)
    print "You rush towards the player and shoot them with you pump shotgun..." 
#   You attempt to kill the other player
    time.sleep(2)
    print "BOP!"
    time.sleep(1)
    print "You dealt 200 damage to them and eliminated them" 
    time.sleep(1)
    print "You have eliminated fortnitegod123" #You killed the player with
#                                               your pump shotgun
    time.sleep(1)
    print "You notice that the player you killed had shield potions"
    time.sleep(2)
    shieldss = raw_input('Do you drink the shield potion?(yes, no): ')
    if (shieldss == "yes"):
        drink_shield()
    elif (shieldss == "no"):
        no_drink()
    else:
        print "sorry, that was not a valid answer"
        kill_win()
        
        
def no_drink():
    '''You don't drink the shield and die to an opponent'''
    time.sleep(1)
    print "You don't drink the shield potions and all of a sudden..."
    time.sleep(2.5)
    print "a player runs up to you and shotguns you in the face"
#    You die because you don't drink the useful shield that is given to you
    time.sleep(1)
    print "You have been killed by ProPlayer123"
    time.sleep(2.5)
    print "You placed 2nd place..." #You placed second place
    time.sleep(1)
    print "ProPlayer123 WON THE GAME!" #The other player won the game
    time.sleep(2)
    ending()


def drink_shield():
    '''You drink the shield potions and you keep on playing the game as you 
    have a higher chance of winning the game'''
    time.sleep(1)
    print "You drink the shield potions and gain more shield"
#   You drink shield which is a smart choice
    time.sleep(2)
    print "..."
    time.sleep(2)
    print "..."
    time.sleep(2)
    print "THERE IS ONLY 1 PLAYER LEFT!" #If you kill this last player you win
    time.sleep(1)
    forthewin = raw_input('Do you want to kill the last player?(yes, no): ')
    if (forthewin == "yes"):
        for_thewin()
    elif (forthewin == "no"):
        not_forthewin()
    else:
        print "sorry, that was not a valid answer"
        drink_shield()


def not_forthewin():
    '''The user chooses keep hiding but then they get killed by an enemy'''
    time.sleep(1)
    print "You keep on hiding..." #You continue to hide, not trying to engage in
#                                 battle
    time.sleep(2.5)
    print "but, the last player sneaks up behind you and kills you with an SMG"
    time.sleep(1)
    print "You have been killed by ProPlayer123"
    time.sleep(1)
    print "You placed 2nd place..." 
    time.sleep(1)
    print "ProPlayer123 WON THE GAME!" #The other player killed you and won 
    time.sleep(2)
    ending()
   
def for_thewin():
    '''User tries to kill the last player and is 
    successful, they win the game'''
    time.sleep(1)
    print "You see the last player and you pull out you assault rifle"
    time.sleep(1)
    print "You shoot at him..." #you decide to kill the last player
    time.sleep(2.5)
    print "one bullet hits..." 
    time.sleep(2.5)
    print "2 bullets hit..." 
    time.sleep(2.5)
    print "the last bullet hits..."
    time.sleep(2)
    print "You have killed ProPlayer123" #You kill the last player
    time.sleep(2)
    print "#1 Victory Royale!!!!" #AND YOU WON THE GAME!
    time.sleep(1)
    print names + " has won the game!"
    time.sleep(1)
    ending()

    
def ending():
    '''Tells user when the game is done, and function is 
    called when game is done'''
    time.sleep(1)
    print "The End"
    
intro()