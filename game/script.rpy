# MAIN GAME ENTRY

define p = Character("You")

label start:

    $ init_relationships()
    $ time_phase = "morning"
    $ current_day = 1

    scene black

    "Summer Camp has just begun."

    "You arrive at the campgrounds surrounded by trees and distant voices of other kids."

    "This will be your home for the next weeks."

    label day_loop:

        $ phase_text = get_phase_text()

        scene black
        "[phase_text]"

        if time_phase == "morning":

            "Kids are waking up and gathering outside."

            "New faces are everywhere."

            $ add_memory("system", "Day started - morning phase")

        elif time_phase == "activity":

    "The kids gather for a group activity."

    $ results = trigger_activity_scene()

    for r in results:
        "[r]"

    "Small moments of play and confusion happen naturally."

    $ add_memory("system", "Activity phase interactions occurred")

        elif time_phase == "freeplay":

            "No strict rules now. Kids move freely."

            "This is where friendships begin forming."

            $ add_memory("system", "Freeplay phase started")

        elif time_phase == "night":

            "The day slows down."

            "Kids gather quietly before sleep."

            $ add_memory("system", "Night phase started")

        menu:
            "What do you do?"

            "Continue":
                $ next_phase()
                jump day_loop

            "End test":
                return
