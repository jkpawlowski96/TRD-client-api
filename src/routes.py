from src import app

@app.route('/help')
def hello_world():
    return 'Hello, World!'