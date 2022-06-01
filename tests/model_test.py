import unittest

from forestdatamodel.model import ForestStand, ReferenceTree, TreeStratum


class TestForestDataModel(unittest.TestCase):

    def test_calculate_dominant_height(self):
        stems = [
            [82, 30],
            [13, 51]
        ]
        diameters = [
            [18.1, 5.7],
            [50.1, 35.9]
        ]
        assertions = [
            # over 100 stems
            ([diameters[0], stems[0]], 15.868),
            # under 100 stems
            ([diameters[1], stems[1]], 38.784375),
        ]
        for i in assertions:
            stand = ForestStand()
            fixtures = [ReferenceTree(breast_height_diameter=d, stems_per_ha=w) for d, w in zip(i[0][0], i[0][1])]
            stand.reference_trees = fixtures
            result = stand.calculate_dominant_height()
            self.assertEqual(i[1], result)

    def test_has_sapling_stems_per_ha(self):
        fixture = TreeStratum()
        assertions = [
            (10.0, True),
            (None, False),
            (-10.0, False),
            (0.0, False),
        ]
        for i in assertions:
            fixture.sapling_stems_per_ha = i[0]
            self.assertEqual(i[1], fixture.has_sapling_stems_per_ha())

    def test_has_height(self):
        fixture = TreeStratum()
        assertions = [
            (10.0, True),
            (None, False),
            (-10.0, False),
            (0.0, False),
        ]
        for i in assertions:
            fixture.mean_height = i[0]
            self.assertEqual(i[1], fixture.has_height())

    def test_stratum_get_breast_height_age(self):
        fixture = TreeStratum()
        assertions = [
            ((10.0, 10.0), 10.0),
            ((10.0, None), 10),
            ((None, 10.0), 0.0),
            ((None, 20.0), 8.0),
            ((None, None), 0.0),
        ]
        for i in assertions:
            fixture.breast_height_age = i[0][0]
            fixture.biological_age = i[0][1]
            self.assertEqual(i[1], fixture.get_breast_height_age())
        # Final test case for different default param.
        fixture.breast_height_age = None
        fixture.biological_age = 20.0
        self.assertEqual(10.0, fixture.get_breast_height_age(subtrahend=10))

    def test_has_stems_per_ha(self):
        fixture = TreeStratum()
        assertions = [
            (10.0, True),
            (None, False),
            (-10.0, False),
            (0.0, False),
        ]
        for i in assertions:
            fixture.stems_per_ha = i[0]
            self.assertEqual(i[1], fixture.has_stems_per_ha())


    def test_stratum_has_basal_area(self):
        fixture = TreeStratum()
        assertions = [
            (10.0, True),
            (None, False),
            (-10.0, False),
            (0.0, False),
        ]
        for i in assertions:
            fixture.basal_area = i[0]
            self.assertEqual(i[1], fixture.has_basal_area())

    def test_stratum_has_breast_height_age(self):
        fixture = TreeStratum()
        assertions = [
            (10.0, True),
            (None, False),
            (-10.0, False),
            (0.0, False),
        ]
        for i in assertions:
            fixture.breast_height_age = i[0]
            self.assertEqual(i[1], fixture.has_breast_height_age())


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
