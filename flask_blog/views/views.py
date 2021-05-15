from flask import render_template, redirect, request, session, flash, url_for

from flask_blog import app


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('USER NOT FOUND')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('PASSWORD NOT FOUND')
        else:
            session['logged_in'] = True
            flash('Logged in succesfully')
            return redirect(url_for('show_entries'))
    return render_template('entries/login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("logged out")
    return redirect(url_for('show_entries'))
