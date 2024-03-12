from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    if request.method == 'POST':
        selected_option = request.form['selected_option']
        action = request.form['action']
        result = f"Processing with {action} for {selected_option}"
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
