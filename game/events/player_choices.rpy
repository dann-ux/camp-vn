label conflict_choice(kids):

    $ a, b = kids[0], kids[1]

    "[a.name] and [b.name] are arguing."

    menu:

        "Intervene calmly":

            "You step in and help them calm down."

            python:
                a.update_mood(1)
                b.update_mood(1)
                change_relationship(a, b, 1)

            return


        "Let them handle it":

            "You watch from a distance."

            python:
                a.update_mood(-1)
                b.update_mood(-1)
                change_relationship(a, b, -1)

            return


        "Take sides":

            "You support one of them."

            $ chosen = renpy.random.choice([a, b])
            "[chosen.name] seems relieved."

            python:
                chosen.update_mood(2)

            return
