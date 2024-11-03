from flask import Flask, jsonify, request
from db import select,transaction,commit
import hashlib

app = Flask(__name__)

def get_sha1_of_string(input_string):
    return hashlib.sha1(input_string.encode()).hexdigest()

@app.post('/register')
def register():
    username = request.form['username']
    password = request.form['password']
    password = get_sha1_of_string(password)
    
    trans = transaction() 
    sql = "insert into user (username,password) values (%s,%s)"
    trans.execute(sql, [username, password])
    commit(trans)
    return jsonify([{'status': True}])

@app.post('/login')
def login():
    username = request.form['username']
    password = request.form['password']
    password = get_sha1_of_string(password)
    
    sql = "select 1 from user where username=%s and password=%s" % (username,password)
    result = select(sql)
    if(len(result) == 0):
        return jsonify({'status':False,'message':'not found'})
    return jsonify({'status':True,'message':'found'})

@app.post('/prelist')
def get_prelist():
    page = request.form['page']
    per_page = request.form['per_page']
    per_page = int(per_page)
    offset = int(page) * int(per_page)    
    sql = 'select * from bnba limit %d offset %d' % (per_page,offset)
    result = select(sql)
    return jsonify(status=True,data=result)

if __name__ == '__main__':
    app.run(debug=True)
