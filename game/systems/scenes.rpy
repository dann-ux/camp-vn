# SCENE SYSTEM
# Converts simulation into VN-readable scenes

init python:

    def format_scene(kids, event_type):

        names = ", ".join([k.name for k in kids])

        if event_type == "play":
            return f"{names} are playing together in the campyard."

        if event_type == "conflict":
            return f"A small disagreement happens between {names}."

        if event_type == "freeplay":
            return f"{names} wander freely around the camp."

        return f"{names} interact quietly."
