from flask import Flask
app= Flask(__name__)
@app.route('/')
def hola_mundo():
    return 'Hola Mundo!'

@app.route('/dojo')
def responder_dojo():
    return '¡Dojo!'

@app.route('/say/<palabra>')
def say(palabra):
    return f"Hola {palabra}"

@app.route('/repeat/<int:numero>/<string:comentario>')
def repetir(numero,comentario):
    palabra =''
    for i in range(0,numero):
        palabra += f"<p>{comentario}</p>"
    return palabra

if __name__=="__main__":
    app.run(debug=True)