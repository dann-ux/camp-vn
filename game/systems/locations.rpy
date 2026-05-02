init python:

    LOCATION_LABELS = {
        "lake": "lake_scene",
        "forest": "forest_scene",
        "playground": "playground_scene",
    }

    def resolve_location(key):
        return LOCATION_LABELS.get(key, "missing_scene")
