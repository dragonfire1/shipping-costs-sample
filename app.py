#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "support.performace_try":
        return {
        "speech": "No such action",
        "displayText": "no such action",
        #"data": {},
        # "contextOut": [],
        "source": "apiai-performance-chat-bot-python"
    }
    result = req.get("result")
    parameters = result.get("parameters")
    date = parameters.get("date-period")
    date_original = parameters.get("date-period-original")

    performance = {'March':100, 'April':200, 'May':300, 'June':400, 'July':500}

    if date_original in performance:
        speech = "The performance for " + str(date_original) + " is " + str(performance[date_original])
    else:
        speech = "The performance for " + str(date) + " is "+str(performance['April'])

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-performance-chat-bot-python"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
