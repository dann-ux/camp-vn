# ⚠️ CRITICAL WARNING — READ BEFORE ANYTHING ELSE ⚠️

NO CHARACTER NAMED ANN EXISTS IN THIS PROJECT.
NO CHARACTER NAMED ANY NAME EXISTS UNLESS LISTED IN SECTION 5.
DO NOT INVENT, SUGGEST, OR WRITE CODE FOR ANY CHARACTER NOT LISTED HERE.
IF YOU MENTION ANN OR ANY INVENTED CHARACTER YOU ARE WRONG.
ASK THE PROJECT OWNER FOR CHARACTER NAMES BEFORE WRITING ANYTHING.

---

# CAMP-VN PROJECT BIBLE
READ THIS FIRST. Any AI starting a session must read this entire document before touching any code.

## 1. PROJECT VISION

Title: Summer Camp Adventures (working title)
Engine: Ren'Py 8.0.3
Platform: PC/Mac
Target audience: All ages
Playtime: 5-10 hours
Genre: Visual Novel with AI-driven simulation

What this game is:
A visual novel set at a summer camp. Tone is a mix of wholesome, adventurous, and dramatic.

The three pillars:
1. AI-driven characters that remember past interactions
2. Choices that deeply matter and ripple through the story
3. Rich world with many characters and distinct personalities

## 2. COMPLETE WORKING CODE

FILE: game/script.rpy
    label start:
        jump title_screen

FILE: game/variables.rpy
    default camp_day = 1

FILE: game/title_screen.rpy
    screen title_main():
        tag menu
        add Solid("#2E86AB")
        vbox:
            xalign 0.5
            yalign 0.35
            spacing 10
            text "Summer Camp Adventures" size 48 bold True color "#FFFFFF" xalign 0.5
            text "A story of friendship, adventure and memory" size 20 color "#D4F1F4" xalign 0.5
        vbox:
            xalign 0.5
            yalign 0.65
            spacing 15
            textbutton "New Game" action Jump("character_creation") text_size 28 xalign 0.5
            textbutton "Load Game" action ShowMenu("load") text_size 28 xalign 0.5
            textbutton "Quit" action Quit() text_size 28 xalign 0.5
    label title_screen:
        call screen title_main
        jump title_screen

FILE: game/character_creation.rpy
    default player_name = "Camp Kid"
    screen char_creation():
        tag menu
        add Solid("#2E86AB")
        vbox:
            xalign 0.5
            yalign 0.4
            spacing 20
            text "What is your name?" size 36 bold True color "#FFFFFF" xalign 0.5
            input:
                value VariableInputValue("player_name")
                length 20
                pixel_width 400
                color "#FFFFFF"
                xalign 0.5
            textbutton "Start Adventure" action Jump("start_game") text_size 28 xalign 0.5
            textbutton "Back" action Jump("title_screen") text_size 24 xalign 0.5
    label character_creation:
        call screen char_creation
        jump character_creation

FILE: game/camp_loop.rpy
    label start_game:
        "The bus pulls up to the camp gates."
        "You step out, bag over your shoulder, ready for the summer."
        jump camp_loop
    label camp_loop:
        "Day [camp_day] at camp."
        menu:
            "Explore the lake":
                "You head down to the lake. The water sparkles."
                $ camp_day += 1
                jump camp_loop
            "Check the cabin":
                "You walk back to your cabin. It smells like pine."
                $ camp_day += 1
                jump camp_loop
            "Go to sleep":
                "You turn in early. Tomorrow will be another day."
                return

## 3. CURRENT STATE

Works:
- script.rpy loads and jumps to title screen
- Title screen renders with buttons
- Character creation loads with name input
- Camp loop runs with day counter and 3 choices

Not built yet:
- Characters/NPCs
- Friendship system
- Memory system
- Events
- World map
- Art, music, sound
- Story arcs and endings
- Settings screen

## 4. CRITICAL REN'PY RULES

VARIABLES:
- Use: default variable_name = value
- NEVER: default store.variable_name
- In dialogue: [variable_name]
- In code: $ variable_name += 1

SCREENS:
- Screen name and label name must ALWAYS be different
  CORRECT: screen title_main + label title_screen
  WRONG: screen title_screen + label title_screen
- Never use background "#COLOR" in a screen — use add Solid("#COLOR")
- Never use radius — not valid in Ren'Py 8
- Never use checkbox — use textbutton with ToggleField
- Never use Variable("name") — use VariableInputValue("name")
- Never use show screen + pause — use call screen + jump

NARRATOR:
- narrator is built-in — NEVER define it
- Plain "text" lines use narrator automatically

CHARACTERS:
- NEVER use p "dialogue" as speaker — p will be the player object
- Use plain "narration" or define characters with unique names

PYTHON LOOPS:
- NEVER: $ for x in list: [indented code]
- ALWAYS use python: block

GIT:
- Push: git add -A && git commit -m "msg" && git push origin main
- Codespaces pull: git fetch origin && git reset --hard origin/main

## 5. NEXT FEATURES TO BUILD (in order)

1. characters.rpy — define NPCs (names TBD by project owner)
2. Add first NPC interaction to camp_loop
3. Friendship counter for first NPC
4. First event scene (campfire)
5. World map with 3 locations
6. Memory system
7. Art assets

## 6. SESSION LOG

2026-05-02 — Wiped old broken code, rebuilt from scratch, all 5 files working
2026-05-02 — Created PROJECT_BIBLE.md

## 7. HOW TO START A NEW SESSION

Paste this to any AI:
Read PROJECT_BIBLE.md before doing anything.
Follow ALL rules in Section 4 strictly.
Check Section 3 for current state.
Do not add features until nothing is broken.
Test after every single file change.
Update Section 3 and Section 6 at the end of the session.
Write all code yourself, do not delegate structure or screens to aider.

CRITICAL RULES FOR ANY AI ASSISTANT:
- Do NOT invent character names. No character named Ann or any other name exists unless the project owner explicitly defines them.
- All NPC names must be approved by the project owner before being written into any code or plan.
- If you want to suggest an NPC, describe the role and ask the owner for a name first.
- Never assume what characters exist. Only what is in this bible is real.
