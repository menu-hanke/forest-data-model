from tests import test_util
from forestdatamodel.converters import species_conversions

class TestConversion(test_util.ConverterTestSuite):
    def test_convert_vmi_species_to_internal_species(self):
        assertions = [
            (["A1"], 12)
        ]
        self.run_with_test_assertions(assertions, species_conversions.vmi_to_internal)