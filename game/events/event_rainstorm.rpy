label event_rainstorm:
    "Dark clouds roll in quickly, and a sudden rainstorm drenches the camp."
    "Kids scramble for shelter under the big pine trees."
    $ for kid in all_kids:
        kid.update_mood(-1)
        kid.add_memory("Caught in a rainstorm")
    return
