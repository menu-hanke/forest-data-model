from typing import Optional


class TreeStratum:
    # VMI data type 2
    # SMK data type TreeStratum
    # No RSD equivalent.

    def __init__(self):
        self.stand: Optional[ForestStand] = None

        # identifier of the stratum within the container stand
        self.identifier: Optional[str] = None

        self.species: Optional[str] = None
        self.origin: Optional[int] = None
        self.stems_per_ha: Optional[float] = None  # stem count within a hectare
        self.mean_diameter: Optional[float] = None  # in decimeters
        self.mean_height: Optional[float] = None  # in meters
        self.breast_height_age: Optional[float] = None  # age in years when reached breast height
        self.biological_age: Optional[float] = None  # age in years
        self.basal_area: Optional[float] = None  # stratum basal area
        self.saw_log_volume_reduction_factor: Optional[float] = None
        self.cutting_year: Optional[int] = None
        self.age_when_10cm_diameter_at_breast_height: Optional[int] = None
        self.tree_number: Optional[int] = None
        # Angle from plot origin, distance (m) to plot origin, height difference (m) with plot origin
        self.stand_origin_relative_position: tuple[float, float, float] = (0.0, 0.0, 0.0)
        self.lowest_living_branch_height: Optional[float] = None
        self.management_category: Optional[int] = None
        self.sapling_stems_per_ha: Optional[float] = None  # sapling stem count within a hectare
        self.sapling_stratum: bool = False  # this reference tree represents saplings

    def __eq__(self, other: 'TreeStratum'):
        return self.identifier == other.identifier

    def has_biological_age(self) -> bool:
        if self.biological_age is None:
            return False
        elif self.biological_age > 0.0:
            return True
        else:
            return False

    def compare_species(self, other: 'TreeStratum') -> bool:
        if self.species is None or other.species is None:
            return False
        elif self.species == other.species:
            return True
        else:
            return False

    def has_height_over_130_cm(self) -> bool:
        if self.mean_height is None:
            return False
        elif self.mean_height > 1.3:
            return True
        else:
            return False

    def has_diameter(self) -> bool:
        if self.mean_diameter is None:
            return False
        elif self.mean_diameter > 0.0:
            return True
        else:
            return False

    def to_sapling_reference_tree(self) -> 'ReferenceTree':
        result = ReferenceTree()
        result.stems_per_ha = self.sapling_stems_per_ha
        result.species = self.species
        result.breast_height_diameter = 0.0
        result.height = self.mean_height
        result.breast_height_age = self.breast_height_age
        result.biological_age = self.biological_age
        result.saw_log_volume_reduction_factor = -1.0
        result.pruning_year = 0.0
        result.age_when_10cm_diameter_at_breast_height = 0.0
        result.origin = self.origin
        result.stand_origin_relative_position = (0.0, 0.0, 0.0)
        result.management_category = 1.0
        result.sapling = True
        return result


class ReferenceTree:
    # VMI data type 3
    # No SMK equivalent
    # Mela RSD logical record for "tree variables"

    def __init__(self):
        self.stand: Optional[ForestStand] = None

        # identifier of the tree within the container stand
        self.identifier: Optional[str] = None

        self.stems_per_ha: Optional[float] = None  # RSD record 1
        self.species: Optional[int] = None  # RSD record 2, 1-8
        self.breast_height_diameter: Optional[float] = None  # RSD record 3, diameter at 1.3 m height
        self.height: Optional[float] = None  # RSD record 4, height in meters
        self.breast_height_age: Optional[float] = None  # RSD record 5, age in years when reached 1.3 m height
        self.biological_age: Optional[float] = None  # RSD record 6, age in years
        self.saw_log_volume_reduction_factor: Optional[float] = None  # RSD record 7, 0.0-1.0
        self.pruning_year: int = 0  # RSD record 8
        # RSD record 9, age when reached 10 cm diameter at 1.3 m height. Hard variable to name...
        self.age_when_10cm_diameter_at_breast_height: int = 0
        self.origin: Optional[int] = None  # RSD record 10, 0-3; natural, seeded, planted, supplementary planted
        self.tree_number: Optional[int] = None  # RSD record 11, default is the order of appearance (or in sample plot)
        # RSD records 12, 13, 14.
        # Angle from plot origin, distance (m) to plot origin, height difference (m) with plot origin
        self.stand_origin_relative_position: tuple[float, float, float] = (0.0, 0.0, 0.0)
        self.lowest_living_branch_height: Optional[float] = None  # RSD record 15, meters
        self.management_category: Optional[int] = None  # RSD record 16
        # RSD record 17 reserved for system

        self.tree_category: Optional[str] = None  # VMI tree_category for living/dead/otherwise unusable tree
        self.sapling: bool = False

    def __eq__(self, other: 'ReferenceTree'):
        return self.identifier == other.identifier

    def validate(self):
        pass

    def has_biological_age(self) -> bool:
        if self.biological_age is None:
            return False
        elif self.biological_age > 0.0:
            return True
        else:
            return False

    def has_diameter(self) -> bool:
        if self.breast_height_diameter is None:
            return False
        elif self.breast_height_diameter > 0.0:
            return True
        else:
            return False

    def has_height_over_130_cm(self) -> bool:
        if self.height is None:
            return False
        elif self.height > 1.3:
            return True
        else:
            return False

    def is_living(self) -> bool:
        return self.tree_category in (None, '0', '1', '3', '7')

    def compare_species(self, other: 'ReferenceTree') -> bool:
        if self.species is None or other.species is None:
            return False
        elif self.species == other.species:
            return True
        else:
            return False

    def as_csv_row(self) -> list[str]:
        result = ["tree", self.identifier]
        result.extend(self.as_rsd_row())
        return result

    def as_rsd_row(self):
        saw_log_volume_reduction_factor = \
            -1 if self.saw_log_volume_reduction_factor is None else self.saw_log_volume_reduction_factor
        return [
            self.stems_per_ha,
            self.species,
            self.breast_height_diameter,
            self.height,
            self.breast_height_age,
            self.biological_age,
            saw_log_volume_reduction_factor,
            self.pruning_year,
            self.age_when_10cm_diameter_at_breast_height,
            self.origin,
            self.tree_number,
            self.stand_origin_relative_position[0],
            self.stand_origin_relative_position[1],
            self.stand_origin_relative_position[2],
            self.lowest_living_branch_height,
            self.management_category,
            None
        ]


class ForestStand:
    # VMI data type 1
    # SMK data type Stand
    # Mela RSD logical record for "sample plot variables"

    def __init__(self):
        self.reference_trees: list[ReferenceTree] = []
        self.tree_strata: list[TreeStratum] = []

        self.identifier: Optional[str] = None  # unique identifier for entity within its domain

        self.management_unit_id: Optional[int] = None  # RSD record 1
        # RSD record 7 (default to management unit id unless overriden)
        self.stand_id: Optional[int] = self.management_unit_id

        self.year: Optional[int] = None  # RSD record 2
        self.area: float = 0.0  # RSD record 3
        self.area_weight: float = self.area  # RSD record 4 (default to area_ha, unless overridden)

        # RSD records 5 (lat), 6 (lon) in ERTS-TM35FIN (EPSG:3067), 8 (height)
        # lat, lon, height above sea level (m), CRS
        self.geo_location: Optional[tuple[float, float, float, str]] = None

        self.degree_days: Optional[float] = None  # RSD record 9
        self.owner_category: Optional[int] = None  # RSD record 10, 0-4
        self.land_use_category: Optional[int] = None  # RSD record 11, 1-9
        self.soil_peatland_category: Optional[int] = None  # RSD record 12, 1-5
        self.site_type_category: Optional[int] = None  # RSD record 13, 1-8
        self.tax_class_reduction: Optional[int] = None  # RSD record 14, 0-4
        self.tax_class: Optional[int] = None  # RSD record 15, 1-7
        self.drainage_category: Optional[int] = None  # RSD record 16, 0-5
        self.drainage_feasibility: Optional[bool] = None  # RSD record 17, (0 yes, 1 no)
        # RSD record 18 is unspecified and defaults to '0'
        self.drainage_year: Optional[int] = None  # RSD record 19
        self.fertilization_year: Optional[int] = None  # RSD record 20
        self.soil_surface_preparation_year: Optional[int] = None  # RSD record 21
        self.natural_regeneration_feasibility: Optional[bool] = None  # RSD record 22 (0 yes, 1 no)
        self.regeneration_area_cleaning_year: Optional[int] = None  # RSD record 23
        self.development_class: Optional[int] = None  # RSD record 24
        self.artificial_regeneration_year: Optional[int] = None  # RSD record 25
        self.young_stand_tending_year: Optional[int] = None  # RSD record 26
        self.pruning_year: Optional[int] = None  # RSD record 27
        self.cutting_year: Optional[int] = None  # RSD record 28
        self.forestry_centre_id: Optional[int] = None  # RSD record 29, 0-13
        self.forest_management_category: Optional[int] = None  # RSD record 30, 1-3,6-7
        self.method_of_last_cutting: Optional[int] = None  # RSD record 31, 0-6
        self.municipality_id: Optional[int] = None  # RSD record 32, code from Statistics Finland
        # RSD record 33 and 34 unused

        # stand specific factors for scaling estimated ReferenceTree count per hectare
        self.stems_per_ha_scaling_factors: tuple[float, float] = (1.0, 1.0)

        self.fra_category: Optional[str] = None  # VMI fra category
        self.land_use_category_detail: Optional[str] = None  # VMI land use category detail
        self.auxiliary_stand: bool = False  # VMI stand number > 1 (meaning sivukoeala, auxiliary stand)

    def __eq__(self, other: 'ForestStand'):
        return self.identifier == other.identifier

    def set_identifiers(self, stand_id: int, management_unit_id: Optional[int] = None):
        self.stand_id = stand_id
        self.management_unit_id = stand_id if management_unit_id is None else management_unit_id

    def set_area(self, area_ha: float, area_weight: Optional[float] = None):
        self.area = area_ha
        self.area_weight = area_ha if area_weight is None else area_weight

    def set_geo_location(self, lat: float, lon: float, height: float, system: str = "ERTS-TM35FIN"):
        if not lat or not lon:
            raise ValueError("Invalid source values for geo location")
        self.geo_location = (lat, lon, height, system)

    def validate(self):
        pass

    def add_tree(self, tree: ReferenceTree):
        self.reference_trees.append(tree)

    def is_auxiliary(self):
        return self.auxiliary_stand

    def is_forest_land(self):
        return self.land_use_category in (1, 2, 3, 4)

    def is_other_excluded_forest(self):
        return (
                self.land_use_category == 4 and
                self.fra_category == '3' and
                self.land_use_category_detail in ('1', '2', '6', '7')
        )

    def has_trees(self):
        return len(self.reference_trees) > 0

    def has_strata(self):
        return len(self.tree_strata) > 0

    def as_csv_row(self) -> list[str]:
        result = ["stand", self.identifier]
        result.extend(self.as_rsd_row())
        return result

    def as_rsd_row(self):
        forestry_centre_id = -1 if self.forestry_centre_id is None else self.forestry_centre_id
        return [
            self.management_unit_id,
            self.year,
            self.area,
            self.area_weight,
            self.geo_location[0],
            self.geo_location[1],
            self.stand_id,
            self.geo_location[2],
            self.degree_days,
            self.owner_category,
            self.land_use_category,
            self.soil_peatland_category,
            self.site_type_category,
            self.tax_class_reduction,
            self.tax_class,
            self.drainage_category,
            self.drainage_feasibility,
            None,
            self.drainage_year,
            self.fertilization_year,
            self.soil_surface_preparation_year,
            self.natural_regeneration_feasibility,
            self.regeneration_area_cleaning_year,
            self.development_class,
            self.artificial_regeneration_year,
            self.young_stand_tending_year,
            self.pruning_year,
            self.cutting_year,
            forestry_centre_id,
            self.forest_management_category,
            self.method_of_last_cutting,
            self.municipality_id,
            None,
            None
        ]
