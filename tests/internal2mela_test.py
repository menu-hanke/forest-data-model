import unittest

from forestdatamodel import ReferenceTree, TreeSpecies, ForestStand, TreeStratum
from forestdatamodel.conversion.internal2mela import species_mapper, mela_stand
from forestdatamodel.enums.mela import MelaTreeSpecies


class Internal2MelaTest(unittest.TestCase):
    def test_species_good(self):
        fixture = ReferenceTree()
        fixture.species = TreeSpecies.THUJA
        result = species_mapper(fixture)
        self.assertEqual(MelaTreeSpecies.OTHER_CONIFEROUS, result.species)

    def test_species_unknown(self):
        fixture = ReferenceTree()
        fixture.species = None
        result = species_mapper(fixture)
        self.assertEqual(MelaTreeSpecies.OTHER_DECIDUOUS, result.species)

    def test_stand_conversion(self):
        fixture = ForestStand()
        tree = ReferenceTree(species=TreeSpecies.SPRUCE)
        stratum = TreeStratum(species=TreeSpecies.PINE)
        fixture.reference_trees.append(tree)
        fixture.tree_strata.append(stratum)
        result = mela_stand(fixture)
        self.assertEqual(MelaTreeSpecies.NORWAY_SPRUCE, result.reference_trees[0].species)
        self.assertEqual(MelaTreeSpecies.SCOTS_PINE, result.tree_strata[0].species)
