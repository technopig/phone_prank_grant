from twilio.rest import *
import random
import time

TWILIO_PHONE_NUMBERS = [
    "+18166084946",         #1 - 46
    "+18544448535",         #2 - 35
    "+18506045775",         #3 - 75
    "+14105670723",         #4 - 23
    "+12798889422",         #5 - 22
    "+14582171818",         #6 - 18
    "+13133073641",         #7 - 41
    ]
ACCOUNT_SID = "AC81bd7a9bcb33865e4b4fd0241dfcf7b8"
TOKEN = "5635202829c71b76c26b24583779d45e"
GRANT_NUMBER = "+15712719166"
TWIML_INSTRUCTIONS_URL = \
    "http://static.fullstackpython.com/phone-calls-python.xml"

client = TwilioRestClient(ACCOUNT_SID, TOKEN)


def dial_grant():
    client.calls.create(
        to=GRANT_NUMBER,
        from_=random.choice(TWILIO_PHONE_NUMBERS),
        url=TWIML_INSTRUCTIONS_URL,
        method="GET"
    )

def text_grant(maint_reqs):
    client.messages.create(
        body=random.choice(maint_reqs),
        from_=random.choice(TWILIO_PHONE_NUMBERS),
        to=GRANT_NUMBER
    )

if __name__ == "__main__":
    # text_numbers(DIAL_NUMBERS)
    lines = []
    with open('maintenance_requests.txt') as infile:
        for line in infile:
            line = line.strip()
            lines.append(line)
    print(random.choice(lines))
    for i in range(10):
        text_grant(lines)
        time.sleep(5)
