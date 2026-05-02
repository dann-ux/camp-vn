screen title_screen():
    tag menu
    add Solid("#87CEEB")
    # Camp logo placeholder (simple rectangle for now)
    frame:
        xalign 0.5
        yalign 0.2
        background "#8B4513"  # Brown color for wood-like frame
        padding 20
        vbox:
            spacing 10
            text "SUMMER CAMP ADVENTURES" size 40 color "#FFFFFF" bold True
    # Menu buttons
    vbox:
        xalign 0.5
        yalign 0.6
        spacing 20
        textbutton "New Game":
            action Jump("character_creation")
            text_size 30
            background "#4CAF50"  # Green
            hover_background "#66BB6A"
        textbutton "Load Game":
            action ShowMenu("load")
            text_size 30
            background "#2196F3"  # Blue
            hover_background "#42A5F5"
        textbutton "Settings":
            action ShowMenu("preferences")
            text_size 30
            background "#FF9800"  # Orange
            hover_background "#FFB74D"
        textbutton "Quit":
            action Quit()
            text_size 30
            background "#F44336"  # Red
            hover_background "#EF5350"
    # Decorative elements
    imagebutton:
        auto "camp_%s.png"  # Placeholder for camp decorations
        xalign 0.1
        yalign 0.9
    imagebutton:
        auto "camp_%s.png"
        xalign 0.9
        yalign 0.9
