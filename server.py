from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index1.html')

# @app.route('/check')
# def check():
#     return render_template('index.html')

@app.route('/blog')
def blog():
    return 'check me here'