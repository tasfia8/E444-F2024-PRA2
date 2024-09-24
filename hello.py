#Example 3-3. hello.py: rendering a template

from flask import Flask, render_template, session, flash, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime, timezone

#A4-C1
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string' #A4-C3
bootstrap = Bootstrap(app)
moment = Moment(app)

#A4-C2
class NameForm(FlaskForm):
 name = StringField('What is your name?', validators=[DataRequired()])
 submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
 
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',
        form = form, name = session.get('name'))





#@app.route('/user/<name>')
#def user(name):
# return render_template('user.html', name=name)

#Example 3-6. hello.py: custom error pages

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)