from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    nome = 'breno'
    letras = list(nome.capitalize())
    pup_dict = {'pup_name': 'Sammy'}
    return render_template('basic.html', nome=nome, letras=letras, pup_dict=pup_dict)

if __name__ == "__main__":
    app.run(debug=True)