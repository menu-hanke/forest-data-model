from enum import Enum


class ForestCentreSpecies(Enum):
    PINE = '1'
    SPRUCE = '2'
    SILVER_BIRCH = '3'
    DOWNY_BIRCH = '4'
    ASPEN = '5'
    GREY_ALDER = '6'
    COMMON_ALDER = '7'
    OTHER_CONIFEROUS = '8'
    OTHER_DECIDUOUS = '9'
    DOUGLAS_FIR = '10'
    JUNIPER = '11'
    SHORE_PINE = '12'
    EUROPEAN_WHITE_ELM = '13'
    LARCH = '14'
    SMALL_LEAVED_LIME = '15'
    BLACK_SPRUCE = '16'
    WILLOW = '17'
    MOUNTAIN_ASH = '18'
    ABIES = '19'
    GOAT_WILLOW = '20'
    COMMON_ASH = '21'
    KEDAR = '22'
    SERBIAN_SPRUCE = '23'
    OAK = '24'
    BIRD_CHERRY = '25'
    MAPLE = '26'
    CURLY_BIRCH = '27'
    WYCH_ELM = '28'
    UNKNOWN_CONIFEROUS = '29'
    UNKNOWN_DECIDUOUS = '30'

class ForestCentreLandUseCategory(Enum):
    FOREST = '1'
    SCRUB_LAND = '2'
    WASTE_LAND = '3'
    OTHER_FOREST = '4'
    AGRICULTURAL = '6'
    REAL_ESTATE = '5'
    OTHER_LAND = '7'
    WATER_BODY = '8'
class ForestCentreOwnerCategory(Enum):
    PRIVATE = "1"
    FOREST_INDUSTRY = "2"
    STATE = "3"
    JULKISYHTEISO = "4"

class ForestCentreSoilPeatlandCategory(Enum):
    MINERAL_SOIL = '1'
    SPRUCE_MIRE = '2'
    PINE_MIRE = '3'
    BARREN_TREELESS_MIRE = '4'
    RICH_TREELESS_MIRE = '5'
