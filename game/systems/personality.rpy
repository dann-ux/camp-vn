init python:

    personalities = ["shy", "energetic", "calm", "playful"]

    def assign_personality(kid):
        import random
        kid.personality = random.choice(personalities)

    def personality_line(kid, context):

        p = getattr(kid, "personality", "calm")

        if context == "play":

            if p == "energetic":
                return "Yay! Let's play! Let's go!"

            elif p == "shy":
                return "Um... okay... I'll try..."

            elif p == "playful":
                return "Hee hee! You can't catch me!"

            else:
                return "Okay, that sounds fun."


        elif context == "conflict":

            if p == "energetic":
                return "Hey! That's not fair!"

            elif p == "shy":
                return "I... I didn't mean to..."

            elif p == "playful":
                return "Oh come on, don't be a baby!"

            else:
                return "Let's just be friends."


        else:

            if p == "shy":
                return "It's... nice here."

            elif p == "energetic":
                return "This is so fun!"

            elif p == "playful":
                return "Hee hee! This is silly!"

            else:
                return "I like this."
