from flask import Flask, request
import sys
import data_ingestion as pdf
import connect_database
import pip
import os, sys
import json
from flask import send_file, abort, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        return pdf.get_data_ingestion
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run( debug=True)
