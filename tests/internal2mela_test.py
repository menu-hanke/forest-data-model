import unittest

from forestdatamodel import ReferenceTree, ForestStand, TreeStratum
from forestdatamodel.conversion.internal2mela import species_mapper, mela_stand
from forestdatamodel.enums.internal import OwnerCategory, TreeSpecies
from forestdatamodel.enums.mela import MelaOwnerCategory, MelaTreeSpecies


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
        tree = ReferenceTree(species=TreeSpecies.SPRUCE, stand=fixture)
        stratum = TreeStratum(species=TreeSpecies.PINE, stand=fixture)
        fixture.reference_trees.append(tree)
        fixture.tree_strata.append(stratum)
        result = mela_stand(fixture)
        self.assertEqual(MelaTreeSpecies.NORWAY_SPRUCE, result.reference_trees[0].species)
        self.assertEqual(MelaTreeSpecies.SCOTS_PINE, result.tree_strata[0].species)

    def test_owner_category(self):
        fixture = ForestStand()
        fixture.owner_category = OwnerCategory.METSAHALLITUS
        result = mela_stand(fixture)
        self.assertEqual(MelaOwnerCategory.STATE, result.owner_category)

        #ownerCategory UNKNOWN should convert to MelaOwnerCategory PRIVATE
        fixture2 = ForestStand()
        fixture2.owner_category = OwnerCategory.UNKNOWN
        result = mela_stand(fixture2)
        self.assertEqual(MelaOwnerCategory.PRIVATE, result.owner_category)
   
