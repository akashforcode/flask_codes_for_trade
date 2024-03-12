from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def function1():
    # This is the first function you want to execute
    return "Function 1 executed!"

def function2():
    # This is the second function you want to execute
    return "Function 2 executed!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_function1', methods=['POST'])
def execute_function1():
    if request.method == 'POST':
        result = function1()
        return jsonify({'result': result})

@app.route('/execute_function2', methods=['POST'])
def execute_function2():
    if request.method == 'POST':
        result = function2()
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
