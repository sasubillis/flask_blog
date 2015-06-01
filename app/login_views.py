from flask import render_template, request,flash, redirect, url_for
from app import app, db
from app.models import User
 
@app.route('/user/add/' , methods=['POST', 'GET'])
def user_add():
    if request.method == 'POST':
        user=User(request.form['name'], request.form['country'])
        db.session.add(user)
        db.session.commit()
        flash('New entry was successfully posted')     
             
    return render_template('user_add.html')

@app.route('/user/' )
def user_index():
  user = User.query.all()    
  return render_template('user_index.html', user=user)
