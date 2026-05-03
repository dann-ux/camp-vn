label start_game:
    scene bg_camp with fade
    "The bus pulls up to the camp gates."
    "You step out, your bag slung over your shoulder, ready for the summer."
    jump camp_loop

label camp_loop:
    "Day [camp_day] at Pine Ridge Summer Camp."
    
    menu:
        "Explore the lake":
            call lake_area
            $ camp_day += 1
            jump camp_loop
        "Check the cabins":
            call cabin_area
            $ camp_day += 1
            jump camp_loop
        "Visit the main lodge":
            call lodge_area
            $ camp_day += 1
            jump camp_loop
        "Go to sleep":
            "You turn in early. Tomorrow will bring new friends and new stories."
            return

label lake_area:
    scene bg_camp with dissolve
    "The lake sparkles under the morning sun. A young fox kid is carefully picking out flat stones near the water."
    show fox1 at center with moveinright
    fox1 "Hey! I'm practicing my stone skips. Want to try?"
    menu:
        "Take a turn":
            "You find a smooth stone and give it your best throw."
            fox1 "Nice arc! We should practice together tomorrow."
            $ fox1_friendship += 2
        "Polite decline":
            fox1 "No worries! Maybe later."
            $ fox1_friendship += 0
    hide fox1 with moveoutleft
    return

label cabin_area:
    scene bg_camp with dissolve
    "The cabin smells like pine and fresh wood. A golden retriever kid is organizing a neat stack of trading cards."
    show dog1 at center with moveinright
    dog1 "Hi there! I'm sorting my deck. Do you like trading cards?"
    menu:
        "Ask to see them":
            dog1 "Check out this one! It's rare. We could swap if you want!"
            $ dog1_friendship += 2
        "Say hi and step away":
            dog1 "Cool. Catch you around!"
            $ dog1_friendship += 0
    hide dog1 with moveoutleft
    return

label lodge_area:
    scene bg_camp with dissolve
    "The main lodge is quiet. A tabby cat kid is curled up in an armchair, deeply focused on a thick storybook."
    show cat1 at center with moveinright
    cat1 "Just a moment... I'm at the best part. It's about a camp for magical animals."
    menu:
        "Ask about the book":
            cat1 "Oh! It says the real magic happens when you make friends. Want to read it together later?"
            $ cat1_friendship += 2
        "Give them space":
            cat1 "Thanks. See you around."
            $ cat1_friendship += 0
    hide cat1 with moveoutleft
    return
