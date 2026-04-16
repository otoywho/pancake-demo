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
    "Police officer" "\"I’d like the usual snack and the warm drink. Yknow wink wink. \""

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

    return