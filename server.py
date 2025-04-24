from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title="Заголовок")


@app.route('/training/<prof>')
def traning(prof):
    if prof in "инженер строитель":
        return render_template('bp_eng_bld.html', title="Заголовок", profession="Инженерные тренажеры")
    else:
        return render_template('bp_other.html', title="Заголовок", profession="Научные симуляторы")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
