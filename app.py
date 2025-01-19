from flask import Flask, render_template, request, redirect, jsonify
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

server = os.getenv('DB_SERVER') 
database = os.getenv('DB_DATABASE') 
username = os.getenv('DB_USERNAME')  
password = os.getenv('DB_PASSWORD')  

conn_string = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes"





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pets', methods=['GET', 'POST'])
def pets():
    if request.method == 'POST':
        nome_pet = request.form['nome_pet']
        especie = request.form['especie']
        idade = request.form['idade']
        raca = request.form['raca']
        observacoes = request.form['observacoes']
        id_cliente = request.form['id_cliente']

        db_connection = pyodbc.connect(conn_string)
        cursor = db_connection.cursor()
        cursor.execute('''
            INSERT INTO Pets (nome_pet, especie, idade, raca, observacoes, id_cliente)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (nome_pet, especie, idade, raca, observacoes, id_cliente))
        db_connection.commit()
        db_connection.close()
        return redirect('/pets')

    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute('SELECT id_cliente, nome FROM Clientes')
    clientes = cursor.fetchall()
    conn.close()

    return render_template('pets.html', clientes=clientes)







@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        telefone = request.form['telefone']

        
        db_connection = pyodbc.connect(conn_string)
        cursor = db_connection.cursor()
        cursor.execute('''
            INSERT INTO Clientes (nome, email, cpf, telefone)
            VALUES (?, ?, ?, ?)
        ''', (nome, email, cpf, telefone))
        db_connection.commit()
        db_connection.close()
        return redirect('/clientes')
    
    return render_template('clientes.html')







@app.route('/consultaclientes')
def consulta_clientes_page():
    return render_template('consultaclientes.html')

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    db_connection = pyodbc.connect(conn_string)
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM Clientes')
    clientes = cursor.fetchall()
    db_connection.close()

    return jsonify([{
        'id_cliente': row[0], 
        'nome': row[1],       
        'email': row[2],       
        'cpf': row[3],         
        'telefone': row[4]     
    } for row in clientes])






@app.route('/consultapets')
def consulta_pets_page():
    return render_template('consultapets.html')

@app.route('/api/pets', methods=['GET'])
def get_pets():
    db_connection = pyodbc.connect(conn_string)
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM Pets')
    pets = cursor.fetchall()
    db_connection.close()

    return jsonify([{
        'id_pet': row[0], 
        'nome_pet': row[1],       
        'especie': row[2],       
        'idade': row[3],         
        'raca': row[4],
        'observacoes': row[5],
        'id_cliente': row[6]     
    } for row in pets])




if __name__ == '__main__':
    app.run(debug=True)