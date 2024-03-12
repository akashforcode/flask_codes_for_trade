from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_variable', methods=['POST'])
def process_variable():
    variable = request.form['variable']
    print("Input variable:", variable)  # Print input variable to terminal
    # Do something with the variable, for example:
    result = f"The entered variable is {variable}"
    print(variable)
    return result


if __name__ == '__main__':
    app.run(debug=True)
