label start_game:
    scene bg_camp with fade
    "The bus pulls up to the camp gates."
    "You step out, your bag slung over your shoulder, ready for the summer."
    jump camp_loop

label camp_loop:
    python:
        current_phase = store.current_phase if hasattr(store, "current_phase") else "morning"
        store.current_phase = current_phase

    "Day [camp_day] - [current_phase.title()] at Pine Ridge Summer Camp."
    
    menu:
        "Explore the lake":
            if current_phase == "evening":
                "The lake is too dark to explore safely right now."
                jump camp_loop
            call lake_area
            jump phase_transition
        "Check the cabins":
            call cabin_area
            jump phase_transition
        "Visit the main lodge":
            call lodge_area
            jump phase_transition
        "Rest and wait":
            "You take a quiet moment to yourself."
            jump phase_transition
        "Go to sleep":
            if current_phase != "evening":
                "It's too early to sleep. The sun is still up."
                jump camp_loop
            "You turn in early. Tomorrow will bring new friends and new stories."
            $ camp_day += 1
            $ store.current_phase = "morning"
            jump camp_loop

label phase_transition:
    python:
        if store.current_phase == "morning":
            store.current_phase = "afternoon"
        elif store.current_phase == "afternoon":
            store.current_phase = "evening"
        else:
            store.current_phase = "morning"
            store.camp_day += 1
    jump camp_loop
label lake_area:
    scene bg_camp with dissolve
    if fox1_relationship <= -10:
        "You spot Fox Kid 1 by the water. They cross their arms and look away when you approach."
        show fox1 at center with moveinright
        fox1 "Don't bother me."
        hide fox1 with moveoutleft
        return
    elif fox1_relationship > 10:
        "Fox Kid 1 waves you over excitedly."
        show fox1 at center with moveinright
        fox1 "Hey! You're just in time. Want to try skipping stones together?"
        menu:
            "Join them":
                "You spend the afternoon laughing and practicing."
                $ fox1_relationship += 3
                $ fox1_saw_stone_skip = True
            "Decline gently":
                fox1 "Alright, catch you later!"
                $ fox1_relationship += 0
        hide fox1 with moveoutleft
        return
    else:
        "A young fox kid is carefully picking out flat stones near the water."
        show fox1 at center with moveinright
        fox1 "Hey! I'm practicing my stone skips. Want to try?"
        menu:
            "Take a turn":
                "You find a smooth stone and give it your best throw."
                fox1 "Nice arc! We should practice together tomorrow."
                $ fox1_relationship += 2
                $ fox1_saw_stone_skip = True
            "Polite decline":
                fox1 "No worries! Maybe later."
                $ fox1_relationship += 0
        hide fox1 with moveoutleft
        return

label cabin_area:
    scene bg_camp with dissolve
    if dog1_relationship <= -10:
        "Dog Kid 1 is inside, but closes the door slightly when they see you."
        show dog1 at center with moveinright
        dog1 "I'm busy right now."
        hide dog1 with moveoutleft
        return
    elif dog1_relationship > 10:
        "Dog Kid 1 pats the empty spot next to them on the bunk."
        show dog1 at center with moveinright
        dog1 "Look what I found! Rare holographic cards. Want to trade?"        menu:
            "Trade fairly":
                "You both swap cards and chat about your favorite games."
                $ dog1_relationship += 3
                $ dog1_shared_cards = True
            "Say you're not interested":
                dog1 "Oh... okay. Maybe later."
                $ dog1_relationship -= 1
        hide dog1 with moveoutleft
        return
    else:
        "A golden retriever kid is organizing a neat stack of trading cards."
        show dog1 at center with moveinright
        dog1 "Hi there! I'm sorting my deck. Do you like trading cards?"
        menu:
            "Ask to see them":
                dog1 "Check out this one! It's rare. We could swap if you want!"
                $ dog1_relationship += 2
                $ dog1_shared_cards = True
            "Say hi and step away":
                dog1 "Cool. Catch you around!"
                $ dog1_relationship += 0
                $ dog1_was_ignored = True
        hide dog1 with moveoutleft
        return

label lodge_area:
    scene bg_camp with dissolve
    if cat1_relationship <= -10:
        "Cat Kid 1 is reading in the corner. They pull their knees up when you enter."
        show cat1 at center with moveinright
        cat1 "Please be quiet."
        hide cat1 with moveoutleft
        return
    elif cat1_relationship > 10:
        "Cat Kid 1 looks up from their book with a small smile."
        show cat1 at center with moveinright
        cat1 "I saved a page for you. It's about a camp where kids learn to talk to animals."
        menu:
            "Read together":
                "You sit close and read aloud together. It feels peaceful."
                $ cat1_relationship += 3
                $ cat1_read_together = True
            "Ask what it's about":
                cat1 "It's a secret. You have to earn it."
                $ cat1_relationship += 0
        hide cat1 with moveoutleft
        return
    else:
        "A tabby cat kid is curled up in an armchair, deeply focused on a thick storybook."        show cat1 at center with moveinright
        cat1 "Just a moment... I'm at the best part. It's about a camp for magical animals."
        menu:
            "Ask about the book":
                cat1 "Oh! It says the real magic happens when you make friends. Want to read it together later?"
                $ cat1_relationship += 2
                $ cat1_read_together = True
            "Give them space":
                cat1 "Thanks. See you around."
                $ cat1_relationship += 0
                $ cat1_was_disturbed = True
        hide cat1 with moveoutleft
        return
