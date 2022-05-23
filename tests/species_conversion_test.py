from forestdatamodel.enums.internal import TreeSpecies
from forestdatamodel.enums.vmi import VmiSpecies
from tests import test_util
from forestdatamodel.conversion import species_conversions

# testaa myös että väärä koodi palauttaa virheen


class TestConversion(test_util.ConverterTestSuite):
    def test_convert_source_species_to_internal_species(self):
        assertions = [
            #VMI
            (["A9","VMI"], TreeSpecies.YEW),
            (["A1","VMI"], TreeSpecies.SHORE_PINE),
            (["0","VMI"], TreeSpecies.UNKNOWN),

            #FFC
            (["1","FFC"], TreeSpecies.PINE),
            (["30","FFC"], TreeSpecies.UNKNOWN_DECIDUOUS),
        ]
        self.run_with_test_assertions(
            assertions, species_conversions.source_species_to_internal)
