from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    key = request.form['name']
    return f'Запись {key}'


if __name__ == '__main__':
    app.run(debug=True)