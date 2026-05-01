# CHILD BEHAVIOR SYSTEM
# Defines how kids behave, react, and interact

class Child:
    def __init__(self, name, age, personality):
        self.name = name
        self.age = age
        self.personality = personality

        # Social state
        self.trust = 0
        self.comfort = 0

        # Internal memory references
        self.memories = []

    def react(self, event_type):
        """
        Basic reaction system based on personality + trust
        """

        if event_type == "play":
            return f"{self.name} joins the game quickly."

        if event_type == "conflict":
            if self.trust < 0:
                return f"{self.name} steps back and looks unsure."
            return f"{self.name} tries to fix the situation."

        if event_type == "comfort":
            self.comfort += 1
            return f"{self.name} stays close quietly."

        return f"{self.name} watches what happens."

    def update_trust(self, amount):
        self.trust += amount

    def add_memory(self, memory):
        self.memories.append(memory)
