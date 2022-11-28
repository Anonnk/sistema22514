from flask import Flask,render_template

app = Flask (__name__)


@app.route('/')
def index():

    return render_template('Empleados/index.html')

@app.route('/christian')
def christian():

    return render_template ('empleados/christian.html')


if __name__ == "__main__":

    app.run(debug=True)

    #punto de entrada de la aplicacion, cuando le damos a correr llama a la aplicacion y ejecuta una app tipo flask
