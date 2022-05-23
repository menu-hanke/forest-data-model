from forestdatamodel.enums.forest_centre import ForestCentreSpecies
from forestdatamodel.enums.vmi import VmiSpecies
from forestdatamodel.enums.mela import MelaTreeSpecies
from forestdatamodel.enums.internal import TreeSpecies
from forestdatamodel.conversion import mapping
from enum import Enum


def source_species_to_internal(species_code: str, source: str) -> TreeSpecies:
    """Tries to convert source data tree species to internal tree species.

    :source: 'VMI' or 'FFC'"""

    if source.upper() == "VMI":
        value = species_code.strip()
        vmi_species = VmiSpecies(value)
        return mapping.vmi_to_internal.get(vmi_species)
    else:
        fc_species = ForestCentreSpecies(species_code)
        return mapping.fc_to_internal.get(fc_species)

