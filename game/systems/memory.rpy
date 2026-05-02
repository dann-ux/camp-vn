# MEMORY SYSTEM
# Stores interaction events between characters

default memory_log = []

init python:

    def add_memory(character, event):
        memory_log.append({
            "character": character,
            "event": event
        })

    def get_memories(character):
        return [m for m in memory_log if m["character"] == character]

    def get_memory_summary(character):
        memories = get_memories(character)
        if not memories:
            return "[character] doesn't remember much yet."
        
        positive = sum(1 for m in memories if "fun" in m["event"] or "friend" in m["event"])
        negative = sum(1 for m in memories if "fight" in m["event"] or "mad" in m["event"])
        
        if positive > negative:
            return "[character] has had mostly good times with friends."
        elif negative > positive:
            return "[character] has had some tough times with others."
        else:
            return "[character] has had both good and bad experiences."
