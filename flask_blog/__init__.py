from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL(app)

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "soumik"
app.config["MYSQL_DATABASE_PASSWORD"] = 'Coke@650km'
app.config["MYSQL_DATABASE_DB"] = 'blogs'
app.config["MYSQL_DATABASE_HOST"] = 'localhost'
app.config["MYSQL_DATABASE_PORT"] = 32000
app.config['SECRET_KEY'] = 'p9Bv<3Eid9%$i01'

from flask_blog.views import entries, views

