# CHARACTER DEFINITIONS

# Minimal Kid class to hold state used throughout the game
init python:

    class Kid(object):
        def __init__(self, name):
            self.name = name
            self.mood = 0          # 0 = neutral, positive = happy, negative = upset
            self.trust = 0         # 0 = neutral, positive = friendly, negative = wary
            self.personality = "calm"  # default personality
            self.memories = []     # list of memory strings

        # Simple state modifiers used by events
        def update_mood(self, delta):
            self.mood += delta

        def update_trust(self, delta):
            self.trust += delta

        def add_memory(self, event):
            self.memories.append(event)

    # Create the player and a friend character
    p = Kid("You")
    ann = Kid("Ann")

    # Global list of all kid objects
    all_kids = [p, ann]

# Expose the Kid class for other modules
define _Kid = Kid
