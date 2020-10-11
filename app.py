import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ------HOME----- #

@app.route("/")
@app.route("/about")
def about():
    return render_template("about.html")

# -----SHOP-----#


@app.route("/shop")
def shop():
    return render_template("shop.html")

# ------PROFILE-----#


# register account
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "on_keto_since": request.form.get("on_keto_since"),
            "personal_success": request.form.get("personal_success"),
            "username_image": request.form.get("username_image"),
            "about": request.form.get("about"),
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure the password matches users input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from database
    user = mongo.db.users.find_one({"username": username.lower()})
    milestones = mongo.db.milestones.find({"created_by": username.lower()})
    recipes = list(mongo.db.recipes.find({"username": username.lower()}))

    if "user" in session:
        return render_template(
            "profile.html", user=user, milestones=milestones, recipes=recipes)

    return redirect(url_for("login"))


# edit profile
@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    user = mongo.db.users.find_one({"username": username.lower()})
    if request.method == "POST":
        submit = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "on_keto_since": request.form.get("on_keto_since"),
            "personal_success": request.form.get("personal_success"),
            "username_image": request.form.get("username_image"),
            "about": request.form.get("about"),
        }
        mongo.db.users.update({"username": username.lower()}, submit)
        flash("Profile updated")

    return render_template("edit_profile.html", user=user)


# delete profile
@app.route("/delete_profile/<username>")
def delete_profile(username):
    mongo.db.users.remove({"username": username.lower()})
    flash("Profile deleted")
    session.pop("user")

    return redirect(url_for("register"))


# milestones
@app.route("/milestones")
def milestones():
    milestones = list(mongo.db.milestones.find())
    return render_template("milestones.html", milestones=milestones)


# add milestone
@app.route("/add_milestone", methods=["GET", "POST"])
def add_milestone():

    if request.method == "POST":
        milestone = {
            "milestone_name": request.form.get("milestone_name"),
            "milestone_date": request.form.get("milestone_date"),
            "milestone_description": request.form.get("milestone_description"),
            "created_by": session["user"]
        }
        mongo.db.milestones.insert_one(milestone)
        flash("Milestone Successfully added")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("add_milestone.html")


# all users
@app.route("/wisemen")
def wisemen():
    users = list(mongo.db.users.find())

    if "user" in session:
        return render_template("wisemen.html", users=users)

    return redirect(url_for("login"))


# logout
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# ------RECIPES------ #


# all recipes
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# search recipe
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# single recipe
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipe)


# add recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_name": request.form.get("recipe_name"),
            "ingredients_list": request.form.get("ingredients_list"),
            "method": request.form.get("method"),
            "preparation_time": request.form.get("preparation_time"),
            "difficulty": request.form.get("difficulty"),
            "keywords": request.form.get("keywords"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find()
    return render_template("add_recipe.html", categories=categories)


# edit recipe
@app.route("/edit_recipe/<recipe_id>)", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_name": request.form.get("recipe_name"),
            "ingredients_list": request.form.get("ingredients_list"),
            "method": request.form.get("method"),
            "preparation_time": request.form.get("preparation_time"),
            "difficulty": request.form.get("difficulty"),
            "keywords": request.form.get("keywords"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# delete recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully removed")
    return redirect(url_for("get_recipes"))


# get_category
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find())

    if "user" in session:
        user = session["user"].lower()
        if user == "administrator":
            return render_template("categories.html", categories=categories)
        else:
            return redirect(url_for("about"))

    else:
        return redirect(url_for("login"))


# add_category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
    if "user" in session:
        user = session["user"].lower()
        if user == "administrator":
            return render_template("add_category.html")
        else:
            return redirect(url_for("about"))
    else:
        return redirect(url_for("login"))


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category successfully updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    if "user" in session:
        user = session["user"].lower()
        if user == "administrator":
            return render_template("edit_category.html", category=category)
        else:
            return redirect(url_for("about"))
    else:
        return redirect(url_for("login"))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):

    if "user" in session:
        user = session["user"].lower()
        if user == "administrator":
            mongo.db.categories.remove({"_id": ObjectId(category_id)})
            flash("Category Successfully Deleted")
            return redirect(url_for("get_categories"))
        else:
            return redirect(url_for("about"))
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)