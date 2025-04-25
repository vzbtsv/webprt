from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.news import News
from forms.user import RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.db")



@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)



def main():
    app.run()

if __name__ == '__main__':
    main()


db_sess = db_session.create_session()

# user = User()
# user.name = "Пользователь 4"
# user.about = "биография пользователя 4"
# user.email = "email4@email.ru"
# db_sess.add(user)
# db_sess.commit()

# news = db_sess.query(News).all()
# for n in news:
#     db_sess.delete(n)
#
# user = db_sess.query(User).first()
# news = News(title="Первая новость", content="Привет блог!",
#             user_id=1, is_private=False)
# db_sess.add(news)
# db_sess.commit()
# news = News(title="Вторая новость", content="Уже вторая запись!",
#             user=user, is_private=False)
# db_sess.add(news)
# db_sess.commit()

# user = db_sess.query(User).filter(User.id == 1).first()
# news = News(title="Личная запись", content="Эта запись личная",
#             is_private=True)
# user.news.append(news)
# db_sess.commit()


for user in db_sess.query(User).all():
    print(user)

news = db_sess.query(News).all()
for n in news:
    print(n)

# for news in user.news:
#     print(news)




