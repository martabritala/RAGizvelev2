import os
import psycopg2
import csv
import time

ELEPHANT_HOST = os.getenv("ELEPHANT_HOST")
ELEPHANT_NAME = os.getenv("ELEPHANT_NAME")
ELEPHANT_PASSWORD = os.getenv("ELEPHANT_PASSWORD")

dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)

def test_connection():
    """Pārbauda pieslēgumu datubāzei
    
    Returns:
        string -- tekstu ar datubāzes versiju
    """
    # saformatē pieslēgšanās parametrus
    # dsn = "host={} dbname={} user={} password={}".format(ELEPHANT_HOST, ELEPHANT_NAME, ELEPHANT_NAME, ELEPHANT_PASSWORD)
    # izveido pieslēgumu
    conn = psycopg2.connect(dsn)
    # izveido kursoru
    cur = conn.cursor()
    # aizsūta kursoram SQL vaicājumu
    cur.execute("SELECT version();")
    # pieprasa no kursora atbildi
    record = cur.fetchone()
    result = "You are connected to - " + str(record)
    # aizver kursoru
    cur.close()
    # aizver peislēgumu daubāzei
    conn.close()
    return result

