#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
from gluon import current
import logging
import logging.handlers

#logger = logging.getLogger('mylogger')
#fileHandler = logging.FileHandler('/usr/local/web2py/logs/pcmtest.log')
#logger.addHandler(fileHandler)
#logger.setLevel(logging.DEBUG)
def init_variables():
    db = current.db
    
    if db(db.tablebar_globals.variable_name == 'wtask').isempty() :
        db.tablebar_globals.insert(variable_name='wtask', variable_value='0')
    else:
        db(db.tablebar_globals.variable_name == 'wtask').update(variable_value='0')
    
    if db(db.tablebar_globals.variable_name == 'lock').isempty() :
        db.tablebar_globals.insert(variable_name='lock', variable_value='False')
    else:
        db(db.tablebar_globals.variable_name == 'lock').update(variable_value='False')

def setTask(wtask):
    db = current.db
    db(db.tablebar_globals.variable_name == 'wtask').update(variable_value=wtask)
    
def getTask():
    db = current.db
    g_wtask = db(db.tablebar_globals.variable_name == 'wtask').select().first().variable_value
    return g_wtask

def setLock(lock):
    db = current.db
    db(db.tablebar_globals.variable_name == 'lock').update(variable_value=lock)
    
def getLock():
    db = current.db
    g_lock = db(db.tablebar_globals.variable_name == 'lock').select().first().variable_value
    return g_lock
