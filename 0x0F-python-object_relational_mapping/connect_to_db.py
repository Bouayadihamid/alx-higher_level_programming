#!/usr/bin/python3
import MySQLdb
MY_HOST = 'localhost'
MY_USER = 'root'
MY_PASS = 'password'
MY_DB = 'mydb'

db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
