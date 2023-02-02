from flask import Flask, request
import sys
from data_ingestion import get_data_ingestion
import pip
import os, sys
import json
from flask import send_file, abort, render_template
import pandas as pd 


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        df=pd.DataFrame()
        df= get_data_ingestion().get_data()
        print(df["age"].mean())
        print("finished")
        context = df.to_dict("records")
        return render_template('templates.html',context=context)
        
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)