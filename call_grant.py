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
TOKEN = "9fbd376409e58c7e3d14f54feb99ef7c"
GRANT_NUMBER = "+15712719166"
REQUESTS_INSTRUCTIONS = [
    "https://technopig.github.io/phone_prank_grant/req1.xml",
    "https://technopig.github.io/phone_prank_grant/req2.xml",
    "https://technopig.github.io/phone_prank_grant/req3.xml"
]

client = TwilioRestClient(ACCOUNT_SID, TOKEN)


def dial_grant(d_request):
    client.calls.create(
        to=GRANT_NUMBER,
        from_=random.choice(TWILIO_PHONE_NUMBERS),
        url=d_request,
        method="GET"
    )

def text_grant(maint_req):
    client.messages.create(
        body=maint_req,
        from_=random.choice(TWILIO_PHONE_NUMBERS),
        to=GRANT_NUMBER
    )

if __name__ == "__main__":
    # text_n(DIAL_NUMBERS)
    time.sleep(900)
    lines = []
    with open('maintenance_requests.txt') as infile:
        for line in infile:
            line = line.strip()
            lines.append(line)

    c = 0
    dial_lines = REQUESTS_INSTRUCTIONS
    while len(lines) > 0:
        c += 1
        req = random.choice(lines)
        lines.remove(req)
        text_grant(req)
        time.sleep(10)
        if c == 6:
            if len(dial_lines > 0):
                c = 0
                d_req = random.choice(dial_lines)
                dial_lines.remove(d_req)
                dial_grant(d_req)
