import flask
from flask import *
from functools import wraps
from yummy_classes import User

app = Flask(__name__)

app.secret_key = 'alvTarino299'
users = {}
user = User()

@app.route('/')  #Route to enable user registration
@app.route('/signup',methods=['GET','POST'])
def signup():

    error = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        flash("You have succesfully been registered {} {}".format(name, password))

        if name and password:
            users[email] = password
            return redirect(url_for('login'))
    return render_template('signup.html', error=error)

#@app.route('/')    #Route enables user to login after registration
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] not in users.keys() or request.form['password'] not in users.values():
            error = 'Invalid Credentials'
        else:
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

    return render_template("signup.html")

@app.route('/login')#, methods=['POST'])
def after_login():
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for('login'))
    return wrap

    return render_template("login.html")
"""
@app.route("/index")
def index():
    #@app.route('/index')
    @after_login
    #def index():

        #Route to main page after login

    recipe_new = user.recipes
    return render_template('index.html', recipe_new=recipe_new)

    #return render_template("index.html")
    #return redirect(url_for('login'))
"""
@app.route('/add_item/<recipe_name>', methods=['GET', 'POST'])  #Route enables user to add recipe item
#@after_login
def add_item(recipe_name):

    error = None
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        items = request.form['items']
        flash("You have succesfully added your recipe {} {}".format(recipe_name, items))

        if recipe_name and items:
            user.update_recipeItem(recipe_name, items)
            return redirect(url_for('item', recipe_name=recipe_name))
    return render_template('add_item.html', recipe_name=recipe_name, error=error)

@app.route('/logout')   #Route logs out user from the site
def logout():
    session.pop('logged_in', None)
    flash('You are Logged Out !')
    return redirect(url_for('login'))

@app.route('/item/<recipe_name>')
#@after_login
def item(recipe_name):
    items = user.read_recipe(recipe_name)
    return render_template('item.html', items=items, recipe_name=recipe_name)

@app.route('/updatelistitem/<recipe_name>/<item_name>', methods=['GET', 'POST'])      #Route enables user to edit recipe item
#@after_login
def updatelistitem(recipe_name, item_name):
    error = None
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        item_name = request.form['item_name']
        new_name = request.form['new_item_name']
        flash("You have succesfully added registered {} {} {}".format(recipe_name, item_name, new_name))

        if recipe_name and item_name:
            user.update_recipe(recipe_name, item_name, new_name)
            return redirect(url_for('item', recipe_name=recipe_name, item_name=item_name))
    return render_template('updatelistitem.html', recipe_name=recipe_name, item_name=item_name)


@app.route('/delete_list/<recipe_name>') #Route enables user to delete recipe
#@after_login
def delete_list(recipe_name):
    user.delete_recipe(recipe_name)
    return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)
