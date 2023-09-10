from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os,sys

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])

def index():

    try:
        raise Exception("We are testing our exception file")#error
    
    except Exception as e:
        ml=CustomException(e,sys)#error message and detail
        logging.info(ml.error_message)

        logging.info("We are testing our logging file")

        return "Welcome to My Project"

if __name__=='__main__':
    app.run()