# CHARACTER CREATION

default player_name = "Camp Kid"

screen char_creation():
    tag menu
    add Solid("#2E86AB")
    vbox:
        xalign 0.5
        yalign 0.4
        spacing 20
        text "What is your name?" size 36 bold True color "#FFFFFF" xalign 0.5
        input:
            value VariableInputValue("player_name")
            length 20
            pixel_width 400
            color "#FFFFFF"
            xalign 0.5
        textbutton "Start Adventure" action Jump("start_game") text_size 28 xalign 0.5
        textbutton "Back" action Jump("title_screen") text_size 24 xalign 0.5

label character_creation:
    call screen char_creation
    jump character_creation
