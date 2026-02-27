from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value, get_option_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"
def BeatCascade(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of cascade."""
    cascadetoleave = get_option_value(multiworld, player, "moonsreqforcascade")  
    if (state.count("Cascade Kingdom Power Moon", player) >= cascadetoleave):
        return True
    if (state.count("Power Moon", player) >= cascadetoleave):
        return True
    return False

def BeatSand(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Sand."""
    cascadetoleave = get_option_value(multiworld, player, "moonsreqforcascade") 
    sandtoleave = get_option_value(multiworld, player, "moonsreqforsand")
    if (state.count("Sand Kingdom Power Moon", player) >= sandtoleave):
        return True
    if (state.count("Power Moon", player) >= cascadetoleave + sandtoleave):
        return True
    return False

def BeatLake(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    cascadetoleave = get_option_value(multiworld, player, "moonsreqforcascade") 
    sandtoleave = get_option_value(multiworld, player, "moonsreqforsand")
    laketoleave = get_option_value(multiworld, player, "moonreqforlake")
    if (state.count("Lake Kingdom Power Moon", player) >= laketoleave):
        return True
    if (state.count("Power Moon", player) >= cascadetoleave + sandtoleave + laketoleave):
        return True
    return False

def BeatWood(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the Lake and wooded."""
    if (state.count("Wooded Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforwooded")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded")):
        return True
    return False

def BeatLost(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Lost."""
    if (state.count("Lost Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforlost")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost")):
        return True
    return False

def BeatMetro(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Metro."""
    if (state.count("Metro Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqformetro")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost") + get_option_value(multiworld, player, "moonsreqformetro")):
        return True
    return False

def BeatSnow(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Snow."""
    if (state.count("Snow Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforsnow")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost") + get_option_value(multiworld, player, "moonsreqformetro") + state.count("Snow Kingdom Power Moon", player) + get_option_value(multiworld, player, "moonsreqforsnow")):
        return True
    return False
def BeatSea(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Snow."""
    if (state.count("Seaside Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforseaside")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost") + get_option_value(multiworld, player, "moonsreqformetro") + state.count("Snow Kingdom Power Moon", player) + get_option_value(multiworld, player, "moonsreqforseaside")):
        return True
def BeatLuncheon(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Luncheon."""
    if (state.count("Luncheon Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforluncheon")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost") + get_option_value(multiworld, player, "moonsreqformetro") + state.count("Seaside Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforseaside") + state.count("Snow Kingdom Power Moon", player) + get_option_value(multiworld, player, "moonsreqforsnow") + state.count("Luncheon Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforluncheon")):
        return True
    return False

def BeatRuined(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player start Ruined."""
    if (state.count("Ruined Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforruined")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost") + get_option_value(multiworld, player, "moonsreqformetro") + state.count("Seaside Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforseaside") + state.count("Snow Kingdom Power Moon", player) + get_option_value(multiworld, player, "moonsreqforsnow") + state.count("Luncheon Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforluncheon") + get_option_value(multiworld, player, "moonsreqforruined")):
        return True
    return False

def BeatBowser(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Bowser."""
    if (state.count("Bowser's Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforbowser") or state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost") + get_option_value(multiworld, player, "moonsreqformetro") + state.count("Seaside Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforseaside") + state.count("Snow Kingdom Power Moon", player) + get_option_value(multiworld, player, "moonsreqforsnow") + state.count("Luncheon Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforluncheon") + get_option_value(multiworld, player, "moonsreqforruined") + state.count("Bowser's Kingdom Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforbowser")):
        return True
    return False