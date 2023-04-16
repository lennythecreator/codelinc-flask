from flask import Flask, render_template, request

app= Flask(__name__,static_folder='static')


@app.route('/')
@app.route('/hello')
@app.route('/hello/<user>')
def hello_world(user=None):
    user = user or 'Shalabh'
    return render_template('index.html', user=user)
    return redirect

@app.route('/Landing.html')
def Landing():
    return render_template('Landing.html')

@app.route('/Challenges.html')
def chal():
    return render_template('Challenges.html')

@app.route('/Calulator.html')
def calc():
    return render_template('Calulator.html')

@app.route('/Tracker.html')
def tracking():
    return render_template('Tracker.html')

@app.route('/Achivements.html')
def ach():
    return render_template('Achivements.html')



def method_name():
    pass
"""@app.route("post_questionare",methods=['POST'])
def Post_Questionare():
    if request.method== 'POST':
        x= request.form['q']
        #return render_template(f"Dashboard/{name}/{MI}/{ME}/{GOAL}")
    pass

@app.route("Dashboard",methods=['GET'])
def Dashboard_values():
    pass
"""
if __name__ == '__main__':
    app.run(debug=True)
