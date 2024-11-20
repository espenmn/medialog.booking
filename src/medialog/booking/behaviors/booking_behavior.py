# -*- coding: utf-8 -*-

from medialog.booking import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
# from plone.supermodel import model
# from Products.CMFPlone.utils import safe_hasattr
# from zope.component import adapter
from zope.interface import Interface
# from zope.interface import implementer
# from zope.interface import provider

# from plone.app.event.dx.behaviors import IEventLocation
from plone.autoform import directives
from datetime import timedelta

# from plone.app.event.dx.behaviors import IEventLocation, IEventAttendees, IEventContact
from plone.app.event.dx.behaviors import IEventBasic
# from plone.app.z3cform.widget import AjaxSelectFieldWidget
# from plone.app.z3cform.widget import AjaxSelectWidget
# from zope import schema
from zope.interface import provider
from zope.interface import invariant
from zope.interface import Invalid
from plone.app.event.base import localized_now
# from Products.CMFPlone.utils import safe_hasattr
# from zope.component import adapter
# from zope.interface import Interface
# from zope.interface import implementer

class StartBeforeNow(Invalid):
    __doc__ = _("error_invalid_date",
                default=u"Invalid dato")


class IBookingBehaviorMarker(Interface):
    pass


# @provider(IFormFieldProvider)
# class IBookingBehavior(model.Schema):
#     """
#     """

#     # location = schema.Choice(
#     #     title="Meeting Location",
#     #     description="Location of the meeting",
#     #     required=True,
#     #     vocabulary= 'XXXX'
#     # )
#     # directives.widget("location", AjaxSelectFieldWidget, klass="event_location")


@provider(IFormFieldProvider)
class IBookingBehavior( IEventBasic):
    """Event Contact Schema."""
    
    # directives.omitted('contact_email')
    # directives.omitted('contact_phone') 
    # directives.omitted('contact_name') 
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
        # defaultFactory=default_start
    )
    
    skift = schema.Choice(
        title=_("Skift"),
        description=_("Velg skift"),
        values=("alle", "dag", "kveld", "natt"),
        required=True,
        default="dag",
    )
    
    # icalendar event uid
    sync_uid = schema.TextLine(required=False)
    directives.mode(sync_uid='hidden')
    
    
    @invariant
    def validate_start_end(data):
        if data.start_date < localized_now().date() :
            raise StartBeforeNow(
                _("error_end_must_be_after_start_date",
                  default=u"Datoen må være etter i dag.")
            )
        
        
        