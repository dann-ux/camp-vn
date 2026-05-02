init python:

    triggered_arcs = set()

    def check_story_arcs(kids):

        if len(kids) < 2:
            return None

        a, b = kids[0], kids[1]

        rel = get_relationship(a, b)

        key = (a.name, b.name)

        # BEST FRIEND ARC
        if rel >= 5 and ("friend", key) not in triggered_arcs:
            triggered_arcs.add(("friend", key))
            return "best_friend_scene"

        # RIVAL ARC
        if rel <= -5 and ("rival", key) not in triggered_arcs:
            triggered_arcs.add(("rival", key))
            return "rival_scene"

        return None
