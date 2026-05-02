label lake_scene:

    $ kids = scene_kids(2)

    if len(kids) < 2:
        jump missing_scene

    $ a = kids[0]
    $ b = kids[1]

    python:
        arc = None
        if "check_story_arcs" in globals():
            arc = check_story_arcs(kids)

    if arc:
        call expression arc
        $ next_phase()
        jump day_loop

    "You reach the lake."
    "The water is still, but the air feels alive."

    $ say_kid(a, "lake_open")
    $ say_kid(b, "lake_open")
    $ say_duo(a, b, "lake", "open")

    python:
        if "choose_event" in globals():
            event_type = choose_event(kids)
        else:
            event_type = renpy.random.choice(["play", "conflict", "quiet"])

    if event_type == "play":

        "[a.name] picks up a pebble and flicks it across the water."
        "[b.name] watches the ripples spread."

        $ say_duo(a, b, "lake", "play")

        menu:
            "Join them":
                "You crouch near the shore and join in."

                python:
                    for kid in kids:
                        kid.update_mood(1)
                        kid.update_trust(1)
                        kid.add_memory("Played by the lake")

                python:
                    if "relationship_event" in globals():
                        relationship_event(kids, "positive")

            "Watch":
                "You stay back and let them keep going."

                python:
                    for kid in kids:
                        kid.update_mood(1)
                        kid.add_memory("Quiet fun by the lake")

    elif event_type == "conflict":

        "[a.name] frowns and folds their arms."
        "[b.name] looks back, annoyed."

        $ say_kid(a, "lake_conflict_a")
        $ say_kid(b, "lake_conflict_b")

        menu:
            "Calm them down":
                "You step in before the argument gets bigger."

                python:
                    for kid in kids:
                        kid.update_mood(1)
                        kid.update_trust(1)
                        kid.add_memory("Got help during an argument")

                python:
                    if "relationship_event" in globals():
                        relationship_event(kids, "positive")

            "Take a side":
                "You support one of them."

                python:
                    kids[0].update_trust(1)
                    kids[0].update_mood(1)
                    kids[1].update_trust(-1)
                    kids[1].update_mood(-1)

                python:
                    if "relationship_event" in globals():
                        relationship_event(kids, "negative")

            "Stay quiet":
                "You say nothing."

                python:
                    for kid in kids:
                        kid.update_mood(-1)
                        kid.add_memory("Unresolved argument")

                python:
                    if "relationship_event" in globals():
                        relationship_event(kids, "negative")

        $ say_kid(a, "lake_conflict_a")
        $ say_kid(b, "lake_conflict_b")

    else:

        "[a.name] sits on a flat stone near the water."
        "[b.name] sits nearby, both of them watching the ripples."

        $ say_kid(a, "lake_quiet")
        $ say_kid(b, "lake_quiet")

        python:
            for kid in kids:
                kid.update_mood(1)
                kid.add_memory("Quiet lake moment")

    "[relationship_note(a, b)]"

    $ next_phase()
    jump day_loop


label forest_scene:

    $ kids = scene_kids(2)

    if len(kids) < 2:
        jump missing_scene

    $ a = kids[0]
    $ b = kids[1]

    python:
        arc = None
        if "check_story_arcs" in globals():
            arc = check_story_arcs(kids)

    if arc:
        call expression arc
        $ next_phase()
        jump day_loop

    "The forest is full of little sounds."
    "[a.name] walks ahead, pushing a branch aside."
    "[b.name] follows carefully."

    $ say_kid(a, "forest_open")
    $ say_kid(b, "forest_open")
    $ say_duo(a, b, "forest", "open")

    python:
        if "choose_event" in globals():
            event_type = choose_event(kids)
        else:
            event_type = renpy.random.choice(["play", "conflict", "quiet"])

    if event_type == "play":

        "[a.name] points to a crooked tree ahead."
        "[b.name] laughs and starts running."

        $ say_duo(a, b, "forest", "play")

        menu:
            "Run with them":
                "You join the race through the trees."

                python:
                    for kid in kids:
                        kid.update_mood(1)
                        kid.update_trust(1)
                        kid.add_memory("Ran through the forest")

                python:
                    if "relationship_event" in globals():
                        relationship_event(kids, "positive")

            "Let them run ahead":
                "You let them go first and keep walking."

                python:
                    for kid in kids:
                        kid.update_mood(1)
                        kid.add_memory("Forest race")

    elif event_type == "conflict":

        "[a.name] stops and points at the path."
        "[b.name] stops too, confused."

        $ say_kid(a, "forest_conflict_a")
        $ say_kid(b, "forest_conflict_b")

        menu:
            "Intervene":
                "You step in and check the path."

                python:
                    for kid in kids:
                        kid.update_mood(1)
                        kid.update_trust(1)
                        kid.add_memory("Got help while lost")

                python:
                    if "relationship_event" in globals():
                        relationship_event(kids, "positive")

            "Let them argue":
                "You let them keep talking until the anger burns out."

                python:
                    for kid in kids:
                        kid.update_mood(-1)
                        kid.add_memory("Forest argument")

                python:
                    if "relationship_event" in globals():
                        relationship_event(kids, "negative")

    else:

        "[a.name] pauses to listen."
        "[b.name] copies them and tries to stay quiet."

        $ say_kid(a, "forest_quiet")
        $ say_kid(b, "forest_quiet")

        python:
            for kid in kids:
                kid.update_mood(1)
                kid.add_memory("Quiet forest moment")

    "[relationship_note(a, b)]"

    $ next_phase()
    jump day_loop


label playground_scene:

    $ kids = scene_kids(2)

    if len(kids) < 2:
        jump missing_scene

    $ a = kids[0]
    $ b = kids[1]

    python:
        arc = None
        if "check_story_arcs" in globals():
            arc = check_story_arcs(kids)

    if arc:
        call expression arc
        $ next_phase()
        jump day_loop

    "The playground is loud before anyone even starts playing."
    "[a.name] is halfway up one of the climbing structures."
    "[b.name] looks up and shakes their head."

    $ say_kid(a, "playground_open")
    $ say_kid(b, "playground_open")
    $ say_duo(a, b, "playground", "open")

    python:
        if "choose_event" in globals():
            event_type = choose_event(kids)
        else:
            event_type = renpy.random.choice(["play", "conflict", "quiet"])

    if event_type == "play":

        "[a.name] jumps down and grins."
        "[b.name] runs after them."

        $ say_duo(a, b, "playground", "play")

        menu:
            "Encourage them":
                "You cheer them on."

                python:
                    for kid in kids:
                        kid.update_mood(1)
                        kid.update_trust(1)
                        kid.add_memory("Played at the playground")

                python:
                    if "relationship_event" in globals():
                        relationship_event(kids, "positive")

            "Stay on the side":
                "You watch them run back and forth."

                python:
                    for kid in kids:
                        kid.update_mood(1)
                        kid.add_memory("Playground running")

    elif event_type == "conflict":

        "[a.name] stops abruptly."
        "[b.name] nearly bumps into them."

        $ say_kid(a, "playground_conflict_a")
        $ say_kid(b, "playground_conflict_b")

        menu:
            "Stop the argument":
                "You get them to breathe and slow down."

                python:
                    for kid in kids:
                        kid.update_mood(1)
                        kid.update_trust(1)
                        kid.add_memory("Calmed down at the playground")

                python:
                    if "relationship_event" in globals():
                        relationship_event(kids, "positive")

            "Let it escalate":
                "You stay back and let the tension rise."

                python:
                    for kid in kids:
                        kid.update_mood(-1)
                        kid.add_memory("Playground conflict")

                python:
                    if "relationship_event" in globals():
                        relationship_event(kids, "negative")

    else:

        "[a.name] sits on the edge of the structure."
        "[b.name] leans against the ladder."

        $ say_kid(a, "playground_quiet")
        $ say_kid(b, "playground_quiet")

        python:
            for kid in kids:
                kid.update_mood(1)
                kid.add_memory("Quiet playground pause")

    "[relationship_note(a, b)]"

    $ next_phase()
    jump day_loop


label missing_scene:

    "This area is not ready yet."

    $ next_phase()
    jump day_loop
