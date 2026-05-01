# CHILD CAST (INITIAL VERSION)

init python:

    # Import your Child class from systems
    # (we assume characters.py exists in systems)
    from game.systems.characters import Child

    # CORE CHILDREN

    kid_a = Child("Milo", 7, "observer")
    kid_b = Child("Rin", 8, "leader")
    kid_c = Child("Sora", 6, "emotional")
    kid_d = Child("Kai", 9, "chaos")

    all_kids = [kid_a, kid_b, kid_c, kid_d]


# OPTIONAL: simple Ren'Py character display names

define m = Character("Milo")
define r = Character("Rin")
define s = Character("Sora")
define k = Character("Kai")
