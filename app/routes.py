from app import app, google_blueprint, google
from flask import url_for, redirect, render_template
from flask_dance.contrib.google import google


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login')
def login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    return "You are {email} on Google".format(email=resp.json()["email"])
    