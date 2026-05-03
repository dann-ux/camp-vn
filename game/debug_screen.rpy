screen debug_overlay():
    zorder 100
    frame:
        xalign 1.0
        yalign 0.0
        xmargin 20
        ymargin 20
        padding (10, 10)
        background Solid("#000000CC")
        vbox:
            spacing 8
            text "DEBUG OVERLAY" size 22 bold True color "#FFFFFF" xalign 0.5
            text "Day: [camp_day]" color "#FFFFFF"
            text "Phase: [current_phase]" color "#FFFFFF"
            null height 5
            text "--- RELATIONSHIPS ---" color "#FFFF00" bold True
            text "Fox1: [fox1_relationship]" color "#FF9933"
            text "Dog1: [dog1_relationship]" color "#8B5A2B"
            text "Cat1: [cat1_relationship]" color "#A0A0A0"
            null height 5
            text "--- MEMORY FLAGS ---" color "#00FF00" bold True
            text "Fox Stone Skip: [fox1_saw_stone_skip]" color "#FF9933"
            text "Dog Shared Cards: [dog1_shared_cards]" color "#8B5A2B"
            text "Cat Read Together: [cat1_read_together]" color "#A0A0A0"
            null height 10
            textbutton "Close Debug" action Hide("debug_overlay") text_size 16 xalign 0.5

label toggle_debug:
    if renpy.get_screen("debug_overlay"):
        hide screen debug_overlay
    else:
        show screen debug_overlay
    jump camp_loop
