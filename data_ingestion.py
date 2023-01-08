import logging
import pandas as pd
from connect import connect_database 

CASSANDRA_KEYSPACE = "insurance"
CASSANDRA_TABLE = "insurance"

class get_data_ingestion:


    def __init__(self):
        self.connect_database= connect_database()
        

    def get_data(self):
        
        logging.info(f"connction sent to connect.py file")
        session = self.connect_database.get_db_connection()
        sql_query = "SELECT * FROM {}.{};".format(CASSANDRA_KEYSPACE, CASSANDRA_TABLE)
        df = pd.DataFrame()
        for row in session.execute(sql_query):
            df = df.append(pd.DataFrame(row, index=[0]))
        df.to_csv("dataset/",mode="w", index=False,header=True)  
        
       


    