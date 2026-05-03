# Relationship states and memory flags
# Ranges: -20 (Enemy) to +20 (Close Friend)
default fox1_relationship = 0
default fox1_saw_stone_skip = False
default fox1_was_supported = False

default dog1_relationship = 0
default dog1_shared_cards = False
default dog1_was_ignored = False

default cat1_relationship = 0
default cat1_read_together = False
default cat1_was_disturbed = False

# Relationship state evaluator
init python:
    def get_relationship_state(value):
        if value <= -10: return "enemy"
        elif value <= 10: return "neutral"
        elif value <= 18: return "friend"
        else: return "close_friend"
