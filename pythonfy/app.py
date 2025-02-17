from flask import Flask, render_template
from flask.json import jsonify


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

@app.route('/')
def index():
    return '<div> <a href="http://127.0.0.1:5000/callback">Login</a> </div>'

@app.route('/callback')
def callback():
    return jsonify({'message': 'success'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)