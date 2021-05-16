from flask import render_template, redirect, session, url_for, request, flash

from flask_blog import app
from flask_blog import mysql
from flask_blog.models.entries import Entries
from flask_blog.views.views import login_required


@app.route('/entries/new', methods=['GET'])
@login_required
def new_entry():
    return render_template('entries/new.html')


@app.route('/entries', methods=['POST'])
@login_required
def add_entry():
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


@app.route('/')
@login_required
def show_entries():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM entries ORDER BY created_at ASC')
    entries = cursor.fetchall()
    return render_template('entries/index.html', entries=entries)


@app.route('/entries/<int:id>')
@login_required
def show_entry(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM entries where id = %s', (id))
    entry = cursor.fetchone()
    return render_template('entries/show.html', entry=entry)

@app.route('/entries/<int:id>/edit')
@login_required
def edit_entry(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM entries where id = %s',(id))
    entry = cursor.fetchone()
    return render_template('entries/edit.html', entry=entry)

@app.route('/entries/<int:id>/update', methods=['POST'])
@login_required
def update_entry(id):
    cursor = mysql.get_db().cursor()
    title = request.form['title']
    text = request.form['text']
    cursor.execute("""UPDATE entries SET title = %s, text = %s WHERE id = %s""", (title, text, id))
    cursor.connection.commit()
    flash('Content has been updated')
    return redirect(url_for('show_entries'))


@app.route('/entries/<int:id>/delete', methods=['POST'])
@login_required
def delete_entry(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("""DELETE FROM entries WHERE id = %s""", (id))
    cursor.connection.commit()
    flash('Blog has been deleted')
    return redirect(url_for('show_entries'))
