# FRIENDSHIP SYSTEM
# Handles relationships between kids

default relationships = {}

init python:

    def init_relationships():
        global relationships
        relationships = {}

        for a in all_kids:
            relationships[a.name] = {}
            for b in all_kids:
                if a.name != b.name:
                    relationships[a.name][b.name] = 0


    def get_relationship(a, b):
        return relationships[a.name][b.name]


    def change_relationship(a, b, amount):
        relationships[a.name][b.name] += amount


    def process_shared_event(kid_list, amount):

        for i in range(len(kid_list)):
            for j in range(i + 1, len(kid_list)):

                a = kid_list[i]
                b = kid_list[j]

                change_relationship(a, b, amount)
                change_relationship(b, a, amount)


    def relationship_event(kid_list, event_type):

        if event_type == "positive":
            process_shared_event(kid_list, 2)

        elif event_type == "negative":
            process_shared_event(kid_list, -2)
def update_relationship_decay():

        # Slowly normalizes relationships over time
        for a in relationships:

            for b in relationships[a]:

                if relationships[a][b] > 0:
                    relationships[a][b] -= 0.01

                elif relationships[a][b] < 0:
                    relationships[a][b] += 0.01

def relationship_bonus(a, b):

        value = get_relationship(a, b)

        if value > 5:
            return 2  # strong friends

        if value < -5:
            return -2  # rivals

        return 0
