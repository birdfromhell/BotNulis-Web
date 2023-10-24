import BotNulis
from flask import Flask, render_template, request, jsonify
from flasgger import Swagger
import time

app = Flask(__name__)
Swagger(app)
waktuFile = time.strftime("%y%m%d-%H%M%S")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/write')
def write():
    # Get the value if exists, else set a default
    text = request.args.get('text', default='')
    pkertas = int(request.args.get('kertas', default='1'))
    pfont = int(request.args.get('font', default='1'))
    header = request.args.get('header', default='')
    tanggal = request.args.get('tanggal', default='')

    if text:  # Check if text is not empty
        bot = BotNulis.BotNulis(text, pkertas, pfont, header, tanggal)
        result = bot.start()
        return jsonify(result)
    else:
        return jsonify({'error': True, 'msg': 'Wajib menambahkan argument text '})


if __name__ == '__main__':
    app.run(debug=True)


