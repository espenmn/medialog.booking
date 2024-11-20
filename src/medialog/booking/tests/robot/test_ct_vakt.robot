# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s medialog.booking -t test_vakt.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src medialog.booking.testing.MEDIALOG_BOOKING_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/medialog/booking/tests/robot/test_vakt.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Vakt
  Given a logged-in site administrator
    and an add Vakt form
   When I type 'My Vakt' into the title field
    and I submit the form
   Then a Vakt with the title 'My Vakt' has been created

Scenario: As a site administrator I can view a Vakt
  Given a logged-in site administrator
    and a Vakt 'My Vakt'
   When I go to the Vakt view
   Then I can see the Vakt title 'My Vakt'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Vakt form
  Go To  ${PLONE_URL}/++add++Vakt

a Vakt 'My Vakt'
  Create content  type=Vakt  id=my-vakt  title=My Vakt

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Vakt view
  Go To  ${PLONE_URL}/my-vakt
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Vakt with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Vakt title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
