screen debug_stats():

    frame:
        xalign 0.98
        yalign 0.02

        has vbox

        text "DEBUG STATS" size 20

        # KID STATS
        for kid in all_kids:

            text "[kid.name] | Mood: [kid.mood] | Trust: [kid.trust]" size 14

            # RELATIONSHIPS
            for other in all_kids:

                if kid != other:

                    $ rel = get_relationship(kid, other)

                    text "  → [other.name]: [rel]" size 12
