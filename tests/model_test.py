import unittest

from forestdatamodel import ForestStand, ReferenceTree


class TestForestDataModel(unittest.TestCase):

    def test_reference_tree_has_biological_age(self):
        fixture = ReferenceTree()
        assertions = [
            (10.0, True),
            (None, False),
            (-10.0, False),
            (0.0, False),
        ]
        for i in assertions:
            fixture.biological_age = i[0]
            self.assertEqual(i[1], fixture.has_biological_age())

    def test_reference_tree_has_diameter(self):
        fixture = ReferenceTree()
        assertions = [
            (11.5, True),
            (None, False),
            (-10.0, False),
            (0.0, False),
        ]
        for i in assertions:
            fixture.breast_height_diameter = i[0]
            self.assertEqual(i[1], fixture.has_diameter())

    def test_set_area_without_weight(self):
        fixture = ForestStand()
        fixture.set_area(1.0)
        self.assertEqual(1.0, fixture.area)
        self.assertEqual(1.0, fixture.area_weight)

    def test_set_area_with_weight(self):
        fixture = ForestStand()
        fixture.set_area(1.0, 2.0)
        self.assertEqual(1.0, fixture.area)
        self.assertEqual(2.0, fixture.area_weight)

    def test_set_geo_location(self):
        fixture = ForestStand()
        assertions = [
            ((6000.1, 304.3, 10.0), (6000.1, 304.3, 10.0, 'ERTS-TM35FIN')),
            ((6000.1, 304.3, None), (6000.1, 304.3, None, 'ERTS-TM35FIN'))
        ]
        failures = [
            (None, 20.3, 20),
            (23.4, None, 20),

        ]
        for i in assertions:
            fixture.set_geo_location(*i[0])
            self.assertEqual(i[1], fixture.geo_location)
        for i in failures:
            self.assertRaises(Exception, lambda: fixture.set_geo_location(*i))
