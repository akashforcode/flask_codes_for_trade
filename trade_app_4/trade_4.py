from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handling form submission here
        pass  # Add your logic here for handling form submission
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template('index.html', current_time=current_time)



@app.route('/start')
def start():
    # Your code to handle start button action goes here
    return "Start Button Clicked!"



if __name__ == '__main__':
    app.run(debug=True)