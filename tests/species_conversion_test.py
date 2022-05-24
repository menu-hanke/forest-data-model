from forestdatamodel.enums.internal import TreeSpecies
from tests import test_util
from forestdatamodel.conversion import fc2internal, vmi2internal

class TestConversion(test_util.ConverterTestSuite):
    def test_convert_VMI_species_to_internal_species(self):
        assertions = [
            (["A9"], TreeSpecies.YEW),
            (["A1"], TreeSpecies.SHORE_PINE),
            (["0"], TreeSpecies.UNKNOWN),
        ]
        self.run_with_test_assertions(
            assertions, vmi2internal.convert_species)

    def test_convert_FC_species_to_internal_species(self):
        assertions = [
            (["1"], TreeSpecies.PINE),
            (["30"], TreeSpecies.UNKNOWN_DECIDUOUS),
        ]
        self.run_with_test_assertions(
            assertions, fc2internal.convert_species)
