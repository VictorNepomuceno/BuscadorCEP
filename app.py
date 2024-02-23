from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def obter_cep(cep):
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    if request.method == 'POST':
        cep = request.form['cep']
        data = obter_cep(cep)
        if data is not None:
            return render_template('resultado.html', data=data)
        else:
            return "Algo deu errado ao obter os dados do CEP."

app.run(debug=True)