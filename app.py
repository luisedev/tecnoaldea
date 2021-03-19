import os
from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/intro', methods=['GET'])
def intro():
    return render_template('intro.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
      
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80", debug = True)