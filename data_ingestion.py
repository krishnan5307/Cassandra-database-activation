import logging
import pandas as pd
import numpy as nd
from config import configuration


class get_data_ingestion:


    def __init__(self):
        self.config =configuration()
        

    def get_data(self) -> pd.DataFrame:

        df = pd.DataFrame()
        df = self.config.get_configuration()
        return df

        
    
        
       


    