# TITLE SCREEN

screen title_main():
    tag menu
    add Solid("#2E86AB")
    vbox:
        xalign 0.5
        yalign 0.35
        spacing 10
        text "Summer Camp Adventures" size 48 bold True color "#FFFFFF" xalign 0.5
        text "A story of friendship, adventure and memory" size 20 color "#D4F1F4" xalign 0.5
    vbox:
        xalign 0.5
        yalign 0.65
        spacing 15
        textbutton "New Game" action Jump("character_creation") text_size 28 xalign 0.5
        textbutton "Load Game" action ShowMenu("load") text_size 28 xalign 0.5
        textbutton "Quit" action Quit() text_size 28 xalign 0.5

label title_screen:
    call screen title_main
    jump title_screen
