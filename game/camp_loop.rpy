# CAMP LOOP

label start_game:
    "The bus pulls up to the camp gates."
    "You step out, bag over your shoulder, ready for the summer."
    jump camp_loop

label camp_loop:
    "Day [camp_day] at camp."
    menu:
        "Explore the lake":
            "You head down to the lake. The water sparkles."
            $ camp_day += 1
            jump camp_loop
        "Check the cabin":
            "You walk back to your cabin. It smells like pine."
            $ camp_day += 1
            jump camp_loop
        "Go to sleep":
            "You turn in early. Tomorrow will be another day."
            return
