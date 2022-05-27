from enum import Enum


class VmiSpecies(Enum):
    PINE = "1"
    SPRUCE = "2"
    SILVER_BIRCH = "3"
    DOWNY_BIRCH = "4"
    ASPEN = "5"
    GREY_ALDER = "6"
    COMMON_ALDER = "7"
    MOUNTAIN_ASH = "8"
    GOAT_WILLOW = "9"
    OTHER_CONIFEROUS = "A0"
    SHORE_PINE = "A1"
    KEDAR = "A2"
    OTHER_PINE = "A3"
    LARCH = "A4"
    ABIES = "A5"
    OTHER_SPRUCE = "A6"
    THUJA = "A7"
    JUNIPER = "A8"
    YEW = "A9"
    OTHER_DECIDUOUS = "B0"
    BAY_WILLOW = "B1"
    EUROPEAN_WHITE_ELM = "B2"
    WYCH_ELM = "B3"
    SMALL_LEAVED_LIME = "B4"
    POPLAR = "B5"
    COMMON_ASH = "B6"
    OAK = "B7"
    BIRD_CHERRY = "B8"
    MAPLE = "B9"
    HAZEL = "C1"
    UNKNOWN = None

    @classmethod
    def _missing_(cls, name):
        if name == "0":
            return cls.UNKNOWN


class VmiOwnerCategory(Enum):
    #private
    PRIVATE = "1"
    #enterprise
    FOREST_INDUSTRY_ENTERPRISE = "2"
    OTHER_ENTERPRISE = "3"
    #state forest
    METSAHALLITUS = "4" 
    OTHER_STATE_AGENCY = "5"
    #communities
    FOREST_COOP = "6" # = yhteismetsä
    MUNICIPALITY = "7"
    CONGREGATION = "8"
    OTHER_COMMUNITY = "9"
    #jakamaton 
    UNDIVIDED = "A" # = jakamaton kuolinpesä
