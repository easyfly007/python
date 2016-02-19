# This is for pySig project database handling
# use Python version 2.7.9
# use SQLite version 3.6.21
# Author: Yanghui Xiao (jack.xiao@outlook.com)

import sqlite3 as lite

global _debug_print_
_debug_print_ = False


class DataIO:
    def __init__(self, dbname, tablename):
        self._db_name = dbname
        self._tbl_name = tablename
        # open db if exists, otherwise create it
        # create a table named as "runresult_result"
        try:
            self._con = lite.connect(self._db_name)
            print "DB connected."
            self._cur = self._con.cursor()
            self._cur.execute('''create table if not exists %s
               (id integer primary key autoincrement not null, casename varchar(100), 
                caselist varchar(10), rundate varchar(8),trandiff real, comparenote varchar(10))''' %self._tbl_name)
        except lite.Error, e:
            print "Error when initializing DB: %s" % e.args[0]

    def __del__(self):
        if self._con:
            self._con.close()
            print "DB closed."


    # store data
    def store(self, casename, caselist, rundate, trandiff, comparenote):
        try:
            self._cur.execute('''select * from %s where casename = "%s" 
                and rundate = "%s" and comparenote = "%s"''' %(self._tbl_name, casename, rundate, comparenote))
            #remove duplicate record if any
            if self._cur.fetchone() is not None:
                self._cur.execute('''delete from %s where casename = "%s"
                    and rundate = "%s" and comparenote = "%s"''' %(self._tbl_name, casename, rundate, comparenote))
                if _debug_print_ == True:
                    print "delete record: %s %s %s from table %s" %(casename, rundate, comparenote, self._tbl_name)
            t = (None, casename, caselist, rundate, trandiff, comparenote)
            self._cur.execute('insert into %s values (?, ?, ?, ?, ?, ?)' %self._tbl_name, t)
            self._con.commit()
        except lite.Error, e:
            print "Error when inserting DB: %s" % e.args[0]
            return -1
        return 1

    # fetch data        
    def get_latest_record_by_casename(self, casename):
        try:
            self._cur.execute('select * from %s where casename = "%s"' %(self._tbl_name, casename))
        except lite.Error, e:
            print "Error when querying DB data. Exit.: %s" % e.args[0]
            return -1
        return self._cur.fetchone()

    def get_records(self, caselist, rundate, comparenote):
        try:
            self._cur.execute('''select * from %s where caselist = "%s" 
                and rundate = "%s" and comparenote = "%s"''' %(self._tbl_name, caselist, rundate, comparenote))
        except lite.Error, e:
            print "Error when querying DB data. Exit.: %s" % e.args[0]
            return -1
        return self._cur.fetchall()
