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



@app.route('/list_prof/<list>')
def list_prof(list):
    sp = ["инженер-исследователь",
          "пилот,"
          "экзобиолог",
          "врач",
          "инженер по терраформированию",
          "климатолог",
          "специалист по радиационной защите"]
    return render_template('list_prof.html', title="Список профессий", sp=sp, sptype=list)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
