# -*- coding: utf-8 -*-
import transaction
from datetime import datetime, timedelta, time, date

def handler(obj, event):
    """ Event handler
    """
    # if object.portal_type in  ['Vakt' ]:
    if hasattr(obj, 'start_date'):
        if obj.start_date is not None:
            startdate= obj.start_date
            skift = obj.skift
            if skift == 'alle':
                starttime = time(7, 0)
                endtime = time(15, 0)
            elif skift == 'dag':
                starttime = time(7, 0)
                endtime = time(14, 0) 
            elif skift == 'kveld':
                starttime = time(14, 0)
                endtime = time(22, 0) 
            elif skift == 'natt':
                starttime = time(22, 0)
                endtime = time(8, 0) 
            
            s_date= datetime.combine(startdate, starttime)
            if skift in ['natt', 'alle']:
                startdate = startdate  + timedelta(days=1)
            e_date= datetime.combine(startdate, endtime)
            setattr(obj, 'start', s_date) 
            setattr(obj, 'end', e_date) 
            setattr(obj, 'location', '') 
            
            transaction.commit()