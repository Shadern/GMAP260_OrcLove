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
    $ punk_greeting_top_ii = False
    $ punk_greeting_top_iii = False

    $ punk_wed_top_i = False
    $ punk_wed_top_ii = False
    $ punk_wed_top_iii = False

    $ punk_fri_top_i = False
    $ punk_fri_top_ii = False
    $ punk_fri_top_iii = False

    $ arc = 'Punk'
    $ day = 'mon'

    #background declarations
    image bg offi = "office_floor.jpeg"
    image bg cube = "cubicle.jpeg"
    image bg bath = "bathroom.jpeg"
    image bg brk = "break.jpeg"
    image bg janitor = "jan_closet.jpeg"
    image bg boss = "boss_offi.jpeg"

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

#-------------------Morning Mon Rooms-----------------------------------
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
        "Boss's Office" "The door is locked. Guess he's busy"

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


label floor_morn_1:
    scene bg offi
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
    


#----------------------------Punk Orc Trees------------------------------------
label punk_greeting_a:

    $ testflag = True
    #----------------------------Monday--------------------------------------
    if day == 'mon':
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

    #---------------------------Wednesday-------------------------------------
    elif day == 'wed':
        menu:
            bg "Oh, it’s you. That was quite a performance you gave in the meeting. It was pretty clear you have no idea what we do here."

            "It’s garden variety corporate bull shit. What more do I need to know?":
                $ aff_bg += 2
                jump choice_good_a

            "Yeah, did you see the look on Borug’s face?":
                $ aff_bg += 1
                jump choice_mid_a

            "I don’t. I’m not even sure what my job title is.":
                jump choice_bad_a

    #---------------------------Friday----------------------------------------
    elif day == 'fri':
        menu:
            bg "Well, you’ve made it through your first week. I’m surprised you’ve lasted this long. | Then again, I’m surprised I’VE lasted this long."

            "You can’t dismantle the establishment on ideals and teenage angst alone.":
                $ aff_bg += 2
                jump choice_good_a

            "At least the party will allow us to get drunk at work":
                $ aff_bg += 1
                jump choice_mid_a

            "Well, I’m glad you did.":
                jump choice_bad_a
    #--------------------------------------------------------------------------

label choice_good_a:
    if day == 'mon':
        bg "Of course not-{p}I like your confidence. Have a seat."

    if day == 'wed':
        bg "Well said. I like the way you think."

    if day == 'fri':
        bg "I couldn’t have said it better myself."

    jump punk_greeting_b

label choice_mid_a:
    if day == 'mon':
        bg "Damn, dude. I was just messing with you."
        bg "You can sit wherever you want."

    if day == 'wed':
        bg "He looked pretty angry. I’ll admit it was pretty funny."

    if day == 'fri':
        bg "You haven’t been getting drunk at work already?"

    jump punk_greeting_b

label choice_bad_a:
    if day == 'mon':
        bg "No, unfortunately."
        bg "You get right to it, don't you?"

    if day == 'wed':
        bg "I’m all for fighting the power, but isn’t that a little cavalier for your first week?"

    if day == 'fri':
        bg "Please stop. You’re going to make me sick."

    jump punk_greeting_b

label punk_greeting_b:

    if punk_greeting_top_i and punk_greeting_top_ii and punk_greeting_top_iii:
        jump punk_greeting_end

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

    #----------------------------Wednesday-----------------------------------------
    elif day == 'wed':
        menu:
            bg "We buy and sell…orc…  …stuff.  You know, I’m not really sure either. I’m just an accountant."

            "We all have enough “orc stuff” on our plates already. Don’t you think?":
                $ aff_bg += 2
                bg "Right? We’ve all got lives and problems, and…urges. | How do they expect us to identify with their corporate agenda?"
                jump punk_greeting_b

            "Why did you make fun of me, then?":
                $ aff_bg += 1
                bg "Fair point. I forgot how much I zone out during those meetings too."
                jump punk_greeting_b

            "Oh, cool! I love orc stuff.":
                bg "I sincerely hope you’re kidding."
                jump punk_greeting_b

    #--------------------------Friday-------------------------------------------
    elif day == 'fri':
        menu:
            bg "I’m excited to get paid to sit around and eat cake for the afternoon. I’m less excited about the speeches Borug is bound to give after a few drinks."

            "Maybe it’ll inspire some future Dwarf Crotch material?":
                $ aff_bg += 2
                bg "Maybe. I’ll have to bring a notebook with me. Straight from the mouth of the establishment, huh?"
                jump punk_greeting_b

            "I expect to spend most of my waking energy trying not to laugh.":
                $ aff_bg += 1
                bg "Same. I’m not sure how successful that’s going to be, though."
                jump punk_greeting_b

            "It’s too bad we have to go. I’d rather be working.":
                bg "So the life of a drone suits you, then? Maybe you’re not who I thought you were."
                jump punk_greeting_b

    #---------------------------------------------------------------------------

label punk_greeting_b_2:
    #--------------------------Monday------------------------------------------
    if day == 'mon':
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

    #--------------------------Wednesday----------------------------------------
    if day == 'wed':
        menu:
            bg "Rage against it, of course! I play the orc bass in a crud punk band called Dwarf Crotch. I’ve always dreamed of going on tour, but this dumb job has kept us from taking the next step."

            "You should go for it!":
                $ aff_bg += 2
                bg "Believe me, I want to. I want people to feel the gnarled, haunted feelings I’ve been feeling my whole life. When I finally do, the world better get ready for a wake-up call."
                jump punk_greeting_b

            "That’s awesome. I would love to see you play sometime.":
                $ aff_bg += 1
                bg "That’s sweet, but we’ve never actually played a show. We don’t record music either. We don’t even have any songs, per se—it’s all just noise, isn’t it? A pretty package to distract from the message."
                jump punk_greeting_b

            "Really? I love Dwarf Crotch! I’ve seen you guys live a bunch of times.":
                bg "We don’t want you to love us. We want to be disgusting. We want to hold up a mirror to society and say, \“Hey world, this is some pretty messed up shit.\”  Also, how could you have seen us live when we’ve never played a show?"
                jump punk_greeting_b

    #------------------------------Friday---------------------------------------
    if day == 'fri':
        menu:
            bg "It totally depends on how spiritually exhausting this party is. There’s a strong chance it’ll put me out of commission altogether. Why do you ask?"

            "I was wondering if you wanted to check out this band I heard about called Screaming Hobbits. Apparently, their keyboard player is a quadruple amputee and plays with his face.":
                $ aff_bg += 2
                bg "That sounds insane! I would hate to miss that."
                jump punk_greeting_b

            "I was wondering if you wanted to go to the Dark Gate later and throw bottles at the big door.":
                $ aff_bg += 1
                bg "I used to do that all the time as a teenager! Brings back a lot of memories. We’ll see."
                jump punk_greeting_b

            "I was wondering if you wanted to get dinner later. Orclebee’s has half-priced appetizers after seven.":
                bg "You put that trash in your body? I’m not sure how hungry I’ll be after the party anyway, but I appreciate the offer!"
                jump punk_greeting_b
    #---------------------------------------------------------------------------

label punk_greeting_b_3:
    #----------------------------Monday----------------------------------------
    if day == 'mon':
        bg "You mean besides everyone? I guess if I had to pick one, it’d be Graag. Graag Prudish. She’s a huge kiss ass, but there’s something…else. Something very off that I can’t quite put my finger on it. My advice? Keep your distance."
        menu:
            bg "{cps=0}You mean besides everyone? I guess if I had to pick one, it’d be Graag. Graag Prudish. She’s a huge kiss ass, but there’s something…else. Something very off that I can’t quite put my finger on it. My advice? Keep your distance.{/cps}"

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

    #-----------------------------Wednesday------------------------------------
    elif day == 'wed':
        menu:
            bg "You mean like—you? I suppose they can be quite attractive. Sometimes. Why do you ask?"

            "Just wondering. Apparently, we’re really good kissers—what with the human tongue and all.":
                $ aff_bg += 2
                bg "Is that so? I guess I’ll believe it when I see it."
                jump punk_greeting_b

            "Interesting. Just asking for a friend!":
                $ aff_bg += 1
                bg "Well in that case, tell your friend I find them a lot less attractive when they beat around the bush."
                jump punk_greeting_b

            "No reason. Follow-up question: Have you ever “made it nice” with someone in a janitor’s closet?":
                bg "Nope. Not planning on it either!"
                jump punk_greeting_b
    #-----------------------------Friday---------------------------------------
    elif day == 'fri':
        menu:
            bg "Where’s this coming from? I didn’t peg you as a musician, but we are looking for a new drummer. Do you have any prior experience?"

            "No, but I hit very, very hard.":
                $ aff_bg += 2
                bg "That’s exactly what I wanted to hear. Musical talent is for robots and old, dead orcs in powdered wigs. You’ve got the right attitude. I’ll see what the other members say."
                jump punk_greeting_b

            "No, but I’m willing to learn!":
                $ aff_bg += 1
                bg "I appreciate your enthusiasm, but I’ll have to talk to the other members first. We have a few interesting offers already. One of them’s a dead guy! Can you imagine that? Having a dead dude play drums in our band?"
                jump punk_greeting_b

            "Does twelve years of jazz camp and a stint at the Juliorc Academy count?":
                bg "That sounds impressive and all, but it’s not quite what we’re looking for. I’m sure skill and precision are great for jazz, but Dwarf Crotch is all about raw, primal fury. Do you think you can manage that?"
                jump punk_greeting_b
    #-------------------------------------------------------------------------

label punk_greeting_end:
    if day == 'mon':
        bg "Well, I should probably be getting back to it. Borug’s been on everybody’s ass about the big meeting on Wednesday—I almost threw up in my mouth thinking about it. See you around."
        $ day = 'wed'
        jump cube_morn_1
    elif day == 'wed':
        bg "Well, this has been fun, but I’m all talked out. Hopefully you figure out what your job is between now and the party on Friday. Borug takes his birthday VERY seriously. See you around."
        $ day = 'fri'
        jump cube_morn_1
    elif day == 'fri':
        bg "Anyway, I should probably get going so I can powder my nose before the party. That was a joke. See you soon."
        return
