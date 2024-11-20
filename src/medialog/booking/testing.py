# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE
    PloneSandboxLayer,
)
from plone.testing import z2

import medialog.booking


class MedialogBookingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=medialog.booking)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.booking:default')


MEDIALOG_BOOKING_FIXTURE = MedialogBookingLayer()


MEDIALOG_BOOKING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_BOOKING_FIXTURE,),
    name='MedialogBookingLayer:IntegrationTesting',
)


MEDIALOG_BOOKING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_BOOKING_FIXTURE,),
    name='MedialogBookingLayer:FunctionalTesting',
)


MEDIALOG_BOOKING_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_BOOKING_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MedialogBookingLayer:AcceptanceTesting',
)
