#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import logging
import logging.handlers

logger = logging.getLogger('pcmlogger')
formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
fileMaxByte = 1024 * 1024 * 10 #10MB
fileHandler = logging.handlers.RotatingFileHandler('/usr/local/web2py/logs/pcm_LCD.log', maxBytes=fileMaxByte, backupCount=1)
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)

def LCDlog2file(line1, line2):
    logger.info(line1)
    logger.info(line2)
    logger.info('================')
