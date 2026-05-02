init python:

    personalities = ["shy", "energetic", "calm", "playful"]

    def assign_personality(kid):
        import random
        kid.personality = random.choice(personalities)


    def personality_line(kid, context):

        p = getattr(kid, "personality", "calm")

        if context == "play":

            if p == "energetic":
                return "Come on! Let’s go!!"

            elif p == "shy":
                return "Uh… okay, I’ll try…"

            elif p == "playful":
                return "Heh, you’re gonna lose!"

            else:
                return "Alright, let’s do it."


        elif context == "conflict":

            if p == "energetic":
                return "Hey! That’s not fair!"

            elif p == "shy":
                return "I… didn’t mean to…"

            elif p == "playful":
                return "Oh come on, don’t get mad."

            else:
                return "Let’s just calm down."


        else:

            if p == "shy":
                return "It’s… nice here."

            elif p == "energetic":
                return "This place is kinda fun!"

            elif p == "playful":
                return "Not bad, huh?"

            else:
                return "It’s peaceful."
