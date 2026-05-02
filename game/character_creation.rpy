screen character_creation():
    tag menu
    add Solid("#87CEEB")
    vbox:
        xalign 0.5
        yalign 0.3
        spacing 30
        text "CREATE YOUR CHARACTER" size 36 bold True color "#FFFFFF" xalign 0.5
        frame:
            background "#FFFFFF"
            xminimum 400
            vbox:
                spacing 15
                xalign 0.5
                text "Your name:" size 22 color "#333333"
                input:
                    value VariableInputValue("player_name")
                    length 20
                    size 24
                    color "#000000"
        hbox:
            xalign 0.5
            spacing 20
            textbutton "Back":
                action Jump("title_screen")
                text_size 22
            textbutton "Start Adventure!":
                action Jump("start_game")
                text_size 22

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
