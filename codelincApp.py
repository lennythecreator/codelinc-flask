from flask import Flask, render_template, request, redirect

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

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/Tracker.html')
def tracking():
    return render_template('Tracker.html')

@app.route('/Achivements.html')
def ach():
    return render_template('Achivements.html')



def method_name():
    pass
@app.route("/post_questionaRe",methods=['POST'])
def Post_Questionare():
    if request.method== 'POST':
        print(request.form['name'])
        print(request.form['ME'])
        print(request.form['MI'])
        print(request.form['GOAL'])
        #x= request.form['Questions']
        return redirect(f"/Dashboard/{request.form['name']}/{request.form['MI']}/{request.form['ME']}/{request.form['GOAL']}")
        return render_template(f"profile/{request.form['name']}{request.form['MI']}/{request.form['ME']}/{request.form['GOAL']}")
    pass

@app.route("/Dashboard/<name>/<MI>/<ME>/<GOAL>")
def Dashboard_values(name,MI,ME,GOAL):
   
    #user = request.args.get(name=name,MI=MI,ME=ME,GOAL=GOAL)
    return render_template('profile.html')
if __name__ == '__main__':
    app.run(debug=True)
