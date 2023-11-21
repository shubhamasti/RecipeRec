from flask import Flask, render_template, redirect, url_for, request, session
import mysql.connector as m
from helper import *
from reciperec import *

app = Flask(__name__)
app.secret_key = 'your secret key'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    msg_reg = ''
    if request.method == 'POST':
        # create variables for easy access
        username = request.form['email_id']
        password = request.form['password']

        account = password_check(username, password)

        if account:
            # create session data, we can access this data in other routes
            session['loggedin'] = True
            session['username'] = account

            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password!'
    
    # show the login form with message (if any)
    return render_template('login.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # for new user registration
    msg = ''
    if request.method == 'POST':
        # create variables for easy access
        username = request.form['username']
        pwd = request.form['password']
        veg = request.form['veg']
        allergen_list = request.form['allergen_list']

        account = user_exists(username)

        if account:
            msg = 'Account already exists!'
        else:
            signup_input(username=username, password=pwd, veg=veg, allergen_list=allergen_list)
            msg = 'You have successfully registered!'

            session ['loggedin'] = True
            session ['username'] = username

            return render_template('login.html', msg_reg=msg)
    
    return render_template('register.html', msg=msg)
    

@app.route('/home', methods=['GET', 'POST'])
def home():
    top_recipes = getTopRecipes(10)
    if request.method == "POST":
        try:
            allergen_toggle = request.form.get('allergenToggle', 'off')
            if allergen_toggle == 'on':
                allergen_list = getAllergenList(session['username'])
                top_recipes = getTopRecipesNoAllergen(allergen_list, 10)
                return render_template('home.html', recipes=top_recipes, checked=1)
            else:
                top_recipes = getTopRecipes(10)
                return render_template('home.html', recipes=top_recipes, checked=0)
        except:        
            rec_id = request.form['rec_id']
            return redirect(url_for('recipe', rec_id=rec_id))
    return render_template('home.html', recipes=top_recipes)


@app.route('/recipe_hidden', methods=['GET', 'POST'])
def recipe_hidden():
    rec_id = request.form['rec_id']
    return redirect(url_for('recipe', rec_id=rec_id))

@app.route('/recipe/<rec_id>', methods=['GET', 'POST'])
def recipe(rec_id):
    bookmark_msg = ''
    if request.method == "POST":
        rec_id = request.form['rec_id']
        if checkBookmark(session['username'], rec_id):
            bookmark_msg = 'Recipe is already bookmarked!'
        else:
            rec_id = request.form['rec_id']
            bookmark(session['username'], rec_id)
            bookmark_msg = 'Recipe bookmarked!'

    recipe_info = getRecipeById(int(rec_id))[0]
    ingredients = recipe_info[2].split(',')
    instructions = recipe_info[5].split('.')[:-1]

    return render_template('recipe.html', info=recipe_info, bookmark_msg=bookmark_msg,
                           ingredients=ingredients, instructions=instructions)


@app.route('/bookmarks', methods=['GET', 'POST'])
def bookmarks():
    bookmarks_ids = getBookmarks(session['username'])
    recipe_info = getRecipeInfoById(bookmarks_ids)
    print(recipe_info)

    if request.method == "POST":
        rec_id = request.form['rec_id']
        return redirect(url_for('recipe', rec_id=rec_id))

    return render_template('bookmarks.html', info=recipe_info)


@app.route('/recipe_recommender', methods=['GET', 'POST'])
def recipe_recommender():
    if request.method == "POST":
        recipe_name = request.form['recipe_name']

        ingredient_list = request.form['ingredients_include']
        if ingredient_list == '':
            ingredient_list = []
        else:
            ingredient_list = ingredient_list.split(',')

        ingredient_exclude = request.form['ingredients_exclude']
        if ingredient_exclude == '':
            ingredient_exclude = []
        else:
            ingredient_exclude = ingredient_exclude.split(',')

        cuisine = request.form['cuisine']

        allergen_toggle = request.form.get('allergenToggle', 'off')
        if allergen_toggle == 'on':
            allergen_list = getAllergenList(session['username'])
            checked_allergen = 1
        else:
            allergen_list = []
            checked_allergen = 0

        veg = request.form['veg']

        recipes = getRecipe(cuisine=cuisine, name=recipe_name, veg=veg, ingredient_list=ingredient_list,
                            ingredients_exclude_list=ingredient_exclude, allergen_list=allergen_list)
        
        return render_template('recipe_recommender.html', recipes=recipes, n=20,
                                checked_allergen=checked_allergen)

    return render_template('recipe_recommender.html')


@app.route('/my_profile', methods=['GET', 'POST'])
def my_profile():
    info = getUserInfo(session['username'])
    return render_template('my_profile.html', user_info=info)

@app.route('/my_profile_change_hidden', methods=['GET', 'POST'])
def my_profile_change_hidden():
    if request.method == "POST":
        username = request.form['username']
        diet_pref = request.form['diet_pref']
        allergens = request.form['allergens']

        print(username, diet_pref, allergens)

        if not username:
            username = session['username']
        else:
            updateUsername(session['username'], username)
            session['username'] = username

        updateUserInfo(username, diet_pref, allergens)

        return redirect(url_for('my_profile'))


if __name__ == '__main__':
    app.run(port=8000, debug=True)


session.clear()