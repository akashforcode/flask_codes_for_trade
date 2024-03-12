from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_title = request.form['input_title']
        combo1_value = request.form['combo1']
        combo2_value = request.form['combo2']
        dynamic_display = request.form['dynamic_display']
        return render_template('index.html', input_title=input_title, combo1_value=combo1_value, combo2_value=combo2_value, dynamic_display=dynamic_display)
"    return render_template('index.html')"


@app.route('/date_time_display')
def date_time_display():
    # Get current date and time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('date_time_display.html', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
