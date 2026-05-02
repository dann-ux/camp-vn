screen camp_map():

    tag menu

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 10

            text "Where do you go?"

            textbutton "Lake":
                action [Hide("camp_map"), Jump("lake_scene")]

            textbutton "Forest":
                action [Hide("camp_map"), Jump("forest_scene")]

            textbutton "Playground":
                action [Hide("camp_map"), Jump("playground_scene")]
