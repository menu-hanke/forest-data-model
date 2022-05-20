from enum import IntEnum


# IntEnum provides easy json serialisation
class TreeSpecies(IntEnum):
    """This list is formed by combining VMI and Forest centre species 
    and listing all the distinct ones. UNKNOWN (38) is not part of either list, 
    but can be assigned to in case the source data species is unexpected."""
    PINE = 1
    SPRUCE = 2
    SILVER_BIRCH = 3
    DOWNY_BIRCH = 4
    ASPEN = 5
    GREY_ALDER = 6
    COMMON_ALDER = 7
    OTHER_CONIFEROUS = 8
    OTHER_DECIDUOUS = 9
    DOUGLAS_FIR = 10
    JUNIPER = 11
    SHORE_PINE = 12
    EUROPEAN_WHITE_ELM = 13
    LARCH = 14
    SMALL_LEAVED_LIME = 15
    BLACK_SPRUCE = 16
    WILLOW = 17
    MOUNTAIN_ASH = 18
    ABIES = 19
    GOAT_WILLOW = 20
    COMMON_ASH = 21
    KEDAR = 22
    SERBIAN_SPRUCE = 23
    OAK = 24
    BIRD_CHERRY = 25
    MAPLE = 26
    CURLY_BIRCH = 27
    WYCH_ELM = 28
    UNKNOWN_CONIFEROUS = 29
    UNKNOWN_DECIDUOUS = 30
    OTHER_PINE = 31
    OTHER_SPRUCE = 32
    THUJA = 33
    YEW = 34
    BAY_WILLOW = 35
    POPLAR = 36
    HAZEL = 37
    UNKNOWN = 38
