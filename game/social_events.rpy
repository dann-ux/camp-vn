
label social_event_check:
    # Check relationship thresholds and memory flags for organic events
    if fox1_dog1_rel <= -10 and not fox1_dog1_argued:
        call event_fox_dog_argument
        return
    elif fox1_cat1_rel >= 10 and not fox1_cat1_hangout:
        call event_fox_cat_storytime
        return
    elif dog1_cat1_rel >= 10 and not dog1_cat1_card_swap:
        call event_dog_cat_trading
        return
    return

label event_fox_dog_argument:
    scene bg_camp with dissolve
    "You hear raised voices near the cabins."
    show fox1 at left with moveinleft
    show dog1 at right with moveinright
    fox1 "You always hog the best spots! It's not fair!"
    dog1 "I was here first! You just don't like sharing!"
    "They glare at each other. The tension is thick."
    menu:
        "Step in and mediate":
            "You calmly suggest taking turns. They both huff but agree."
            $ fox1_dog1_rel += 5
            "They seem to calm down a bit."
        "Watch from a distance":
            "You decide it's best not to get involved right now."
            "The argument fizzles out, but the air stays tense."
        "Walk away":
            "You quietly slip away before they notice you."
    hide fox1 with moveoutleft
    hide dog1 with moveoutright
    $ fox1_dog1_argued = True
    return

label event_fox_cat_storytime:
    scene bg_camp with dissolve
    "You find Fox Kid 1 and Cat Kid 1 sitting together under a large oak tree."
    show fox1 at left with moveinleft
    show cat1 at right with moveinright
    cat1 "...and then the hero realized the treasure was the friends they made along the way."
    fox1 "Whoa! That's actually really cool. What happens next?"
    "They're completely absorbed in the story. They notice you and wave."
    menu:
        "Join the story circle":
            "You sit down and listen. It's a peaceful moment."
            $ fox1_cat1_rel += 5
            "They make room for you."
        "Wave and keep walking":
            "You give a small wave. They smile back and return to the book."
            $ fox1_cat1_rel += 0
    hide fox1 with moveoutleft
    hide cat1 with moveoutright
    $ fox1_cat1_hangout = True
    return

label event_dog_cat_trading:
    scene bg_camp with dissolve
    "Near the lodge, Dog Kid 1 and Cat Kid 1 are exchanging small items."
    show dog1 at left with moveinleft
    show cat1 at right with moveinright
    dog1 "I'll trade you this shiny rock for your extra bookmark!"
    cat1 "Deal. It's a fair swap."
    "They high-paw, clearly enjoying each other's company."
    menu:
        "Compliment their trade":
            "You mention it looks like a great deal. They both beam with pride."
            $ dog1_cat1_rel += 5
        "Ask to see the rock":
            dog1 "Sure! It's super smooth. I found it by the creek."
            "They show it off happily."
            $ dog1_cat1_rel += 3
    hide dog1 with moveoutleft
    hide cat1 with moveoutright
    $ dog1_cat1_card_swap = True
    return
