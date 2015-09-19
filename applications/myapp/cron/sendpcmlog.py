#import requests
import sys
from tablebar_send_email import *

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = p.communicate()[0]
    return output

def print_tail():
    cmd = "tail -n 10 /usr/local/web2py/logs/pcm_LCD.log"
    printTail = run_cmd(cmd)
    return printTail

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
    send_email(print_tail())
    return "Send E-mail : Okay"


if __name__ == '__main__':
    main()
