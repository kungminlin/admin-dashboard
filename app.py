import requests
import json

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    url = "http://localhost:5000/registration/v1/list"
    headers = {"Authorization": "Bearer foobar"}
    response = requests.get(url=url, headers=headers)
    print(response)
    users = response.json()
    return render_template('signup_list.html', users=users)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='8080')
