from datetime import datetime

from flask import Flask, render_template, redirect, make_response, request, session, abort
from data import db_session
from data.users import User
from data.jobs import Job
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/mars_explorer.db")
session = db_session.create_session()


@app.route("/")
@app.route("/index")
def index():
    jobs = session.query(Job).all()
    return render_template("index.html", jobs=jobs)


def main():
    app.run()


if __name__ == '__main__':
    main()
