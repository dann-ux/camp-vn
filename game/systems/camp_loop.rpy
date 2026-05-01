# CAMP LOOP ENGINE
# Controls day structure and event flow

default current_day = 1
default time_phase = "morning"  # morning / activity / freeplay / night

init python:

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
