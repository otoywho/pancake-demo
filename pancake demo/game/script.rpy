label start:

    scene bg_black

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

    jump tutorial_order

    return

    # (Tariro TUT order)
label tutorial_order:
    menu:
        "Hot Chocolate":
            char_tariro "\"See? You got it! Now let's see how you do tomorrow!\""
            jump tutorial_continue

        "Espresso":
            jump tutorial_wrong_answer

        "Milk":
            jump tutorial_wrong_answer

        "Americanó":
            jump tutorial_wrong_answer

    return

label tutorial_wrong_answer:
    char_tariro "\"Nope, but thankfully this is just a test.\""
    jump tutorial_order

    return

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

    return

label start_day_2:

    return