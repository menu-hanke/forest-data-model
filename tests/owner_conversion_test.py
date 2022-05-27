from tests import test_util
from forestdatamodel.conversion import fc2internal, vmi2internal
from forestdatamodel.enums.internal import OwnerCategory

class TestConversion(test_util.ConverterTestSuite):
    def test_convert_VMI_owner_to_internal(self):
        assertions = [
            (["1"], OwnerCategory.PRIVATE),
            (["2"], OwnerCategory.ENTERPRISE),
            (["A"], OwnerCategory.PUBLIC_CORPORATION)
        ]

        self.run_with_test_assertions(
            assertions, vmi2internal.convert_owner
        )

    def test_convert_FFC_owner_to_internal(self):
        assertions = [
            (["1"], OwnerCategory.PRIVATE),
            (["2"], OwnerCategory.ENTERPRISE),
            (["4"], OwnerCategory.PUBLIC_CORPORATION)
        ]

        self.run_with_test_assertions(
            assertions, fc2internal.convert_owner
        )
