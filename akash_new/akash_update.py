from flask import Flask, render_template, request

app = Flask(__name__)

xx = 47500  # Initial value for xx
strikevalue = ""


def update():
    global xx
    global strikevalue
    try:
        xx = int(strikevalue)  # Convert to int if needed
        print("Updated xx:", xx)
    except ValueError:
        print("Invalid input! Could not update xx.")


@app.route('/process_strikevalue', methods=['POST'])
def process_strikevalue():
    global strikevalue  # Declare strikevalue as global
    strikevalue = request.form['strikevalue']
    update()  # Call the update function after the value is assigned
    result = f"The entered strikevalue is {strikevalue}"
    return result


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', xx=xx)


if __name__ == '__main__':
    app.run(debug=True)
