from forestdatamodel.enums.forest_centre import ForestCentreOwnerCategory, ForestCentreSpecies
from forestdatamodel.enums.internal import OwnerCategory, TreeSpecies

species_map = {
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

owner_map = {
    ForestCentreOwnerCategory.PRIVATE: OwnerCategory.PRIVATE,
    ForestCentreOwnerCategory.FOREST_INDUSTRY: OwnerCategory.ENTERPRISE,
    ForestCentreOwnerCategory.STATE: OwnerCategory.STATE,
    ForestCentreOwnerCategory.PUBLIC_CORPORATION: OwnerCategory.PUBLIC_CORPORATION
}

def convert_species(species_code: str) -> TreeSpecies:
    """Converts FC species code to internal TreeSpecies code"""
    fc_species = ForestCentreSpecies(species_code)
    return species_map.get(fc_species)


def convert_owner(owner_code: str) -> OwnerCategory:
    fc_owner = ForestCentreOwnerCategory(owner_code)
    return owner_map.get(fc_owner)