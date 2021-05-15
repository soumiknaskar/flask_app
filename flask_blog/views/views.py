from flask import render_template, redirect, request, session, flash, url_for
from flask_blog import mysql
from flask_blog import app


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    cursor = mysql.get_db().cursor()
    if request.method == 'POST':
        username= request.form['username']
        password= request.form['password']
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        if account:
            session['logged_in'] = True
            session['username'] = username
            flash('Logged in succesfully')
            return redirect(url_for('show_entries'))
        else:
            # Account doesnt exist or username/password incorrect
            flash('username/password incorrect')
    return render_template('entries/login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("logged out")
    return redirect(url_for('show_entries'))
