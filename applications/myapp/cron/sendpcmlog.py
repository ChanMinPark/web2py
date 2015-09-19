#import requests
import sys
from tablebar_send_email import *

import logging
import logging.handlers

logger = logging.getLogger('pcmlogger')
formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
fileMaxByte = 1024 * 1024 * 10 #10MB
fileHandler = logging.handlers.RotatingFileHandler('/usr/local/web2py/logs/pcm_email_test.log', maxBytes=fileMaxByte, backupCount=1)
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

def print_tail():
    #cmd = "tail -n 10 /usr/local/web2py/logs/pcm_LCD.log"
    #printTail = run_cmd(cmd)
    f = open('/usr/local/web2py/logs/pcm_LCD.log', 'r')
    lines = f.readlines()
    logger.info(lines)
    pstr = lines[-1]#+"\n"+lines[-9]+"\n"+lines[-8]+"\n"+lines[-7]+"\n"+lines[-6]+"\n"+lines[-5]+"\n"+lines[-4]+"\n"+lines[-3]+"\n"+lines[-2]+"\n"+lines[-1]
    logger.info(pstr)
    return pstr

def main():
    """
    requests.post(
        "https://api.mailgun.net/v3/sandbox54f98034843b4141b17c7334201d0628.mailgun.org/messages",
        auth=("api", "key-e5a9135df9910d5b8c14dad503d8c5e6"),
        data={"from": "Excited User <mailgun@sandbox54f98034843b4141b17c7334201d0628.mailgun.org>",
              "to": ["walkinpcm@gmail.com"],
              "subject": "TableBar Log",
              "text": print_tail()})
    """
    logger.info(print_tail())
    send_email(print_tail())
    return "Send E-mail : Okay"


if __name__ == '__main__':
    main()
