label event_firefly_show:
    "As night falls, fireflies begin to flicker, turning the clearing into a sparkling wonderland."
    "Everyone sits quietly, watching the tiny lights dance."
    python:
        for kid in all_kids:
            kid.update_mood(2)
            kid.add_memory("Saw fireflies at night")
    return
