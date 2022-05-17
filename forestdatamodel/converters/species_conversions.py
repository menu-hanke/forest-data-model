from forestdatamodel.constants.forest_centre_const import ForestCentreSpecies
from forestdatamodel.constants.vmi_const import VMISpecies
from forestdatamodel.constants.internal_const import InternalTreeSpecies


def vmi_to_internal(vmicode: str) -> InternalTreeSpecies:
    try:
        vmi_species_name = VMISpecies(vmicode).name
        # getting the INternalTreeSpecies at "SHORE_PINE" doesn't make sense - need to access by value, not key/name
        internal_species = InternalTreeSpecies[vmi_species_name]
        return internal_species

    except Exception as e:
        print(f"could not convert vmi code {vmicode} to internal code")
        raise


def fc_to_internal(fc_code: int) -> InternalTreeSpecies:
    try:
        fc_species_name = ForestCentreSpecies(fc_code).name
        internal_species = InternalTreeSpecies(fc_species_name)
        return internal_species
    except Exception as e:
        print(
            f"could not convert forest centre code {fc_species_name} to internal code")
        raise


# testaa että väärä koodi palauttaa virheen
