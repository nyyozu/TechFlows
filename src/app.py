from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__, template_folder='templates')
app.secret_key = 'f3b1a2c4d5e6f7a8b9c0d1e2f3a4b5c6'

USUARIO_VALIDO = "admin"
SENHA_VALIDA = "1234"


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        if usuario == USUARIO_VALIDO and senha == SENHA_VALIDA:
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Usuário ou senha inválidos.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)