# -*- coding: utf-8 -*-

from plone.api.portal import getRequest
from medialog.booking import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import Interface
from plone.autoform import directives
from datetime import datetime, timedelta
from plone.app.event.dx.behaviors import IEventBasic
from zope.interface import provider
from zope.interface import invariant
from zope.interface import Invalid
from plone.app.event.base import localized_now 
from zope.component import adapter
from zope.interface import Interface 
from zope.schema.interfaces import IContextAwareDefaultFactory


#
# Note: Somewhere from Plone 5 to 6 the date passed from fullcalender 'disappared'
# So 'Event' does not work, this is a 'hack around it'
# Maybe it should be fixed in patternslib or similar ??

@provider(IContextAwareDefaultFactory)
def day_clicked(context=None):
    """Default factory for the start_date field."""
    request = getRequest()
    date_str = request.get('date', None)  # Get 'date' parameter from request
    if date_str:
        try:
            # Convert the date string to a datetime object
            parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            return parsed_date
        except ValueError:
            # Handle invalid date format
            pass
    return None  # Fallback if 'date' is not in the request or invalid


class StartBeforeNow(Invalid):
    __doc__ = _("error_invalid_date",
                default=u"Invalid dato")

class IBookingBehaviorMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IBookingBehavior( IEventBasic):
    """Event Contact Schema."""
    
    # icalendar event uid
    sync_uid = schema.TextLine(required=False)
    directives.mode(sync_uid='hidden')
    
    directives.omitted('start','end','whole_day', 'open_end')
    
    
    start_date = schema.Date(
        title=_(
            u'label_vakt',
            default=u'Tilgjengelig dato'
        ),
        description=_(
            u'help_event_start',
            default=u'Date ledig for skift.'
        ),
        required=True,
        defaultFactory= day_clicked
    )
    
    skift = schema.Choice(
        title=_("Skift"),
        description=_("Velg skift"),
        values=("alle", "dag", "kveld", "natt"),
        required=True,
        default="dag",
    )
    

    
    
    @invariant
    def validate_start_end(data):
        import pdb; pdb.set_trace()
        if data.start_date < localized_now().date() :
            raise StartBeforeNow(
                _("error_end_must_be_after_start_date",
                  default=u"Datoen må være etter i dag.")
            )
        
        
@adapter(IBookingBehaviorMarker)
class BookingBehavior(object):
    def __init__(self, context):
        self.context = context
        
 

  