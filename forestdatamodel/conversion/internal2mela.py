from copy import deepcopy
from typing import Callable

from forestdatamodel import ReferenceTree, TreeStratum, ForestStand
from forestdatamodel.enums.mela import MelaTreeSpecies
from forestdatamodel.enums.internal import TreeSpecies

species_map = {
    TreeSpecies.PINE: MelaTreeSpecies.SCOTS_PINE,
    TreeSpecies.SPRUCE: MelaTreeSpecies.NORWAY_SPRUCE,
    TreeSpecies.SILVER_BIRCH: MelaTreeSpecies.SILVER_BIRCH,
    TreeSpecies.DOWNY_BIRCH: MelaTreeSpecies.DOWNY_BIRCH,
    TreeSpecies.ASPEN: MelaTreeSpecies.ASPEN,
    TreeSpecies.GREY_ALDER: MelaTreeSpecies.ALDER,
    TreeSpecies.OTHER_CONIFEROUS: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.OTHER_DECIDUOUS: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.DOUGLAS_FIR: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.JUNIPER: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.SHORE_PINE: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.EUROPEAN_WHITE_ELM: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.LARCH: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.SMALL_LEAVED_LIME: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.BLACK_SPRUCE: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.WILLOW: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.MOUNTAIN_ASH: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.ABIES: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.GOAT_WILLOW: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.COMMON_ASH: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.KEDAR: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.SERBIAN_SPRUCE: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.OAK: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.BIRD_CHERRY: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.MAPLE: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.CURLY_BIRCH: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.WYCH_ELM: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.UNKNOWN_CONIFEROUS: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.UNKNOWN_DECIDUOUS: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.OTHER_PINE: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.OTHER_SPRUCE: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.THUJA: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.YEW: MelaTreeSpecies.OTHER_CONIFEROUS,
    TreeSpecies.BAY_WILLOW: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.POPLAR: MelaTreeSpecies.OTHER_DECIDUOUS,
    TreeSpecies.HAZEL: MelaTreeSpecies.OTHER_DECIDUOUS
}


def species_mapper(target: ReferenceTree or TreeStratum) -> ReferenceTree or TreeStratum:
    """in-place mapping from internal tree species to mela tree species"""
    target.species = species_map.get(target.species, MelaTreeSpecies.OTHER_DECIDUOUS)
    return target


default_mappers = [species_mapper]


def apply_mappers(target, *mappers):
    """apply a list of mapper functions to a target object"""
    for mapper in mappers:
        target = mapper(target)
    return target


def mela_tree(tree: ReferenceTree) -> ReferenceTree:
    """Convert a ReferenceTree so that enumerated category variables are converted to Mela value space"""
    return apply_mappers(tree, *default_mappers)


def mela_stratum(stratum: TreeStratum) -> TreeStratum:
    """Convert a TreeStratum so that enumerated category variables are converted to Mela value space"""
    return apply_mappers(stratum, *default_mappers)


def mela_stand(stand: ForestStand) -> ForestStand:
    """Convert a ForestStand so that enumerated category variables are converted to Mela value space"""
    stand.reference_trees = list(map(mela_tree, stand.reference_trees))
    stand.tree_strata = list(map(mela_stratum, stand.tree_strata))
    return stand
