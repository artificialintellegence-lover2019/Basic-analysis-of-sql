# -*- coding: utf-8 -*-
"""Machine-Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nrL9hE7Z-58FG0jl8uVTqO1BUwBgGALG
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas as pd

!pip install ibm_db

import ibm_db

dsn_hostname = "dashdb-txn-sbox-yp-lon02-04.services.eu-gb.bluemix.net" # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_uid = "bmt70440"        # e.g. "abc12345"
dsn_pwd = "k54tm9n1rbnmb@dd"      # e.g. "7dBZ3wWt9XN6$o0J"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_port = "50000"                # e.g. "50000" 
dsn_protocol = "TCPIP"

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

#print the connection string to check correct values are specified
print(dsn)

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )

import pandas as pd
import ibm_db_dbi

pconn1 = ibm_db_dbi.Connection(conn)

selectQuery1 = "select count(*) from CRIME"
df1 = pd.read_sql(selectQuery1, pconn1)

#Find the total number of crimes recorded in the crime table
np.array(df1)

selectQuery2 = "select * from CRIME LIMIT 10"
df2 = pd.read_sql(selectQuery2, pconn1)

# Retrieve first 10 rows from the CRIME table
df2

selectQuery3 = "select count(*) from CRIME where ARREST = TRUE"
df3 = pd.read_sql(selectQuery3, pconn1)

#How many crimes involve an arrest
np.array(df3)

selectQuery4 = "select distinct PRIMARY_TYPE from CRIME where LOCATION_DESCRIPTION = 'GAS STATION'"
df4 = pd.read_sql(selectQuery4, pconn1)

# Which unique types of crimes have been recorded at a GAS STATION?
df4

selectQuery5 = "select COMMUNITY_AREA_NAME from CENSUS where COMMUNITY_AREA_NAME like 'B%'"
df5 = pd.read_sql(selectQuery5, pconn1)

#In the CENUS_DATA table list all community areas whose names start with the letter ‘B’
df5

selectQuery6 = "select NAME_OF_SCHOOL from \
(select NAME_OF_SCHOOL, HEALTHY_SCHOOL_CERTIFIED, COMMUNITY_AREA_NUMBER from PUBLICSCHOOL where COMMUNITY_AREA_NUMBER between 10 and 15 and HEALTHY_SCHOOL_CERTIFIED = 'Yes')"

df6 = pd.read_sql(selectQuery7, pconn1)

#List the schools in Community Areas 10 to 15 that are healthy school certified?
df6

selectQuery7 = "select avg(SAFETY_SCORE) from PUBLICSCHOOL"
df7 = pd.read_sql(selectQuery7, pconn1)

#What is the average school Safety Score?
np.array(df7)

selectQuery = "select COMMUNITY_AREA_NAME, COLLEGE_ENROLLMENT as number_of_students from PUBLICSCHOOL \
order by number_of_students desc fetch first 5 rows only"
df= pd.read_sql(selectQuery, pconn1)

df

selectQuery8 = "select COMMUNITY_AREA_NAME from CENSUS \
where COMMUNITY_AREA_NUMBER = \
(select COMMUNITY_AREA_NUMBER from PUBLICSCHOOL order by SAFETY_SCORE limit 1)"
df8 = pd.read_sql(selectQuery8, pconn1)

# Use a sub-query to determine which Community Area has the least value for Safety Score?
df8

selectQuery9 = "select PER_CAPITA_INCOME, COMMUNITY_AREA_NAME from CENSUS \
where COMMUNITY_AREA_NUMBER = \
(select COMMUNITY_AREA_NUMBER from PUBLICSCHOOL \
where SAFETY_SCORE = 1)"
df9 = pd.read_sql(selectQuery9, pconn1)

#Find the Per Capita Income of the Community Area which has a school Safety Score of 1
df9

selectQuery8 = "select COMMUNITY_AREA_NAME , COLLEGE_ENROLLMENT from PUBLICSCHOOL order by COLLEGE_ENROLLMENT desc LIMIT 5 "
df8 = pd.read_sql(selectQuery, pconn1)

#List the top 5 Community Areas by average College Enrollments [number of students]
df8