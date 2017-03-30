
import os
import psycopg2
import urlparse

#urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse("postgres://wooogfeghpytns:43e10f466c0cf5e0e3fdf6813cd0b23527798006cacf5d08802b0c71b3e0ce6e@ec2-54-163-254-48.compute-1.amazonaws.com:5432/ddu92rj5uj238p")

class Connector():
    def __init__(self):
         conn = psycopg2.connect(
          database=url.path[1:],
           user=url.username,
             password=url.password,
             host=url.hostname,
             port=url.port)

    def getConn(self):
        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port)
        return conn

    def setConn(self,url):
        self.url = url
