"""
    Routing API v8

    A location service providing customizable route calculations for a variety of vehicle types as well as pedestrian modes.  # noqa: E501

    The version of the OpenAPI document: 8.22.2
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import routing
from routing.model.access_point_place import AccessPointPlace
from routing.model.charging_connector_attributes import ChargingConnectorAttributes
from routing.model.charging_station_brand import ChargingStationBrand
from routing.model.charging_station_place import ChargingStationPlace
from routing.model.parking_lot_place import ParkingLotPlace
from routing.model.place import Place
from routing.model.station_place import StationPlace
from routing.model.time_restricted_price import TimeRestrictedPrice
globals()['AccessPointPlace'] = AccessPointPlace
globals()['ChargingConnectorAttributes'] = ChargingConnectorAttributes
globals()['ChargingStationBrand'] = ChargingStationBrand
globals()['ChargingStationPlace'] = ChargingStationPlace
globals()['ParkingLotPlace'] = ParkingLotPlace
globals()['Place'] = Place
globals()['StationPlace'] = StationPlace
globals()['TimeRestrictedPrice'] = TimeRestrictedPrice
from routing.model.vehicle_place import VehiclePlace


class TestVehiclePlace(unittest.TestCase):
    """VehiclePlace unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVehiclePlace(self):
        """Test VehiclePlace"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VehiclePlace()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
