from db_connector import Connector
from dateutil import parser
import psycopg2

def query_exec(query,conn):
    curr = conn.cursor()
    curr.execute(query)
    return curr
performance = {"March":100, "April":200, "May":300, "June":400, "July":500}
date="2016-12-1"
date_original = "March"

day = parser.parse("01-3-2017").day

result=''
try:
    conn = Connector().getConn();
    result = query_exec("select * from pres_w_rx_repatha_short limit 1 offset "+ str(day), conn)
except  ValueError:
    print ValueError

print("The performance for " + str(result.fetchall()[0][13]) + " is ")

speech=''
if date_original in performance:
    speech = "The performance for the " + str(date_original) + " is " + str(performance[str(date_original)])
else:
    speech = "The performance for " + str(date) + " is "+str(performance['April'])

print speech

conn = Connector()

