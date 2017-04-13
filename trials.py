from db_connector import Connector
from dateutil import parser
import psycopg2

def query_exec(query,conn):
    curr = conn.cursor()
    curr.execute(query)
    return curr

def zero(s):
     print s

# d = {"may":zero}
# d["may"]("this")
# d["may"]("that")
# d["may"]("eerything")

# performance = {"March":100, "April":200, "May":300, "June":400, "July":500}
# date="2016-12-1"
# date_original = "March"
#
# day = parser.parse("01-3-2017").day
#
# result=''
# try:
#     conn = Connector().getConn();
#     result = query_exec("select distinct(cust_affl_name) from pres_w_rx_repatha_short", conn)
# except  ValueError:
#     print ValueError
#
# for name in result.fetchall():
#     print name[0]


# speech=''
# if date_original in performance:
#     speech = "The performance for the " + str(date_original) + " is " + str(performance[str(date_original)])
# else:
#     speech = "The performance for " + str(date) + " is "+str(performance['April'])
#
# print speech

# conn = Connector()


import nltk

text = nltk.word_tokenize("what are the sales of my customers")
print(nltk.pos_tag(text))


