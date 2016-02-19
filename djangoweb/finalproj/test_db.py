# This is for test db
# use Python version 2.7.9
# use SQLite version 3.6.21
# Author: Yanghui Xiao (jack.xiao@outlook.com)

from db.DataIO import DataIO
from report_analyzer import get_ac_diff
import sys

DB_NAME = "db2.sqlite3"
TABLE_NAME = "runresult_result"

def testDataIO():
    dbio = DataIO(DB_NAME, TABLE_NAME)

    buf = open("demo.acc").read()

    result = get_ac_diff(buf)
    if result is not None:
        for entry in result:
            print entry
            dbio.store(entry[0], "list.test", "20150517", entry[2], "hspvsfsm")

    
    print dbio.get_latest_record_by_casename("c1/c2/c3/bp/19/c1/uu.sp")

if __name__== '__main__':
    testDataIO()
