from forestdatamodel.enums.forest_centre import ForestCentreOwnerCategory, ForestCentreSoilPeatlandCategory, ForestCentreSpecies, ForestCentreLandUseCategory
from forestdatamodel.enums.internal import OwnerCategory, SoilPeatlandCategory, TreeSpecies, LandUseCategory

__species_map = {
    ForestCentreSpecies.PINE: TreeSpecies.PINE,
    ForestCentreSpecies.SPRUCE: TreeSpecies.SPRUCE,
    ForestCentreSpecies.SILVER_BIRCH: TreeSpecies.SILVER_BIRCH,
    ForestCentreSpecies.DOWNY_BIRCH: TreeSpecies.DOWNY_BIRCH,
    ForestCentreSpecies.ASPEN: TreeSpecies.ASPEN,
    ForestCentreSpecies.GREY_ALDER: TreeSpecies.GREY_ALDER,
    ForestCentreSpecies.COMMON_ALDER: TreeSpecies.COMMON_ALDER,
    ForestCentreSpecies.OTHER_CONIFEROUS: TreeSpecies.OTHER_CONIFEROUS,
    ForestCentreSpecies.OTHER_DECIDUOUS: TreeSpecies.OTHER_DECIDUOUS,
    ForestCentreSpecies.DOUGLAS_FIR: TreeSpecies.DOUGLAS_FIR,
    ForestCentreSpecies.JUNIPER: TreeSpecies.JUNIPER,
    ForestCentreSpecies.SHORE_PINE: TreeSpecies.SHORE_PINE,
    ForestCentreSpecies.EUROPEAN_WHITE_ELM: TreeSpecies.EUROPEAN_WHITE_ELM,
    ForestCentreSpecies.LARCH: TreeSpecies.LARCH,
    ForestCentreSpecies.SMALL_LEAVED_LIME: TreeSpecies.SMALL_LEAVED_LIME,
    ForestCentreSpecies.BLACK_SPRUCE: TreeSpecies.BLACK_SPRUCE,
    ForestCentreSpecies.WILLOW: TreeSpecies.WILLOW,
    ForestCentreSpecies.MOUNTAIN_ASH: TreeSpecies.MOUNTAIN_ASH,
    ForestCentreSpecies.ABIES: TreeSpecies.ABIES,
    ForestCentreSpecies.GOAT_WILLOW: TreeSpecies.GOAT_WILLOW,
    ForestCentreSpecies.COMMON_ASH: TreeSpecies.COMMON_ASH,
    ForestCentreSpecies.KEDAR: TreeSpecies.KEDAR,
    ForestCentreSpecies.SERBIAN_SPRUCE: TreeSpecies.SERBIAN_SPRUCE,
    ForestCentreSpecies.OAK: TreeSpecies.OAK,
    ForestCentreSpecies.BIRD_CHERRY: TreeSpecies.BIRD_CHERRY,
    ForestCentreSpecies.MAPLE: TreeSpecies.MAPLE,
    ForestCentreSpecies.CURLY_BIRCH: TreeSpecies.CURLY_BIRCH,
    ForestCentreSpecies.WYCH_ELM: TreeSpecies.WYCH_ELM,
    ForestCentreSpecies.UNKNOWN_CONIFEROUS: TreeSpecies.UNKNOWN_CONIFEROUS,
    ForestCentreSpecies.UNKNOWN_DECIDUOUS: TreeSpecies.UNKNOWN_DECIDUOUS,
}

__land_use_map = {
    ForestCentreLandUseCategory.FOREST: LandUseCategory.FOREST,
    ForestCentreLandUseCategory.SCRUB_LAND: LandUseCategory.SCRUB_LAND,
    ForestCentreLandUseCategory.WASTE_LAND: LandUseCategory.WASTE_LAND,
    ForestCentreLandUseCategory.OTHER_FOREST: LandUseCategory.OTHER_FOREST,
    ForestCentreLandUseCategory.AGRICULTURAL: LandUseCategory.AGRICULTURAL,
    ForestCentreLandUseCategory.REAL_ESTATE: LandUseCategory.REAL_ESTATE,
    ForestCentreLandUseCategory.OTHER_LAND: LandUseCategory.OTHER_LAND,
    ForestCentreLandUseCategory.WATER_BODY: LandUseCategory.WATER_BODY
}

__owner_map = {
    ForestCentreOwnerCategory.PRIVATE: OwnerCategory.PRIVATE,
    ForestCentreOwnerCategory.FOREST_INDUSTRY: OwnerCategory.FOREST_INDUSTRY,
    ForestCentreOwnerCategory.STATE: OwnerCategory.OTHER_STATE_AGENCY,
    ForestCentreOwnerCategory.JULKISYHTEISO: OwnerCategory.OTHER_COMMUNITY
}

__soil_peatland_map = {
    ForestCentreSoilPeatlandCategory.MINERAL_SOIL: SoilPeatlandCategory.MINERAL_SOIL,
    ForestCentreSoilPeatlandCategory.SPRUCE_MIRE: SoilPeatlandCategory.SPRUCE_MIRE,
    ForestCentreSoilPeatlandCategory.PINE_MIRE: SoilPeatlandCategory.PINE_MIRE,
    ForestCentreSoilPeatlandCategory.BARREN_TREELESS_MIRE: SoilPeatlandCategory.BARREN_TREELESS_MIRE,
    ForestCentreSoilPeatlandCategory.RICH_TREELESS_MIRE: SoilPeatlandCategory.RICH_TREELESS_MIRE
}

def convert_soil_peatland_category(sp_code: str) -> SoilPeatlandCategory:
    value = ForestCentreSoilPeatlandCategory(sp_code)
    return __soil_peatland_map.get(value)


def convert_land_use_category(lu_code: str) -> LandUseCategory:
    fc_category = ForestCentreLandUseCategory(lu_code)
    return __land_use_map.get(fc_category)


def convert_species(species_code: str) -> TreeSpecies:
    """Converts FC species code to internal TreeSpecies code"""
    fc_species = ForestCentreSpecies(species_code)
    return __species_map.get(fc_species)


def convert_owner(owner_code: str) -> OwnerCategory:
    fc_owner = ForestCentreOwnerCategory(owner_code)
    return __owner_map.get(fc_owner)
