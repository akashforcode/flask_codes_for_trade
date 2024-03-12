from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
