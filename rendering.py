from flask import Flask,session,render_template, request,redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/signup',methods=['GET','POST'])
def signup():
    return render_template("signup.html")

@app.route('/login')#, methods=['POST'])
def login():
    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug = True)
