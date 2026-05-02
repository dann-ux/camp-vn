label event_campfire_story:
    "The counselors light a campfire, and everyone gathers around."
    "Someone starts telling a spooky story, and the kids listen wide‑eyed."
    $ for kid in all_kids:
        $ kid.update_mood(1)
        $ kid.add_memory("Heard a campfire story")
    return
