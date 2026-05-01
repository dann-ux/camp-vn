init python:

    import random

    class Child:
        def __init__(self, name, age, personality):
            self.name = name
            self.age = age
            self.personality = personality

            self.trust = 0
            self.comfort = 0
            self.memories = []

        mood = self.mood_modifier()
        def react(self, event_type):

            if event_type == "play":
    if mood == "happy":
        return self.name + " runs in excitedly."

    return self.name + " joins the game quickly."

            if event_type == "conflict":

    if mood == "uneasy":
        return self.name + " avoids eye contact and steps back."

    if self.trust < 0:
        return self.name + " looks unsure and keeps distance."

    return self.name + " tries to fix the situation."

            if event_type == "comfort":
                self.comfort += 1
                return self.name + " stays close quietly."

            return self.name + " watches."

        def add_memory(self, m):

    self.memories.append(m)

    # Apply emotional effect immediately
    self.apply_memory_effect(m)

        def update_trust(self, v):
            self.trust += v


    kid_a = Child("Milo", 7, "observer")
    kid_b = Child("Rin", 8, "leader")
    kid_c = Child("Sora", 6, "emotional")
    kid_d = Child("Kai", 9, "chaos")

    all_kids = [kid_a, kid_b, kid_c, kid_d]

def mood_modifier(self):

        # Simple emotional state based on trust + comfort
        if self.trust > 5:
            return "happy"

        if self.trust < -3:
            return "uneasy"

        if self.comfort > 3:
            return "calm"

        return "neutral"


    def apply_memory_effect(self, event):

        # Memory influences long-term trust

        if "Played together" in event:
            self.trust += 0.2

        if "Small disagreement" in event:
            self.trust -= 0.3
