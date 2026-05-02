init python:

    def has_negative_memory(kid):
        for m in kid.memories:
            if "disagreement" in m:
                return True
        return False
