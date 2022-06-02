from parameterized import parameterized
import unittest
from forestdatamodel.enums.internal import SoilPeatlandCategory
from forestdatamodel.conversion import vmi2internal, fc2internal
class TestConversion(unittest.TestCase):
    
    @parameterized.expand(
        [
            ('1', SoilPeatlandCategory.MINERAL_SOIL),
            ('2', SoilPeatlandCategory.SPRUCE_MIRE),
            ('3', SoilPeatlandCategory.PINE_MIRE),
            ('4', SoilPeatlandCategory.UNSPECIFIED_TREELESS_MIRE),
        ]
    )
    def test_convert_VMI_soil_category_to_internal(self, sp_code, expected):
        result = vmi2internal.convert_soil_peatland_category(sp_code)
        self.assertEqual(result, expected)


    @parameterized.expand(
        [
            ('1', SoilPeatlandCategory.MINERAL_SOIL),
            ('2', SoilPeatlandCategory.SPRUCE_MIRE),
            ('3', SoilPeatlandCategory.PINE_MIRE),
            ('4', SoilPeatlandCategory.BARREN_TREELESS_MIRE),
            ('5', SoilPeatlandCategory.RICH_TREELESS_MIRE),
        ]
    )
    def test_convert_FFC_soil_category_to_internal(self, sp_code, expected):
        result = fc2internal.convert_soil_peatland_category(sp_code)
        self.assertEqual(result, expected)