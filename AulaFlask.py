#Flask versão 0.12.2

from flask import Flask 
from flask import render_template 

app = Flask(__name__)


@app.route('/inicio')
def ola():
    return render_template('lista.html')

app.run()