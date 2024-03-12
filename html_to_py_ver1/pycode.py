from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        age = int(request.form['age'])
        
        # Process the data (here, just printing)
        print("Name:", name)
        print("Age:", age)
        
        # You can perform any other operations with the data here
        
        # Redirect back to the form or any other page
        return render_template('result.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
