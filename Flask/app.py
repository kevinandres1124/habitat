from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    categorias = ['Dormitorios', 'Salas', 'Cocinas', 'Comedores', 'Oficinas', 'Otros']
    return render_template('index.html', categorias=categorias)


if __name__ == '__main__':
    app.run(debug=True)
