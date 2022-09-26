#import Flask
from flask import Flask,render_template,url_for,redirect

# create an instance(app)
app=Flask(__name__)

#Normal Route
@app.route("/")

#define method
def sample():
    return "Welcome to flask"
#dynamic routing
@app.route("/<name>")
def sample2(name):
    return (f'Hello{name}')

    #flask- content passing to template
    @app.route("/template/<name>")
    def sample3(name):
        return render_template('index1.html',name=name)

#flask-redirect
@app-route("/route/template2/<role>")
def sample4(role):
    if role=="guest":
        return redirect(url_for('sample2'))
    else:
        return redirect(url_for('sample3',name=role))
    #list rendering with for tag
    @app.route("/list/rendering")
    def sample5():
        lst=['abc','def','ghi']
        return render_template('index3.html',names=lst)

    if __name__ == "__main__":
        app.run()