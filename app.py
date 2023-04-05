from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/breeds')
def breeds():
    return render_template('breeds.html')

@app.route('/behavior')
def behavior():
    return render_template('behavior.html')

@app.route('/care')
def care():
    return render_template('care.html')

@app.route('/products')
def products():
    return render_template('products.html')
if __name__ == '__main__':
    app.run(debug=True)
