label event_lost_item:
    "A small, squeaky toy is found near the lake. Someone is clearly missing it."
    menu:
        "Help find the owner":
            "You gather the kids and start looking around."
            $ for kid in all_kids:
                $ kid.update_trust(1)
                $ kid.add_memory("Helped find a lost toy")
        "Ignore it":
            "You decide it's not a big deal."
            $ for kid in all_kids:
                $ kid.update_mood(-1)
                $ kid.add_memory("Ignored a lost toy")
    return
