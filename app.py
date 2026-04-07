from flask import Flask, render_template
import os

app = Flask(__name__)

# Página Inicial
@app.route('/')
def inicio():
    return render_template('inicio.html')

# Página Serviços
@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

# Página Contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

