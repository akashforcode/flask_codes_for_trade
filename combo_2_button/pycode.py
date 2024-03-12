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
        if action == 'Button 1':
            result = f"Processing with Button 1 for {selected_option}"
        elif action == 'Button 2':
            result = f"Processing with Button 2 for {selected_option}"
        else:
            result = "Invalid action"
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
