# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import implementer


class IVakt(model.Schema):
    """ Marker interface for Vakt
    """


@implementer(IVakt)
class Vakt(Item):
    """ Content-type class for INotification
    """