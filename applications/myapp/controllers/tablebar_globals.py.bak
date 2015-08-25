#!/usr/bin/env python
# -*- coding: utf-8 -*-
# try something like

from gluon import *

global g_wtask
global g_lock
g_wtask = "0"
g_lock = "False"

def setTask():
    global g_wtask
    g_wtask = request.args(0)
    return "setTask ok : %s"%g_wtask
    
def getTask():
    global g_wtask
    return g_wtask

def setLock():
    global g_lock
    g_lock = request.args(0)
    return "setLock ok : %s"%g_lock
    
def getLock():
    global g_lock
    return g_lock
