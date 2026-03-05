# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg idk

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    shn "(How did this all start...)"
    shn "(Right, I quit my job.)"
    shn "(The office life was way too hectic for me.)"
    shn "(I wanted to try something different.)"
    shn "(I may have used… a lot of my savings to get this new place…)"
    shn "(But, it feels like a good fresh start.)"
    shn "(This place is 2 blocks away from my new apartment so it’s really convenient.)"
    shn "(Enough inner chattering, it's time for me to officially head to work.)"

    "You would walk to the new shop that you had bought with the rest of your savings."
    "It's starting to become a bit cloudy."
    "You see your friend, Tariro waving at you at the entrance of the cafe."
    "As soon as you greet Tariro you head inside."

    trr "Look at this place!"
    shn "I know, it took quite a bit to get it!"
    trr "I bet it did!" 
    trr "So how do you plan on taking orders?"
    shn "Uhm... Hi, welcome to Chilli's?"
    trr "WHAT?? NO!!"
    trr "I'm going to be your practice for you so you can be ready for tomorrow!" 
    trr "Customers will give you descriptions on the types of drinks they want!"
    trr "You get only 1 chance to get their drinks right."
    trr "Let's give it a try."
    trr "I want a warm milky drink that also tastes chocolatey with marshmallows!"

    menu:
        "Hot Chocolate":
            trr "See? You got it! Now let's see how you do tomorrow!"
        "Espresso":
            trr "Nope but thankfully this is just a test!"
        "Milk":
            trr "Nope but thankfully this is just a test!"
        "Americanó":
            trr "Nope but thankfully this is just a test!"

    trr "Just remember to pay attention to what the customers are saying! Good luck!"
    shn "Thanks Tari… I'll need it for sure.."
    trr "Well, you'll get used to it eventually!"
    trr "It's getting ready to storm, I'm going to head home don't forget to close up!"
    shn "Yeah, I know."

    "You and Tariro waved to each other goodbye."
    "The cafe would be silent."
    "You’d take a deep breath, enjoying the silence."
    shn "To a new start for me.. What could go wrong?"
    "There would be a loud roar of thunder outside as soon."
    "The rain would start to pour."
    shn "(Guess I should close up and head home.)"
    "You grab your umbrella and head outside to close up shop."
    "As you were about to close up you see someone on the crub, sitting in the rain."
    "You hesistated before approaching them with the umbrella."
    "He'd looked up at you, like a wet dog who got caught doing nothing."
    "You's squat down to his level, holding out your umbrella cover him."
    shn "Are you okay?"

    #ahn's first interaction started

    # This ends the game.

    return
