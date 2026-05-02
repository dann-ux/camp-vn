# CAMP LOOP SYSTEM
label camp_loop:

    p "We are now in the camp."
    p "The daily camp activities can begin."

    $ kids = [p, ann]
    $ event_description = format_scene(kids, "freeplay")
    p event_description

    menu:
        "Wander around camp":
            p "I will wander around camp."
            jump camp_loop
        "Think about something else":
            p "I need a moment to think."
            jump camp_loop
