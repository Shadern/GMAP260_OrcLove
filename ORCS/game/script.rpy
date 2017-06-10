# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    #Character declarations
    define bg = Character("Bigash Gaadush", image="punk")
    define vp = Character ("Vor Priol", image="manic")
    define gp = Character("Graag Prudish", image="prude")
    define boss = Character ("Mr. Borog", image="boss")
    

    #Flag declarations
    $ punk_greeting_top_i = False
    $ punk_greeting_top_ii = False
    $ punk_greeting_top_iii = False

    #$ punk_wed_top_i = False
    #$ punk_wed_top_ii = False
    #$ punk_wed_top_iii = False

    #$ punk_fri_top_i = False
    #$ punk_fri_top_ii = False
    #$ punk_fri_top_iii = False

    $ manic_greeting_top_i = False
    $ manic_greeting_top_ii = False
    $ manic_greeting_top_iii = False
    
    $ prude_greeting_top_i = False
    $ prude_greeting_top_ii = False
    $ prude_greeting_top_iii = False
    
    $ arc = 'Punk'
    $ day = 'mon'

    #background declarations
    image bg offi = "office_floor.jpg"
    image bg cube = "cubicle.jpg"
    image bg bath = "bathroom.jpeg"
    image bg brk = "break.jpeg"
    image bg janitor = "jan_closet.jpeg"
    image bg boss = "boss_offi.jpg"

    #sprite declarations
    image punk neut = "punk(old).jpg"
    #image boss neut = ""
    

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
        aff_score = 0
        #aff_bg = 0
        #aff_vp = 0
        #aff_gp = 0



        #Ask the player for thier name
        pcname = renpy.input("What is your name?", length=12)
        pcname = pcname.strip()

        #Default if input is blank
        if not pcname:
            pcname = "Borok"
            
    boss "Ah right [pcname] welcome to blah... Here's the singles in our office which catches your eye?"
    menu:
        "Bigash Gaadush":
            $ arc = 'Punk'
            
        "Vor Priol":
            $ arc = 'Manic'
            
        "Graag Pruish":
            $ arc = 'Prude'



    jump morn

#-------------------Morning Mon Rooms-----------------------------------
label morn:
    #-------------------Monday Morning Dialog-------------------------------
    if day == 'mon':
        scene bg boss
        #show boss neut at right
        boss "Welcome to Second Tower Inc. I’ll be your boss, Borug. Can I get you started with something to drink? | Just a joke. By any means, welcome. Let me show you to your cubicle."
        
        scene bg cube
        boss "Well, here we are. The old six by six—brings back memories. | One day, you’re toiling away from 9 to 5. Next, you’re sitting in your own office with a “World’s Best Boss” mug, slurping down that sweet, morning joe. How the time flies. | Forgive me for rambling. Let me introduce you to some of the office."
        
        boss "This is our accounting team, Bigash and Ponk Gaadush."
        show punk neut at right 
        extend "Ponk doesn’t say much, but their sibling’s quite the live wire. Isn’t that right, Big?"
        
        bg "Please don’t call me Big—or a live wire—ever again. Same goes for you, newbie."
        
        boss "Aren’t they just a big ball of sunshine? My apologies, Bigash. Let me introduce you to one of our sales reps. This is Graag Prudish."
        
        #show prude neut at right
        gp "Pleasure to make your acquaintance. I look forward to a long and fruitful work relationship."
        
        boss "Graag may seem a little—icy at first, but I’m sure you’ll become fast friends. Isn’t that right, Graag?"
        
        gp "Only time will tell, Borug."
        
        boss "See what I mean? Anyway, here’s our quirky HR rep, Vor Priol. Say hi, Vor."
        
        vp "Hello. What’s so quirky about me, Borug?"
        
        boss "I don’t know—all your weird hobbies and obscure music and stuff. Vor’s what you would call a hipster. Isn’t that right, Vor?"
        
        vp "Whatever you say, Borug."
        
        boss "I detect a note of sarcasm, but what do you expect from an ironic hipster-types? | Anyway, it’s just about lunch time, so I’ll leave you to your own devices. Hope the rest of your day goes down as smoothly as this Columbian dark roast. | See you around."
    #-------------------Wednesday Morning Dialog--------------------------
    elif day == 'wed':
        boss "What the hell happened in there, newbie? | I’ve never heard so much warg manure out of one orc in my entire life. You’re on very, VERY thin ice. | … | You’ll have to excuse me. My temper flares when I haven’t had my third cup before lunch. I’ll have to upgrade this next one to a red eye. | Speaking of lunch, it’s about that time. I suggest you use it to get your head in the game. | Don’t let me down like this again."
        
    #------------------Friday Morning Dialog------------------
    elif day == 'fri':
        $ daystr = 'Friday'

label cube_morn_1:
    #narrator "Monday"
    scene bg cube
    $ daystr = ""
    if day == 'mon':
        $ daystr = 'Monday'
    elif day == 'wed':
        $ daystr = 'Wednesday'
    elif day == 'fri':
        $ daystr = 'Friday'
    menu:
        "Cubicle" "Today is [daystr]"

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
        "Boss's Office" "He's not here."

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
    if arc == 'Punk':
        show punk neut at right
        jump punk_greeting_a

    elif arc == 'Manic':
        show manic neut at right
        jump manic_greeting_a
        
    elif arc == 'Prude':
        show prude neut at right
        jump prude_greeting_a

label floor_morn_1:
    scene bg offi
    menu:
        "Office Floor" "Seems empty for now"

        "Go to Bathroom":
            jump bthr_morn_1

        "Go to Boss's Office":
            jump boss_morn_1

        "Go to Janitor's Closet":
            jump jani_morn_1

        "Go to Cubicle":
            jump cube_morn_1

        "Go to Break Room":
            jump brk_morn_1
    


#----------------------------Punk Orc Trees------------------------------------
label punk_greeting_a:

    $ testflag = True
    #----------------------------Monday--------------------------------------
    if day == 'mon':
        $ shuffle_menu()
        menu:
            bg "What are you looking at?"

            "You. Is that a problem?":
                $ aff_score += 2
                jump punk_op_good_a

            "Nothing! Didn't mean to stare. Can I sit down?":
                $ aff_score += 1
                jump punk_op_mid_a

            "Your heads. Anyone sitting here?":
                jump punk_op_bad_a

    #---------------------------Wednesday-------------------------------------
    elif day == 'wed':
        $ shuffle_menu()
        menu:
            bg "Oh, it’s you. That was quite a performance you gave in the meeting. It was pretty clear you have no idea what we do here."

            "It’s garden variety corporate bull shit. What more do I need to know?":
                $ aff_score += 2
                jump punk_op_good_a

            "Yeah, did you see the look on Borug’s face?":
                $ aff_score += 1
                jump punk_op_mid_a

            "I don’t. I’m not even sure what my job title is.":
                jump punk_op_bad_a

    #---------------------------Friday----------------------------------------
    elif day == 'fri':
        $ shuffle_menu()
        menu:
            bg "Well, you’ve made it through your first week. I’m surprised you’ve lasted this long. Then again, I’m surprised I’VE lasted this long."

            "You can’t dismantle the establishment on ideals and teenage angst alone.":
                $ aff_score += 2
                jump punk_op_good_a

            "At least the party will allow us to get drunk at work":
                $ aff_score += 1
                jump punk_op_mid_a

            "Well, I’m glad you did.":
                jump punk_op_bad_a
    #--------------------------------------------------------------------------

label punk_op_good_a:
    #------------------Monday---------------------------------------------
    if day == 'mon':
        bg "Of course not-I like your confidence. Have a seat."

    #-----------------Wednesday---------------------------------------------
    if day == 'wed':
        bg "Well said. I like the way you think."

    #-----------------Friday------------------------------------------------
    if day == 'fri':
        bg "I couldn’t have said it better myself."

    jump punk_greeting_b

label punk_op_mid_a:
    #---------------Monday-----------------------------------------
    if day == 'mon':
        bg "Damn, dude. I was just messing with you."
        bg "You can sit wherever you want."

    #---------------Wednesday------------------------------------------
    if day == 'wed':
        bg "He looked pretty angry. I’ll admit it was pretty funny."

    #---------------Friday----------------------------------------
    if day == 'fri':
        bg "You haven’t been getting drunk at work already?"

    jump punk_greeting_b

label punk_op_bad_a:
    #------------------Monday-------------------------------------
    if day == 'mon':
        bg "No, unfortunately."
        bg "You get right to it, don't you?"

    #-----------------Wednesday------------------------------------
    if day == 'wed':
        bg "I’m all for fighting the power, but isn’t that a little cavalier for your first week?"

    #-----------------Friday---------------------------------------
    if day == 'fri':
        bg "Please stop. You’re going to make me sick."

    jump punk_greeting_b

label punk_greeting_b:

    if punk_greeting_top_i and punk_greeting_top_ii and punk_greeting_top_iii:
        jump punk_greeting_end

    $ unshuffle_menu()
    menu:
        bg "What's up?"
        #------------------------------Monday topics---------------------------
        "How do you like working here?" if day == 'mon' and punk_greeting_top_i == False:
            $ punk_greeting_top_i = True
            jump punk_greeting_b_1

        "What’s Borug like as a boss?" if day == 'mon' and punk_greeting_top_ii == False:
            $ punk_greeting_top_ii = True
            jump punk_greeting_b_2

        "Anyone I should watch out for around the office?" if day == 'mon' and punk_greeting_top_iii == False:
            $ punk_greeting_top_iii = True
            jump punk_greeting_b_3
        #----------------------------------------------------------------------

        #----------------------------Wednesday topics-------------------------
        "What do we do here then?" if day == 'wed' and punk_greeting_top_i == False:
            $ punk_greeting_top_i = True
            jump punk_greeting_b_1

        "What do you do for fun when you’re not working for the machine?" if day == 'wed' and punk_greeting_top_ii == False:
            $ punk_greeting_top_ii = True
            jump punk_greeting_b_2

        "How do you feel about orc-human hybrids?" if day == 'wed' and punk_greeting_top_iii == False:
            $ punk_greeting_top_iii = True
            jump punk_greeting_b_3
        #---------------------------------------------------------------------

        #----------------------------Friday topics----------------------------
        "Are you excited for the party?" if day == 'fri' and punk_greeting_top_i == False:
            $ punk_greeting_top_i = True
            jump punk_greeting_b_1

        "What are you doing after work?" if day == 'fri' and punk_greeting_top_ii == False:
            $ punk_greeting_top_ii = True
            jump punk_greeting_b_2

        "Can I join your band?" if day == 'fri' and punk_greeting_top_iii == False:
            $ punk_greeting_top_iii = True
            jump punk_greeting_b_3
        #---------------------------------------------------------------------

label punk_greeting_b_1:
    #------------------------------Monday---------------------------------------
    if day == 'mon':
        $ shuffle_menu()
        menu:
            bg "It pays the bills. You can’t dismantle the machine on rage and ideals alone."

            "Don’t I know it, sister.":
                $ aff_score += 2
                bg "Right? Everyone else in this office is such a square. They don’t get it. Glad to know I have a comrade in this hell hole."
                jump punk_greeting_b

            "Yeah, but sometimes it seems hopeless.":
                $ aff_score += 1
                bg "That’s why we have to keep fighting! I felt the same way before I went straight edge. You should try it."
                jump punk_greeting_b

            "I guess we all have to grow up sometimes.":
                bg "Are you serious? The moment I grow up is the moment I die. Don’t be such a downer."
                jump punk_greeting_b

    #----------------------------Wednesday-----------------------------------------
    elif day == 'wed':
        $ shuffle_menu()
        menu:
            bg "We buy and sell...orc...  ...stuff.  You know, I’m not really sure either. I’m just an accountant."

            "We all have enough “orc stuff” on our plates already. Don’t you think?":
                $ aff_score += 2
                bg "Right? We’ve all got lives and problems, and...urges. How do they expect us to identify with their corporate agenda?"
                jump punk_greeting_b

            "Why did you make fun of me, then?":
                $ aff_score += 1
                bg "Fair point. I forgot how much I zone out during those meetings too."
                jump punk_greeting_b

            "Oh, cool! I love orc stuff.":
                bg "I sincerely hope you’re kidding."
                jump punk_greeting_b

    #--------------------------Friday-------------------------------------------
    elif day == 'fri':
        $ shuffle_menu()
        menu:
            bg "I’m excited to get paid to sit around and eat cake for the afternoon. I’m less excited about the speeches Borug is bound to give after a few drinks."

            "Maybe it’ll inspire some future Dwarf Crotch material?":
                $ aff_score += 2
                bg "Maybe. I’ll have to bring a notebook with me. Straight from the mouth of the establishment, huh?"
                jump punk_greeting_b

            "I expect to spend most of my waking energy trying not to laugh.":
                $ aff_score += 1
                bg "Same. I’m not sure how successful that’s going to be, though."
                jump punk_greeting_b

            "It’s too bad we have to go. I’d rather be working.":
                bg "So the life of a drone suits you, then? Maybe you’re not who I thought you were."
                jump punk_greeting_b

    #---------------------------------------------------------------------------

label punk_greeting_b_2:
    #--------------------------Monday------------------------------------------
    if day == 'mon':
        $ shuffle_menu()
        menu:
            bg "Ugh, what a drone. Don’t get me started. He’s been Second Tower’s bitch since day one, and he takes it out on all of us. The only comfort he has in this world is his stupid coffee."

            "It’s shameful. Lone wolves like us shouldn’t have to answer to sheep.":
                $ aff_score += 2
                bg "Tell me about it! I will NOT be ground into the dust. That’s why us lone wolves need to stick together."
                jump punk_greeting_b

            "As we are slaves to Borug, so is he to his vices. I pity him, comrade.":
                $ aff_score += 1
                bg "I never thought of it that way. Maybe you’re right. It’s sad, isn’t it?"
                jump punk_greeting_b

            "Yeah, what a jerk. He can take that coffee and shove it up his orc butt.":
                bg "...I guess? I’m not sure how that would work..."
                jump punk_greeting_b

    #--------------------------Wednesday----------------------------------------
    if day == 'wed':
        $ shuffle_menu()
        menu:
            bg "Rage against it, of course! I play the orc bass in a crud punk band called Dwarf Crotch. I’ve always dreamed of going on tour, but this dumb job has kept us from taking the next step."

            "You should go for it!":
                $ aff_score += 2
                bg "Believe me, I want to. I want people to feel the gnarled, haunted feelings I’ve been feeling my whole life. When I finally do, the world better get ready for a wake-up call."
                jump punk_greeting_b

            "That’s awesome. I would love to see you play sometime.":
                $ aff_score += 1
                bg "That’s sweet, but we’ve never actually played a show. We don’t record music either. We don’t even have any songs, per se-it’s all just noise, isn’t it? A pretty package to distract from the message."
                jump punk_greeting_b

            "Really? I love Dwarf Crotch! I’ve seen you guys live a bunch of times.":
                bg "We don’t want you to love us. We want to be disgusting. We want to hold up a mirror to society and say, \“Hey world, this is some pretty messed up shit.\”  Also, how could you have seen us live when we’ve never played a show?"
                jump punk_greeting_b

    #------------------------------Friday---------------------------------------
    if day == 'fri':
        $ shuffle_menu()
        menu:
            bg "It totally depends on how spiritually exhausting this party is. There’s a strong chance it’ll put me out of commission altogether. Why do you ask?"

            "I was wondering if you wanted to check out this band I heard about called Screaming Hobbits. Apparently, their keyboard player is a quadruple amputee and plays with his face.":
                $ aff_score += 2
                bg "That sounds insane! I would hate to miss that."
                jump punk_greeting_b

            "I was wondering if you wanted to go to the Dark Gate later and throw bottles at the big door.":
                $ aff_score += 1
                bg "I used to do that all the time as a teenager! Brings back a lot of memories. We’ll see."
                jump punk_greeting_b

            "I was wondering if you wanted to get dinner later. Orclebee’s has half-priced appetizers after seven.":
                bg "You put that trash in your body? I’m not sure how hungry I’ll be after the party anyway, but I appreciate the offer!"
                jump punk_greeting_b
    #---------------------------------------------------------------------------

label punk_greeting_b_3:
    #----------------------------Monday----------------------------------------
    if day == 'mon':
        bg "You mean besides everyone? I guess if I had to pick one, it’d be Graag. Graag Prudish. She’s a huge kiss ass, but there’s something...else. Something very off that I can’t quite put my finger on it. My advice? Keep your distance."
        $ shuffle_menu()
        menu:
            bg "{cps=0}You mean besides everyone? I guess if I had to pick one, it’d be Graag. Graag Prudish. She’s a huge kiss ass, but there’s something...else. Something very off that I can’t quite put my finger on it. My advice? Keep your distance.{/cps}"

            "Why should I trust you?":
                $ aff_score += 2
                bg "You shouldn’t. No one should trust anyone. Cynicism is a healthy part of a well-balanced breakfast."
                jump punk_greeting_b

            "Yikes, I’ll take your word for it.":
                $ aff_score += 1
                bg "Be careful. Blind trust is how they get you. I could be lying to you right now..I’m kidding. You need to lighten up!"
                jump punk_greeting_b

            "Are you sure you’re not just jealous?":
                bg "Ha. As if. How could I be jealous of someone that tightly wound? Don’t blame me if you’re in the splash zone when she snaps"
                jump punk_greeting_b

    #-----------------------------Wednesday------------------------------------
    elif day == 'wed':
        $ shuffle_menu()
        menu:
            bg "You mean like-you? I suppose they can be quite attractive. Sometimes. Why do you ask?"

            "Just wondering. Apparently, we’re really good kissers-what with the human tongue and all.":
                $ aff_score += 2
                bg "Is that so? I guess I’ll believe it when I see it."
                jump punk_greeting_b

            "Interesting. Just asking for a friend!":
                $ aff_score += 1
                bg "Well in that case, tell your friend I find them a lot less attractive when they beat around the bush."
                jump punk_greeting_b

            "No reason. Follow-up question: Have you ever “made it nice” with someone in a janitor’s closet?":
                bg "Nope. Not planning on it either!"
                jump punk_greeting_b
    #-----------------------------Friday---------------------------------------
    elif day == 'fri':
        $ shuffle_menu()
        menu:
            bg "Where’s this coming from? I didn’t peg you as a musician, but we are looking for a new drummer. Do you have any prior experience?"

            "No, but I hit very, very hard.":
                $ aff_score += 2
                bg "That’s exactly what I wanted to hear. Musical talent is for robots and old, dead orcs in powdered wigs. You’ve got the right attitude. I’ll see what the other members say."
                jump punk_greeting_b

            "No, but I’m willing to learn!":
                $ aff_score += 1
                bg "I appreciate your enthusiasm, but I’ll have to talk to the other members first. We have a few interesting offers already. One of them’s a dead guy! Can you imagine that? Having a dead dude play drums in our band?"
                jump punk_greeting_b

            "Does twelve years of jazz camp and a stint at the Juliorc Academy count?":
                bg "That sounds impressive and all, but it’s not quite what we’re looking for. I’m sure skill and precision are great for jazz, but Dwarf Crotch is all about raw, primal fury. Do you think you can manage that?"
                jump punk_greeting_b
    #-------------------------------------------------------------------------

label punk_greeting_end:
    if day == 'mon':
        bg "Well, I should probably be getting back to it. Borug’s been on everybody’s ass about the big meeting on Wednesday..I almost threw up in my mouth thinking about it. See you around."
        $ day = 'wed'
        $ punk_greeting_top_i = False
        $ punk_greeting_top_ii = False
        $ punk_greeting_top_iii = False
        jump cube_morn_1
    elif day == 'wed':
        bg "Well, this has been fun, but I’m all talked out. Hopefully you figure out what your job is between now and the party on Friday. Borug takes his birthday VERY seriously. See you around."
        $ day = 'fri'
        $ punk_greeting_top_i = False
        $ punk_greeting_top_ii = False
        $ punk_greeting_top_iii = False
        jump cube_morn_1
    elif day == 'fri':
        bg "Anyway, I should probably get going so I can powder my nose before the party. That was a joke. See you soon."
        jump punk_end

label punk_end:
    if aff_score > 6:
        centered "You got the best ending"
    elif aff_score > 2:
        centered "You got the okay ending"
    elif aff_score == 0:
        centered "You got the worst ending"
        return
        
#----------------------------Manic Orc Trees------------------------------------
label manic_greeting_a:

    $ testflag = True
    #----------------------------Monday--------------------------------------
    if day == 'mon':
        $ shuffle_menu()
        menu:
            bg "What are you looking at?"

            "You. Is that a problem?":
                $ aff_score += 2
                jump manic_op_good_a

            "Nothing! Didn't mean to stare. Can I sit down?":
                $ aff_score += 1
                jump manic_op_mid_a

            "Your heads. Anyone sitting here?":
                jump manic_op_bad_a

    #---------------------------Wednesday-------------------------------------
    elif day == 'wed':
        $ shuffle_menu()
        menu:
            bg "Oh, it’s you. That was quite a performance you gave in the meeting. It was pretty clear you have no idea what we do here."

            "It’s garden variety corporate bull shit. What more do I need to know?":
                $ aff_score += 2
                jump manic_op_good_a

            "Yeah, did you see the look on Borug’s face?":
                $ aff_score += 1
                jump manic_op_mid_a

            "I don’t. I’m not even sure what my job title is.":
                jump manic_op_bad_a

    #---------------------------Friday----------------------------------------
    elif day == 'fri':
        $ shuffle_menu()
        menu:
            bg "Well, you’ve made it through your first week. I’m surprised you’ve lasted this long. Then again, I’m surprised I’VE lasted this long."

            "You can’t dismantle the establishment on ideals and teenage angst alone.":
                $ aff_score += 2
                jump manic_op_good_a

            "At least the party will allow us to get drunk at work":
                $ aff_score += 1
                jump manic_op_mid_a

            "Well, I’m glad you did.":
                jump manic_op_bad_a
    #--------------------------------------------------------------------------

label manic_op_good_a:
    #------------------Monday---------------------------------------------
    if day == 'mon':
        bg "Of course not-I like your confidence. Have a seat."

    #-----------------Wednesday---------------------------------------------
    if day == 'wed':
        bg "Well said. I like the way you think."

    #-----------------Friday------------------------------------------------
    if day == 'fri':
        bg "I couldn’t have said it better myself."

    jump manic_greeting_b

label manic_op_mid_a:
    #---------------Monday-----------------------------------------
    if day == 'mon':
        bg "Damn, dude. I was just messing with you."
        bg "You can sit wherever you want."

    #---------------Wednesday------------------------------------------
    if day == 'wed':
        bg "He looked pretty angry. I’ll admit it was pretty funny."

    #---------------Friday----------------------------------------
    if day == 'fri':
        bg "You haven’t been getting drunk at work already?"

    jump manic_greeting_b

label manic_op_bad_a:
    #------------------Monday-------------------------------------
    if day == 'mon':
        bg "No, unfortunately."
        bg "You get right to it, don't you?"

    #-----------------Wednesday------------------------------------
    if day == 'wed':
        bg "I’m all for fighting the power, but isn’t that a little cavalier for your first week?"

    #-----------------Friday---------------------------------------
    if day == 'fri':
        bg "Please stop. You’re going to make me sick."

    jump manic_greeting_b

label manic_greeting_b:

    if manic_greeting_top_i and manic_greeting_top_ii and manic_greeting_top_iii:
        jump manic_greeting_end

    $ unshuffle_menu()
    menu:
        bg "What's up?"
        #------------------------------Monday topics---------------------------
        "How do you like working here?" if day == 'mon' and manic_greeting_top_i == False:
            $ manic_greeting_top_i = True
            jump manic_greeting_b_1

        "What’s Borug like as a boss?" if day == 'mon' and manic_greeting_top_ii == False:
            $ manic_greeting_top_ii = True
            jump manic_greeting_b_2

        "Anyone I should watch out for around the office?" if day == 'mon' and manic_greeting_top_iii == False:
            $ manic_greeting_top_iii = True
            jump manic_greeting_b_3
        #----------------------------------------------------------------------

        #----------------------------Wednesday topics-------------------------
        "What do we do here then?" if day == 'wed' and manic_greeting_top_i == False:
            $ manic_greeting_top_i = True
            jump manic_greeting_b_1

        "What do you do for fun when you’re not working for the machine?" if day == 'wed' and manic_greeting_top_ii == False:
            $ manic_greeting_top_ii = True
            jump manic_greeting_b_2

        "How do you feel about orc-human hybrids?" if day == 'wed' and manic_greeting_top_iii == False:
            $ manic_greeting_top_iii = True
            jump manic_greeting_b_3
        #---------------------------------------------------------------------

        #----------------------------Friday topics----------------------------
        "Are you excited for the party?" if day == 'fri' and manic_greeting_top_i == False:
            $ manic_greeting_top_i = True
            jump manic_greeting_b_1

        "What are you doing after work?" if day == 'fri' and manic_greeting_top_ii == False:
            $ manic_greeting_top_ii = True
            jump manic_greeting_b_2

        "Can I join your band?" if day == 'fri' and manic_greeting_top_iii == False:
            $ manic_greeting_top_iii = True
            jump manic_greeting_b_3
        #---------------------------------------------------------------------

label manic_greeting_b_1:
    #------------------------------Monday---------------------------------------
    if day == 'mon':
        $ shuffle_menu()
        menu:
            bg "It pays the bills. You can’t dismantle the machine on rage and ideals alone."

            "Don’t I know it, sister.":
                $ aff_score += 2
                bg "Right? Everyone else in this office is such a square. They don’t get it. Glad to know I have a comrade in this hell hole."
                jump manic_greeting_b

            "Yeah, but sometimes it seems hopeless.":
                $ aff_score += 1
                bg "That’s why we have to keep fighting! I felt the same way before I went straight edge. You should try it."
                jump manic_greeting_b

            "I guess we all have to grow up sometimes.":
                bg "Are you serious? The moment I grow up is the moment I die. Don’t be such a downer."
                jump manic_greeting_b

    #----------------------------Wednesday-----------------------------------------
    elif day == 'wed':
        $ shuffle_menu()
        menu:
            bg "We buy and sell...orc...  ...stuff.  You know, I’m not really sure either. I’m just an accountant."

            "We all have enough “orc stuff” on our plates already. Don’t you think?":
                $ aff_score += 2
                bg "Right? We’ve all got lives and problems, and...urges. How do they expect us to identify with their corporate agenda?"
                jump manic_greeting_b

            "Why did you make fun of me, then?":
                $ aff_score += 1
                bg "Fair point. I forgot how much I zone out during those meetings too."
                jump manic_greeting_b

            "Oh, cool! I love orc stuff.":
                bg "I sincerely hope you’re kidding."
                jump manic_greeting_b

    #--------------------------Friday-------------------------------------------
    elif day == 'fri':
        $ shuffle_menu()
        menu:
            bg "I’m excited to get paid to sit around and eat cake for the afternoon. I’m less excited about the speeches Borug is bound to give after a few drinks."

            "Maybe it’ll inspire some future Dwarf Crotch material?":
                $ aff_score += 2
                bg "Maybe. I’ll have to bring a notebook with me. Straight from the mouth of the establishment, huh?"
                jump manic_greeting_b

            "I expect to spend most of my waking energy trying not to laugh.":
                $ aff_score += 1
                bg "Same. I’m not sure how successful that’s going to be, though."
                jump manic_greeting_b

            "It’s too bad we have to go. I’d rather be working.":
                bg "So the life of a drone suits you, then? Maybe you’re not who I thought you were."
                jump manic_greeting_b

    #---------------------------------------------------------------------------

label manic_greeting_b_2:
    #--------------------------Monday------------------------------------------
    if day == 'mon':
        $ shuffle_menu()
        menu:
            bg "Ugh, what a drone. Don’t get me started. He’s been Second Tower’s bitch since day one, and he takes it out on all of us. The only comfort he has in this world is his stupid coffee."

            "It’s shameful. Lone wolves like us shouldn’t have to answer to sheep.":
                $ aff_score += 2
                bg "Tell me about it! I will NOT be ground into the dust. That’s why us lone wolves need to stick together."
                jump manic_greeting_b

            "As we are slaves to Borug, so is he to his vices. I pity him, comrade.":
                $ aff_score += 1
                bg "I never thought of it that way. Maybe you’re right. It’s sad, isn’t it?"
                jump manic_greeting_b

            "Yeah, what a jerk. He can take that coffee and shove it up his orc butt.":
                bg "...I guess? I’m not sure how that would work..."
                jump manic_greeting_b

    #--------------------------Wednesday----------------------------------------
    if day == 'wed':
        $ shuffle_menu()
        menu:
            bg "Rage against it, of course! I play the orc bass in a crud manic band called Dwarf Crotch. I’ve always dreamed of going on tour, but this dumb job has kept us from taking the next step."

            "You should go for it!":
                $ aff_score += 2
                bg "Believe me, I want to. I want people to feel the gnarled, haunted feelings I’ve been feeling my whole life. When I finally do, the world better get ready for a wake-up call."
                jump manic_greeting_b

            "That’s awesome. I would love to see you play sometime.":
                $ aff_score += 1
                bg "That’s sweet, but we’ve never actually played a show. We don’t record music either. We don’t even have any songs, per se-it’s all just noise, isn’t it? A pretty package to distract from the message."
                jump manic_greeting_b

            "Really? I love Dwarf Crotch! I’ve seen you guys live a bunch of times.":
                bg "We don’t want you to love us. We want to be disgusting. We want to hold up a mirror to society and say, \“Hey world, this is some pretty messed up shit.\”  Also, how could you have seen us live when we’ve never played a show?"
                jump manic_greeting_b

    #------------------------------Friday---------------------------------------
    if day == 'fri':
        $ shuffle_menu()
        menu:
            bg "It totally depends on how spiritually exhausting this party is. There’s a strong chance it’ll put me out of commission altogether. Why do you ask?"

            "I was wondering if you wanted to check out this band I heard about called Screaming Hobbits. Apparently, their keyboard player is a quadruple amputee and plays with his face.":
                $ aff_score += 2
                bg "That sounds insane! I would hate to miss that."
                jump manic_greeting_b

            "I was wondering if you wanted to go to the Dark Gate later and throw bottles at the big door.":
                $ aff_score += 1
                bg "I used to do that all the time as a teenager! Brings back a lot of memories. We’ll see."
                jump manic_greeting_b

            "I was wondering if you wanted to get dinner later. Orclebee’s has half-priced appetizers after seven.":
                bg "You put that trash in your body? I’m not sure how hungry I’ll be after the party anyway, but I appreciate the offer!"
                jump manic_greeting_b
    #---------------------------------------------------------------------------

label manic_greeting_b_3:
    #----------------------------Monday----------------------------------------
    if day == 'mon':
        bg "You mean besides everyone? I guess if I had to pick one, it’d be Graag. Graag Prudish. She’s a huge kiss ass, but there’s something...else. Something very off that I can’t quite put my finger on it. My advice? Keep your distance."
        $ shuffle_menu()
        menu:
            bg "{cps=0}You mean besides everyone? I guess if I had to pick one, it’d be Graag. Graag Prudish. She’s a huge kiss ass, but there’s something...else. Something very off that I can’t quite put my finger on it. My advice? Keep your distance.{/cps}"

            "Why should I trust you?":
                $ aff_score += 2
                bg "You shouldn’t. No one should trust anyone. Cynicism is a healthy part of a well-balanced breakfast."
                jump manic_greeting_b

            "Yikes, I’ll take your word for it.":
                $ aff_score += 1
                bg "Be careful. Blind trust is how they get you. I could be lying to you right now..I’m kidding. You need to lighten up!"
                jump manic_greeting_b

            "Are you sure you’re not just jealous?":
                bg "Ha. As if. How could I be jealous of someone that tightly wound? Don’t blame me if you’re in the splash zone when she snaps"
                jump manic_greeting_b

    #-----------------------------Wednesday------------------------------------
    elif day == 'wed':
        $ shuffle_menu()
        menu:
            bg "You mean like-you? I suppose they can be quite attractive. Sometimes. Why do you ask?"

            "Just wondering. Apparently, we’re really good kissers-what with the human tongue and all.":
                $ aff_score += 2
                bg "Is that so? I guess I’ll believe it when I see it."
                jump manic_greeting_b

            "Interesting. Just asking for a friend!":
                $ aff_score += 1
                bg "Well in that case, tell your friend I find them a lot less attractive when they beat around the bush."
                jump manic_greeting_b

            "No reason. Follow-up question: Have you ever “made it nice” with someone in a janitor’s closet?":
                bg "Nope. Not planning on it either!"
                jump manic_greeting_b
    #-----------------------------Friday---------------------------------------
    elif day == 'fri':
        $ shuffle_menu()
        menu:
            bg "Where’s this coming from? I didn’t peg you as a musician, but we are looking for a new drummer. Do you have any prior experience?"

            "No, but I hit very, very hard.":
                $ aff_score += 2
                bg "That’s exactly what I wanted to hear. Musical talent is for robots and old, dead orcs in powdered wigs. You’ve got the right attitude. I’ll see what the other members say."
                jump manic_greeting_b

            "No, but I’m willing to learn!":
                $ aff_score += 1
                bg "I appreciate your enthusiasm, but I’ll have to talk to the other members first. We have a few interesting offers already. One of them’s a dead guy! Can you imagine that? Having a dead dude play drums in our band?"
                jump manic_greeting_b

            "Does twelve years of jazz camp and a stint at the Juliorc Academy count?":
                bg "That sounds impressive and all, but it’s not quite what we’re looking for. I’m sure skill and precision are great for jazz, but Dwarf Crotch is all about raw, primal fury. Do you think you can manage that?"
                jump manic_greeting_b
    #-------------------------------------------------------------------------

label manic_greeting_end:
    if day == 'mon':
        bg "Well, I should probably be getting back to it. Borug’s been on everybody’s ass about the big meeting on Wednesday..I almost threw up in my mouth thinking about it. See you around."
        $ day = 'wed'
        $ manic_greeting_top_i = False
        $ manic_greeting_top_ii = False
        $ manic_greeting_top_iii = False
        jump cube_morn_1
    elif day == 'wed':
        bg "Well, this has been fun, but I’m all talked out. Hopefully you figure out what your job is between now and the party on Friday. Borug takes his birthday VERY seriously. See you around."
        $ day = 'fri'
        $ manic_greeting_top_i = False
        $ manic_greeting_top_ii = False
        $ manic_greeting_top_iii = False
        jump cube_morn_1
    elif day == 'fri':
        bg "Anyway, I should probably get going so I can powder my nose before the party. That was a joke. See you soon."
        jump manic_end

label manic_end:
    if aff_score > 6:
        centered "You got the best ending"
    elif aff_score > 2:
        centered "You got the okay ending"
    elif aff_score == 0:
        centered "You got the worst ending"
        return


#----------------------------Prude Orc Trees------------------------------------
label prude_greeting_a:

    $ testflag = True
    #----------------------------Monday--------------------------------------
    if day == 'mon':
        $ shuffle_menu()
        menu:
            gp "Can i help you?"

            "I hope so! I’m still getting my bearings, and I was wondering if I could pick your brain over lunch.":
                $ aff_score += 2
                jump prude_op_good_a

            "Maybe. Is it okay if I sit here?":
                $ aff_score += 1
                jump prude_op_mid_a

            "I don’t know. I was just looking for somewhere to sit.":
                jump prude_op_bad_a

    #---------------------------Wednesday-------------------------------------
    elif day == 'wed':
        $ shuffle_menu()
        menu:
            gp "Good Afternoon. Have you removed your tail from between your legs yet?"

            "That meeting was a disaster. What am I going to do? Help me, Graag!":
                $ aff_score += 2
                jump prude_op_good_a

            "That meeting was rough. I feel like I made an ass of myself...":
                $ aff_score += 1
                jump prude_op_mid_a

            "That meeting was so boring. I didn’t understand a word of what you guys were talking about...":
                jump prude_op_bad_a

    #---------------------------Friday----------------------------------------
    elif day == 'fri':
        $ shuffle_menu()
        menu:
            gp "Oh, it’s you. Hanging in there, I see?"

            "I wouldn’t have been able to do it without you. I’m totally in your debt.":
                $ aff_score += 2
                jump prude_op_good_a

            "I certainly am! Thanks for your help.":
                $ aff_score += 1
                jump prude_op_mid_a

            "Yeah, and I’m ready to partaaay!":
                jump prude_op_bad_a
    #--------------------------------------------------------------------------

label prude_op_good_a:
    #------------------Monday---------------------------------------------
    if day == 'mon':
        gp "It would be my pleasure. Have a seat."

    #-----------------Wednesday---------------------------------------------
    if day == 'wed':
        gp "It was certainly a blunder on your part, but we all find our purpose eventually. | I suggest you stick close to me from now on."

    #-----------------Friday------------------------------------------------
    if day == 'fri':
        gp "Totally? I like the sound of that."

    jump prude_greeting_b

label prude_op_mid_a:
    #---------------Monday-----------------------------------------
    if day == 'mon':
        gp "I don’t see why not."

    #---------------Wednesday------------------------------------------
    if day == 'wed':
        gp "Not the rhetoric I would have chosen, but yes. I would agree with your assessment."

    #---------------Friday----------------------------------------
    if day == 'fri':
        gp "It was my pleasure. I’ll make a note of your gratitude in my personal records."

    jump prude_greeting_b

label prude_op_bad_a:
    #------------------Monday-------------------------------------
    if day == 'mon':
        gp "I’m flattered."

    #-----------------Wednesday------------------------------------
    if day == 'wed':
        gp "Am I supposed to find the situation humorous? I fail to see what the joke is..."

    #-----------------Friday---------------------------------------
    if day == 'fri':
        gp "How pedestrian. If only you applied the same enthusiasm to your work."

    jump prude_greeting_b

label prude_greeting_b:

    if prude_greeting_top_i and prude_greeting_top_ii and prude_greeting_top_iii:
        jump prude_greeting_end

    $ unshuffle_menu()
    menu:
        gp "What shall we discuss?"
        #------------------------------Monday topics---------------------------
        "You look a little stressed. Is everything alright?" if day == 'mon' and prude_greeting_top_i == False:
            $ prude_greeting_top_i = True
            jump prude_greeting_b_1

        "Is Borug a good boss?" if day == 'mon' and prude_greeting_top_ii == False:
            $ prude_greeting_top_ii = True
            jump prude_greeting_b_2

        "Anyone I should watch out for around the office?" if day == 'mon' and prude_greeting_top_iii == False:
            $ prude_greeting_top_iii = True
            jump prude_greeting_b_3
        #----------------------------------------------------------------------

        #----------------------------Wednesday topics-------------------------
        "Can you explain what it is we do here?" if day == 'wed' and prude_greeting_top_i == False:
            $ prude_greeting_top_i = True
            jump prude_greeting_b_1

        "How do I get on Borug’s good side? He really seems to like you." if day == 'wed' and prude_greeting_top_ii == False:
            $ prude_greeting_top_ii = True
            jump prude_greeting_b_2

        "What do you do for fun when you’re not at work?" if day == 'wed' and prude_greeting_top_iii == False:
            $ prude_greeting_top_iii = True
            jump prude_greeting_b_3
        #---------------------------------------------------------------------

        #----------------------------Friday topics----------------------------
        "Are you excited for the party?" if day == 'fri' and prude_greeting_top_i == False:
            $ prude_greeting_top_i = True
            jump prude_greeting_b_1

        "Do you REALLY think Borug’s a good boss?" if day == 'fri' and prude_greeting_top_ii == False:
            $ prude_greeting_top_ii = True
            jump prude_greeting_b_2

        "What’s your policy on office romances?" if day == 'fri' and prude_greeting_top_iii == False:
            $ prude_greeting_top_iii = True
            jump prude_greeting_b_3
        #---------------------------------------------------------------------

label prude_greeting_b_1:
    #------------------------------Monday---------------------------------------
    if day == 'mon':
        $ shuffle_menu()
        menu:
            gp "Never better. What’s a day’s work without a swift, five-minute lunch break?"

            "Agreed. The swifter the better, I always say.":
                $ aff_score += 2
                gp "Pardon me for being so cynical, but I’m pleasantly surprised to hear you say so. Some of our coworkers are far too precious with their “leisure time”. | It’s positively infuriating."
                jump prude_greeting_b

            "You can finish that entire rack of ribs in five minutes? That’s impressive.":
                $ aff_score += 1
                gp "A productive day at the office begets a voracious appetite. Wouldn’t you agree?"
                jump prude_greeting_b

            "Five minutes? Isn’t that a little harsh?":
                gp "I will remind you that this is a place of business, not a high school cafeteria. I would expect you treat it as such."
                jump prude_greeting_b

    #----------------------------Wednesday-----------------------------------------
    elif day == 'wed':
        $ shuffle_menu()
        menu:
            gp "Business. Commerce. Synergy. Do any of these words ring a bell? | Haven’t you read the employee manual?"

            "I read it every night before I fall asleep, but I can’t make heads or tails of it. Do you think you could help me?":
                $ aff_score += 2
                gp "With the manual or falling asleep? | … | A joke. I’ll take enthusiasm over aptitude any day of the week. | It would be my pleasure."
                jump prude_greeting_b

            "I read over it when I first got the position. It’s all a little fuzzy now.":
                $ aff_score += 1
                gp "Well, I’d be happy to jog your memory if need be. In return, I ask only for enthusiasm and a voracious appetite. | … | To learn."
                jump prude_greeting_b

            "I’ve been using it as a paperweight if that counts.":
                gp "A practical application considering its density, but disrespectful to your position nonetheless."
                jump prude_greeting_b

    #--------------------------Friday-------------------------------------------
    elif day == 'fri':
        $ shuffle_menu()
        menu:
            gp "No less excited than I am about any of my other work responsibilities. It’s just another task on the agenda, isn’t it?"

            "How do you keep such an even keel? | You’re more complex and beautiful than the gaff-rigged topsail of a multi-masted packet boat!":
                $ aff_score += 2
                gp "That was perhaps the nicest thing anyone has ever said to me. This must be why I’ve been keeping you around."
                jump prude_greeting_b

            "It does feel like a desperate grab for attention...":
                $ aff_score += 1
                gp "Same. I’m not sure how successful that’s going to be, though."
                jump prude_greeting_b

            "Do you have to be such a downer all the time?":
                gp "I don’t consider myself to be a downer. Perhaps you’re a downer? | What is a downer?"
                jump prude_greeting_b

    #---------------------------------------------------------------------------

label prude_greeting_b_2:
    #--------------------------Monday------------------------------------------
    if day == 'mon':
        $ shuffle_menu()
        menu:
            gp "That is for administration to decide. I concern myself only with my work and the responsibilities it entails."

            "A fair point. I only ask because it seems like you could do his job better.":
                $ aff_score += 2
                gp "I must admit—the thought had crossed my mind. However unprofessional it was for you to say so, your flattery is noted."
                jump prude_greeting_b

            "That’s very judicious of you. I wish I could be so rational.":
                $ aff_score += 1
                gp "There’s no quality more stimulating in an orc than a healthy dose of dispassion. Remember that, and you’ll do just fine here."
                jump prude_greeting_b

            "Yeah...but, how is he?":
                gp "This kind of talk is highly unprofessional. I would advise you drop the issue and refrain from discussing such things in the future."
                jump prude_greeting_b

    #--------------------------Wednesday----------------------------------------
    if day == 'wed':
        $ shuffle_menu()
        menu:
            gp "He certainly appreciates my work ethic. I could talk to him for you. | That is, of course, if you do me the occasional favor around the office."

            "You’re my hero. Just tell me when to jump!":
                $ aff_score += 2
                gp "Excellent. I love an orc that doesn’t ask questions. | You’re a rare breed these days. You should be proud."
                jump prude_greeting_b

            "That’s very thoughtful! What kind of favors?":
                $ aff_score += 1
                gp "That’s for me to know and you to find out. If I’m to take you on as an apprentice, I need your absolute trust."
                jump prude_greeting_b

            "Why are you looking at me like that?":
                gp "If this is to work out, I can’t have you asking so many impertinent questions. "
                jump prude_greeting_b

    #------------------------------Friday---------------------------------------
    if day == 'fri':
        $ shuffle_menu()
        menu:
            gp "Hm. No. As inappropriate as it for me to speak on this issue now, I’ve found him to be incompetent since the day he took over. | One day, though, he will slip up, I assure you that, and when that moment comes, I will be ready and waiting to return Second Tower to its former glory!"

            "Finally, someone’s brave enough to say it. Lead us into the golden age, Graag!":
                $ aff_score += 2
                gp "With pleasure. There’s a place for everyone in the new order—if you play your cards right. | How does assistant to the new regional manager sound?"
                jump prude_greeting_b

            "Sounds devious. I love it.":
                $ aff_score += 1
                gp "I would prefer to use the word pragmatic, but I am happy to see you’re on board. I could use an assistant."
                jump prude_greeting_b

            "That sounds super evil.":
                gp "I don’t follow. I’m simply stating the facts. If you’re concerned with my capacity for leadership, I assure you, you’ll be the first to go."
                jump prude_greeting_b
    #---------------------------------------------------------------------------

label prude_greeting_b_3:
    #----------------------------Monday----------------------------------------
    if day == 'mon':
        gp "I consider office gossip thoroughly beneath me… | But if I must, I suggest you keep an eye out for that two-headed creature Bigash Gaadush. Their utter disrespect for authority has been a blight on this company since they arrived. | It would be in your best interest to steer clear."
        $ shuffle_menu()
        menu:
            gp "{cps=0}I consider office gossip thoroughly beneath me… | But if I must, I suggest you keep an eye out for that two-headed creature Bigash Gaadush. Their utter disrespect for authority has been a blight on this company since they arrived. | It would be in your best interest to steer clear.{/cps}"

            "Thanks for the tip. I’m glad I heard it from you first.":
                $ aff_score += 2
                gp "One must surround themselves for the right people to be successful. I’m happy to see you’re taking the proper steps."
                jump prude_greeting_b

            "Yeah, what was the deal with the two heads thing?":
                $ aff_score += 1
                gp "How should I know? I suppose corporate wanted a little “diversity” in the workplace. Personally, I find it distracting."
                jump prude_greeting_b

            "She seemed nice enough to me!":
                gp "Of course she did. She may have fooled most of the office, but she hasn’t fooled me. You’re lucky you heard it from me first."
                jump prude_greeting_b

    #-----------------------------Wednesday------------------------------------
    elif day == 'wed':
        $ shuffle_menu()
        menu:
            gp "I don’t believe in the concept of leisure time. I like to think everything I do has its time and purpose, but if you mean what I do while I’m not at work… | That’s between me and the orc I’m doing it with."

            "Maybe we can find a time and purpose together sometime.":
                $ aff_score += 2
                gp "Perhaps if you play your cards right. Are you sure you have enough time in your schedule to get the job done?"
                jump prude_greeting_b

            "Are you saying what I think you’re saying?":
                $ aff_score += 1
                gp "You catch on quickly, don’t you? I find your innocence strangely intriguing."
                jump prude_greeting_b

            "I don’t follow. Could you explain yourself in explicit detail?":
                gp "Maybe another time. Why don’t you ask your mother and father when you get home later?"
                jump prude_greeting_b
    #-----------------------------Friday---------------------------------------
    elif day == 'fri':
        $ shuffle_menu()
        menu:
            gp "I’m not sure if I’m capable of romance, per se, but if you’re simply referring to non-platonic coworker relations, then I’ve certainly had my fair share."

            "Intriguing. I’ll make sure to log this exchange in my personal records for future use.":
                $ aff_score += 2
                gp "You certainly have a way with words. Now I’m all hot and bothered."
                jump prude_greeting_b

            "Any chance I could end up a part of that fair share?":
                $ aff_score += 1
                gp "Perhaps. If you have a resume I can look at, I’ll take it into consideration."
                jump prude_greeting_b

            "What’s work without a little play, am I right?":
                gp "Just work I suppose. I tend to prefer things that way."
                jump prude_greeting_b
    #-------------------------------------------------------------------------

label prude_greeting_end:
    if day == 'mon':
        gp "Well, my five minutes are up. I’m heading back. I suggest you do the same. | You have a lot of prep work to do before the all staff meeting on Wednesday, so keep your nose to the grindstone, and you’ll do just fine here. | Good day."
        
        scene bg cube
        boss "Well, hope your first day went well. We’re happy to have you, but you better not let me down or there’ll be hell to pay! | Another joke, but seriously—don’t."
        boss "By the way, I saw you making googly eyes at Bigash at lunch earlier. I’m sure I don’t need to remind you of our policy on office romances… | They’re totally allowed, but from orc to orc, I suggest you tread lightly."
        boss "Like I said, total live wire, that one. Don’t be surprised if you get burned. | Anyway, I’ll see you tomorrow. I suggest you start getting ready for the all staff meeting on Wednesday. It’s going to be a big one! "
        
        $ day = 'wed'
        $ prude_greeting_top_i = False
        $ prude_greeting_top_ii = False
        $ prude_greeting_top_iii = False
        jump cube_morn_1
    elif day == 'wed':
        gp "Well, this has been scintillating to say the least, but I must return to work at once. We all must make an appearance at Borug’s party on Friday, and I refuse to fall behind. | Good day."
        $ day = 'fri'
        $ prude_greeting_top_i = False
        $ prude_greeting_top_ii = False
        $ prude_greeting_top_iii = False
        jump cube_morn_1
    elif day == 'fri':
        gp "Well, that’s enough nutrition for one day. I must return to my desk to steel my mind against the ensuing birthday celebration. See you at the party."
        jump prude_end

label prude_end:
    if aff_score > 6:
        centered "You got the best ending"
    elif aff_score > 2:
        centered "You got the okay ending"
    elif aff_score == 0:
        centered "You got the worst ending"
        return