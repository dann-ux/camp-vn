# MEMORY SYSTEM
# Stores all important events between characters

default memory_log = []

init python:

    def add_memory(character, event):
        memory_log.append({
            "character": character,
            "event": event
        })

    def get_memories(character):
        return [m for m in memory_log if m["character"] == character]
