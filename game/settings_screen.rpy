screen settings():

    tag menu

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

            text "Settings" size 30 bold True

            # Placeholder settings
            text "Volume Control" size 20
            bar value FieldValue(config, "volume")

            text "Text Speed" size 20
            bar value FieldValue(config, "text_speed")

            textbutton "Auto-Forward":
                action ToggleField(config, "auto_forward")
                text_size 20
                background "#9E9E9E"
                hover_background "#757575"

            # Navigation
            textbutton "Back":
                action Return()
                text_size 20
                background "#9E9E9E"
                hover_background "#757575"
                xalign 0.5
