from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory
import pandas as pd
from flask import Flask,request,app,jsonify,url_for,render_template



class configuration:

    
    def __init__(self):
        self.cluster = Cluster
        self.PlainTextAuthProvider = PlainTextAuthProvider
        self.dict_factory = dict_factory

    def get_configuration(self) -> pd.DataFrame:

        try:
            
            print("reached get configuration function")
            cloud_config =  {
                ##'secure_connect_bundle': '<</PATH/TO/>>secure-connect-health-insurance-premium-prediction.zip'
                'secure_connect_bundle': 'bundle\\secure-connect-health-insurance-premium-prediction.zip'    
         
            }   
    
            auth_provider = self.PlainTextAuthProvider('lXSEkrnNwjRAZIMrrqDofZEt', 'Ky3RyksHe+NXdWbSsz7zAfkR5wZgodh-I4ZCmL,1Z.SvT7freEDqrB-Ffr2L5SddiRzX7NqYMXo28.PH7lrQ839wn1wz3DqBC-QUMi1550_4ZramWzGz5GMsgAthZC5E')
            cluster = self.cluster(cloud=cloud_config, auth_provider= auth_provider)
            session = cluster.connect()
            session.row_factory = dict_factory

               
            data= pd.DataFrame()
            ##sql_test="SELECT * FROM insurance.insurance LIMIT 300"
            ##se = session.execute(sql_test)
            ##print(se)

            sql_query = "SELECT * FROM insurance.insurance"
            print("Initiating sql query to slect from database and table")
            for row in session.execute(sql_query):
                data = data.append(pd.DataFrame(row, index=[0]))
            ##    data = pd.concat(pd.DataFrame(row, index=[0]))
            data = data.reset_index(drop=True).fillna(pd.np.nan)    
            print("convertuing to csv file")
            data.to_csv("dataset/dataset.csv",mode="w", index=False,header=True)
            
            #session.shutdown(0)
            return data

        except Exception as e:
            print(e)    