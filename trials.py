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


colu = "$_Sales_03/10/2017_W1,$_Sales_03/03/2017_W2,$_Sales_02/24/2017_W3,$_Sales_02/17/2017_W4,$_Sales_02/10/2017_W5,$_Sales_02/03/2017_W6,$_Sales_01/27/2017_W7,$_Sales_01/20/2017_W8,$_Sales_01/13/2017_W9,$_Sales_01/06/2017_W10,$_Sales_12/30/2016_W11,$_Sales_12/23/2016_W12,$_Sales_12/16/2016_W13,$_Sales_12/09/2016_W14,$_Sales_12/02/2016_W15,$_Sales_11/25/2016_W16,$_Sales_11/18/2016_W17,$_Sales_11/11/2016_W18,$_Sales_11/04/2016_W19,$_Sales_10/28/2016_W20,$_Sales_10/21/2016_W21,$_Sales_10/14/2016_W22,$_Sales_10/07/2016_W23,$_Sales_09/30/2016_W24,$_Sales_09/23/2016_W25,$_Sales_09/16/2016_W26,$_Sales_09/09/2016_W27,$_Sales_09/02/2016_W28,$_Sales_08/26/2016_W29,$_Sales_08/19/2016_W30,$_Sales_08/12/2016_W31,$_Sales_08/05/2016_W32,$_Sales_07/29/2016_W33,$_Sales_07/22/2016_W34,$_Sales_07/15/2016_W35,$_Sales_07/08/2016_W36,$_Sales_07/01/2016_W37,$_Sales_06/24/2016_W38,$_Sales_06/17/2016_W39,$_Sales_06/10/2016_W40,$_Sales_06/03/2016_W41,$_Sales_05/27/2016_W42,$_Sales_05/20/2016_W43,$_Sales_05/13/2016_W44,$_Sales_05/06/2016_W45,$_Sales_04/29/2016_W46,$_Sales_04/22/2016_W47,$_Sales_04/15/2016_W48,$_Sales_04/08/2016_W49,$_Sales_04/01/2016_W50,$_Sales_03/25/2016_W51,$_Sales_03/18/2016_W52"

colum_lt=colu.split(",")

query=''
for i in colum_lt:

    query= query+"select w_sales_repatha_id,Terr_Name,Cust_Affl,Cust_Type,Cust_Affl_Name,Address,City,State,Zip,Primary_Specialty,Opportunity_Flag,Pres_Seg,Product, '"+i[8:18]+"' as week , `"+i+"` as sales from repatha_sales union all " \
                                             ""

print query