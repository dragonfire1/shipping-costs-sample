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

def performace(req):
    result = req.get("result")
    parameters = result.get("parameters")
    date = parameters.get("date-period")
    date_original = parameters.get("date-period-original")

    performance = {"march":100, "april":200, "may":300, "june":400, "july":500}
    date_intial = date.split("/")[0]
    date_end = date.split("/")[1]
    month_ini = parser.parse(date_intial).month
    result=''
    try:
        conn = Connector().getConn();
        result = query_exec("select sum(sales) from d_repatha_sales where to_date(week,'MM/DD/YYYY') > to_date('"+date_intial+"','YYYY-MM-DD') and to_date(week,'MM/DD/YYYY') < to_date('"+date_end+"','YYYY-MM_DD')" , conn)
    except  ValueError:
        print ValueError

    speech ="The performance for "+str(date)+" is " + str(result.fetchall()[0])

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

def customer_list(req):

    result = req.get("result")
    parameters = result.get("parameters")
    customer = parameters.get("customer")

    try:
        conn = Connector().getConn();
        result = query_exec("select distinct(cust_affl_name) from pres_w_rx_repatha_short", conn)
    except  ValueError:
        print ValueError
    speech=''
    for name in result.fetchall():
        speech = speech+", "+name[0]

    speech ="The customers are is " + speech[1:]

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
    action_name = req.get("result").get("action")

    indent_response_call_dict = {"support.performance_try":performace,"support.customer_list":customer_list}

    if action_name in indent_response_call_dict:
        res = indent_response_call_dict[action_name](req)
        return res
    else:
        return {
        "speech": "No such action",
        "displayText": "no such action",
        #"data": {},
        # "contextOut": [],
        "source": "apiai-performance-chat-bot-python"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print "Starting app on port %d" % port
    app.run(debug=True, port=port, host='0.0.0.0')