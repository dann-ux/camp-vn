label event_surprise_visitor:
    "A friendly ranger arrives with a bag of new games and snacks."
    "The kids' excitement spikes as they try the new activities."
    $ for kid in all_kids:
        kid.update_mood(2)
        kid.update_trust(1)
        kid.add_memory("Met a surprise visitor")
    return
