from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_logged_in = True
    nome = 'breno'
    letras = list(nome.capitalize())
    pup_dict = {'pup_name': 'Sammy'}
    puppies = ['Fluffy', 'Rufus', 'Spike']
    return render_template('basic.html', nome=nome, letras=letras, pup_dict=pup_dict, puppies=puppies, user_logged_in=user_logged_in)

if __name__ == "__main__":
    app.run(debug=True)