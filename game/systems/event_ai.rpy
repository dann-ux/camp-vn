init python:

    import random

    def choose_event(kids):

        # Base weights
        weights = {
            "play": 5,
            "conflict": 2,
            "quiet": 3
        }

        # Modify based on relationships
        if len(kids) >= 2:
            rel = get_relationship(kids[0], kids[1])

            if rel > 2:
                weights["play"] += 3
                weights["conflict"] -= 1

            elif rel < -2:
                weights["conflict"] += 4
                weights["play"] -= 2

        # Modify based on mood
        avg_mood = sum(k.mood for k in kids) / len(kids)

        if avg_mood < -1:
            weights["conflict"] += 2

        elif avg_mood > 1:
            weights["play"] += 2

        # Prevent negative weights
        for k in weights:
            weights[k] = max(1, weights[k])

        # Weighted choice
        choices = []
        for event, w in weights.items():
            choices.extend([event] * w)

        return random.choice(choices)
