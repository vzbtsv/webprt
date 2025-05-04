from flask import Flask, render_template, redirect, make_response, request, session, abort
from data import db_session
from data.users import User
from data.news import News
from forms.user import RegisterForm, LoginForm
import datetime
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms.news import NewsForm

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)
db_session.global_init("db/blogs.db")


def main():
    app.run()


if __name__ == '__main__':
    main()

db_sess = db_session.create_session()

