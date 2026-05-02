screen character_creation():

    tag menu

    # Background
    add Solid("#87CEEB")

    frame:
        xalign 0.5
        yalign 0.5
        background "#FFFFFF"
        padding 30
        xmaximum 600
        ymaximum 700

        vbox:
            spacing 20

            text "Create Your Character" size 30 bold True

            # Name input
            text "Name:" size 20
            input:
                value ScreenVariableInputValue("player_name")
                length 20
                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

            # Species selection
            text "Species:" size 20
            viewport:
                mousewheel True
                yinitial 0
                ymaximum 200

                vbox:
                    for species_id, species_name in SPECIES_OPTIONS:
                        textbutton species_name:
                            action SetField(p, "species", species_id)
                            hover_background "#BDBDBD"

            # Character preview placeholder (shows a colored square based on species)
            frame:
                background "#CCCCCC"
                xfill True
                ysize 150
                if p:
                    if p.species == "human":
                        $ preview_color = "#FFDAB9"
                    elif p.species == "cat":
                        $ preview_color = "#FFCC99"
                    elif p.species == "dog":
                        $ preview_color = "#FFE4B5"
                    elif p.species == "rabbit":
                        $ preview_color = "#FFF0F5"
                    elif p.species == "fox":
                        $ preview_color = "#FFEFD5"
                    elif p.species == "bear":
                        $ preview_color = "#D2B48C"
                    else:
                        $ preview_color = "#CCCCCC"
                else:
                    $ preview_color = "#CCCCCC"
                add Solid(preview_color) xpos 0 ypos 0 xsize 200 ysize 150

            # Navigation buttons
            hbox:
                spacing 20
                xalign 0.5

                textbutton "Back":
                    action Jump("title_screen")
                    text_size 20
                    background "#9E9E9E"
                    hover_background "#757575"

                textbutton "Start Game":
                    action Jump("start_game")
                    text_size 20
                    background "#4CAF50"
                    hover_background "#66BB6A"

# Character creation label
label character_creation:

    # Initialize player name
    $ player_name = "Camp Kid"

    # Create player character (species will be set by the screen)
    $ p = Kid(player_name, species="human")
    $ all_kids = [p]  # Start with just the player

    # Show character creation screen
    call screen character_creation

    # After character creation, start the game
    jump start_game

label start_game:

    # Initialize other kids
    $ ann = Kid("Ann", species="cat")
    $ all_kids.append(ann)

    # Assign personalities
    python:
        for kid in all_kids:
            assign_personality(kid)

    # Start the game
    jump camp_loop
