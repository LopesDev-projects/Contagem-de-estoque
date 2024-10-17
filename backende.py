from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def connect_db():
    conn = sqlite3.connect('users.db')
    return conn

# Rota para a página de login
@app.route('/')
def login():
    return render_template('login.html')

# Rota para processar o login
@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['usuario']
    password = request.form['senha']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        return "Login bem-sucedido!"
    else:
        return "Usuário ou senha incorretos."

# Rota para criar conta
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['usuario']
        password = request.form['senha']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return redirect(url_for('login'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

    
#Banco de dados dos usuarios
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Criar tabela de usuários
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

conn.commit()
conn.close()
