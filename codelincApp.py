from flask import Flask, render_template, request

app= Flask(__name__)


@app.route('/')
@app.route('/hello')
@app.route('/hello/<user>')
def hello_world(user=None):
    user = user or 'Shalabh'
    return render_template('index.html', user=user)

@app.route('/profile/<profile>')
def profile(profile=None):
    profile = profile or 'Shalabh'
    return render_template('profile.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)
