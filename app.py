from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main-page.html')

@app.route('/home')
def home():
    return render_template('index-final.html')

@app.route('/data')
def data():
    return render_template('reviews-final.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/about')
def dashboards():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)