from forestdatamodel.enums.vmi import VmiOwnerCategory, VmiSoilPeatlandCategory, VmiSpecies, VmiLandUseCategory
from forestdatamodel.enums.internal import OwnerCategory, SoilPeatlandCategory, TreeSpecies, LandUseCategory

__species_map = {
    VmiSpecies.PINE: TreeSpecies.PINE,
    VmiSpecies.SPRUCE: TreeSpecies.SPRUCE,
    VmiSpecies.SILVER_BIRCH: TreeSpecies.SILVER_BIRCH,
    VmiSpecies.DOWNY_BIRCH: TreeSpecies.DOWNY_BIRCH,
    VmiSpecies.ASPEN: TreeSpecies.ASPEN,
    VmiSpecies.GREY_ALDER: TreeSpecies.GREY_ALDER,
    VmiSpecies.COMMON_ALDER: TreeSpecies.COMMON_ALDER,
    VmiSpecies.MOUNTAIN_ASH: TreeSpecies.MOUNTAIN_ASH,
    VmiSpecies.GOAT_WILLOW: TreeSpecies.GOAT_WILLOW,
    VmiSpecies.OTHER_CONIFEROUS: TreeSpecies.OTHER_CONIFEROUS,
    VmiSpecies.SHORE_PINE: TreeSpecies.SHORE_PINE,
    VmiSpecies.KEDAR: TreeSpecies.KEDAR,
    VmiSpecies.OTHER_PINE: TreeSpecies.OTHER_PINE,
    VmiSpecies.LARCH: TreeSpecies.LARCH,
    VmiSpecies.ABIES: TreeSpecies.ABIES,
    VmiSpecies.OTHER_SPRUCE: TreeSpecies.OTHER_SPRUCE,
    VmiSpecies.THUJA: TreeSpecies.THUJA,
    VmiSpecies.JUNIPER: TreeSpecies.JUNIPER,
    VmiSpecies.YEW: TreeSpecies.YEW,
    VmiSpecies.OTHER_DECIDUOUS: TreeSpecies.OTHER_DECIDUOUS,
    VmiSpecies.BAY_WILLOW: TreeSpecies.BAY_WILLOW,
    VmiSpecies.EUROPEAN_WHITE_ELM: TreeSpecies.EUROPEAN_WHITE_ELM,
    VmiSpecies.WYCH_ELM: TreeSpecies.WYCH_ELM,
    VmiSpecies.SMALL_LEAVED_LIME: TreeSpecies.SMALL_LEAVED_LIME,
    VmiSpecies.POPLAR: TreeSpecies.POPLAR,
    VmiSpecies.COMMON_ASH: TreeSpecies.COMMON_ASH,
    VmiSpecies.OAK: TreeSpecies.OAK,
    VmiSpecies.BIRD_CHERRY: TreeSpecies.BIRD_CHERRY,
    VmiSpecies.MAPLE: TreeSpecies.MAPLE,
    VmiSpecies.HAZEL: TreeSpecies.HAZEL,
    VmiSpecies.UNKNOWN: TreeSpecies.UNKNOWN,
}

__land_use_map = {
    VmiLandUseCategory.FOREST: LandUseCategory.FOREST,
    VmiLandUseCategory.SCRUB_LAND: LandUseCategory.SCRUB_LAND,
    VmiLandUseCategory.WASTE_LAND: LandUseCategory.WASTE_LAND,
    VmiLandUseCategory.OTHER_FOREST: LandUseCategory.OTHER_FOREST,
    VmiLandUseCategory.AGRICULTURAL: LandUseCategory.AGRICULTURAL,
    VmiLandUseCategory.BUILT_LAND: LandUseCategory.BUILT_LAND,
    VmiLandUseCategory.ROAD: LandUseCategory.ROAD,
    VmiLandUseCategory.ENERGY_TRANSMISSION_LINE: LandUseCategory.ENERGY_TRANSMISSION_LINE,
    VmiLandUseCategory.FRESHWATER: LandUseCategory.FRESHWATER,
    VmiLandUseCategory.SEA: LandUseCategory.SEA
}

__owner_map = {
    VmiOwnerCategory.UNKNOWN: OwnerCategory.UNKNOWN,
    VmiOwnerCategory.PRIVATE: OwnerCategory.PRIVATE,
    VmiOwnerCategory.FOREST_INDUSTRY_ENTERPRISE: OwnerCategory.FOREST_INDUSTRY,
    VmiOwnerCategory.OTHER_ENTERPRISE: OwnerCategory.OTHER_ENTERPRISE,
    VmiOwnerCategory.METSAHALLITUS: OwnerCategory.METSAHALLITUS,
    VmiOwnerCategory.OTHER_STATE_AGENCY: OwnerCategory.OTHER_STATE_AGENCY,
    VmiOwnerCategory.FOREST_COOP: OwnerCategory.FOREST_COOP,
    VmiOwnerCategory.MUNICIPALITY: OwnerCategory.MUNICIPALITY,
    VmiOwnerCategory.CONGREGATION: OwnerCategory.CONGREGATION,
    VmiOwnerCategory.OTHER_COMMUNITY: OwnerCategory.OTHER_COMMUNITY,
    VmiOwnerCategory.UNDIVIDED: OwnerCategory.UNDIVIDED
}

__soil_peatland_map = {
    VmiSoilPeatlandCategory.MINERAL_SOIL: SoilPeatlandCategory.MINERAL_SOIL,
    VmiSoilPeatlandCategory.SPRUCE_MIRE: SoilPeatlandCategory.SPRUCE_MIRE,
    VmiSoilPeatlandCategory.PINE_MIRE: SoilPeatlandCategory.PINE_MIRE,
    VmiSoilPeatlandCategory.TREELESS_MIRE: SoilPeatlandCategory.UNSPECIFIED_TREELESS_MIRE,
}

def convert_soil_peatland_category(sp_code: str) -> LandUseCategory:
    vmi_category = VmiSoilPeatlandCategory(sp_code)
    return __soil_peatland_map.get(vmi_category)

def convert_land_use_category(lu_code: str) -> LandUseCategory:
    """sanitization of lu_code is the responsibility of the caller, 
    meaning that this conversion will fail e.g. if the parameter is a lower-case letter."""
    vmi_category = VmiLandUseCategory(lu_code)
    return __land_use_map.get(vmi_category)


def convert_species(species_code: str) -> TreeSpecies:
    """Converts VMI species code to internal TreeSpecies code"""
    value = species_code.strip()
    vmi_species = VmiSpecies(value)
    return __species_map.get(vmi_species)

def convert_owner(owner_code: str) -> OwnerCategory:
    vmi_owner = VmiOwnerCategory(owner_code)
    return __owner_map.get(vmi_owner)