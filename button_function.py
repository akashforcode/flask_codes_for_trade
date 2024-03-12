from flask import Flask, render_template, request

app = Flask(__name__)

# Define the function that will be executed when the button is clicked
def my_function(button_id):
    return f"Button {button_id} clicked!"

# Define a route to render the HTML page with the buttons
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Button Example</title>
        <style>
            .container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
            }
            .button {
                margin: 10px;
                padding: 10px 20px;
                font-size: 16px;
            }
        </style>
        <script>
            function executeFunction(buttonId) {
                fetch('/execute_function', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ 'button_id': buttonId })
                })
                .then(response => response.text())
                .then(result => {
                    document.getElementById('result').innerHTML = result;
                });
            }
        </script>
    </head>
    <body>
        <h1>Click a button to execute the function</h1>
        <div class="container">
            <button class="button" onclick="executeFunction(1)">Button 1</button>
            <button class="button" onclick="executeFunction(2)">Button 2</button>
            <button class="button" onclick="executeFunction(3)">Button 3</button>
            <button class="button" onclick="executeFunction(4)">Button 4</button>
            <button class="button" onclick="executeFunction(5)">Button 5</button>
            <button class="button" onclick="executeFunction(6)">Button 6</button>
            <button class="button" onclick="executeFunction(7)">Button 7</button>
            <button class="button" onclick="executeFunction(8)">Button 8</button>
            <button class="button" onclick="executeFunction(9)">Button 9</button>
            <button class="button" onclick="executeFunction(10)">Button 10</button>
        </div>
        <div id="result"></div>
    </body>
    </html>
    """

# Define a route to execute the function when a button is clicked
@app.route('/execute_function', methods=['POST'])
def execute_function():
    button_id = int(request.json['button_id'])
    # Call the function with the button ID
    result = my_function(button_id)
    # Return the result
    return result

if __name__ == '__main__':
    app.run(debug=True)
