# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    #Character declarations
    define bg = Character("Bigash Gaadush")
    define vp = Character ("Vor Priol")
    define gp = Character("Graag Pruish")
    
    #Flag declarations
    $ punk_greeting_top_i = False
    $ punk_greeting_top_2 = False
    $ punk_greeting_top_iii = False   
    
    #background declarations
    image bg offi = "office_floor.jpeg"
    image bg cube = "cubicle.jpeg"
    image bg bath = "bathroom.jpeg"
    image bg brk = "break.jpeg"
    image bg janitor = "jan_closet.jpeg"
    image bg boss = "boss_offi.jpg"
    
    image punk neut = "punk.jpg"
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
    scene bg cube
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
    scene bg bath
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
    scene bg boss
    menu:
        "Boss's Office" "The door is locked. Guess like's he's busy"
        
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
    scene bg janitor
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
    scene bg brk
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
    scene bg offi
    show punk neut at right
    jump punk_greeting_a
    
            
#--------------Punk Orc Trees-------------------
label punk_greeting_a:

    $ testflag = True
    menu:
        bg "What are you looking at?"
        
        "You. Is that a problem?":
            $ aff_bg += 2
            jump choice_good_a
            
        "Nothing! Didn't mean to stare. Can I sit down?":
            $ aff_bg += 1
            jump choice_mid_a
            
        "Your heads. Anyone sitting here?":
            jump choice_bad_a

label choice_good_a:
    bg "Of course not-I like your confidence. Have a seat."
    jump punk_greeting_b
    
label choice_mid_a:
    bg "Damn, dude. I was just messing with you."
    bg "You can sit wherever you want."
    jump punk_greeting_b
    
label choice_bad_a:
    bg "No, unfortunately."
    bg "You get right to it, don't you?"
    jump punk_greeting_b

label punk_greeting_b:

    if punk_greeting_top_i and punk_greeting_top_2 and punk_greeting_top_iii:
        jump punk_greeting_end
    
    menu:
        bg "What's up?"
        "How do you like working here?" if punk_greeting_top_i == False:
            $ punk_greeting_top_i = True
            jump punk_greeting_b_1
            
        "What’s Borug like as a boss?" if punk_greeting_top_2 == False:
            $ punk_greeting_top_2 = True
            jump punk_greeting_b_2
            
        "Anyone I should watch out for around the office?" if punk_greeting_top_iii == False:
            $ punk_greeting_top_iii = True
            jump punk_greeting_b_3
            
label punk_greeting_b_1:
    menu:
        bg "It pays the bills. You can’t dismantle the machine on rage and ideals alone."
        "Don’t I know it, sister.":
            $ aff_bg += 2
            bg "Right? Everyone else in this office is such a square. They don’t get it. Glad to know I have a comrade in this hell hole."
            jump punk_greeting_b
            
        "Yeah, but sometimes it seems hopeless.":
            $ aff_bg += 1
            bg "That’s why we have to keep fighting! I felt the same way before I went straight edge. You should try it."
            jump punk_greeting_b
            
        "I guess we all have to grow up sometimes.":
            bg "Are you serious? The moment I grow up is the moment I die. Don’t be such a downer."
            jump punk_greeting_b

label punk_greeting_b_2:
    menu:
        bg "Ugh, what a drone. Don’t get me started. He’s been Second Tower’s bitch since day one, and he takes it out on all of us. The only comfort he has in this world is his stupid coffee."
        
        "It’s shameful. Lone wolves like us shouldn’t have to answer to sheep.":
            $ aff_bg += 2
            bg "Tell me about it! I will NOT be ground into the dust. That’s why us lone wolves need to stick together."
            jump punk_greeting_b
            
        "As we are slaves to Borug, so is he to his vices. I pity him, comrade.":
            $ aff_bg += 1
            bg "I never thought of it that way. Maybe you’re right. It’s sad, isn’t it?"
            jump punk_greeting_b
            
        "Yeah, what a jerk. He can take that coffee and shove it up his orc butt.":
            bg "…I guess? I’m not sure how that would work…"
            jump punk_greeting_b
            
label punk_greeting_b_3:
    menu:
        bg "You mean besides everyone? I guess if I had to pick one, it’d be Graag. Graag Prudish. She’s a huge kiss ass, but there’s something…else. Something very off that I can’t quite put my finger on it. My advice? Keep your distance."
        
        "Why should I trust you?":
            $ aff_bg += 2
            bg "You shouldn’t. No one should trust anyone. Cynicism is a healthy part of a well-balanced breakfast."
            jump punk_greeting_b
            
        "Yikes, I’ll take your word for it.":
            $ aff_bg += 1
            bg "Be careful. Blind trust is how they get you. I could be lying to you right now…I’m kidding. You need to lighten up!"
            jump punk_greeting_b
            
        "Are you sure you’re not just jealous?":
            bg "Ha. As if. How could I be jealous of someone that tightly wound? Don’t blame me if you’re in the splash zone when she snaps"
            jump punk_greeting_b
            
label punk_greeting_end:
    bg "Well, I should probably be getting back to it. Borug’s been on everybody’s ass about the big meeting on Wednesday—I almost threw up in my mouth thinking about it. See you around."
    return
