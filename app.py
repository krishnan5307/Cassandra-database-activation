from flask import Flask, request
import sys
from data_ingestion import get_data_ingestion
import pip
import os, sys
import json
from flask import send_file, abort, render_template
import pandas as pd 
from flask import Flask,request,app,jsonify,url_for,render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        df=pd.DataFrame()
        df= get_data_ingestion().get_data()
        print(df["age"].mean())
        print("finished")
        return render_template('template.html')
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)