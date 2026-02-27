from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value, get_option_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def BeatCascade(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of cascade."""
    if (state.count("Cascade Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade")):
        return True
    return False

def BeatSand(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Sand."""
    if (state.count("Sand Moon", player) >= get_option_value(multiworld, player, "moonsreqforsand")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand")):
        return True
    return False

def BeatLake(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if (state.count("Lake Moon", player) >= get_option_value(multiworld, player, "moonsreqforlake")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake")):
        return True
    return False

def BeatWooded(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the Lake and wooded."""
    if (state.count("Wooded Moon", player) >= get_option_value(multiworld, player, "moonsreqforwooded")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonsreqforwooded")):
        return True
    return False

def BeatLost(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Lost."""
    if (state.count("Lost Moon", player) >= get_option_value(multiworld, player, "moonsreqforlost")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost")):
        return True
    return False

def BeatMetro(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Metro."""
    if (state.count("Metro Moon", player) >= get_option_value(multiworld, player, "moonsreqformetro")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost") + get_option_value(multiworld, player, "moonsreqformetro")):
        return True
    return False

def BeatSnow(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Snow."""
    if (state.count("Snow Moon", player) >= get_option_value(multiworld, player, "moonsreqforsnow")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost") + get_option_value(multiworld, player, "moonsreqformetro") + get_option_value(multiworld, player, "moonsreqforsnow")):
        return True
    return False
def BeatSeaside(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Snow."""
    if (state.count("Seaside Moon", player) >= get_option_value(multiworld, player, "moonsreqforseaside")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost") + get_option_value(multiworld, player, "moonsreqformetro") + get_option_value(multiworld, player, "moonsreqforseaside")):
        return True
def BeatLuncheon(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Luncheon."""
    if (state.count("Luncheon Moon", player) >= get_option_value(multiworld, player, "moonsreqforluncheon")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost") + get_option_value(multiworld, player, "moonsreqformetro") + get_option_value(multiworld, player, "moonsreqforsnow") + get_option_value(multiworld, player, "moonsreqforseaside") + get_option_value(multiworld, player, "moonsreqforluncheon")):
        return True
    return False

def BeatRuined(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player start Ruined."""
    if (state.count("Ruined Moon", player) >= get_option_value(multiworld, player, "moonsreqforruined")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost") + get_option_value(multiworld, player, "moonsreqformetro") + get_option_value(multiworld, player, "moonsreqforsnow") + get_option_value(multiworld, player, "moonsreqforseaside") + get_option_value(multiworld, player, "moonsreqforluncheon") + get_option_value(multiworld, player, "moonsreqforruined")):
        return True
    return False

def BeatBowser(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """can the player reach the end of Bowser."""
    if (state.count("Bowser Moon", player) >= get_option_value(multiworld, player, "moonsreqforbowser")):
        return True
    if (state.count("Power Moon", player) >= get_option_value(multiworld, player, "moonsreqforcascade") + get_option_value(multiworld, player, "moonsreqforsand") + get_option_value(multiworld, player, "moonreqforlake") + get_option_value(multiworld, player, "moonsreqforwooded") + get_option_value(multiworld, player, "moonsreqforlost") + get_option_value(multiworld, player, "moonsreqformetro") + get_option_value(multiworld, player, "moonsreqforsnow") + get_option_value(multiworld, player, "moonsreqforseaside") + get_option_value(multiworld, player, "moonsreqforluncheon") + get_option_value(multiworld, player, "moonsreqforruined") + get_option_value(multiworld, player, "moonsreqforbowser")):
        return True