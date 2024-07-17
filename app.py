from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Define a route and its handler
@app.route('/')
def hello():
    return 'This is HP'


# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
