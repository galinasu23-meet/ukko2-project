from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

config = {
  "apiKey": "AIzaSyBde2FTODt9WKWpMHrJQovdpPRN11LTjfM",
  "authDomain": "ukko-final-project.firebaseapp.com",
  "databaseURL": "https://ukko-final-project-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "ukko-final-project",
  "storageBucket": "ukko-final-project.appspot.com",
  "messagingSenderId": "790719983301",
  "appId": "1:790719983301:web:1a240d7e0134e922f48aac",
  "measurementId": "G-767LHYRXX6",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route("/", methods = ['GET', 'POST'])
def signin():
	return render_template("main.html")

#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)