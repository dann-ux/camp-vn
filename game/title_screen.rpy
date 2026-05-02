screen title_screen():
    tag menu
    add Solid("#87CEEB")
    vbox:
        xalign 0.5
        yalign 0.4
        spacing 20
        text "SUMMER CAMP ADVENTURES" size 40 color "#FFFFFF" bold True
    vbox:
        xalign 0.5
        yalign 0.6
        spacing 20
        textbutton "New Game":
            action Jump("character_creation")
            text_size 30
        textbutton "Load Game":
            action ShowMenu("load")
            text_size 30
        textbutton "Settings":
            action ShowMenu("preferences")
            text_size 30
        textbutton "Quit":
            action Quit()
            text_size 30

label title_screen:
    call screen title_screen
