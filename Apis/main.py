from flask import Flask,request,jsonify #pip install Flask
import psycopg2  #pip install psycopg2
from psycopg2.extras import RealDictCursor
from flask_cors import CORS #pip install flask-cors

app = Flask(__name__)
CORS(app)

def conexion():
    return psycopg2.connect(
    host="localhost",
    database="bdExample",
    user="postgres",
    password="abril302")

@app.route('/',  methods=['GET'])
def index():
    conn = conexion()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM notes")
    rows = cur.fetchall() 
    conn.close()
    cur.close()
    return jsonify(rows)


@app.route('/', methods=['POST'])
def saveTeam():
    conn = conexion()
    cur = conn.cursor()
    name = request.form['name']
    description = request.form['description']
    cur.execute("INSERT INTO notes (name, description) VALUES (%s, %s)",(name, description))
    conn.commit()
    conn.close()
    cur.close()
    return jsonify(msg='added successfully!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

#cd desktop
#mkdir apisoccer
#python3 -m venv venv
#activar entorno virtual
#venv\Scripts\activate