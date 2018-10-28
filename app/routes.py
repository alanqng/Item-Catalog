from app import app
from flask import url_for, redirect, render_template


@app.route("/")
def index():
    return render_template('test.html')

@app.route("/login")
def login():
    pass