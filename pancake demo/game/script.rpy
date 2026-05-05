label start:

    scene bg_black with dissolve

    # TODO: Day 1 Title
    "[[DAY 1]"

    "How did this all start.."
    "Right, I quit my job."
    "The office life was way too hectic for me."
    "I wanted to try something different."
    "I may have used... a lot of my savings to get this new place...."
    "But it feels like a good fresh start."
    "This place is 2 blocks away from my new apartment, so it's really convenient."
    "Enough inner chattering, it's time for me to officially head to work."

    # TODO Screen bg/Cutscreen: Cafe entrance (Morning)

    "You would walk to the new shop that you had bought with the rest of your savings."
    "It's starting to become a bit cloudy."
    "You see your friend, Tariro, waving at you at the entrance of the cafe."
    "As soon as you greet Tariro, you head inside."

    scene bg_cafe_behind_counter_morning with dissolve

    char_tariro "\"Look at this place!\""
    char_shin "\"I know, it took quite a bit to get it!\""
    char_tariro "\"I bet it did!\"" 
    char_tariro "\"So how do you plan on taking orders?\""
    char_shin "\"Uhm... hi, welcome to Chili's?\""
    char_tariro "\"WHAT?? NO!!\""

    # (Tariro tut intro; Choices Event)
    char_tariro "\"I'm going to be your practice for you so you can be ready for tomorrow!\"" 
    char_tariro "\"Customers will give you descriptions on the types of drinks they want!\""
    char_tariro "\"You get only 1 chance to get their drinks right.\""
    char_tariro "\"Let's give it a try.\""
    char_shin "\"What can I get you?\""
    char_tariro "\"I want a warm milky drink that also tastes chocolatey with marshmallows!\""

    # (Tariro TUT order)
label tutorial_order:
    menu:
        "Hot Chocolate":
            char_tariro "\"See? You got it! Now let's see how you do tomorrow!\""
            jump tutorial_continue

        "Espresso":
            char_tariro "\"Nope, but thankfully this is just a test.\""
            jump tutorial_order

        "Milk":
            char_tariro "\"Nope, but thankfully this is just a test.\""
            jump tutorial_order

        "Americanó":
            char_tariro "\"Nope, but thankfully this is just a test.\""
            jump tutorial_order

label tutorial_continue:
    char_tariro "\"Just remember to pay attention to what the customers are saying! Good luck!\""
    char_shin "\"Thanks, Tari... I'll need it for sure.\""

    # TODO: tariro after tut intro
    char_tariro "\"Well, you'll get used to it eventually!\""
    char_tariro "\"Well, it's getting ready to storm, I'm going to head home, don't forget to close up!\""
    char_shin "\"Yeah, I know.\""

    "You and Tariro waved goodbye to each other."
    "The cafe was silent now."
    "You take a deep breath, enjoying the silence."

    char_shin "\"To a new start for me.. What could go wrong?\""

    "There was a roar of thunder outside."
    "Rain had started to pour."
    char_monologue "Guess I should close up and head home."

    # TODO: Screen bg: Cafe entrance (raining)
    "You grab your umbrella and head outside to close up shop."
    "As you were about to close up, you saw someone on the curb, sitting out in the rain."
    "You hesitated before approaching them with the umbrella."
    "He'd looked up at you, like a wet dog who had got caught doing nothing."
    "You squat down to his level, holding out your umbrella to cover him."

    char_shin "\"Are you okay?\""

    # Ahn's first interaction started.
    char_shin "\"What are you doing out here in the rain?\""
    char_ahn "\"I didn't think anyone lived here.\""
    char_shin "\"Well, I don't, I just bought the shop here.\""
    char_ahn "\"Oh, I didn't know that..\""

    # TODO: Screen bg: Cafe behind counter (raining)

    "You open back up for a moment, just to let the storm pass and get your new friend something to eat."
    "He waits for you at the counter."
    "He stares at the little written menu."
    "But not just that..."
    "He stares at the doodle of the little pancake."

    # Ahn's order (only 1 choice)
    char_shin "\"What can I get you?\""
    char_ahn "\"I don't feel like coffee... I don't want tea. I want something cold... to go with something warm and ... fluffy..\"" 
    char_ahn "\"What would you recommend?\""

    menu:
        "Milk & fluffy pancakes.":
            pass

    char_ahn "\"Mmmm.. my favorite...\""
    "You serve Ahn and watch him sit at a table in the corner by the window."
    "The cafe was empty anyway, so maybe some small talk wouldn't hurt."

    char_shin "\"I can join you, if You like.. You're my first customer! ^^.\""

    "Ahn nodded at you."
    "You sit down and reintroduce yourself, and talk about yourself."
    "A lot about yourself."
    "You talk and talk."
    "There was a moment when you pet his head."
    "Ahn would finish his meal and throw it away."
    
    char_ahn "\"Thank you for eating with me.. It was nice to learn about you.\""
    char_shin "\"Don't mention it! I'm new here, so I want to make as many friends as I can!\""
    char_ahn "\"Do you really plan to run this place by yourself?\""
    char_shin "\"Yeah, it would be nice to have a partner, but I'll manage.\""
    "\"Anyways, I have to close up!\""
    char_shin "\"You can have my umbrella, I have a spare one anyway!\""
    char_ahn "\"Thank you.\""
    char_shin "\"What a cute kid..\"" 
    char_ahn "\"See you soon...\""
    
    "Ahn would leave first with your umbrella."
    "It matched him in a way."
    "You take a deep breath."

    char_shin "\"What a day, time to close up now.\""

    "You close up shop and head home."

    "On your way home, you noticed a figure."
    "It was Tariro from earlier."

    # Tariro interaction 
    char_tariro "\"Hey chump! How's the cafe hangin'?\""
    char_shin "\"Doing as much as I can..\""
    char_tariro "\"It'll be alright! It's a new start ~!\"" 
    char_shin "\"I suppose you're right! I can only wish for the best.\""
    char_tariro "\"Speaking of wishing for the best..\"" 
    char_tariro "\"I've noticed someone lurking around the shop after you close.\""
    char_shin "\"Really?!\""
    char_tariro "\"Better make sure you lock up carefully!\""
    char_shin "\"I'll keep an eye out.\""

    "You wave your best friend goodbye as he walks the other direction."
    "With that, you proceed to head home."
    "You flop yourself on your bed."
    char_monologue "I hope things go well tomorrow. Big plans.. big..plans.."
    "You sleep till the next day."

label start_day_2:
    scene bg_black with dissolve
    "[[DAY 2]"

    "You would hear the loud ringing of an alarm."
    char_monologue "5 more minutes…"
    "You wait for 5 minutes, and then you get up."
    "You do your normal daily morning routine before heading off to your shop."

    scene bg_cafe_behind_counter_morning with dissolve #(temporary)
    "The bell would ring, a customer is here!"

    #Office Worker order
    "Office Worker" "\"I’m in a hurry!\""
    char_shin "\"What can I get you?\""
    "Office Worker" "\"Can I get a chocolate-like drink that can keep me up?\""

label d2_order1:
    #Random drink tba
    menu: 
        "Random Drink":
            "Office Worker" "\"This isn't what I wanted!!\""
            "Office Worker" "\"Whatever, I have to go!\""
        "Dark Chocolate Espresso":
            "Office Worker" "\"Thanks!\""
        "Random Drink":
            "Office Worker" "\"This isn't what I wanted!!\""
            "Office Worker" "\"Whatever, I have to go!\""
        "Random Drink":
            "Office Worker" "\"This isn't what I wanted!!\""
            "Office Worker" "\"Whatever, I have to go!\""

label d2_continue1:
    char_shin "\"Couldn’t imagine working in a hectic office again…\""
    "The bell would ring, a customer is here!"

    #Young Girl order
    "Young Girl" "\"Hello~! I didn't know if I could order or not!\""
    char_shin "\"What can I get you?"
    "Young Girl" "\"I want something cold and caramelly~ haha!\""

label d2_order2:
    #Random drink tba
    menu: 
        "Random Drink":
            "Young Girl" "\" Not exactly what I wanted, but it doesn't taste half bad..!\""
        "Random Drink":
            "Young Girl" "\" Not exactly what I wanted, but it doesn't taste half bad..!\""
        "Random Drink":
            "Young Girl" "\" Not exactly what I wanted, but it doesn't taste half bad..!\""
        "Iced Caramel Cappuccino":
            "Young Girl" "\"Mmm! Delish! I'll tell my friends about this place!\""

label d2_continue2:
    char_shin "\"I’ll get better eventually..\""
    "The bell would ring, a customer is here!"

    #Gamer order
    "Gamer" "\"I heard this was a new coffee place!\""
    char_shin "\"What can I get you?\""
    "Gamer" "\"Could I get something kinda like a black coffee that's kinda like a simple espresso but lighter?\""

label d2_order3:
    #Random drink tba
    menu: 
        "Random Drink":
            "Gamer" "\"Ugh, it tastes like a loss streak in Val.\""
        "Random Drink":
            "Gamer" "\"Ugh, it tastes like a loss streak in Val.\""
        "Caffé Americanó":
            "Gamer" "\"Thanks, maybe I'll bring my laptop here for gaming sesh!\""
        "Random Drink":
            "Gamer" "\"Ugh, it tastes like a loss streak in Val.\""

label d2_continue3:
    char_shin "\"Ha, I wish I could play games all day.\""
    "The bell would ring, a customer is here!"

    #Old Lady order
    "Old Lady" "\"What a fancy-looking cafe..\""
    char_shin "\"What can I get you?\""
    "Old Lady" "\"Hello sweetheart, can I have a tea drink and something spicy and crunchy with it?\""

label d2_order4:
    #Random drink tba
    menu: 
        "Random Drink":
            "Old Lady" "\"Not quite, but you've done your best.. Here you go.\""
        "Green Tea with Ginger cookies":
            "Old Lady" "\"Thank you dear, here's a tip.\""
        "Random Drink":
            "Old Lady" "\"Not quite, but you've done your best.. Here you go.\""
        "Random Drink":
            "Old Lady" "\"Not quite, but you've done your best.. Here you go.\""

label d2_continue4:
    char_shin "\"What a sweet lady…\""
    #Shift over
    "You take a deep breath."
    char_shin "\"What a day, time to close up now.\""
    "You close up shop and headed home.."
    "On your way home, you noticed a figure."
    "It was the Young Lady from earlier."

    #Young Lady side convo
    "Young Lady" "\"Oh hey, you’re that barista from that cafe!\""
    char_shin "\"Oh hey! What are you doing out here so late?\""
    "Young Lady" "\"Well, I’m just about to head home, just taking a shortcut!\""
    char_shin "\"Down there? Looks scary..\""
    "Young Lady" "\"Scary? I go that way every day! Don’t worry!\""
    char_shin "\" Well, I guess, be safe!\""
    "Young Lady" "\"Thanks! Good luck with the Cafe!\""
    char_shin "\"Thank you!\""
    "Young Lady" "\"I’ll def come by tomorrow!\""
    
    "You wave her goodbye as she disappears into the wooded trail."
    "With that, you proceed to head home."
    "You lie on your couch, too tired to head to your bed."
    "You sleep till the next day."

label start_day_3:
    scene bg_black with dissolve
    "[[DAY 3]"
    "You wake up before your alarm."
    char_monologue "Just a few more days to go. The goal is looking far but I feel like I can make it through."
    "You grab your keys and head down to your shop."
    "You open up shop."

    #Open up 
    scene bg_cafe_behind_counter_morning with dissolve
    "The bell would ring, a customer is here!"

    #Edgy Teen order
    "Edgy Teen" "\"Hey you, the dead have been waiting forever. Can I order now?\""
    char_shin "\"What can I get you?\""
    "Edgy Teen" "\"I want something gloomy and green. Got that spooky latte taste..\""

label d3_order1:
    #Random drink tba
    menu: 
        "Mocha Latte":
            "Edgy Teen" "\"Thanks.\""
            "Edgy Teen" "\"By the way.. There’s something stalking this place. I like it.\""
        "Random Drink":
            "Edgy Teen" "\"What’s this? Whatevs prolly why you’re cursed now..\""
        "Random Drink":
            "Edgy Teen" "\"What’s this? Whatevs prolly why you’re cursed now..\""
        "Random Drink":
            "Edgy Teen" "\"What’s this? Whatevs prolly why you’re cursed now..\""

label d3_continue1:
    char_shin "\"I really hope I didn’t get cursed just now…\""
    "The bell would ring, a customer is here!"

    #Police officer order
    "Police officer" "\"Good afternoon young man.\""
    char_shin "\"What can I get you?\""
    "Police officer" "\"I’d like the usual snack and the warm drink. Yknow wink wink.\""

label d3_order2:
    #Random drink tba
    menu: 
        "Random Drink":
            "Police officer" "\"What about the donuts? :C\""
        "Random Drink":
            "Police officer" "\"What about the donuts? :C\""
        "Random Drink":
            "Police officer" "\"What about the donuts? :C\""
        "Coffee and Sprinkle Donut":
            "Police officer" "\"That's refreshing! Back to duty.\""

label d3_continue2:
    char_shin "\"Maybe police cliche stereotypes are true ..\""
    "The bell would ring, a customer is here!"

    #Karen order
    "Karen" "\"You there! Are you finally taking my order?\""
    char_shin "\"What can I get you?\""
    "Karen" "\"About time, I want a pumpkin drink that is extra creamy and I DON'T want it cold. Make sure to make it extra drizzly and not just that, make sure it is a LARGE. Did you get all of that?\""
    "Karen" "\"Oh and a bagel but like not normal bagel, give it some flavor.\""

label d3_order3:
    #Random drink tba
    menu: 
        "Random Drink":
            "Karen" "\"Is this a joke? I demand to speak to your manager!\""
        "Random Drink":
            "Karen" "\"Is this a joke? I demand to speak to your manager!\""
        "Extra Large Pumpkin spice latte with caramel drizzle and extra cream no ice and a raisin bagel":
            "Karen" "\"I’ll be leaving a 4 star review. Your manager would be proud of that!\""
        "Random Drink":
            "Karen" "\"Is this a joke? I demand to speak to your manager!\""

label d3_continue3:
    char_shin "\"I am.. The manager..\""
    "The bell would ring, a customer is here!"

    #Office worker Lady order
    "Office worker lady" "\"Hey, you!\""
    char_shin "\"What can I get you?\""
    "Office worker lady" "\"I need a drink for the boss, STAT. Something roasted but not too much.\""

label d3_order4:
    #Random drink tba
    menu: 
        "Random Drink":
            "Office worker lady" "\"You must like your job if it’s to dissatisfy people.\""
        "Random Drink":
            "Office worker lady" "\"You must like your job if it’s to dissatisfy people.\""
        "Random Drink":
            "Office worker lady" "\"You must like your job if it’s to dissatisfy people.\""
        "Light Roast":
            "Office worker lady" "\"Good Job kid, maybe you’ll get a tip next time.\""

label d3_continue4:
    #Shift over
    "You take a deep breath."
    char_shin "\"What a day, time to close up now.\""

    "You close up shop and head home."
    "On your way home, you noticed a figure."
    "It was the police officer from earlier."

    #Police officer side convo
    #Screen bg: Side street, evening.
    #Sprite PNG: Nervous Shin.

    "Police officer" "\"You there!\"" 
    char_shin "\"Me????\""
    "Police officer" "\"Have you noticed anything strange lately around these parts?\""
    char_shin "\"Not that I can think of, sir…\""
    "Police officer" "\"Well, please let me know if you do, people have gone missing, and I had to see one of them be you.\""
    char_shin "\"Got it…\""
    "Police officer" "\"Oh yeah, if you could, I would buy maybe 2 dozen of your donuts and send them to the station!\""
    char_shin "\"Sure! I can do that.\""

    "You wave the officer goodbye as he walks the other direction."
    char_monologue "Strange.. I haven't seen Tariro in a while either.."
    char_monologue "Maybe I should visit him tomorrow.."
    "With that, you proceed to head home."
    "You flop yourself on your bed."
    "You sleep till the next day."

label start_day_4:
    scene bg_black with dissolve
    "[[DAY 4]"
    #Screen bg: Shin’s Living room
    "You wake up the next morning before you go to work to check on your friend."

    #Screen Bg: Tariro’s house outside.
    "You would arrive at his front door."
    "You knocked a lot."
    "No response."

    #Sprite PNG: Nervous Shin. 
    char_shin "\"Hmmm..\""
    char_monologue "Stange.."
    char_monologue "Normally, he’d answer by now."
    char_monologue "Maybe I should look around for his spare key.."
    char_monologue "I’m sure it was around somewhere"

    "You looked around the porch for anything."
    char_monologue "If I’m not mistaken… He put the spare under something."

label choice_d4:
    menu:
        "Check in plant pot":
            "It's not there. Let's find somewhere else."
            jump choice_d4
        "Check under the rug":
            pass
        "Check mailbox":
            "It's not there. Let's find somewhere else."
            jump choice_d4

    #Screen Bg: Tariro’s house inside.
    "You open the door to find an empty house."
    char_monologue "It’s so quiet here…"
    "You would call out for your friend."
    "No response."
    char_monologue "Maybe he's on a trip? But surely, he'd never just leave without saying anything."
    "You leave the house, locking up behind you before heading to work."
    char_monologue "Still strange.."

    "You head to work and open up shop."
    #Screen bg: Cafe behind counter morning
    #Open shop
    "The bell would ring, a customer is here!"

    #Hippie guy order
    "Hippie Guy" "\"Yuh dude, can I get a coffee?\""
    char_shin "\"What can I get you?\""
    "Hippie Guy" "\"I kinda want uhhhh… I dunno, an earthy drink.. Know like the thing that uhh, grows in the forest. The shrooms feeling y’know?\""

label d4_order1:
    #Random drink tba
    menu: 
        "Random Drink":
            "Hippie Guy" "\"Uhhhh, can’t complain, not exactly what I wanted.. Thanks, though.\""
        "Random Drink":
            "Hippie Guy" "\"Uhhhh, can’t complain, not exactly what I wanted.. Thanks, though.\""
        "Random Drink":
            "Hippie Guy" "\"Uhhhh, can’t complain, not exactly what I wanted.. Thanks, though.\""
        "Mushroom Latte":
            "Hippie Guy" "\"Tots earthy my dudddeee.\""

label d4_continue1:
    Shin : "\"What an earthy guy, huh?\""

    "The bell would ring, a customer is here!"
    
    #Biker order
    "Biker" "\"....\""
    char_shin "\"What can I get you?\""
    "Biker" "\"Dark.\""

label d4_order2:
    #Random drink tba
    menu: 
        "Random Drink":
            "Biker" "\"Ough..!\""
        "Dark Coffee":
            "Biker" "\"Thanks..\""
        "Random Drink":
            "Biker" "\"Ough..!\""
        "Random Drink":
            "Biker" "\"Ough..!\""

label d4_continue2:
    char_shin "\"That was scary..\""


    "The bell would ring, a customer is here!"

    #Wizard guy order
    "Wizard guy" "\"Yoddles!!\""
    char_shin "\"What can I get you?\""
    "Wizard guy" "\"Skibbidity yoinky slorpy big bonkers morking 6 7 among us glorp glorp meowdy!\""

label d4_order3:
    #Random drink tba
    menu: 
        "Clorp Drink":
            "Wizard guy" "\"Thanks, man.\""
        "Random Drink":
            "Wizard guy" "\"Grrrrrrrr! Fire bal-\""
        "Random Drink":
            "Wizard guy" "\"Grrrrrrrr! Fire bal-\""
        "Random Drink":
            "Wizard guy" "\"Grrrrrrrr! Fire bal-\""

label d4_continue3:
    char_shin "\"What on earth is happening in this game..\"" #(Don’t ask me - Dev; idek what is going on lmao - waffle)

    "The bell would ring, a customer is here!"

    #Young Man order
    "Young Man" "\"Hey there, my girlfriend came here once, could I order something?\""
    char_shin "\"What can I get you?\""
    "Young Man" "\"There’s this like Earl gay Ethiopian like drink she got me into.. Do you have something like that?\""

label d4_order4:
    #Random drink tba
    menu: 
        "Random Drink":
            "Young Man" "\"Ugh… This is not even close to what I wanted.\""
        "Random Drink":
            "Young Man" "\"Ugh… This is not even close to what I wanted.\""
        "Yirgacheffe Earl Grey Brew":
            "Young Man" "\"Thanks, I can’t wait to get this more.\""
        "Random Drink":
            "Young Man" "\"Ugh… This is not even close to what I wanted.\""

label d4_continue4:
    char_shin "\"So jealous.. When’s my turn to get a partner?\""

    "As you wait for any more customers, you decide to clean up."
    "You sweep up the floor."
    "You hear the bell and turn to see who."
    "It’s Ahn."
    "Wiping his cheek."

    #Ahn side convo 2
    char_ahn "\"You’re here..!\""
    char_shin "\"Uh.. yeah? Glad to see you’re okay!\""
    char_shin "\"There have been a lot of people going missing recently after all!\""
    char_ahn "\"... I know.\""
    char_shin "\"Oh, you do?\""
    char_ahn "\"I heard on the news, of course. It’s best to be with someone in times like this, y’know?\""
    "He’d smiled with his hands behind his back."
    char_shin "\"You’re right, haha, it’s not the best to be alone at this time.\""
    char_ahn "\"So now what....\""
    char_shin "\"Don't know....\""
    char_shin "\"Would you like to come in for pancakes again? I noticed you really liked them the first time I made them..!\""
    char_ahn "\"Of course!\""
    char_ahn "\"Lead the way..\""

    "You finished up cleaning and led the way to taking Ahn’s order."
    "You sit and talk about yourself while Ahn eats."
    "And he just listens all the way through."
    "Guess someone likes hearing about your endless rambles about pointless things."
    "After a while, Ahn would leave."
    "The store would be quiet again."
    "You take a deep breath."
    char_shin "\"What a day, time to close up now.\""


    "You close up shop and head home.."
    "On your way home, you noticed a figure."
    "It was Hippie from earlier."
    
    #Hippie guy side convo
    char_hippie "\"Yoooo dudeeee!\""
    char_shin "\"Uhhh, you okay?\""
    char_hippie "\"Yahhhh, I just heard some weirdddddddd noises, my man..\""
    char_hippie "\"Maybe my head is spin’n buttttt it was like spokayyyy\""
    char_shin "\"Uhh.. get home safe, dude. Drink some water.\""

    "As the guy left, wobbling away."
    "You thought about what he said."
    char_monologue "With everything going on.. Maybe…"

    "What would you do?"
    menu:
        "Investigate":
            jump investigate
        "Go home":
            jump go_home

label go_home:
    char_monologue "I shouldn’t think too much about it."
    "You shake your head and sigh."
    "You proceed to head home."
    "You flop yourself on your couch, too lazy to go to your bed."
    "You sleep till the next day."

    #Day end.

label start_day_5:
    scene bg_black with dissolve
    "[[DAY 5]"
    #Scene Shin living room
    char_monologue "Well, today’s the last day to make the goal."
    "I pray today will be a good day."

    "You head to work and open up shop."
    "You were ready, you were energized."
    "Motivated!"
    char_monologue "Come on Shin! The goal is so close!!"

    #Screen bg: Cafe behind counter (morning)
    "The bell would ring, a customer is here!"

    #Blogger’s order
    "Blogger" "\"Yo people~! We are checking out the new cafe! What should we get chat?\""
    char_shin "\"What can I get you?\""
    "Blogger" "\"Uhhh, let’s see, chat is saying frap, purple color, iced?\""

label d5_order1:
    #Random drink tba
    menu: 
        "Random Drink":
            "Blogger" "\"And that’s a thumbs down, guys! Beware chat!\""
        "Random Drink":
            "Blogger" "\"And that’s a thumbs down, guys! Beware chat!\""
        "Random Drink":
            "Blogger" "\"And that’s a thumbs down, guys! Beware chat!\""
        "Ube Frappuccino":
            "Blogger" "\"We gotta winner chat! Can we get some gifted subs!! And some donos to the baristiaaaaaa!\""

label d5_continue1:
    char_shin "\"Are you.. Are you talking to me?\""

    "The bell would ring, a customer is here!"

    #Drag Queen order
    "Drag Queen" "\"Hello, darling!\""
    char_shin "\"What can I get you?\""
    "Drag Queen" "\"I want a latte with some passion.\""

label d5_order2:
    #Random drink tba
    menu: 
        "Random Drink":
            "Drag Queen" "\"Oh girl, this is not it.\""
        "Passion Fruit Latte":
            "Drag Queen" "\"Thank you baby.\""
        "Random Drink":
            "Drag Queen" "\"Oh girl, this is not it.\""
        "Random Drink":
            "Drag Queen" "\"Oh girl, this is not it.\""

label d5_continue2:
    char_shin "\"What a Diva..\""

    "The bell would ring, a customer is here!"

    #Art Teacher’s order
    "Art teacher" "\"Yohoo~ A student suggested this place. Can I order?\""
    char_shin "\"What can I get you?\""
    "Art teacher" "\"I was wondering if I could get a latte that’s kinda flowery but cookie-like..?\""

label d5_order3:
    #Random drink tba
    menu: 
        "Lotus Biscoff Latte":
            "Art teacher" "\"Thanks, maybe I'll come here more for a doodle sesh.\""
        "Random Drink":
            "Art teacher" "\"I'll draw you pregnant.\"" #(Holy mpreg *rubbing hands*- waffle)
        "Random Drink":
            "Art teacher" "\"I'll draw you pregnant.\""
        "Random Drink":
            "Art teacher" "\"I'll draw you pregnant.\""

label d5_continue3:
    char_shin "\"She reminds me of my past of sketch books.\""
    "The bell would ring, a customer is here!"

    #Traveler’s order
    "Traveler" "\"Hello! Are you still open?\""
    char_shin "\"What can I get you?\""
    "Traveler" "\"I’m traveling from Vietnam, and I want something close to home!\""

label d5_order4:
    #Random drink tba
    menu: 
        "Random Drink":
            "Traveler" "\"Oh… well this isn’t … well this isn't so bad.. But not what I wanted.\""
        "Random Drink":
            "Traveler" "\"Oh… well this isn’t … well this isn't so bad.. But not what I wanted.\""
        "Vietnamese Coffee":
            "Traveler" "\"Mmmmm, just like home.\""
        "Random Drink":
            "Traveler" "\"Oh… well this isn’t … well this isn't so bad.. But not what I wanted.\""

label d5_continue4:
    char_shin "\"I hope she stays safe traveling.\""

    #Shift over 

    "You start to clean up the cafe, then head outside to lock up the shop."
    "As you close up, you can hear faint footsteps approaching you."
    "You turn around to see who it is."
    "Ahn?"
    "He’s running towards you and waving."

    #Ahn’s side convo and confession 
    #Screen side street
    char_ahn "\"Shin!\""
    char_shin "\"Oh, Ahn! You startled me a bit!\""
    char_shin "\"What's up?\""
    char_ahn "\"Are you about to close up?\""
    char_shin "\"It would appear so, yeah.\""
    char_ahn "\"I was wondering if I could help.\""
    char_shin "\"I don’t see why not!\""
    char_ahn "\"I was also wondering if I could do more.\""
    char_shin "\"Oh? What do you mean by more?\""
    char_ahn "\"Shin Eyofumi, I want to go out with you.\""
    char_shin "\"Oh!\""

    #Accept Ahn’s feelings.
    #Reject Ahn’s feelings.
    
    #Temporary replacement:
    menu:
        "Money reached + accept":
            jump good_end
        "Money reached + reject (assuming it is same as \"money not reached + reject\")": #(assuming it is same as "money not reached + reject")
            jump bad_end2
        "Money not reached + accept":
            jump bad_end1
        "Money not reached + reject":
            jump bad_end2
        
label good_end:
    "You accept Ahn’s feelings."

    char_shin "\"It would be nice to have a helping hand and some romance in the workplace.. I don’t see why not.\""
    char_ahn "\"Really?? You mean it?\""
    char_shin "\"Yeah, plus, I think you’re really cute.\""
    char_ahn "\"Heh, you’re cute too.\""
    char_shin "\"Let’s go out!\""
    char_ahn "\"With pleasure!\""
    char_ahn "\"If anyone looks at you funny, I’ll make them go missing.\""
    char_shin "\"What?\""
    char_ahn "\"Just Kidding ~.\""

    #cutscene

    char_shin "\"A few people have stopped going missing after I hired Ahn to work alongside me.\""
    char_shin "\"And now… Well, I got a boyfriend and a successful running business.\""
    char_shin "\"Couldn’t ask for anything more.\""
    char_shin "\"Though I can’t shake the feeling I’m forgetting something.\""

    "You accepted Ahn without investigating anything and got all orders right."
    
    return

label bad_end1:
    "You accept Ahn’s feelings."

    char_shin "\"It would be nice to have a helping hand and some romance in the workplace.. I don’t see why not.\""
    char_ahn "\"Really?? You mean it?\""
    char_shin "\"Yeah, plus, I think you’re really cute.\""
    char_ahn "\"Heh, you’re cute too.\""
    char_shin "\"Let’s go out!\""
    char_ahn "\"With pleasure!\""
    char_ahn "\"If anyone looks at you funny, I’ll make them go missing.\""
    char_shin "\"What?\""
    char_ahn "\"Just Kidding ~.\""

    "When the time came to check how much you made.."
    "You didn’t make much."
    "Not even close to the goal.."

    char_shin "\"I should have paid more attention to what customers were ordering..\""
    char_shin "\"Guess it’s back to the office life…\""

    "You managed to get all the orders wrong.. how…"

    #cutscene

    return

label bad_end2:
    "You reject Ahn’s feelings."

    char_shin "\"I’m sorry, but I don’t think I can accept your feelings. Things have been hectic, and I don’t think I can.\""
    char_ahn "\"I see..\""
    char_ahn "\"That’s disappointing.\""
    char_ahn "\"I was hoping things would turn out differently.\""
    char_shin "\"What?\""
    char_ahn "\"I’m sorry.\""
    char_shin "\"Sorry?\""
    char_shin "\"Augh!\""
    "You feel a sharp pain in your side as you’re pushed against the glass."
    "Ahn would lean his head into your chest."
    char_ahn "\"I didn’t want to have to hurt you, but you leave me no choice.\""
    char_shin "\"Ugh.. Why..?\""
    char_ahn "\"I can’t let anyone else have you.\""
    char_ahn "\"You. are. Mine.\""

    "With that, everything faded to black."
    "When you wake up, lying against the table inside the cafe."
    "You could hear noises in the background"
    "You turned to see Ahn smiling at you."
    "He’d wave at you as your lashes fluttered close."

    char_shin "\"Augh… This sucks.\""
    char_shin "\"Maybe I should’ve thought about it first.\""

    "You broke Ahn’s heart and your wallet."

    return

label investigate:
    "You walk down the strange path to find a trail of blood leading to what you never thought you would see."
    "You see the dead bodies of a few customers and your best friend."
    "Dead."
    "All of them are dead."
    "You pat yourself down to check for your phone."

    char_shin "\"Damnit..!\""

    char_monologue "How could I leave my phone at home at a time like this??? I have to hurry back!!"

    "You start to run home."
    "You would bust into your house trying to look for your phone, but you couldn't find it."
    "It wasn't in your room."
    "It wasn't in your bathroom."
    "It wasn't in your living room."
    "You stop in the kitchen."
    "You see a plate of pancakes with blood on top of it."
    "You stare at it for a moment before feeling your heart sink."
    "You hear a creak behind you."
    "You attempt to turn around, but as soon as you do, everything fades to black."

    "You wake up to see your legs and arms tied to a chair."
    "You hear faint footsteps approaching you."
    "You see Ahn as you look up."
    "He smiles at you, mischievously."
    "Ahn would sit in front of you, close to your face."

    #Side convo with Ahn
    "You groaned before looking up to see a cute smiling face."
    char_ahn "\"I’m sorry, did I hurt you? I hope it didn’t hurt you too badly?\""
    char_shin "\"Ugh.. what happened…?\""
    char_ahn "\"I hit you upside the head with a frying pan! :D\"" 
    char_shin "\"WHAT?! WHY WOULD YOU DO THAT???\""
    char_ahn "\"To stop you, of course.\""
    char_shin "\"STOP ME?? FROM DOING WHAT???\""
    char_ahn "\"Calling the police.\""
    char_shin "\"Why would you stop me from calling the…\""
    char_shin "\"Ahn, did you… kill all those people?\""
    char_ahn "\"Well… I wouldn't say I didn’t.\""
    char_shin "\"WHAT???\""
    char_ahn "\"I don't know~ I just had to make sure to take out anyone who got in my way..\""
    char_shin "\"In your way of what?\""
    char_ahn "\"Taking you away from me.\""
    char_shin "\"What…?\""
    char_ahn "\"I like you, Shin Eyofumi.\""
    char_shin "\"What on Earth..\""
    char_ahn "\"Be mine, Shin.\""
    char_shin "\"I…\""

    menu:
        "Accept Ahn’s feelings":
            jump neutral_end
        "Reject Ahn’s feelings":
            jump bad_end3

label neutral_end:
    "You accepted his confession, feeling uneasy."

    "You sighed."
    char_shin "\"I’ll accept you under one condition.\""
    "Ahn would get excited."
    char_ahn "\"Really?? You won’t tell on me?!\""
    char_shin "\"I can’t be certain, but just as long as you promise not to hurt anyone anymore.\""
    char_ahn "\"Mmm…\""
    char_shin "\"Please? I need the customers.\""
    char_ahn "\"Fine, but if anyone tries to take you away from me, I’ll kill them.\""
    char_shin "\"I... fine. Tell you what! You can work with me!\""
    char_ahn "\"That’s perfect!\""
    char_ahn "\"That way I could be under you..and watch..\""
    char_shin "\"Ahnnn…\""
    char_ahn "\"Fine... but you’re my boyfriend now. If anyone tries-\""
    char_shin "\"I get it. Now, may I please be untied? It kinda hurts.\""

    "He untied you."
    "You knew it was a bad idea to test him, after all the bodies."
    "You went back to the cafe with Ahn."
    "Days would go by with Ahn by your side."
    "Everything felt on edge, but still going swiftly."
    "Customers would come and go, but still…"
    "There was an unsettling feeling in the air."

    char_shin "\"I still feel uneasy with Ahn.\""
    char_shin "\"The business is booming and all, but I still can't help but get worried about everything.. about him.\""
    char_shin "\"Just as long as he's happy and not hurting people, I'll be alright… right..?\""

    "You reach the goal and accept Ahn's confession, knowing what he’s done."

    return

label bad_end3:
    "You reject Ahn’s feelings."

    "You sighed."

    char_shin "\"No, you’ve hurt people! I could never like someone hurting people.\""
    "Ahn's face would drop."
    char_ahn "\"That… disappointing.\""
    char_shin "\"If you like me, you turn yourself in and let me go.\""
    char_ahn "\"I can’t do that, Shin..\""
    char_ahn "\"I can’t have you leave me either.\""
    "Ahn would sigh before sitting on your lap."
    "He’d put his head to your chest."
    char_shin "\"What are you doing?\""
    char_ahn "\"Making sure you’ll never leave me.\""
    char_shin "\"Ahn..?\""
    "He'd shake his head before stabbing you in the gut."
    "You feel a sharp pain in your side."
    "That's going to leave a mark in the morning."
    char_ahn "\"You are mine.\""

    "You start to feel dizzy."
    "Ahn would untie you and leave you on the ground."
    "Your eyes would flutter open for just a moment."

    char_shin "\"Where did I go wrong?\""
    char_shin "\"I really should've mined my business.\""
    char_shin "\"Just my luck,\""

    "Investigating and rejecting Ahn was a bad way to go."

    return