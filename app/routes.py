from flask import render_template

from app import app



@app.route('/', methods=['GET', 'POST'])
def index():
    msg = ""
    return render_template("index.html",
                           title="index page",
                           msg=msg)

@app.route('/get_suppliers')
def get_suppliers():
    # lakes = Lake.query.all()
    # return render_template('get_lakes.html', title='Список водоемов',
    #                        lakes=lakes)
    return "all"