#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import logging
import logging.handlers

def LCDlog2file(line1, line2):
    logger = logging.getLogger('pcmlogger')
    formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
    fileHandler = logging.FileHandler('/usr/local/web2py/logs/pcm_LCD.log')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)
    logger.info(line1)
    logger.info(line2)
    logger.info('================')
