init python:

    # Assign personalities to all kids at game start
    def setup_kids():
        for kid in all_kids:
            assign_personality(kid)

    # Call the setup function when the game starts
    setup_kids()
