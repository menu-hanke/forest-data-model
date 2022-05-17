from forestdatamodel.enums.internal import TreeSpecies
from forestdatamodel.enums.vmi import VmiSpecies
from tests import test_util
from forestdatamodel.converters import species_conversions

# testaa myös että väärä koodi palauttaa virheen


class TestConversion(test_util.ConverterTestSuite):
    def test_convert_vmi_species_to_internal_species(self):
        assertions = [
            (["A1"], TreeSpecies.SHORE_PINE)
        ]
        self.run_with_test_assertions(
            assertions, species_conversions.vmi_to_internal)

    def test_convert_fc_species_to_internal_species(self):
        assertions = [
            ([1], TreeSpecies.PINE)
        ]
        self.run_with_test_assertions(
            assertions, species_conversions.fc_to_internal)
