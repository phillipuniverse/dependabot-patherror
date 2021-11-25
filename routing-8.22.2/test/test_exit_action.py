"""
    Routing API v8

    A location service providing customizable route calculations for a variety of vehicle types as well as pedestrian modes.  # noqa: E501

    The version of the OpenAPI document: 8.22.2
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import routing
from routing.model.localized_string import LocalizedString
from routing.model.turn_action_direction import TurnActionDirection
from routing.model.turn_action_severity import TurnActionSeverity
globals()['LocalizedString'] = LocalizedString
globals()['TurnActionDirection'] = TurnActionDirection
globals()['TurnActionSeverity'] = TurnActionSeverity
from routing.model.exit_action import ExitAction


class TestExitAction(unittest.TestCase):
    """ExitAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExitAction(self):
        """Test ExitAction"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ExitAction()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
