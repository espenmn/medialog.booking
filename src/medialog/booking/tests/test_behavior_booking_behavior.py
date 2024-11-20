# -*- coding: utf-8 -*-
from medialog.booking.behaviors.booking_behavior import IBookingBehaviorMarker
from medialog.booking.testing import MEDIALOG_BOOKING_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class BookingBehaviorIntegrationTest(unittest.TestCase):

    layer = MEDIALOG_BOOKING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_booking_behavior(self):
        behavior = getUtility(IBehavior, 'medialog.booking.booking_behavior')
        self.assertEqual(
            behavior.marker,
            IBookingBehaviorMarker,
        )
