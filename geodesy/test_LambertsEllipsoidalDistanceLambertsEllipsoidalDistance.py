# geodesy/lamberts_ellipsoidal_distance.py
from math import atan, cos, radians, sin, tan, sqrt, asin

# Constants for WGS84
AXIS_A = 6378137.0  # Equatorial radius in meters
AXIS_B = 6356752.314245  # Polar radius in meters
EQUATORIAL_RADIUS = AXIS_A

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate great circle distance between two points in a sphere,
    given longitudes and latitudes using the Haversine formula.
    """
    # CONSTANTS per WGS84
    RADIUS = 6371000  # Average radius of Earth in meters

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    return RADIUS * c

def lamberts_ellipsoidal_distance(
    lat1: float, lon1: float, lat2: float, lon2: float
) -> float:
    """
    Calculate the shortest distance along the surface of an ellipsoid between
    two points on the surface of earth given longitudes and latitudes.
    """
    flattening = (AXIS_A - AXIS_B) / AXIS_A
    b_lat1 = atan((1 - flattening) * tan(radians(lat1)))
    b_lat2 = atan((1 - flattening) * tan(radians(lat2)))

    sigma = haversine_distance(lat1, lon1, lat2, lon2) / EQUATORIAL_RADIUS

    p_value = (b_lat1 + b_lat2) / 2
    q_value = (b_lat2 - b_lat1) / 2

    x_numerator = (sin(p_value) ** 2) * (cos(q_value) ** 2)
    x_demonimator = cos(sigma / 2) ** 2
    x_value = (sigma - sin(sigma)) * (x_numerator / x_demonimator)

    y_numerator = (cos(p_value) ** 2) * (sin(q_value) ** 2)
    y_denominator = sin(sigma / 2) ** 2
    y_value = (sigma + sin(sigma)) * (y_numerator / y_denominator)

    return EQUATORIAL_RADIUS * (sigma - ((flattening / 2) * (x_value + y_value)))

# geodesy/test_LambertsEllipsoidalDistanceLambertsEllipsoidalDistance.py
import pytest
from lamberts_ellipsoidal_distance import lamberts_ellipsoidal_distance

class Test_LambertsEllipsoidalDistance:

    @pytest.mark.positive
    def test_distance_nearby_points(self):
        SAN_FRANCISCO = (37.774856, -122.424227)
        YOSEMITE = (37.864742, -119.537521)
        distance = lamberts_ellipsoidal_distance(*SAN_FRANCISCO, *YOSEMITE)
        assert pytest.approx(distance, rel=1e-3) == 254351

    @pytest.mark.positive
    def test_distance_distant_points(self):
        SAN_FRANCISCO = (37.774856, -122.424227)
        NEW_YORK = (40.713019, -74.012647)
        distance = lamberts_ellipsoidal_distance(*SAN_FRANCISCO, *NEW_YORK)
        assert pytest.approx(distance, rel=1e-3) == 4138992

    @pytest.mark.positive
    def test_distance_across_continents(self):
        SAN_FRANCISCO = (37.774856, -122.424227)
        VENICE = (45.443012, 12.313071)
        distance = lamberts_ellipsoidal_distance(*SAN_FRANCISCO, *VENICE)
        assert pytest.approx(distance, rel=1e-3) == 9737326

    @pytest.mark.positive
    def test_distance_identical_points(self):
        SAN_FRANCISCO = (37.774856, -122.424227)
        distance = lamberts_ellipsoidal_distance(*SAN_FRANCISCO, *SAN_FRANCISCO)
        assert distance == 0

    @pytest.mark.positive
    def test_distance_across_equator(self):
        POINT_NORTH = (1.0, 30.0)
        POINT_SOUTH = (-1.0, 30.0)
        distance = lamberts_ellipsoidal_distance(*POINT_NORTH, *POINT_SOUTH)
        expected_distance = 222389
        assert pytest.approx(distance, rel=1e-3) == expected_distance
