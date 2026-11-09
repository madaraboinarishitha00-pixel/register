
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def func():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    event = request.form['event']
    return render_template('success.html', name=name, event=event)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)
