#Example 3-3. hello.py: rendering a template

from flask import Flask, render_template, session, flash, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime, timezone

#A1_4-C1
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import Email, DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string' #A1_4-p1 C3
bootstrap = Bootstrap(app)
moment = Moment(app)

#A1_4p1-C2
class NameForm(FlaskForm):
 name = StringField('What is your name?', validators=[DataRequired()])
 #A1_4p2 C1
 #email= EmailField('What is your UofT Email address?', validators=[DataRequired(),Email()])
 email= EmailField('What is your UofT Email address?', validators=[DataRequired()])
 
 submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
  
 
    if form.validate_on_submit():
        old_name = session.get('name')
        email_prev = session.get('email')

        #If user change their name
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')

        #Email verify 
        email_input = form.email.data or ''
        valid_email = 'utoronto' in email_input and '@' in email_input.split("utoronto")[0]
        
        if email_prev != email_input:
            flash('Looks like you have changed your email!')
       
      
        session['name'] = form.name.data
        
        
        session['email'] = email_input        
        return redirect(url_for('index'))

    session_email = session.get('email', '')  
    valid_email = 'utoronto' in session_email and '@' in session_email.split("utoronto")[0] if session_email else False  
    

    return render_template('index.html', form=form, name=session.get('name'), email=session_email, valid_email=valid_email)


    
''' Old Code Tuesday below
        if 'utoronto' not in form.email.data:
            flash('Looks like you have changed your email!')

            #If user inputs invalid email, then session clears
            session['email'] = None
            return render_template('index.html', form=form, name=form.name.data, email=None)

            #return redirect(url_for('index'))

        #If user change their name
        if email_prev is not None and email_prev != form.email.data:
            flash('Looks like you have changed your name!')
        
        #Keeping the email, name in storage session
        session['name'] = form.name.data
        session['email'] = form.email.data
        
        return redirect(url_for('index'))
    
    return render_template('index.html', form = form, 
                           name = session.get('name'), email = session.get('email'))

Old code Tuesday above ''' 


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

#Example 3-6. hello.py: custom error pages

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)