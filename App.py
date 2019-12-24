from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
    return 'Hola Mundo Desde Flask'

@app.route('/add_contact')
def add_contact():
    return 'Añadir Contacto'

if __name__=='__main__':
    app.run(port=3000,debug=True)