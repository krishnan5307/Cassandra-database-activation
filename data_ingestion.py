


class get_data_ingestion:


    def __init__(self):
        pass

    def get_data(self)-> session





            #from cassandra database using connction variable to download dataset to dataframe and later to csv
            download_url = self.data_ingestion_config.dataset_download_url
            logging.info(f"connction sent to connect_databsae.py file")
            
            session = self.database_connection.get_db_connection()
            
            sql_query = "SELECT * FROM {}.{};".format(constant.CASSANDRA_KEYSPACE, constant.CASSANDRA_TABLE)
            df = pd.DataFrame()
            for row in session.execute(sql_query):
                    df = df.append(pd.DataFrame(row, index=[0]))

            session.shutdown()