init python:

    import random

    current_day = 1
    time_phase = "morning"

    def next_phase():
        global time_phase

        if time_phase == "morning":
            time_phase = "activity"

        elif time_phase == "activity":
            time_phase = "freeplay"

        elif time_phase == "freeplay":
            time_phase = "night"

        elif time_phase == "night":
            next_day()

    def next_day():
        global current_day, time_phase
        current_day += 1
        time_phase = "morning"

    def get_phase_text():
        return f"Day {current_day} - {time_phase}"


    def get_random_kids(n=2):
        return random.sample(all_kids, n)


    def trigger_activity_scene():

        kids = get_random_kids(2)
        results = []

        for kid in kids:
            results.append(kid.react("play"))
            kid.add_memory("Played together")
            kid.update_trust(1)

        return results


    def trigger_conflict_scene():

        kids = get_random_kids(2)
        results = []

        for kid in kids:
            results.append(kid.react("conflict"))
            kid.add_memory("Small disagreement")
            kid.update_trust(-1)

        return results
