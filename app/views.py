"""
Views
"""
from flask import render_template
import MySQLdb as mdb
from app import app

@app.route('/')
@app.route('/index')
def index():
    con = mdb.connect('localhost', 'root', '', 'collective');
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("select * from status order by date desc")
    statuses = cur.fetchall()
    return render_template('index.html', statuses=statuses)
    