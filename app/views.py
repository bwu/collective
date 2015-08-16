"""
Views
"""
from flask import render_template, jsonify, request
import MySQLdb as mdb
from app import app

def query_mysql(query):
    con = mdb.connect('localhost', 'root', '', 'collective');
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute(query)
    return cur.fetchall()

@app.route('/')
@app.route('/index')
def index():
    statuses = query_mysql("select * from status order by date desc")
    return render_template('index.html', statuses=statuses)

@app.route('/_following')
def following():
    user_id = request.args.get('id')
    statuses = query_mysql("select * from status s join follow f on s.user_id=f.follow_user_id where f.user_id={id} order by date desc".format(id=user_id))
    return jsonify(statuses=statuses)

    