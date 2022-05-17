import typing
import unittest


class ConverterTestSuite(unittest.TestCase):
    def run_with_test_assertions(self, assertions: typing.List[typing.Tuple], fn: typing.Callable):
        for case in assertions:
            result = fn(*case[0])
            self.assertEqual(case[1], result)

    def assertions_should_raise_ValueError(self, assertions: typing.List[typing.Tuple], fn: typing.Callable):
        for case in assertions:
            result = fn(*case[0])
            self.assertRaises(ValueError)
