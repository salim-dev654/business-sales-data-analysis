import mysql.connector

def connect_db():
    return mysql.connector.connect(
        user="root",
        password="",
        unix_socket="/data/data/com.termux/files/usr/var/run/mysqld.sock",
        database="sales_analysis_db"
    )

