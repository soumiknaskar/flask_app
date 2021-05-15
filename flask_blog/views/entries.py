from flask import render_template, redirect, session, url_for, request, flash

from flask_blog import app
from flask_blog import mysql
from flask_blog.models.entries import Entries


@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/index.html')


@app.route('/entries/new', methods=['GET'])
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')


@app.route('/entries', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    cursor = mysql.get_db().cursor()
    entry = Entries(
        title=request.form['title'],
        text=request.form['text']
    )
    title, text, created_at = entry.user()
    cursor.execute('INSERT INTO entries (title, text, created_at) VALUES ( %s, %s, %s)', (title, text, created_at))
    cursor.connection.commit()
    flash('A new article has been created')
    return redirect(url_for('show_entries'))
