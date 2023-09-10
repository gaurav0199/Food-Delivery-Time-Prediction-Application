from flask import Flask
from src.logger import logging


app=Flask(__name__)
@app.route("/",methods=["GET"])#if ['GET','POST'] not work the use only one method,post(use if you have private information)

def index():
    logging.info("We are testing our logging file")

    return "Welcome to My Project"

if __name__=='__main__':
    app.run(debug=True)