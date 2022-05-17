from forestdatamodel.enums.forest_centre import ForestCentreSpecies
from forestdatamodel.enums.vmi import VmiSpecies
from forestdatamodel.enums.mela import MelaTreeSpecies
from forestdatamodel.enums.internal import TreeSpecies
from forestdatamodel.converters import mapping


def vmi_to_internal(vmi_code: str) -> TreeSpecies:
    vmi_species = VmiSpecies(vmi_code)
    return mapping.vmi_to_internal[vmi_species]


def fc_to_internal(fc_code: int) -> TreeSpecies:
    fc_species = ForestCentreSpecies(fc_code)
    return mapping.fc_to_internal[fc_species]
