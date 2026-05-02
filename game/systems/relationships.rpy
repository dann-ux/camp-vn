init python:

    # Store relationships between kids
    # Key: (kid1, kid2)
    # Value: integer (positive = friends, negative = conflict)
    relationships = {}

    def get_relationship(a, b):
        return relationships.get((a, b), 0)

    def change_relationship(a, b, value):
        relationships[(a, b)] = relationships.get((a, b), 0) + value
        relationships[(b, a)] = relationships.get((b, a), 0) + value

    def relationship_event(kids, kind):
        if len(kids) < 2:
            return

        a, b = kids[0], kids[1]

        if kind == "positive":
            change_relationship(a, b, 1)
        elif kind == "negative":
            change_relationship(a, b, -1)
