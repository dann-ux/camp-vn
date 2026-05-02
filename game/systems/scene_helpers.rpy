init -10 python:

    import random

    def scene_kids(n=2):
        pool = globals().get("all_kids", [])

        if not pool:
            return []

        if "get_social_group" in globals():
            try:
                return get_social_group(n)
            except:
                pass

        if "get_random_kids" in globals():
            try:
                return get_random_kids(n)
            except:
                pass

        n = min(n, len(pool))
        return random.sample(pool, n)

    def say_kid(kid, text):
        renpy.say(None, kid.name + ": " + text)

    def relationship_note(a, b):
        rel = 0

        if "get_relationship" in globals():
            try:
                rel = get_relationship(a, b)
            except:
                rel = 0

        if rel >= 5:
            return a.name + " and " + b.name + " feel close now."
        elif rel <= -5:
            return a.name + " and " + b.name + " clearly avoid each other."
        elif rel > 0:
            return a.name + " and " + b.name + " seem warmer toward each other."
        elif rel < 0:
            return a.name + " and " + b.name + " still feel tense."

        return a.name + " and " + b.name + " are still figuring each other out."
