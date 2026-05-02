# CAMP LOOP SYSTEM
# This label runs the main daily loop, handling time progression,
# random daily events, and the visual novel style UI.

init python:
    import random
    import renpy.store as store

    # Define the parts of the day. Each part lasts a fixed number of turns.
    DAY_PARTS = ["Morning", "Afternoon", "Evening", "Night"]
    TURNS_PER_PART = 3  # Number of loops before the day part changes

    # Global variables to track time. Use the Ren'Py store so they persist across
    # saves and are accessible from the script.
    if not hasattr(store, 'current_day'):
        store.current_day = 1
        store.current_part_index = 0
        store.turn_counter = 0

    # Random daily events that can happen at any time.
    DAILY_EVENTS = [
        ("rainstorm", "A sudden rainstorm makes everyone run for shelter."),
        ("firefly_show", "Fireflies light up the night, creating a magical glow."),
        ("lost_item", "Someone lost a favorite toy near the lake."),
        ("campfire_story", "A campfire story starts, and everyone gathers around."),
        ("surprise_visitor", "A surprise visitor arrives, bringing new games."),
    ]

    def advance_time():
        """Advance the turn counter and change day parts as needed."""
        store.turn_counter += 1
        if store.turn_counter >= TURNS_PER_PART:
            store.turn_counter = 0
            store.current_part_index = (store.current_part_index + 1) % len(DAY_PARTS)
            if store.current_part_index == 0:
                store.current_day += 1

    def current_day_part():
        return DAY_PARTS[store.current_part_index]

    def trigger_random_event():
        """Pick a random event with a small chance each turn."""
        if random.random() < 0.25:  # 25% chance per turn
            event_key, description = random.choice(DAILY_EVENTS)
            renpy.call_in_new_context("event_" + event_key)
            return True
        return False

label camp_loop:

    # Display a short narration about the time of day
    $ part = current_day_part()
    "[part] of Day [store.current_day]."

    # Core camp activities (existing logic)
    p "We are now in the camp."
    p "The daily camp activities can begin."

    $ kids = [p, ann]
    $ event_description = format_scene(kids, "freeplay")
    p "[event_description]"

    # Random event check
    $ _ = trigger_random_event()

    menu:
        "Wander around camp":
            p "I will wander around camp."
            return
        "Think about something else":
            p "I need a moment to think."
            return
        "Open map":
            return
        "Check journal":
            call screen journal_screen
            return

    # Advance time after each action
    $ advance_time()
    return
