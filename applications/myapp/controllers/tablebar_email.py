# -*- coding: utf-8 -*-
# try something like
#def index(): return dict(message="hello from tablebar_email.py")
import requests
from tablebar_send_email import *

def send_email_with_Attach():
    """
    requests.post(
        "https://api.mailgun.net/v3/sandbox54f98034843b4141b17c7334201d0628.mailgun.org/messages",
        auth=("api", "key-e5a9135df9910d5b8c14dad503d8c5e6"),
        files={
                  "attachment[0]": ("pcm_LCD.log", open('/usr/local/web2py/logs/pcm_LCD.log', 'rb'))
              },
        data={"from": "Excited User <mailgun@sandbox54f98034843b4141b17c7334201d0628.mailgun.org>",
              "to": ["walkinpcm@gmail.com"],
              "subject": "TableBar Log with Attachment",
              "text": "log file"})
    """
    send_email_with_Attachment()
    return "Send E-mail : Okay with Attachment"
