# -*- coding: utf-8 -*-

# from medialog.booking import _
from Products.Five.browser import BrowserView
from zope.interface import Interface
from plone import api

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IVaktView(Interface):
    """ Marker Interface for IVaktView"""


class VaktView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('vakt_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
    
    def get_user(self):
        return self.context.Creator()
        # current_user = api.user.get_current()
        # return current_user.getProperty('fullname')
        
        #return None
        
