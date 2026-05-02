# CAMP LOOP SYSTEM
label camp_loop:

    p "We are now in the camp."
    p "The daily camp activities can begin."

    $ kids = [p, ann]
    $ event_description = format_scene(kids, "freeplay")
    p event_description

    $ add_memory(p, "entered camp loop") # Example memory addition

    menu:
        "Wander around camp":
            p "I will wander around camp."
            jump camp_loop
        "Think about something else":
            p "I need a moment to think."
            jump camp_loop
