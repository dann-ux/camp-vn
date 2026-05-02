screen character_creation():
    tag menu
    add Solid("#87CEEB")
    frame:
        xalign 0.5
        yalign 0.5
        background "#FFFFFF"
        xmaximum 500
        ymaximum 400
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            text "Create Your Character" size 30 bold True
            text "Enter your name:" size 20
            input:
                value VariableInputValue("player_name")
                length 20
            textbutton "Start Game":
                action Jump("start_game")
                text_size 20
            textbutton "Back":
                action Jump("title_screen")
                text_size 20

label character_creation:
    $ player_name = "Camp Kid"
    $ p = Kid(player_name, species="human")
    $ all_kids = [p]
    call screen character_creation
    jump start_game

label start_game:
    $ ann = Kid("Ann", species="cat")
    $ all_kids.append(ann)
    python:
        for kid in all_kids:
            assign_personality(kid)
    jump camp_loop
