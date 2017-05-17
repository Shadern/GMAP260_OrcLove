# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    #Character declarations
    define bg = Character("Bigash Gaadush")
    define vp = Character ("Vor Priol")
    define gp = Character("Graag Pruish")
    
    #background declarations
    image bg test = "bg test.png"
    
    #sprite declarations

#Rooms are:
#cubicle
#office floor
#boss office
#janitor's closet
#break room
#bathroom

# The game starts here.

label start:
    scene bg room
    python:
        #Affection counter declarations
        aff_bg = 0
        aff_vp = 0
        aff_gp = 0
        
        #Ask the player for thier name
        pcname = renpy.input("What is your name?", length=12)
        pcname = pcname.strip()
        
        #Default if input is blank
        if not pcname:
            pcname = "Borok"


    scene bg test


    jump cube_morn_1
    
#-------------------Morning Day 1 Rooms-----------------------------------
label cube_morn_1:
    menu:
        "Cubicle" "This is your cubicle where you will do work."
        
        "Go to Bathroom":
            jump bthr_morn_1
            
        "Go to Boss's Office":
            jump boss_morn_1
            
        "Go to Janitor's Closet":
            jump jani_morn_1
        
        "Go to Break Room":
            jump brk_morn_1
            
        "Go to Office Floor":
            jump floor_morn_1

label bthr_morn_1:
    menu:
        "Bathroom" "I hope this doesn't need explaining..."
        
        "Go to Cubicle":
            jump cube_morn_1
            
        "Go to Boss's Office":
            jump boss_morn_1
            
        "Go to Janitor's Closet":
            jump jani_morn_1
        
        "Go to Break Room":
            jump brk_morn_1
            
        "Go to Office Floor":
            jump floor_morn_1

label boss_morn_1:
    menu:
        "Boss's Office" "The door is locked. Looks like's he's busy"
        
        "Go to Bathroom":
            jump bthr_morn_1
            
        "Go to Cubicle":
            jump cube_morn_1
            
        "Go to Janitor's Closet":
            jump jani_morn_1
        
        "Go to Break Room":
            jump brk_morn_1
            
        "Go to Office Floor":
            jump floor_morn_1
    
    
label jani_morn_1:
    menu:
        "Janitor's Closet" "Door's shut."
        
        "Go to Bathroom":
            jump bthr_morn_1
            
        "Go to Boss's Office":
            jump boss_morn_1
            
        "Go to Cubicle":
            jump cube_morn_1
        
        "Go to Break Room":
            jump brk_morn_1
            
        "Go to Office Floor":
            jump floor_morn_1
    
    
label brk_morn_1:
    menu:
        "Break Room" "Seems empty for now"
        
        "Go to Bathroom":
            jump bthr_morn_1
            
        "Go to Boss's Office":
            jump boss_morn_1
            
        "Go to Janitor's Closet":
            jump jani_morn_1
        
        "Go to Cubicle":
            jump cube_morn_1
            
        "Go to Office Floor":
            jump floor_morn_1
    
    
label floor_morn_1:
    show eileen happy at right
    jump punk_greeting
    
            
#--------------Punk Orc Trees-------------------
label punk_greeting:
    menu:
        p "What are you looking at?"
        
        "You. Is that a problem?":
            $ aff_bg += 2
            jump choice_good
            
        "Nothing! Didn't mean to stare. Can I sit down?":
            $ aff_bg += 1
            jump choice_mid
            
        "Your heads. Anyone sitting here?":
            jump choice_bad

label choice_good:
    bg "Of course not-I like your confidence. Have a seat."
    jump end_game
    
label choice_mid:
    bg "Damn, dude. I was just messing with you."
    bg "You can sit wherever you want."
    jump end_game
    
label choice_bad:
    bg "No, unfortunately."
    bg "You get right to it, don't you?"
    jump end_game
    
label end_game:
    bg "I have to go though. See you around the office."
    return
