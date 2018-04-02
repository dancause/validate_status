# coding: utf8
# JD Metro_CMS (nom provisoir) en attente d'une meilleur idée

import requests

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
from database import Database
from database import Website
from flask import render_template

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
    web = validate_status()
    return render_template('temp_liste_server.html',web=web)


def validate_status():
    liste = get_db().get_url()
    error = []
    good = []
    for link in liste:
        code = validate_url(link.link)
        now = datetime.now()
        if code >= 500:
            get_db().save_log(link.link,now.isoformat(),code)
            p = Website(link.number, link.link,now.isoformat(), code)
            error.append(p)
        get_db().update_link(link.number,link.link, now.isoformat(),code)
    return get_db().get_url()


def validate_url(link):
    temp = 0
    try:
        r = requests.head(link)
        print r.url
        print r.status_code
        temp = r.status_code
    except Exception as value:
        temp = 500
    return temp

def send_courriel():
    pass