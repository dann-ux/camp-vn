label best_friend_scene:

    $ a, b = get_social_group(2)

    "[a.name] and [b.name] sit together quietly."

    "[a.name] looks at [b.name] seriously."

    "[a.name]: You're my best friend."

    "[b.name] smiles and nods."

    "[b.name]: You're my best friend too."

    python:
        a.update_trust(3)
        b.update_trust(3)
        a.add_memory("Made a best friend")
        b.add_memory("Made a best friend")

    return


label rival_scene:

    $ a, b = get_social_group(2)

    "[a.name] and [b.name] are glaring at each other."

    "[a.name]: I don't like you."

    "[b.name]: I don't like you either."

    "They turn away from each other."

    python:
        a.update_mood(-2)
        b.update_mood(-2)
        a.add_memory("Made an enemy")
        b.add_memory("Made an enemy")

    return
