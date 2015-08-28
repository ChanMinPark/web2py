import request

def main():
    requests.post("https://api.mailgun.net/v3/sandbox54f98034843b4141b17c7334201d0628.mailgun.org/messages",
              auth=("api", "key-e5a9135df9910d5b8c14dad503d8c5e6"),
              files={
                  "attachment[0]": ("/usr/local/web2py/logs/pcm_LCD.log", open(FILE_PATH_1, 'rb'))
              },
              data={"from": "ChanMinPark <walkinpcm@gmail.com>",
                    "to": ["walkinpcm@gmail.com"],
                    "subject": "pcmWall LCD log",
                    "text": "pcmWall LCD log"
              })


if __name__ == '__main__':
    main()
