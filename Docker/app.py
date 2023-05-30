from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:1234@db:5432/dbPostgres'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/')
def hello():
    try:
        db.session.execute('SELECT 1')
        db.session.commit()
        return 'Conexão com o banco de dados estabelecida com sucesso!'
    except Exception as e:
        return f'Erro ao conectar ao banco de dados: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
