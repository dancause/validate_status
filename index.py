# coding: utf8
# JD Metro_CMS (nom provisoir) en attente d'une meilleur idée

import os
import time
import uuid
import httplib
import hashlib
import requests

from ua_parser import user_agent_parser
from werkzeug.utils import secure_filename

from datetime import datetime
from flask import g
from flask import json
from flask import Flask

from flask import session
from flask import jsonify
from flask import url_for
from flask import request
from flask import Response
from flask import make_response
from flask import redirect
from functools import wraps
from database import Articles
from database import Database
from flask import render_template


from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, StringField
from werkzeug.utils import secure_filename


app = Flask(__name__, static_url_path="", static_folder="static")
UPLOAD_FOLDER = 'static/images'
DELETE_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DELETE_FOLDER'] = DELETE_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.route('/')
def start_page():
    return render_template('temp_liste_server.html')


def validate_status():

    return 0


def validate_url(link):
    r = requests.head(link)
    return r.status_code

