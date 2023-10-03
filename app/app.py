from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configura la URL de conexión a la base de datos PostgreSQL.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db/postgres'

# Crea una instancia de SQLAlchemy.
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)