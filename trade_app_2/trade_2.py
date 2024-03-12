from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dynamic_display')
def dynamic_display():
    # Generate and return a random number
    random_number = random.randint(1, 100)
    return render_template('dynamic_display.html', random_number=random_number)

@app.route('/date_time_display')
def date_time_display():
    # Get current date and time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('date_time_display.html', current_time=current_time)

if __name__ == '__main__':5555
app.run(debug=True)