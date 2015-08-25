#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import urllib2
import logging
import logging.handlers

logger = logging.getLogger('mylogger')
fileHandler = logging.FileHandler('/usr/local/web2py/logs/pcmtest.log')
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)

def setTask(wtask):
    page = urllib2.urlopen("https://169.254.1.89:8000/myapp/tablebar_globals/setTask/%s"%wtask)
    logger.info("https://169.254.1.89:8000/myapp/tablebar_globals/setTask/%s"%wtask)
    text = page.read()
    logger.info(text)
    
def getTask():
    page = urllib2.urlopen("https://169.254.1.89:8000/myapp/tablebar_globals/getTask")
    g_wtask = getTaskpage.read()
    logger.info(g_wtask)
    return g_wtask

def setLock(lock):
    page = urllib2.urlopen("https://169.254.1.89:8000/myapp/tablebar_globals/setLock/%s"%lock)
    logger.info("https://169.254.1.89:8000/myapp/tablebar_globals/setLock/%s"%lock)
    text = page.read()
    logger.info(text)
    
def getLock():
    page = urllib2.urlopen("https://169.254.1.89:8000/myapp/tablebar_globals/getLock")
    g_lock = getLockpage.read()
    logger.info(g_lock)
    return g_lock
