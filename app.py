from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Customers')
def customers():
    return render_template('cutomers.html')

@app.route('/Orders')
def orders():
    return render_template('orders.html')
if __name__ == '__main__':
    app.run(debug=True)