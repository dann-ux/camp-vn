# CHARACTER DEFINITIONS

# Minimal Kid class to hold state used throughout the game
init python:

    class Kid(object):
        def __init__(self, name, species="human"):
            self.name = name
            self.species = species
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

    # Species options for character creation
    SPECIES_OPTIONS = [
        ("human", "Human"),
        ("cat", "Cat"),
        ("dog", "Dog"),
        ("rabbit", "Rabbit"),
        ("fox", "Fox"),
        ("bear", "Bear"),
    ]

    # Create the player (will be set after character creation)
    p = None

    # Global list of all kid objects
    all_kids = []

# Expose the Kid class for other modules
define _Kid = Kid
