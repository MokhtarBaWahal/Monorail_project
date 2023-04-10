from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    # Implement the signup logic here
    # ...
    return render_template('trip.html')

@app.route('/signup', methods=['POST'])
def login():

    # Implement the login logic here
    # ...
    return render_template('signup.html')

@app.route('/guest', methods=['POST'])
def guest():
    # Implement the guest login logic here
    # ...
    return render_template('trip.html')

if __name__ == '__main__':
    app.run(debug=True)
