from flask import Flask, render_template, request

app = Flask(__name__)

# Define the options for the dropdown
options = ['Option 1', 'Option 2', 'Option 3']

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_option = None

    if request.method == 'POST':
        selected_option = request.form['option']

    return render_template('index.html', options=options, selected_option=selected_option)

if __name__ == '__main__':
    app.run(debug=True)
