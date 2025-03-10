# Player Stats

default player_drunkness = 25
default player_max_drunkness = 100
default player_money = 35
default player_max_money = 35
default friendship = 0


# Opponent Stats

default opponent_drunkness = 25
default opponent_max_drunkness = 100


# Player Companion

default player_homies = "The Squad"
default player_bff = ""
default squad_level = 3

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Me", color = "#df1927")
define s = Character("[player_homies]", color="#d22aae")
define b = Character("[player_bff]", color = "#d3d32ad8")
define j = Character("Chad", color = "#5a44ecdc")
define k = Character("Jenny", color = "#ec44acdc")
define l = Character("Bouncer", color = "#31f40fdc")

# Backgrounds

image bg intro = im.Scale("bg intro.png", 1920, 1080)
image bg battle = im.Scale("bg battle.png", 1920, 1080)
image bg bathroom = im.Scale("bg bathroom.png", 1920, 1080)
image bg curb = im.Scale("bg curb.png", 1920, 1080)
image bg hospital = im.Scale("bg hospital.png", 1920, 1080)
# Battle Screen

screen battle_screen():
    modal True
    tag battle
    add "chad.png" xalign 0.85 yalign 0.1
    add "squad.png" xalign 0.1 yalign 0.6
        

    # Display Hit Bars (oppo)
    frame:
        xalign 0.95
        yalign 0.05
        background "#fdd5222b"
        padding (10, 10, 10, 10)
        vbox:
            text "Chad" color "#fff" size 20
            bar value opponent_drunkness range opponent_max_drunkness
            xalign 0.0 yalign 0.1 xmaximum 200
    # Display Hit Bars (Player)
    frame:
        xalign 0.05
        yalign 0.75
        background "#fdd5222b"
        padding (10, 10, 10, 10)
        vbox:
            text "[player_homies]" color "#fff" size 20
            bar value player_drunkness range player_max_drunkness 
            bar value player_money range player_max_money
            xalign 0.0 yalign 0.1 xmaximum 200


    # Display battle menu
    frame:
        xalign 0.5
        yalign 0.55
        background "#0009"
        padding (10, 10, 10, 10)
        hbox spacing 15:
            textbutton "Fight" action Return("fight") text_color "#ff0000"
            textbutton "Chop it up" action Return("talk") text_color "#f000f0"
            textbutton "Buy a drink" action Return("drinks") text_color "#7e27c5"
screen battle_screen1():
    modal True
    tag battle
    add "jenny.png" xalign 0.85 yalign 0.1
    add "squad.png" xalign 0.1 yalign 0.6
        

    # Display Hit Bars (oppo)
    frame:
        xalign 0.95
        yalign 0.05
        background "#fdd5222b"
        padding (10, 10, 10, 10)
        vbox:
            text "Jenny" color "#fff" size 20
            bar value opponent_drunkness range opponent_max_drunkness
            xalign 0.0 yalign 0.1 xmaximum 200
    # Display Hit Bars (Player)
    frame:
        xalign 0.05
        yalign 0.75
        background "#fdd5222b"
        padding (10, 10, 10, 10)
        vbox:
            text "[player_homies]" color "#fff" size 20
            bar value player_drunkness range player_max_drunkness 
            bar value player_money range player_max_money
            xalign 0.0 yalign 0.1 xmaximum 200


    # Display battle menu
    frame:
        xalign 0.5
        yalign 0.55
        background "#0009"
        padding (10, 10, 10, 10)
        hbox spacing 15:
            textbutton "Fight" action Return("fight") text_color "#ff0000"
            textbutton "Chop it up" action Return("talk") text_color "#f000f0"
            textbutton "Buy a drink" action Return("drinks") text_color "#7e27c5"
screen battle_screen2():
    modal True
    tag battle
    add "bouncer.png" xalign 0.85 yalign 0.1
    add "player.png" xalign 0.1 yalign 0.6
        

    # Display Hit Bars (oppo)
    frame:
        xalign 0.95
        yalign 0.05
        background "#fdd5222b"
        padding (10, 10, 10, 10)
        vbox:
            text "Bouncer" color "#fff" size 20
            xalign 0.0 yalign 0.1 xmaximum 200
    # Display Hit Bars (Player)
    frame:
        xalign 0.05
        yalign 0.75
        background "#fdd5222b"
        padding (10, 10, 10, 10)
        vbox:
            text "[player_homies]" color "#fff" size 20
            bar value player_drunkness range player_max_drunkness 
            bar value player_money range player_max_money
            xalign 0.0 yalign 0.1 xmaximum 200


    # Display battle menu
    frame:
        xalign 0.5
        yalign 0.55
        background "#0009"
        padding (10, 10, 10, 10)
        hbox spacing 15:
            textbutton "Fight" action Return("fight") text_color "#ff0000"
            textbutton "Chop it up" action Return("talk") text_color "#f000f0"
            textbutton "Buy a drink" action Return("drinks") text_color "#7e27c5"


    # Character Selection
screen squad_selection():
    modal True
    tag Selection
    frame:
        xalign 0.5
        yalign 0.5
        background "#130606"
        vbox:
            spacing 25
            text "Choose your BFF!" color "#ff0000" size 30
            textbutton "The Enforcer" action [SetVariable ("player_bff", "The Enforcer"), Jump("battle_intro1")] text_color "#490404"
            textbutton "The Chiller" action [SetVariable ("player_bff", "The Chiller"), Jump ("battle_intro1")] text_color "#8a6c7ad6"
            textbutton "The Deep Pockets" action [SetVariable ("player_bff", "The Deep Pockets"), Jump("battle_intro1")] text_color "#16b846"


# The game starts here.

label start:
    scene bg intro with dissolve
    "Welcome to the bar, you and your squad have arrived fashionably late, because you are chill like that."
    "You are nervous because it is your first time in a bar but your brother's friend said your fake id will definitely work"
    "You turn to your BFF, wait but you're kinda buzzed, who's your bestie again?"
    call screen squad_selection
   
label battle_intro1:
    scene bg battle with fade
    "Holding your breath and repeating your fake name and address in your head, you hand your ID to the bouncer"
    "He stamps your hand without even looking at it"
    "You enter a crowded area of the bar with [player_homies] at your side and get in line to buy some drinks"
    j "Hey buddy, why don't you um... scoot up out the way, my squad is trying to get drinks"
    b "First of all, we're in line. Second don't you ever buddy my boy like that... BUDDY!"
    "The two opposing squads size each other up, nobody else in the bar seems to care even remotely."
    jump battle_sequence

label battle_sequence:
    "The squads continue to stare menacingly at each other in silence"
    j "Sorry... pal"
    show screen battle_screen
    $ result = ui.interact()

    if result == "fight":
        hide screen battle_screen
        "Your squad makes eye contact and you all immediately try to scrap with the opposing squad"
        $ opponent_drunkness += 10
        $ player_drunkness += 10
        "You guys did not win the fight, but you're all quite happy you could coordinate an attack without saying anything, the opposing squad is thrown out of the bar, but you hide in the bathroom"
        $ friendship += 1
        jump bathroom
    elif result == "talk":
        hide screen battle_screen
        m "Soo... where are you from bro?"
        "The usage of bro creates an instant connection between you guys, Chad feels understood"
        $ opponent_drunkness += 30
        $ player_drunkness += 15
        j "Dude I'm from Boston, let me show you how we really drink on the Beast Coast"
        "He orders three shots (two for him, one) back to back and passes out"
        jump battle_intro2
        
    elif result == "drinks":
        hide screen battle_screen
        "You decide to ignore them and go ahead and order a drink"
        m "One beverage please bartender"
        $ player_money -=10
        jump battle_intro2
label bathroom:
    scene bg bathroom with dissolve
    b "I thought bar fights were a myth, we were throwing some haymakers out there!"
    m "Me too, the way we clocked those guys was unreal"
    m "Drinks on me to celebrate our victory"
    $ player_money -= 15
    $ player_drunkness += 10
    "You guys did not in fact throw a single punch"
    $ friendship += 1
    jump battle_intro2 

label battle_intro2:
    scene bg battle with fade
    "[player_homies] chill for a while and return to the bartender for another round"
    "The meanest girl in school, Jenny, approaches right after you receive your drink"
    k "Um, why are you here"
    m "Good to see you too, Jenny"
    "Jenny spills your drink all over your going out shirt"
    k "oops"
    jump battle_sequence2   

label battle_sequence2:
    b "Not cool at all Jenny"
    "You are PISSED, she really is the meanest..."
    "You stare each other down"
    show screen battle_screen1
    $ result = ui.interact()
    if result == "fight":
        hide screen battle_screen1
        "You take [player_bff]'s drink and throw it on Jenny"
        k "WHAT THE FUCK!!!"
        "You get angrily screamed at by 14 people at the same time and have to leave the area drinkless"
        $ player_drunkness -= 10
        jump fight2
    elif result == "talk":
        hide screen battle_screen1
        m "Oh no, I think I got some of my shirt on your drink, I'm sorry about that"
        "Jenny has a realization that you are actually super chill because you should be pissed rn"
        k "I'm so sorry about that let me buy you a drink to make up for it"
        "The squad is shook by your sudden change of heart, Jenny was literally your least favorite person 2 minutes ago"
        $ player_drunkness += 10
        $ opponent_drunkness += 10
        jump talk2
    elif result == "drinks":
        hide screen battle_screen1
        "You turn around and ignore Jenny"
        m "Lets get some drinks squad!"
        $ player_drunkness += 10
        $ player_money -= 10
        jump drinks2

label fight2:
    scene bg bathroom with fade
    b "Okay that was a little unexpected. I knew you hated Jenny, but not that much"
    m "I perhaps might've lost my cool a little bit"
    m "But like, nobody screamed when she threw her drink on me I don't understand why everyone got so mad"
    b "You threw my full pitcher of beer and drenched like 7 other people along with her..."
    m "Well, when you put it like that it may sound a little worse"
    "You guys leave the bathroom to find the bar bouncers waiting for you..."
    jump battle_sequence3

label talk2:
    scene bg battle with fade
    k "I didn't realize how cool you were! We should be hanging out more" 
    "You don't know what to say, but realize there are more pressing issues at hand"
    "Jenny's friends already grabbed the bouncer when you guys faced off"
    jump battle_sequence3

label drinks2:
    scene bg battle with fade
    "Your drinks come out but a cold and dark feeling comes over your section of the bar"
    "The coldness and darkness overcome you, making you feel as if you're never going to be happy again"
    "The bouncer is making a beeline straight for you"
    jump battle_sequence3

label battle_sequence3:
    l "So, I've heard you've been causing quite a bit of trouble here tonight"
    m "I have not one bit Mr. Bouncer Sir"
    l "Well that's not what I heard, I'm gonna need to take a closer look at your ID, you look awfully young"
    "You stare the bouncer dead in the eyes, puffing up your chest and trying not to look absolutely terriffied"
    show screen battle_screen2
    $ result = ui.interact()
    if result == "fight":
        hide screen battle_screen2
        "You attempt to land a big right hook on the bouncer, he swiflty catches your punch betweeen his pointer finger and thumb"
        l "You should not have done that"
        "Would've been nice to know that the bouncer is a washed up heavyweight UFC fighter before you did that"
        "He proceeds to give you the worst ass whooping in the history of ass whoopings, throws you out on the curb and whispers in your ear"
        l "You are never allowed back in my bar"
        "It is in no way, shape, or form his bar. He gets paid 14 an hour to work 10 pm to close on Saturdays. But he did kick your ass."
        jump sadend
    elif result == "talk":
        hide screen battle_screen2
        m "I really have not been trying to cause any trouble tonight sir, here is my ID"
        "You shit your pants a little, he looks at your fake ID for 0.1 seconds"
        l "This is the fakest ID I've ever seen, I don't think anybody is actually from Idaho"
        l "You seem like a good person though, $20 bucks and I'll let it slide"
        if player_money >= 20:
            m "Here's your twenty, I appreciate it sir"
            jump happyend
        elif player_money <= 20:
            m "I unfortunately don't have enough money on me"
            "He swiftly breaks your ID in half, and carries you out of the bar by your collar and drops you on the curb"
            l "Broke ass"
            jump sadend
        
    elif result == "drinks":
        hide screen battle_screen2
        "You turn around and ignore the bouncer, then turn around to go get drinks"
        m "Lets get some drinks squad!"
        "The bouncer does not take kindly to this"
        l "YOU'RE DONE! NOBODY DISRESPECTS ME LIKE THAT AND GETS AWAY WITH IT!"
        m "Surely I'm about to, tough guy"
        "He punches you so square in the nose"
        jump saddestend
label sadend:
    scene bg curb
    "You sit on the curb alone for a while, pondering the decisions you made throughout the night"
    "The bar is truly not what you thought it would be, maybe you aren't ready for college life yet"
    "You walk home alone through the cold rain and contemplate the meanings of life and happiness"
    return
label happyend:
    scene bg battle with fade
    "You have an electric night with friends at the bar, both old and new as you stay until closing time"
    "One of the best walks and conversations of your entire life occurs on the walk back home after"
    return
label saddestend:
    scene bg hospital with dissolve
    "You wake up with a broken nose and a horrible headache"
    "Going to the bar was one of the worst decisions of your life, you were also charged for identity theft and aggravated assault of the bouncer"
    "You end up spending three long years in prison after losing the trial, this derails your entire future and leaves you to lead a life full of regret, poverty, bad luck, and hatred"
    "In the end, you know that you are the one to blame for your cursed life although you never wind up admitting or accepting this"
    return