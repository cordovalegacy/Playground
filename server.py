from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'URL endpoint should be /play'

@app.route('/play/')
def boxes_level_1():
    return render_template('boxes.html', num=3, color="blue")

@app.route('/play/<int:num>')
def boxes_level_2(num):
    return render_template('boxes.html', num=num, color="blue")

@app.route('/play/<int:num>/<color>')
def boxes_level_3(num, color):
    return render_template('boxes.html', num=num, color=color)

if __name__=='__main__':
    app.run(debug=True)

#http://localhost:5000/