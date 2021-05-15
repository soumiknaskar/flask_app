from flask import render_template, redirect, session, url_for

from flask_blog import app


@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/index.html')
