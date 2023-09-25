from flask import Flask ,url_for , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_page')
def about():
    return '<h1>This is About page.</h1>'

@app.route('/contact_page')
def contact():
    return '<h1>This is Contact page.</h1>'

if __name__ == "__main__":
    app.run(host='0.0.0.0')