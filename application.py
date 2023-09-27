from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

application = Flask(__name__) # initializing a flask application

@cross_origin()
@application.route('/',methods=['GET'])  # route to display the home page

def homePage():
    return render_template('home.html')
if __name__ == "__main__":
    application.run()