#!/usr/bin/python
"""Script for creating SQLite DB from HuGaDB textfiles. 
Database contains two tables 'files' and and 'data'. 
'Files' table contains two columns: id, filename.
'Data' table contains 42 columns: id, file_id, timestamp and data features.
'File_id' contains id of file from which data downloaded. 

To use this script type:
python create_db.py path_to_HuGaDB_folder [dbname.db]

Parameter in square brackets is optional database name. 
By default database have name HuGaDB.db
"""

import glob
import sys
import sqlite3
from os.path import exists, isabs, basename, join, isdir
import numpy as np

def create_tabels(dbname='HuGaDB.db'):
    """Create 'files' and 'data' tables in SQLite DB
       Parameters:
            dbname: string
                name of the SQLite database
        Return: bool 
            False - if database was already created
    """
    rows_type = "id INTEGER PRIMARY KEY, file_id INTEGER, timestamp INTEGER, " + \
    "acc_rf_x  INTEGER,  acc_rf_y INTEGER,  acc_rf_z INTEGER, gyro_rf_x INTEGER,  gyro_rf_y INTEGER,  gyro_rf_z INTEGER," + \
    "acc_rs_x INTEGER,  acc_rs_y INTEGER, acc_rs_z INTEGER, gyro_rs_x INTEGER, gyro_rs_y INTEGER, gyro_rs_z INTEGER, " +  \
    "acc_rt_x INTEGER,  acc_rt_y INTEGER, acc_rt_z INTEGER, gyro_rt_x INTEGER, gyro_rt_y INTEGER, gyro_rt_z INTEGER, " +  \
    "acc_lf_x INTEGER,  acc_lf_y INTEGER, acc_lf_z INTEGER, gyro_lf_x INTEGER, gyro_lf_y INTEGER, gyro_lf_z INTEGER, " +  \
    "acc_ls_x INTEGER,  acc_ls_y INTEGER, acc_ls_z INTEGER, gyro_ls_x INTEGER, gyro_ls_y INTEGER, gyro_ls_z INTEGER, " +   \
    "acc_lt_x INTEGER,  acc_lt_y INTEGER, acc_lt_z INTEGER, gyro_lt_x INTEGER, gyro_lt_y INTEGER, gyro_lt_z INTEGER, " +  \
    "EMG_r INTEGER, EMG_l INTEGER, act INTEGER"  
    
    if not exists(dbname):
        con = sqlite3.connect(dbname)                    
        cur = con.cursor()
        cur.execute('CREATE TABLE files (id INTEGER PRIMARY KEY, filename VARCHAR(100))')
        con.commit()
        cur.execute('CREATE TABLE data (' + rows_type + ')')
        con.commit()
        con.close()
        return True
    else:
        return False       
    
def add_file_to_db(filename, dbname='HuGaDB.db'):
    """Add data from HuGaDB file in SQLite table
       Parameters:
           filename: string
               path to HuGaDB 
           dbname: string
               name of the SQLite database
        Return: bool 
            False - if database was already created
    """
    con = sqlite3.connect(dbname)                    
    cur = con.cursor()    
    
    data = np.genfromtxt(filename, delimiter='\t', skip_header=4)
    
    if isabs(filename):
        filename=basename(filename)

    cur.execute("INSERT INTO files VALUES(NULL, '{0}')".format(filename))
    con.commit()
    row_id = cur.execute('SELECT id FROM files WHERE filename="{0}"'.format(filename)).fetchone()[0]
    con.commit()
   
    for i, row in enumerate(data):
        cur.execute("INSERT INTO data VALUES(NULL, {0}, {1}, ".format(row_id, i) +  str(tuple(row.tolist())).replace("(", ""))
    con.commit()
    con.close()
    
def create_db(path_to_HuGaDB_folder, dbname='HuGaDB.db'):
    """Creating SQLite database from HuGaDB text files
       Parameters:
           path_to_HuGaDB_folder: string
               path to folder with HuGaDB 
           dbname: string
               name of the SQLite database
    """
    if not isdir(path_to_HuGaDB_folder):
        print("No such folder " + path_to_HuGaDB_folder)
        return
    files = glob.glob(join(path_to_HuGaDB_folder, 'HuGaDB*.txt'))
    length = len(files)
    if length == 0:
        print("No HuGaDB files in folder")
        return
	
    if not create_tabels(dbname=dbname):
        print("DB is already exist")
        return 
    for i, filename in enumerate(files):
        sys.stdout.write('\r')
        sys.stdout.write("Creating database: file {0}/{1}".format(i+1, length))
        add_file_to_db(filename, dbname=dbname)
        sys.stdout.flush()


if len(sys.argv) == 1:
    print("You should add path to HuGaDB folder as second argument")
elif len(sys.argv) == 2:
    path_to_HuGaDB_folder=sys.argv[1]
    dbname = 'HuGaDB.db'
    create_db(path_to_HuGaDB_folder=path_to_HuGaDB_folder, dbname=dbname)
elif len(sys.argv) == 3:    
    path_to_HuGaDB_folder=sys.argv[1]
    dbname=sys.argv[2]
    create_db(path_to_HuGaDB_folder=path_to_HuGaDB_folder, dbname=dbname)

