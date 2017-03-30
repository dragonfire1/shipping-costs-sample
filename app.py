#!/usr/bin/env python

import urllib
import json
import os

from dateutil import parser
##Custom connector
from db_connector import Connector
##

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

def query_exec(query,conn):
    curr = conn.cursor()
    curr.execute(query)
    return curr

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

    performance = {"march":100, "april":200, "may":300, "june":400, "july":500}
    date_intial = date.split("/")[0]
    day = parser.parse(date_intial).day
    result=''
    try:
        conn = Connector().getConn();
        result = query_exec("select * from pres_w_rx_repatha_short limit 1 offset "+ str(day), conn)
    except  ValueError:
        print ValueError

    speech ="The performance for "+str(date)+"is" + str(result.fetchall()[0][13])

    # if date_original.lower() in performance:
    #     speech = "The performance for the " + str(date_original) + " is " + str(performance[str(date_original.lower())])
    # else:
    #     speech = "The performance for " + str(result.fetchall[1]) + " is "+str(performance['april'])

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

