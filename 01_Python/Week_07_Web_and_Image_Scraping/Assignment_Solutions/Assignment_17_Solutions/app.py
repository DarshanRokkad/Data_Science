from flask import Flask , render_template , request , jsonify
from flask_cors import CORS,cross_origin
import requests 
from bs4 import BeautifulSoup as bs 
from urllib.request import urlopen
import logging 
import pymongo 

app = Flask(__name__)

@app.route('/',methods = ['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')

@app.route('/youtube_info',methods = ['GET','POST'])
def scrap():
    if request.method == 'POST':
        try:
            search_string = input()
            youtube_url = 'https://www.youtube.com/@PW-Foundation/videos'
            youtube_page = urlopen(youtube_url).read()
            youtube_html = bs(youtube_page,'html.parser')

        except Exception as e:
            print('The exception message is:',e)
            return 'Something went wrong'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')