import unittest

from forestdatamodel.model import ReferenceTree, ForestStand, TreeStratum
from forestdatamodel.conversion.internal2mela import species_mapper, mela_stand
from forestdatamodel.enums.internal import TreeSpecies
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

    def test_stand_species_conversion(self):
        fixture = ForestStand(geo_location=(6654200, 102598, 0.0, "EPSG:3067"), area=100.0, area_weight=100.0, auxiliary_stand=True)
        tree = ReferenceTree(species=TreeSpecies.SPRUCE, stand=fixture)
        stratum = TreeStratum(species=TreeSpecies.PINE, stand=fixture)
        fixture.reference_trees.append(tree)
        fixture.tree_strata.append(stratum)
        result = mela_stand(fixture)
        self.assertEqual(MelaTreeSpecies.NORWAY_SPRUCE, result.reference_trees[0].species)
        self.assertEqual(MelaTreeSpecies.SCOTS_PINE, result.tree_strata[0].species)
        self.assertEqual((6654.2, 102.598, 0.0, "EPSG:3067"), result.geo_location)
        self.assertEqual(0.0, result.area)
        self.assertEqual(100.0, result.area_weight)
