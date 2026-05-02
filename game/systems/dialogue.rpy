init python:

    import random

    DIALOGUE_HISTORY = {}

    DIALOGUE_BANK = {
        "lake_open": {
            "default": [
                "The water is calm today.",
                "The lake feels quieter than usual.",
                "This place always makes the noise feel farther away.",
            ],
            "shy": [
                "It is easier to talk here when everything is quiet.",
                "I like it when the water keeps things calm.",
                "This place feels safer somehow.",
            ],
            "energetic": [
                "This is perfect. We could do something fun here.",
                "The lake is way better when people start moving around.",
                "Come on, it is too nice to just sit still.",
            ],
            "calm": [
                "It is peaceful here.",
                "I think this is the kind of place you remember later.",
                "A quiet place like this is hard to find.",
            ],
            "playful": [
                "This place is asking for trouble in a fun way.",
                "The lake looks like it wants a game.",
                "I bet something silly will happen here soon.",
            ],
        },
        "lake_play_a": {
            "default": [
                "I am going to try this one more time.",
                "That one almost worked.",
                "Okay, maybe I can do better.",
            ],
            "shy": [
                "I guess I can try one more.",
                "I hope this does not go badly.",
                "That was not as bad as I thought.",
            ],
            "energetic": [
                "Watch this.",
                "I can do better than that.",
                "That one was too easy.",
            ],
            "calm": [
                "Let us see what happens.",
                "That was a decent throw.",
                "I think I can do one more.",
            ],
            "playful": [
                "Try and beat that.",
                "I am clearly winning this one.",
                "You are going to have to catch up.",
            ],
        },
        "lake_play_b": {
            "default": [
                "You are being way too confident.",
                "That one almost got me.",
                "I did not expect that.",
            ],
            "shy": [
                "You keep surprising me.",
                "I was not ready for that.",
                "Okay, that was actually fun.",
            ],
            "energetic": [
                "No fair, I can do that too.",
                "You are not the only one who can play.",
                "That was a good one.",
            ],
            "calm": [
                "That was close.",
                "You are getting better at this.",
                "I should probably try again.",
            ],
            "playful": [
                "That was sneaky.",
                "You always turn it into a game.",
                "Fine, I am not losing this one.",
            ],
        },
        "lake_conflict_a": {
            "default": [
                "You keep changing the rules.",
                "That is not what we agreed on.",
                "You are not being fair.",
            ],
            "shy": [
                "This is getting a little uncomfortable.",
                "I thought we were doing this differently.",
                "I do not like this part.",
            ],
            "energetic": [
                "No, that is wrong.",
                "You are making this harder on purpose.",
                "Come on, you know that is not fair.",
            ],
            "calm": [
                "We should slow down.",
                "This is getting messy.",
                "We need to talk before this gets worse.",
            ],
            "playful": [
                "You are being dramatic now.",
                "Come on, that was barely fair.",
                "You are making this more serious than it should be.",
            ],
        },
        "lake_conflict_b": {
            "default": [
                "I did not change anything important.",
                "You are making a big deal out of nothing.",
                "That is not what happened.",
            ],
            "shy": [
                "I did not mean to upset you.",
                "I was only trying to help.",
                "I am not trying to argue.",
            ],
            "energetic": [
                "You are the one getting worked up.",
                "I can explain it if you want.",
                "That is not how I saw it.",
            ],
            "calm": [
                "Maybe we both saw it differently.",
                "We are talking past each other.",
                "I do not think either of us wants to fight.",
            ],
            "playful": [
                "Okay, okay, I get it.",
                "You really want to win this one.",
                "Maybe we are both a little stubborn.",
            ],
        },
        "lake_quiet": {
            "default": [
                "It is nice when nothing has to happen for a while.",
                "Moments like this are easy to forget, but hard to replace.",
                "Sometimes the quiet part matters the most.",
            ],
            "shy": [
                "I like it when nobody pushes me to talk.",
                "This is the kind of quiet I can handle.",
                "It feels easier to breathe here.",
            ],
            "energetic": [
                "I still wish something exciting would happen.",
                "Even the quiet here feels kind of good.",
                "Maybe the calm is nice for once.",
            ],
            "calm": [
                "This is enough for now.",
                "A quiet pause can fix a lot.",
                "We do not need to rush this moment.",
            ],
            "playful": [
                "Quiet before the next disaster, maybe.",
                "This feels suspiciously peaceful.",
                "I bet someone breaks the silence soon.",
            ],
        },

        "forest_open": {
            "default": [
                "The forest always sounds like it is whispering.",
                "The trees make everything feel smaller.",
                "It is quieter in here than outside the camp.",
            ],
            "shy": [
                "I like places where I do not have to talk first.",
                "This feels easier than the noisy parts of camp.",
                "The trees make it feel like nobody is watching.",
            ],
            "energetic": [
                "This place makes me want to run somewhere.",
                "It feels like something should happen here.",
                "Come on, the forest is way too quiet.",
            ],
            "calm": [
                "There is something steady about this place.",
                "I do not mind the silence here.",
                "The forest gives people room to think.",
            ],
            "playful": [
                "This is exactly where a weird story starts.",
                "The trees are definitely hiding something.",
                "This place feels like it is waiting for us.",
            ],
        },
        "forest_play_a": {
            "default": [
                "Race you to the next tree.",
                "I want to see how fast you can keep up.",
                "You are going to have to move if you want to win.",
            ],
            "shy": [
                "I guess I can run too.",
                "Try not to leave me behind.",
                "I will do my best.",
            ],
            "energetic": [
                "You are already too slow.",
                "I am going to win this easily.",
                "Keep up if you can.",
            ],
            "calm": [
                "We can take it at a steady pace.",
                "No need to rush it.",
                "Let us just see where it goes.",
            ],
            "playful": [
                "Try not to trip over your own feet.",
                "I already know I am winning.",
                "This is the kind of game I like.",
            ],
        },
        "forest_play_b": {
            "default": [
                "You always turn everything into a race.",
                "That is not fair, you started early.",
                "I am not losing just because you said that.",
            ],
            "shy": [
                "Wait for me a second.",
                "You are going too fast.",
                "I am trying to keep up.",
            ],
            "energetic": [
                "No way, I can beat you.",
                "You are not the only one who can run.",
                "Okay, now I am excited.",
            ],
            "calm": [
                "Alright, that sounds fine.",
                "Let us not make it too serious.",
                "A race is okay, I guess.",
            ],
            "playful": [
                "You are always picking the loudest challenge.",
                "You are on. Do not cry when I win.",
                "This should be fun.",
            ],
        },
        "forest_conflict_a": {
            "default": [
                "You are going the wrong way.",
                "I told you to stop rushing.",
                "You are not listening.",
            ],
            "shy": [
                "I think we may be lost.",
                "I did not want this to turn into a problem.",
                "I should have spoken up sooner.",
            ],
            "energetic": [
                "We should have moved faster.",
                "You are slowing everything down.",
                "I knew this would happen.",
            ],
            "calm": [
                "We need to stop and check the path.",
                "There is no point arguing if we are both unsure.",
                "We can fix this if we calm down.",
            ],
            "playful": [
                "You are making this much harder than it needs to be.",
                "Of course this turned into a mess.",
                "You always make simple things dramatic.",
            ],
        },
        "forest_conflict_b": {
            "default": [
                "I was not rushing.",
                "You are acting like this is my fault.",
                "We are not even that lost.",
            ],
            "shy": [
                "I was just trying to help.",
                "I did not mean to mess this up.",
                "Please do not blame me for everything.",
            ],
            "energetic": [
                "Then show me the right way.",
                "I am not the one slowing us down.",
                "This is not all on me.",
            ],
            "calm": [
                "We should both pay attention.",
                "This is a mistake, not a fight.",
                "Let us figure it out together.",
            ],
            "playful": [
                "You are always quick to blame somebody.",
                "We are only a little lost, not trapped forever.",
                "You are being too serious again.",
            ],
        },
        "forest_quiet": {
            "default": [
                "The forest is doing most of the talking.",
                "It feels better when nobody rushes things here.",
                "This is the kind of quiet that stays with you.",
            ],
            "shy": [
                "I like how the trees hide the noise.",
                "It feels safe to stay quiet here.",
                "I do not mind this at all.",
            ],
            "energetic": [
                "Even this calm place feels kind of exciting.",
                "I wish there was a trail farther ahead.",
                "The silence is almost too much.",
            ],
            "calm": [
                "This is a good place to slow down.",
                "We should enjoy the quiet while it lasts.",
                "The forest feels balanced today.",
            ],
            "playful": [
                "This is where something unexpected usually happens.",
                "I am waiting for the hidden surprise.",
                "The forest looks like it knows a secret.",
            ],
        },

        "playground_open": {
            "default": [
                "The playground is loud before anyone even starts playing.",
                "There is always movement here.",
                "It feels impossible to stand still in this place.",
            ],
            "shy": [
                "This place is a little overwhelming.",
                "I can watch for a moment before joining.",
                "There is too much happening all at once.",
            ],
            "energetic": [
                "Now this is more like it.",
                "I was hoping for something fast.",
                "Finally, a place with some energy.",
            ],
            "calm": [
                "The noise does not bother me too much.",
                "There is a rhythm to this place.",
                "The playground has its own kind of order.",
            ],
            "playful": [
                "This is where trouble starts in a fun way.",
                "I already know somebody is going to get competitive.",
                "The playground always turns into a game.",
            ],
        },
        "playground_play_a": {
            "default": [
                "Try to keep up.",
                "I can go faster than that.",
                "This is the easy part.",
            ],
            "shy": [
                "I will try not to mess this up.",
                "Okay, I can do this.",
                "That was not as scary as I thought.",
            ],
            "energetic": [
                "Watch me go.",
                "You are not catching me.",
                "This is what I am good at.",
            ],
            "calm": [
                "Let us keep it steady.",
                "No need to rush too hard.",
                "This is fine at this pace.",
            ],
            "playful": [
                "You are already losing.",
                "This is my kind of game.",
                "I want a rematch after this.",
            ],
        },
        "playground_play_b": {
            "default": [
                "You think you are faster than me?",
                "That is not fair, you started first.",
                "I can still catch up.",
            ],
            "shy": [
                "Wait, give me a second.",
                "You are moving so fast.",
                "I am trying, I really am.",
            ],
            "energetic": [
                "No way, I am right behind you.",
                "I am not letting you win.",
                "This is actually fun.",
            ],
            "calm": [
                "Okay, I am still with you.",
                "We can keep going like this.",
                "I am not in a hurry.",
            ],
            "playful": [
                "You are going to have to work for it.",
                "I already know I am winning.",
                "This is way more fun than sitting around.",
            ],
        },
        "playground_conflict_a": {
            "default": [
                "You cheated.",
                "That was not the rule.",
                "You keep changing things.",
            ],
            "shy": [
                "That made me uncomfortable.",
                "I do not like when this happens.",
                "Please just stop a second.",
            ],
            "energetic": [
                "That was clearly cheating.",
                "You cannot just do that.",
                "You know that was wrong.",
            ],
            "calm": [
                "We should not keep this going.",
                "This is getting messy.",
                "We need to cool off.",
            ],
            "playful": [
                "You got caught, that is all.",
                "You really thought I would not notice?",
                "You are making this more dramatic than it needs to be.",
            ],
        },
        "playground_conflict_b": {
            "default": [
                "I did not cheat.",
                "You are being too serious.",
                "That is not what happened.",
            ],
            "shy": [
                "I was not trying to hurt you.",
                "I just wanted to play.",
                "I did not mean anything by it.",
            ],
            "energetic": [
                "I played by the rules.",
                "You are the one getting mad.",
                "That is not fair to say.",
            ],
            "calm": [
                "We should take a breath.",
                "This does not need to become a fight.",
                "Maybe we are both being stubborn.",
            ],
            "playful": [
                "You always accuse me when you lose.",
                "You are being way too intense right now.",
                "You are acting like this is the end of the world.",
            ],
        },
        "playground_quiet": {
            "default": [
                "Even the playground can go still for a second.",
                "It is almost strange when nobody is shouting.",
                "The noise fades if you wait long enough.",
            ],
            "shy": [
                "This is better when it gets quieter.",
                "I can think here if I ignore the noise.",
                "It is easier to stay here when things settle down.",
            ],
            "energetic": [
                "I am still ready for something to happen.",
                "Quiet does not last long around here.",
                "This is the pause before the next game.",
            ],
            "calm": [
                "A small pause is nice.",
                "The playground does not always have to be loud.",
                "This is a good moment to breathe.",
            ],
            "playful": [
                "Somebody is going to break the silence soon.",
                "This feels suspiciously peaceful.",
                "I am waiting for the next thing to happen.",
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
