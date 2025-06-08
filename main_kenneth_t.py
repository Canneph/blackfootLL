# Blackfoot Final Project
# Kenneth Tan
# Dec. 4, 2022

import pygame
import cmpt120image
import draw
import random

###############################################################
# Keep this block at the beginning of your code. Do not modify.
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    while env not in "mri":
        print("Environment not recognized, type again.")
        env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the playSound() function below to play sounds. 
# soundfilename does not include the .wav extension, 
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,env):
    if env == "m":
        exec("sounds." + soundfilename + ".play()")
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
    elif env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()

ENV = initEnv()
###############################################################

# Get item names directly from the csv file so that I don't hardcode file names
blackfoot = open("blackfoot.csv")
item_names = []
bf_len = 0
for line in blackfoot:
    item_names.append(line.strip('\n'))
    bf_len += 1

# Show menu to user to choose if they want to Learn, Play, or change Settings
response = ""
learn_difficulty = 3

# Keep the program running so long as the user has not decided to exit
while response != '4':
    # Display the menu and ask for input
    print("\n\nMAIN MENU")
    print("1. Learn - Word Flashcards")
    print("2. Play - Seek and Find Game")
    print("3. Settings - Change Difficulty")
    print("4. Exit\n")

    response = input("Choose an option: ")
    print('')


    # Code for different options of the program:
    # LEARN
    # Show image on random canvas location and play sound of item in order of the csv.
    # Default is 3 items
    if response == '1':
        # For first run of first item, lines 64 and 65
        initialize_window = cmpt120image.getWhiteImage(400,300)
        cmpt120image.showImage(initialize_window)

        # For each item, do the following
        for i in range(learn_difficulty):
            canvas = cmpt120image.getWhiteImage(400,300)
            item = cmpt120image.getImage('images/'+item_names[i]+'.png')
            draw.distributeItems(canvas, item, 1)
            cmpt120image.showImage(canvas)
            playSound(item_names[i],ENV)
            input(str(i + 1) + '.' + " Press enter to continue...")


    # PLAY
    elif response == '2':
        # Display text for user
        print('PLAY')
        print('This is a seek and find game. You will hear a word.')
        print('Count how many of that item you find!\n')
        num_rounds = int(input('How many rounds would you like to play? '))
        
        # Initialize window for first run
        initialize_window = cmpt120image.getWhiteImage(400,300)
        cmpt120image.showImage(initialize_window)
        
        # For loop that controls rounds
        for i in range(num_rounds):
            # Create a list of length 3 for each round
            # that grabs from a random selection from the difficulty list
            # and shuffle its order
            learn_dif_shuffled = item_names[:(learn_difficulty)]
            random.shuffle(learn_dif_shuffled)
            challenge_lst = learn_dif_shuffled[:3]
            
            # Prep canvas for the round
            canvas = cmpt120image.getWhiteImage(400,300)

            # Randomly choose the word of focus for the round
            num_word_of_focus = random.randint(0,2)

            # Choose the correct answer to the number of the WOF
            cor_ans = 0
            
            # For loop that will determine the properties of
            # learn_difficulty number of items to be displayed
            for j in range(3):                
                # Prep items for the round
                # Note: challenge_lst is not being used because of its
                # random order in this case, but because its length is appropriate
                item = cmpt120image.getImage('images/'+challenge_lst[j]+'.png')
                
                # ITEM-UNIQUE PROPERTIES:
                # Decide on the number of items to be displayed
                num_items_display = random.randint(1,4)
                # Grab the number for the WOF:
                if j == num_word_of_focus:
                    cor_ans = num_items_display
                
                # Decide on recolouring
                item_col = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

                # Decide minify, (0 no, 1 yes)
                is_minify = random.randint(0,1)

                # Decide mirror, (0 no, 1 yes)
                is_mirror = random.randint(0,1)
                
                # Apply modifications
                modified_item = draw.recolorImage(item,item_col)
                if is_minify == 1:
                    modified_item = draw.minify(modified_item)
                if is_mirror == 1:
                    modified_item = draw.mirror(modified_item)

                # Draw the item on to the canvas
                draw.distributeItems(canvas, modified_item, num_items_display)

            # What user will experience
            cmpt120image.showImage(canvas)
            playSound(challenge_lst[num_word_of_focus], ENV)
            answer = int(input('Listen to the word. How many of them can you find? '))
            if answer == cor_ans:
                input('Right! Press Enter to continue.\n')
            else:
                input('Sorry, there were ' + str(cor_ans) + '. Press Enter to continue.\n')

            
    # SETTINGS
    elif response == '3':
        print("You are currently learning " + str(learn_difficulty) + " words.")
        user_req_dif = int(input("How many would you like to learn (3-" + str(bf_len) + ")? "))
        if user_req_dif <= bf_len and user_req_dif >= 3:
            learn_difficulty = user_req_dif
        else:
            print("Sorry, that is not a valid number. Resetting to 3 words.")


print("Goodbye!")
    
    

