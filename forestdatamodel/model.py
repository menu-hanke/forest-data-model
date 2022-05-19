import dataclasses
from typing import Optional
from dataclasses import dataclass
from forestdatamodel.enums.internal import TreeSpecies
from forestdatamodel.util import property_matches_condition, gt, eq, value_exists


@dataclass
class TreeStratum:
    # VMI data type 2
    # SMK data type TreeStratum
    # No RSD equivalent.

    stand: Optional['ForestStand'] = None

    # identifier of the stratum within the container stand
    identifier: Optional[str] = None

    species: Optional[TreeSpecies] = None
    origin: Optional[int] = None
    stems_per_ha: Optional[float] = None  # stem count within a hectare
    mean_diameter: Optional[float] = None  # in decimeters
    mean_height: Optional[float] = None  # in meters
    # age in years when reached breast height
    breast_height_age: Optional[float] = None
    biological_age: Optional[float] = None  # age in years
    basal_area: Optional[float] = None  # stratum basal area
    saw_log_volume_reduction_factor: Optional[float] = None
    cutting_year: Optional[int] = None
    age_when_10cm_diameter_at_breast_height: Optional[int] = None
    tree_number: Optional[int] = None
    # Angle from plot origin, distance (m) to plot origin, height difference (m) with plot origin
    stand_origin_relative_position: tuple[float, float, float] = (
        0.0, 0.0, 0.0)
    lowest_living_branch_height: Optional[float] = None
    management_category: Optional[int] = None
    # sapling stem count within a hectare
    sapling_stems_per_ha: Optional[float] = None
    sapling_stratum: bool = False  # this reference tree represents saplings

    def __eq__(self, other: 'TreeStratum'):
        return self.identifier == other.identifier

    def has_height(self):
        """DEPRECATED; use forestdatamodel.util.property_matches_condition directly instead"""
        return property_matches_condition(self.mean_height, lambda x: gt(x, 0.0))

    def has_sapling_stems_per_ha(self) -> bool:
        """DEPRECATED; use forestdatamodel.util.property_matches_condition directly instead"""
        return property_matches_condition(self.sapling_stems_per_ha, lambda x: gt(x, 0.0))

    def has_stems_per_ha(self) -> bool:
        """DEPRECATED; use forestdatamodel.util.property_matches_condition directly instead"""
        return property_matches_condition(self.stems_per_ha, lambda x: gt(x, 0.0))

    def has_diameter(self) -> bool:
        """DEPRECATED; use forestdatamodel.util.property_matches_condition directly instead"""
        return property_matches_condition(self.mean_diameter, lambda x: gt(x, 0.0))

    def has_breast_height_age(self) -> bool:
        """DEPRECATED; use forestdatamodel.util.property_matches_condition directly instead"""
        return property_matches_condition(self.breast_height_age, lambda x: gt(x, 0.0))

    def has_biological_age(self) -> bool:
        """DEPRECATED; use forestdatamodel.util.property_matches_condition directly instead"""
        return property_matches_condition(self.biological_age, lambda x: gt(x, 0.0))

    def has_basal_area(self) -> bool:
        """DEPRECATED; use forestdatamodel.util.property_matches_condition directly instead"""
        return property_matches_condition(self.basal_area, lambda x: gt(x, 0.0))

    def has_height_over_130_cm(self) -> bool:
        """DEPRECATED; use forestdatamodel.util.property_matches_condition directly instead"""
        return property_matches_condition(self.mean_height, lambda x: gt(x, 1.3))

    def compare_species(self, other: 'TreeStratum') -> bool:
        if not value_exists(self.species) or not value_exists(other.species):
            return False
        elif self.species == other.species:
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

    def get_breast_height_age(self, subtrahend: float = 12.0) -> float:
        if self.has_breast_height_age():
            return self.breast_height_age
        elif self.has_biological_age():
            new_breast_height_age = self.biological_age - subtrahend
            return 0.0 if new_breast_height_age <= 0.0 else new_breast_height_age
        else:
            return 0.0


@dataclass
class ReferenceTree:
    # VMI data type 3
    # No SMK equivalent
    # Mela RSD logical record for "tree variables"

    stand: Optional['ForestStand'] = None

    # identifier of the tree within the container stand
    identifier: Optional[str] = None

    stems_per_ha: Optional[float] = None  # RSD record 1
    species: Optional[TreeSpecies] = None  # RSD record 2, 1-8
    # RSD record 3, diameter at 1.3 m height
    breast_height_diameter: Optional[float] = None
    height: Optional[float] = None  # RSD record 4, height in meters
    # RSD record 5, age in years when reached 1.3 m height
    breast_height_age: Optional[float] = None
    biological_age: Optional[float] = None  # RSD record 6, age in years
    # RSD record 7, 0.0-1.0
    saw_log_volume_reduction_factor: Optional[float] = None
    pruning_year: int = 0  # RSD record 8
    # RSD record 9, age when reached 10 cm diameter at 1.3 m height. Hard variable to name...
    age_when_10cm_diameter_at_breast_height: int = 0
    # RSD record 10, 0-3; natural, seeded, planted, supplementary planted
    origin: Optional[int] = None
    # RSD record 11, default is the order of appearance (or in sample plot)
    tree_number: Optional[int] = None
    # RSD records 12, 13, 14.
    # Angle from plot origin, distance (m) to plot origin, height difference (m) with plot origin
    stand_origin_relative_position: tuple[float, float, float] = (
        0.0, 0.0, 0.0)
    # RSD record 15, meters
    lowest_living_branch_height: Optional[float] = None
    management_category: Optional[int] = None  # RSD record 16
    # RSD record 17 reserved for system

    # VMI tree_category for living/dead/otherwise unusable tree
    tree_category: Optional[str] = None
    sapling: bool = False

    def __eq__(self, other: 'ReferenceTree'):
        return self.identifier == other.identifier

    def validate(self):
        pass

    def has_biological_age(self) -> bool:
        """DEPRECATED; use forestdatamodel.util.property_matches_condition directly instead"""
        return property_matches_condition(self.biological_age, lambda x: gt(x, 0.0))

    def has_diameter(self) -> bool:
        """DEPRECATED; use forestdatamodel.util.property_matches_condition directly instead"""
        return property_matches_condition(self.breast_height_diameter, lambda x: gt(x, 0.0))

    def has_height_over_130_cm(self) -> bool:
        """DEPRECATED; use forestdatamodel.util.property_matches_condition directly instead"""
        return property_matches_condition(self.height, lambda x: gt(x, 1.3))

    def is_living(self) -> bool:
        return self.tree_category in (None, '0', '1', '3', '7')

    def compare_species(self, other: 'ReferenceTree') -> bool:
        if not value_exists(self.species) or not value_exists(other.species):
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


@dataclass
class ForestStand:
    # VMI data type 1
    # SMK data type Stand
    # Mela RSD logical record for "sample plot variables"

    reference_trees: list[ReferenceTree] = dataclasses.field(
        default_factory=list)
    tree_strata: list[TreeStratum] = dataclasses.field(default_factory=list)

    # unique identifier for entity within its domain
    identifier: Optional[str] = None

    management_unit_id: Optional[int] = None  # RSD record 1
    # RSD record 7 (default to management unit id unless overriden)
    stand_id: Optional[int] = management_unit_id

    year: Optional[int] = None  # RSD record 2
    area: float = 0.0  # RSD record 3
    # RSD record 4 (default to area_ha, unless overridden)
    area_weight: float = area

    # RSD records 5 (lat), 6 (lon) in ERTS-TM35FIN (EPSG:3067), 8 (height)
    # lat, lon, height above sea level (m), CRS
    geo_location: Optional[tuple[float, float, float, str]] = None

    degree_days: Optional[float] = None  # RSD record 9
    owner_category: Optional[int] = None  # RSD record 10, 0-4
    land_use_category: Optional[int] = None  # RSD record 11, 1-9
    soil_peatland_category: Optional[int] = None  # RSD record 12, 1-5
    site_type_category: Optional[int] = None  # RSD record 13, 1-8
    tax_class_reduction: Optional[int] = None  # RSD record 14, 0-4
    tax_class: Optional[int] = None  # RSD record 15, 1-7
    drainage_category: Optional[int] = None  # RSD record 16, 0-5
    drainage_feasibility: Optional[bool] = None  # RSD record 17, (0 yes, 1 no)
    # RSD record 18 is unspecified and defaults to '0'
    drainage_year: Optional[int] = None  # RSD record 19
    fertilization_year: Optional[int] = None  # RSD record 20
    soil_surface_preparation_year: Optional[int] = None  # RSD record 21
    # RSD record 22 (0 yes, 1 no)
    natural_regeneration_feasibility: Optional[bool] = None
    regeneration_area_cleaning_year: Optional[int] = None  # RSD record 23
    development_class: Optional[int] = None  # RSD record 24
    artificial_regeneration_year: Optional[int] = None  # RSD record 25
    young_stand_tending_year: Optional[int] = None  # RSD record 26
    pruning_year: Optional[int] = None  # RSD record 27
    cutting_year: Optional[int] = None  # RSD record 28
    forestry_centre_id: Optional[int] = None  # RSD record 29, 0-13
    forest_management_category: Optional[int] = None  # RSD record 30, 1-3,6-7
    method_of_last_cutting: Optional[int] = None  # RSD record 31, 0-6
    # RSD record 32, code from Statistics Finland
    municipality_id: Optional[int] = None
    # RSD record 33 and 34 unused

    # stand specific factors for scaling estimated ReferenceTree count per hectare
    stems_per_ha_scaling_factors: tuple[float, float] = (1.0, 1.0)

    fra_category: Optional[str] = None  # VMI fra category
    # VMI land use category detail
    land_use_category_detail: Optional[str] = None
    # VMI stand number > 1 (meaning sivukoeala, auxiliary stand)
    auxiliary_stand: bool = False

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
        forestry_centre_id = -1 if not value_exists(self.forestry_centre_id) else self.forestry_centre_id
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
