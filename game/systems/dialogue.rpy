init python:

    import random

    DIALOGUE_HISTORY = {}

    DIALOGUE_BANK = {
        "lake_open": {
            "default": [
                "The water looks so pretty today.",
                "I like it when the lake is calm.",
                "It's so quiet here.",
            ],
            "shy": [
                "I like this place. It's not too loud.",
                "The water makes me feel calm.",
                "Nobody's watching us here.",
            ],
            "energetic": [
                "We could play in the water!",
                "Let's skip rocks!",
                "This is the best spot!",
            ],
            "calm": [
                "It's peaceful here.",
                "I like watching the water.",
                "This is my favorite place.",
            ],
            "playful": [
                "I bet I can skip more rocks!",
                "The water looks like it wants to play.",
                "Something fun is going to happen here!",
            ],
        },
        "lake_play_a": {
            "default": [
                "Watch me try again!",
                "I almost got it!",
                "One more time!",
            ],
            "shy": [
                "I'll try... but I might not be good.",
                "Okay, I'll try one more.",
                "That wasn't too bad.",
            ],
            "energetic": [
                "I'm gonna win!",
                "I'm the best at this!",
                "You can't beat me!",
            ],
            "calm": [
                "Let's see if I can do it.",
                "That was pretty good.",
                "I think I can do better.",
            ],
            "playful": [
                "Bet you can't beat that!",
                "I'm totally winning!",
                "You have to try harder!",
            ],
        },
        "lake_play_b": {
            "default": [
                "You're showing off!",
                "That was sneaky!",
                "I didn't see that coming!",
            ],
            "shy": [
                "Wow... you're good at that.",
                "You surprised me.",
                "That was actually fun.",
            ],
            "energetic": [
                "No fair! I can do that too!",
                "You're not the only one who's good!",
                "That was awesome!",
            ],
            "calm": [
                "That was close.",
                "You're getting better.",
                "I should try again.",
            ],
            "playful": [
                "You cheated!",
                "You always win!",
                "I'm gonna get you back!",
            ],
        },
        "lake_conflict_a": {
            "default": [
                "You're not playing fair!",
                "That's not how we play!",
                "You changed the rules!",
            ],
            "shy": [
                "I don't like this game anymore.",
                "Can we stop now?",
                "This isn't fun.",
            ],
            "energetic": [
                "Hey! That's not allowed!",
                "You're cheating!",
                "That's not fair!",
            ],
            "calm": [
                "Let's play something else.",
                "This isn't working.",
                "We should stop fighting.",
            ],
            "playful": [
                "You're being a sore loser!",
                "That was totally cheating!",
                "You're not playing right!",
            ],
        },
        "lake_conflict_b": {
            "default": [
                "I didn't do anything!",
                "You're being mean!",
                "I was just playing!",
            ],
            "shy": [
                "I didn't mean to upset you.",
                "I just wanted to play.",
                "I'm sorry.",
            ],
            "energetic": [
                "You're the one being mean!",
                "I was playing by the rules!",
                "You're overreacting!",
            ],
            "calm": [
                "Let's just calm down.",
                "We can play nice.",
                "It's not a big deal.",
            ],
            "playful": [
                "You're such a baby!",
                "You always get mad!",
                "You can't take a joke!",
            ],
        },
        "lake_quiet": {
            "default": [
                "It's nice when it's quiet.",
                "I like this peaceful feeling.",
                "Sometimes quiet is the best.",
            ],
            "shy": [
                "I like it when nobody talks.",
                "This is my favorite part.",
                "I feel safe here.",
            ],
            "energetic": [
                "Even quiet is kind of fun.",
                "I wonder what we'll do next.",
                "This is almost too calm.",
            ],
            "calm": [
                "This is perfect.",
                "I'm happy right now.",
                "This is the best feeling.",
            ],
            "playful": [
                "Quiet before the fun starts!",
                "Something's about to happen!",
                "I bet someone's gonna break this!",
            ],
        },

        "forest_open": {
            "default": [
                "The forest looks so green today.",
                "It's like a secret place.",
                "I love all the trees.",
            ],
            "shy": [
                "It's like nobody can see us here.",
                "I like how quiet it is.",
                "This place feels safe.",
            ],
            "energetic": [
                "Let's explore!",
                "I bet there's cool stuff here!",
                "Race you to that tree!",
            ],
            "calm": [
                "It's so peaceful in here.",
                "I like the forest sounds.",
                "This is my happy place.",
            ],
            "playful": [
                "I bet there's treasure here!",
                "The trees are hiding something!",
                "This is where adventures happen!",
            ],
        },
        "forest_play_a": {
            "default": [
                "Race you to the big tree!",
                "Try to catch me!",
                "I'm faster than you!",
            ],
            "shy": [
                "Okay... but don't leave me.",
                "I'll try my best.",
                "Please wait for me.",
            ],
            "energetic": [
                "You can't catch me!",
                "I'm the fastest!",
                "You're too slow!",
            ],
            "calm": [
                "Let's walk together.",
                "No need to run.",
                "We can take our time.",
            ],
            "playful": [
                "You're gonna lose!",
                "I'm totally winning!",
                "Try to keep up!",
            ],
        },
        "forest_play_b": {
            "default": [
                "You always run too fast!",
                "Wait for me!",
                "That's not fair!",
            ],
            "shy": [
                "You're going too fast.",
                "I can't keep up.",
                "Please slow down.",
            ],
            "energetic": [
                "I can beat you too!",
                "You're not the only fast one!",
                "Watch me go!",
            ],
            "calm": [
                "It's okay, I'm here.",
                "We can walk together.",
                "I'm not in a hurry.",
            ],
            "playful": [
                "You're such a show-off!",
                "You always have to win!",
                "I'm gonna get you!",
            ],
        },
        "forest_conflict_a": {
            "default": [
                "You're going the wrong way!",
                "We're lost because of you!",
                "You never listen!",
            ],
            "shy": [
                "I think we're lost.",
                "I'm scared now.",
                "Can we go back?",
            ],
            "energetic": [
                "You're making us lost!",
                "You never pay attention!",
                "This is all your fault!",
            ],
            "calm": [
                "Let's stop and think.",
                "We need to find our way.",
                "This is scary.",
            ],
            "playful": [
                "You always mess things up!",
                "This is your fault!",
                "You're the worst navigator!",
            ],
        },
        "forest_conflict_b": {
            "default": [
                "I'm not lost!",
                "You're blaming me!",
                "It's not my fault!",
            ],
            "shy": [
                "I didn't mean to get us lost.",
                "I'm sorry.",
                "Please don't be mad.",
            ],
            "energetic": [
                "You're the one who's scared!",
                "I know where we are!",
                "Stop blaming me!",
            ],
            "calm": [
                "Let's just find our way.",
                "We'll be okay.",
                "It's not a big deal.",
            ],
            "playful": [
                "You're such a scaredy-cat!",
                "You always blame me!",
                "You're overreacting!",
            ],
        },
        "forest_quiet": {
            "default": [
                "The forest is so pretty.",
                "I like the quiet sounds.",
                "This is nice.",
            ],
            "shy": [
                "I like hiding in the trees.",
                "Nobody can see me here.",
                "This is my secret spot.",
            ],
            "energetic": [
                "Even quiet is exciting!",
                "I wonder what's next!",
                "This is fun too!",
            ],
            "calm": [
                "I feel peaceful here.",
                "This is my happy place.",
                "I love this feeling.",
            ],
            "playful": [
                "Something's about to happen!",
                "The trees are watching us!",
                "Adventure time!",
            ],
        },

        "playground_open": {
            "default": [
                "The playground is so loud!",
                "I love all the energy here.",
                "This place is always fun.",
            ],
            "shy": [
                "It's a bit overwhelming.",
                "I need a minute to watch.",
                "There's so much happening.",
            ],
            "energetic": [
                "YES! The playground!",
                "I love this place!",
                "Let's play everything!",
            ],
            "calm": [
                "It's nice to see everyone playing.",
                "The playground has good energy.",
                "I like watching others play.",
            ],
            "playful": [
                "This is where the fun begins!",
                "I bet someone's gonna get competitive!",
                "Playground chaos incoming!",
            ],
        },
        "playground_play_a": {
            "default": [
                "Try to catch me!",
                "I'm the best at this!",
                "You can't beat me!",
            ],
            "shy": [
                "Okay... I'll try.",
                "Please don't laugh if I mess up.",
                "I'm not very good at this.",
            ],
            "energetic": [
                "Watch me go!",
                "I'm unstoppable!",
                "You're too slow!",
            ],
            "calm": [
                "Let's take it easy.",
                "This is fun.",
                "No need to rush.",
            ],
            "playful": [
                "You're gonna lose!",
                "I'm totally winning!",
                "Try to keep up!",
            ],
        },
        "playground_play_b": {
            "default": [
                "You're always showing off!",
                "That's not fair!",
                "I can do that too!",
            ],
            "shy": [
                "You're too fast.",
                "Can you slow down?",
                "I'm trying my best.",
            ],
            "energetic": [
                "I can beat you!",
                "You're not the only one!",
                "Watch this!",
            ],
            "calm": [
                "It's okay, I'm here.",
                "We can play together.",
                "I'm not in a rush.",
            ],
            "playful": [
                "You're such a show-off!",
                "You always have to win!",
                "I'm gonna get you!",
            ],
        },
        "playground_conflict_a": {
            "default": [
                "You cheated!",
                "That's not allowed!",
                "You're not playing fair!",
            ],
            "shy": [
                "That made me sad.",
                "Can we stop now?",
                "This isn't fun anymore.",
            ],
            "energetic": [
                "Hey! That's cheating!",
                "You can't do that!",
                "That's against the rules!",
            ],
            "calm": [
                "Let's play something else.",
                "This isn't working.",
                "We need to calm down.",
            ],
            "playful": [
                "You got caught!",
                "You always cheat!",
                "That's not fair!",
            ],
        },
        "playground_conflict_b": {
            "default": [
                "I didn't cheat!",
                "You're being mean!",
                "I was just playing!",
            ],
            "shy": [
                "I didn't mean to hurt you.",
                "I just wanted to play.",
                "I'm sorry.",
            ],
            "energetic": [
                "You're the one being mean!",
                "I was playing fair!",
                "You're overreacting!",
            ],
            "calm": [
                "Let's just take a break.",
                "We can play nice.",
                "It's not a big deal.",
            ],
            "playful": [
                "You're such a baby!",
                "You always get mad!",
                "You can't take a joke!",
            ],
        },
        "playground_quiet": {
            "default": [
                "Even the playground can be quiet.",
                "It's nice when it's calm.",
                "I like this peaceful moment.",
            ],
            "shy": [
                "This is better when it's quiet.",
                "I can think here.",
                "Nobody's watching me.",
            ],
            "energetic": [
                "I'm ready for more fun!",
                "Quiet won't last long!",
                "Something exciting is coming!",
            ],
            "calm": [
                "This is a nice break.",
                "I'm happy right now.",
                "This feels good.",
            ],
            "playful": [
                "Someone's gonna break this!",
                "The quiet is suspicious!",
                "Adventure time soon!",
            ],
        },
    }

    def choose_dialogue(key, personality="default"):
        bank = DIALOGUE_BANK.get(key, {})
        options = bank.get(personality) or bank.get("default") or []

        if not options:
            return ""

        recent = DIALOGUE_HISTORY.setdefault(key, [])
        available = [line for line in options if line not in recent]

        if not available:
            recent[:] = []
            available = list(options)

        line = random.choice(available)
        recent.append(line)
        recent[:] = recent[-3:]

        return line

    def say_kid(kid, key):
        personality = getattr(kid, "personality", "default")
        line = choose_dialogue(key, personality)
        renpy.say(None, kid.name + ": " + line)
        return line

    def say_duo(a, b, scene, beat):
        say_kid(a, scene + "_" + beat + "_a")
        say_kid(b, scene + "_" + beat + "_b")
