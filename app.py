from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


# Define a route and its handler
@app.route('/')
def hello():
    return render_template('home.html')


# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
