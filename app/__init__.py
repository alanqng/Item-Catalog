from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook

google_blueprint = make_google_blueprint(client_id='35189606116-d1pge95126e7vmllgvc69v8ihmr5p9cl.apps.googleusercontent.com', client_secret='zY4T7G2Xp__FmRPhAEd_YKDE',)


app = Flask(__name__)
app.register_blueprint(google_blueprint, url_prefix='/login')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///items.db"
app.config['SECRET_KEY'] = 'thisissupersecret'

db = SQLAlchemy(app)

from app import routes