label best_friend_scene:

    $ a, b = get_social_group(2)

    "[a.name] and [b.name] sit together quietly."

    "[a.name] shares something personal."

    "[b.name] listens carefully."

    "They seem much closer now."

    python:
        a.update_trust(2)
        b.update_trust(2)

    return


label rival_scene:

    $ a, b = get_social_group(2)

    "[a.name] and [b.name] avoid each other."

    "The tension is obvious."

    "Even small things turn into conflict."

    python:
        a.update_mood(-1)
        b.update_mood(-1)

    return
