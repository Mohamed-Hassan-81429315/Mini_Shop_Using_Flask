from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session

# Valid user credentials
valid_user = {
    "username": "admin",
    "password": "1234"
}

# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Login page
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == valid_user['username'] and password == valid_user['password']:
            session['logged_in'] = True
            session['username'] = username
            # Redirect to profile page after login
            return redirect(url_for('profile'))
        else:
            error = 'Invalid username or password!'
            return render_template('login.html', error=error)
    
    # GET request shows the login page
    return render_template('login.html')


# Profile page
@app.route('/profile')
def profile():
    if 'logged_in' in session and session['logged_in'] == True:
        username = session.get('username')
        return render_template('profile.html', username=username)
    else:
        # If not logged in, redirect to login page
        return redirect(url_for('login'))


# Products page (optional)
@app.route('/products')
def products():
    return render_template('template/index.html')


# Logout route (optional, for completeness)
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)