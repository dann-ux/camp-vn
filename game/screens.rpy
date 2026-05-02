# SCREEN DEFINITIONS FOR A VISUAL NOVEL STYLE UI

# Day/Night HUD --------------------------------------------------------------
screen day_hud():
    tag day_hud
    zorder 100

    frame:
        background "#00000080"
        xalign 0.5
        yalign 0.0
        padding (10, 5)

        text "Day [current_day] – [current_day_part()]" size 22 color "#FFFFFF"

# Dialogue Box ---------------------------------------------------------------
screen say(who, what):
    # Use Ren'Py's built-in say screen as a base, but add a simple border
    window:
        id "window"
        style "say_window"
        background Frame("gui/textbox.png", 12, 12, 12, 12) # placeholder
        xalign 0.5
        yalign 0.9
        xmaximum 800

        vbox:
            if who:
                text who style "say_label"
            text what style "say_dialogue"

# Journal Screen -------------------------------------------------------------
screen journal_screen():
    tag menu
    modal True
    zorder 200

    frame:
        background "#FFFFFF"
        xalign 0.5
        yalign 0.5
        xmaximum 700
        ymaximum 500
        padding 20

        vbox:
            spacing 15
            text "Journal – Day [current_day]" size 30 bold True

            # List recent memories for each kid
            for kid in all_kids:
                text "[kid.name]'s memories:" size 22 underline True
                $ mems = get_memories(kid)
                if mems:
                    for m in mems[-5:]:
                        text "- [m['event']]" size 18
                else:
                    text "- No memories yet." size 18

            textbutton "Close":
                action Hide("journal_screen")
                text_size 20
                background "#9E9E9E"
                hover_background "#757575"
                xalign 0.5

# Simple button style ---------------------------------------------------------
style button:
    background "#4CAF50"
    foreground "#FFFFFF"
    padding (8, 4)
    radius 5

style button_hover:
    background "#66BB6A"

# Text styles ---------------------------------------------------------------
style say_label:
    size 24
    color "#FFD700"
    bold True

style say_dialogue:
    size 28
    color "#FFFFFF"

style say_window:
    background "#00000080"
    padding (15, 10)
