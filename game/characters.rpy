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

        def react(self, event_type):

            if event_type == "play":
                return self.name + " joins the game quickly."

            if event_type == "conflict":
                if self.trust < 0:
                    return self.name + " steps back quietly."
                return self.name + " tries to fix the situation."

            if event_type == "comfort":
                self.comfort += 1
                return self.name + " stays close quietly."

            return self.name + " watches."

        def add_memory(self, m):
            self.memories.append(m)

        def update_trust(self, v):
            self.trust += v


    kid_a = Child("Milo", 7, "observer")
    kid_b = Child("Rin", 8, "leader")
    kid_c = Child("Sora", 6, "emotional")
    kid_d = Child("Kai", 9, "chaos")

    all_kids = [kid_a, kid_b, kid_c, kid_d]
