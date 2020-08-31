from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import random
import time



app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    replies = []
    with open("replies.txt") as rfile:
        for line in rfile:
            line = line.strip()
            replies.append(line)

    resp.message(random.choice(replies))
    time.sleep(10)
    return str(resp)


@app.route('/')
def home():
    # etc etc, flask app code
    return "hello!"

if __name__ == "__main__":
    app.run(debug=True)
