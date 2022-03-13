from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Playground Practice Assignment'

@app.route('/play/')
def playInit(times =3, color ='blue'):
     return  render_template('index.html',times = times, color = color)

@app.route('/play/<int:times>')
def playTimes(times, color ='blue'):
     return  render_template('index.html',times = times, color = color)

@app.route('/play/<int:times>/<color>')
def play( times, color):
    return render_template('index.html',times = times, color = color)

if __name__ == '__main__':
    app.run(debug=True)
