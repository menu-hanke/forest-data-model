from enum import Enum

#index starts at 0 for variables which start at 0 in the MELA doc, same for those starting at 1

class MelaOwnerCategory(Enum):
    PRIVATE = 0
    ENTERPRISE = 1
    STATE = 2
    MUNICIPALITY = 3
    COMMUNITY = 4

class MelaLandUseCategory(Enum):
    FOREST_LAND = 1
    SCRUB_LAND = 2
    WASTE_LAND = 3
    OTHER = 4
    AGRICULTURAL_LAND = 5
    BUILT_UP_LAND = 6
    ROADS_OR_ELECTRIC_LINES = 7
    LAKES_AND_RIVERS = 8
    SEA = 9

class MelaSoilAndPeatlandCategory(Enum):
    MINERAL_SOIL = 1
    PEATLAND_SPRUCE_MIRE = 2
    PEATLAND_PINE_MIRE = 3
    PEATLAN_BARREN_TREELESS_MIRE = 4
    PEATLAND_RICH_TREELESS_MIRE = 5


class MelaSiteTypeCategory(Enum):
    VERY_RICH_SITE = 1
    RICH_SITE = 2
    DAMP_SITE = 3
    SUB_DRY_SITE = 4
    DRY_SITE = 5
    BARREN_SITE = 6
    ROCKY_OR_SANDY_AREA = 7
    OPEN_MOUNTAINS = 8

class MelaReductionOfForestTaxationClass(Enum):
    NO_REDUCTION = 0
    STONY_SOIL = 1
    WET_SOIL = 2
    THICK_MOSS_LAYER_EXPRESSING_LOW_SOIL_PRODUCTIVITY = 3
    UNFAVOURABLE_LOCATION = 4


class MelaSiteFertilityCategory(Enum):
    '''Finnish forest taxation class or site fertility category'''
    IA_RESPECTIVE_TO_VERY_RICH_OR_RICH_SITES = 1
    IB_RESPECTIVE_TO_DAMP_SITES = 2
    II_RESPECTIVE_TO_SUB_DRY_SITES = 3
    III_RESPECTIVE_TO_DRY_SITES = 4
    IV_RESPECTIVE_TO_BARREN_SITES_OR_LOWER_IF_FOREST_LAND = 5
    SCRUB_LAND = 6
    WASTE_LAND = 7

class MelaDrainageCategory(Enum):
    UNDRAINED_MINERAL_SOIL = 0
    DITCHED_MINERAL_SOIL = 1
    UNDRAINED_MIRE = 2
    DITCHED_MIRE = 3
    TRANSFORMING_MIRE  = 4
    TRANSFORMED_MIRE = 5

class MelaForestryCentre(Enum):
    AHVENANMAA = 0
    RANNIKKO = 1
    LOUNAIS_SUOMI = 2
    HAME_UUSIMAA = 3
    KAAKKOIS_SUOMI = 4
    PIRKANMAA = 5
    ETELA_SAVO = 6
    ETELA_POHJANMAA = 7
    KESKI_SUOMI = 8
    POHJOIS_SAVO = 9
    POHJOIS_KARJALA = 10
    KAINUU = 11
    POHJOIS_POHJANMAA = 12
    LAPPI = 13

class MelaForestManagementCategory(Enum):
    '''NOTE: codes 4 and 5 do not exist in the Mela doc'''
    FOREST_LAND_NO_RESTRICTIONS_FOR_TIMBER_PRODUCTION = 1
    FOREST_LAND_ADMINISTRATIONAL_RESTRICTIONS_FOR_TIMBER_PRODUCTION = 2
    SCRUB_LAND_NO_RESTRICTIONS_FOR_TIMBER_PRODUCTION = 3
    WASTE_LAND_NO_RESTRICTIONS_FOR_TIMBER_PRODUCTION= 6
    FOREST_SCRUB_OR_WASTE_LAND_NO_TIMBER_PRODUCTION_ALLOWED = 7

class MelaMethodOfTheLastCutting(Enum):
    NO_CUTTING = 0
    THINNING = 1
    CLEARCUTTING = 2
    FIRST_THINNING = 3
    OVER_STORY_REMOVAL = 4
    SEED_TREE_CUTTING = 5
    sHELTERWOOD_CUTTING = 6

class MelaTreeSpecies(Enum):
    SCOTS_PINE = 1
    NORWAY_SPRUCE = 2
    SILVER_BIRCH = 3
    DOWNY_BIRCH = 4
    ASPEN = 5
    ALDER = 6
    OTHER_CONIFEROUS_SPECIES_THAN_1_OR_2 = 7
    OTHER_DECIDUOUS_SPECIES_THAN_3_TO_6 = 8

class MelaTreeOrigin(Enum):
    NATURAL = 0
    SEEDED = 1
    PLANTED = 2
    SUPPLEMENTARY_PLANTED = 3