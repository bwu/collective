"""
Views
"""
import re
from flask import render_template, jsonify, request, session, redirect, url_for, escape
import MySQLdb as mdb
from app import app

def query_mysql(query):
    con = mdb.connect('localhost', 'root', '', 'collective');
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    return results

def update_mysql(query):
    con = mdb.connect('localhost', 'root', '', 'collective');
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    cur.close()
    return True

@app.route('/')
@app.route('/index')
def index():
    user_id = session.get('id')
    if user_id:
        statuses = query_mysql("select * from status s join follow f on s.user_id=f.follow_user_id where f.user_id={id} and s.deleted=0 order by s.date desc".format(id=user_id))
    else:
        statuses = query_mysql("select * from status where deleted=0 order by date desc")
    return render_template('index.html', statuses=statuses, check_login=user_id is None)

@app.route('/login', methods=['POST'])
def login():
    session['id'] = request.form['id']
    return redirect(url_for('index'))

@app.route('/<user_id>')
def user(user_id):
    statuses = query_mysql("select * from status where user_id={id} order by date desc".format(id=user_id))
    return render_template('index.html', statuses=statuses, check_login=False)

@app.route('/post', methods=['POST'])
def post():
    status = request.form.get('status')
    user_id = session.get('id')
    link = re.search('\S*spotify\:track\S*', status)
    if link is None:
        return jsonify(error=True)
    link = link.group(0)
    status = status.replace(link, '').rstrip()
    update_mysql("insert into status (user_id, msg, link, date) values ({id}, '{msg}', '{link}', now());".format(id=user_id, msg=status, link=link))
    return redirect(url_for('index'))


    