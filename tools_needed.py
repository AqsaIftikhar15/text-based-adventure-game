from agents import function_tool
import random

@function_tool
def roll_dice() -> str:
    return f"You rolled a dice: {random.randint(1, 6)}!"

@function_tool
def generate_event() -> str:
    events = [
        "You spotted a group of goblins in the forest.",
        "You saw a mysterious stranger lurking around the local tavern.",
        "You are about to encounter a severe storm brewing on the horizon.",
        "You stumbled upon a hidden cave filled with ancient treasures.",
    ]

    return random.choice(events)