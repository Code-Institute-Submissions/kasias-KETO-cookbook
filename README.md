<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1601467758/Logo/salmon_clipart__vyx2yu.png" width="100" height="100" alt="Thank you for visiting my Readme"></p>

<hr>

![](wireframes/screens.png)



# [Salmon of Wisdom, the keto cookbook](https://keto-cookbook.herokuapp.com/)<hr>

[![Salmon of Wisdom on Heroku](https://img.shields.io/badge/Deployed%20on%20Heroku-Salmon%20of%20Wisdom-5D4E68)](https://keto-cookbook.herokuapp.com/) 





In the ever evolving world of different diets, the Food Pyramid as we know it no longer applies for most people. Many diets would at this stage have eliminated certain contents of the pyramid, in Keto's case that pyramid has been literally turned up-side-down. This website was developed to assist those who are embarking on their lifestyle change as well as those who are looking for some inspiration to their existing journey.

## Table of Contents
* [UX](#ux)
  * [User Stories](#user-stories)
  * [Design](#design)
  * [Wireframes](#wireframes)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Defensive Design](#defensive-design)
  * [Features Testing](#features-testing)
  * [Defensive Design Testing](#defensive-design-testing)
* [Deployment](#deployment)
* [Credits and References](#credits)





# UX<hr>
 
The theme of this page is cooking, and there are various types of users this page may appeal to:

*User type 1: Person interested in changing their lifestyle and considering starting KETO*

*User type 2: Those already practicing the KETO lifestyle and diet, but looking for inspiration for daily menus*




## User Stories<hr>

#### Guest User

- As a guest user of this website I want to just browse - I expect this site to have some content available for me
- As a guest user I want to know what the website is about when I am visiting first time
- As a guest user I want to be able to access, search and share recipes
- As a guest user I want to be able to register and log in easily
- As a guest user I want to be able to check out Social Networks of this website
- As a guest user I want to be able to visit some recommended by this website shops

#### Registered User

- As a registered user I want to be able to get a confirmation every time I log in
- As a registered user I want to be able to add recipes
- As a registered user I want to be able to search recipes
- As a registered user I want to be able to delete recipes I have added
- As a registered user I want to be able to store my information in a dedicated profile
- As a registered user I want to be able to upload my profile picture
- As a registered user I want to be able to be able to share my success within my profile
- As a registered user I want to be able to see other users profiles and check out their achievements
- As a registered user I want to be able to add my own milestones to motivate myself and others
- As a registered user I want to be able to delete my profile when I am no longer interested in being part of this group

[Back to top](#table-of-contents)

## Design<hr>
#### :framed_picture: Framework
- Materialize
- jQuery
- Flask
####  :rainbow: Color Scheme
I opted for a very calm, minimalistic color scheme. Various shades of purple and gray, to ensure the page is not too busy

<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1602675799/AdobeColor-Salmon_of_Wisdom_yryooh.jpg" alt="Salmon logo"></p>

#### :bowtie: Icons
On this project I have used Font Awesome icons. As well as that, I have chosen icon from the web to illustrate the Instructions (Method) of cooking on both, Add Recipe and Edit Recipe form.
<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1600807724/Logo/chef_rbminz.png" width="70" height="70" alt="chef"></p>

#### :abc: Typography
- Montserrat - used to style main headings and buttons as well as a secondary font within the logo
- Poppins - used as a secondary logo for paragraphs within the website
- OnceSignature - utilised while designing the main logo for the website.
<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1601398907/Logo/salmon_of_wisdom_tr_bwxbu3.png" alt="Typography"></p>

## Wireframes<hr>
<details><summary>Base Template</summary>
 
![](wireframes/base.jpg)
</details>
<br>
<details><summary>Registered User View Template</summary>
 
![](wireframes/reg_base.jpg)
</details>
<br>
<details><summary>About Keto</summary>
 
![](wireframes/about.jpg)
</details>
<br>
<details><summary>All Recipes</summary>
 
![](wireframes/all_recipes.jpg)
</details>
<br>
<details><summary>Recipe</summary>
 
![](wireframes/recipe.jpg)
</details>
<br>
<details><summary>Register</summary>
  
![](wireframes/register.jpg)

</details>
<br>
<details><summary>Login</summary>
 
![](wireframes/login.jpg)
</details>
<br>
<details><summary>Profile</summary>
 
![](wireframes/profile.jpg)
</details>
<br>
<details><summary>Add Recipe</summary>
 
![](wireframes/add_recipe.jpg)
</details>
<br>
<details><summary>Members Zone</summary>
 
![](wireframes/members.jpg)
</details>

[Back to top](#table-of-contents)

# Features<hr>


## Existing Features <hr>

***Visible to all users***
### About Keto
This section is introducing the user to what the page is all about, and it's the Keto diet. The About section is answering to the assumption that not everyone visiting this page will know what Keto is, and if they do, they might need more information about it. The About section delivers this information
### All Recipes
This is the main highlight of the page, it contains the selection of recipes, which combine both recipes added by the users as well as those by the administrators.
### Recipe
From All Recipes the user will navigate their way to the Recipe by clicking on the "Cook" button.
### Share Recipe
On the Recipe card there is an option to choose some networks that this recipe can be shared to. There are few defaults like Facebook, Email or WhatsApp but the user can also click on the plus sign to choose other channels.
### Login
The option to Login is visible to all users, however, only those registered can access it.
### Register
The option of registering is visible to all users, however, only usernames that do not yet exist in the database can be registered via this route.

***Accessible only by registered user***
### Profile
This is the page that will welcome a registered user who has just logged onto the site. The layout is very simplistic, a profile photograph with username and the achievement underneath it. This is followed by About section, which allows this registered user tell few words about themselves. 
### Add Milestone
A diary-like feature, which lets the user to record their progress directly from their profile. These milestones are to motivate them and others that might visit their profile. The milestones are public and visible to all users.
### Edit Profile
While on the main Wise Zone page, the session user can access profiles of others, plus additional options for their own profile. One of those options is to edit the profile. This gives the session user the opportunity to amend anything in their profile. Since this is a dieting page, the objectives or achievements are subject to amendments.
### Delete Profile
The other option accessible to the session user is the deletion of the profile. This would be possible once the user decides themselves that they no longer wish to be part of this website. Upon clicking the delete button a modal pops up to inform of the final nature of this action. Once the session user clicks "OK", the profile is removed from database, session cookie removed from the browser and the user is redirected to the Register page.
### Wise Zone
This page contains a selection of registered users. Anyone can check out their profiles and see what objectives others are headed towards or achievements reached. From here any user can check out others profiles, the session user can access more options related to their own profile, as addressed in detail above.
### Add Recipe and Edit Recipe
These are available to the users, for they might want to either add their own favourite creations or note down recipes found in other sources. 
### Delete Recipe
The third button on the recipe cover card is the Delete button. While the creator of that recipe can freely delete it from the database, the modal will pop up first to ensure the user knows this is final and cannot be reversed.

***Accessible only by Administrator***
### Manage Categories
At this time there are three main Categories, however, the page assumes that the Administrator might want to expand on it in the future. Therefore there are three options available here:
- Add Category
- Edit Category
- Delete Category


## Features Left to Implement <hr>
Some future features may include:
- Setting the Diary entries to Private
- Functionality to share videos of own cooking tutorials
- Functionality to contact other members
- Pagination

[Back to top](#table-of-contents)

# Technologies Used<hr>

[![Gitpod](https://img.shields.io/badge/IDE-Gitpod-blue)](https://www.gitpod.io/) Used as my primary IDE for coding<br>
[![Github](https://img.shields.io/badge/Remote%20code-Github-white)](https://github.com/) Remote storing of my code online<br>
[![Photoshop](https://img.shields.io/badge/Photoediting-Photoshop-lightblue)](https://www.adobe.com/ie/products/photoshop.html) to edit the cover photo of the responsive view<br>
[![Goodnotes](https://img.shields.io/badge/Wireframes-Goodnotes-Orange)](https://www.goodnotes.com/) to create Wireframes<br>
[![Procreate](https://img.shields.io/badge/Logo-Procreate-yellowgreen)](https://procreate.art/) to create the main Salmon of Wisdom logo<br>
[![Pixlr.com](https://img.shields.io/badge/Image%20editing-Pixlr-blue)](https://pixlr.com/x/) used to edit the user images<br>
[![Cloudinary](https://img.shields.io/badge/Cloud%20image%20storing-Cloudinary-0F4E97)](https://cloudinary.com/) used to store my images<br>


[![HTML](https://img.shields.io/badge/Mark%20up%20text-HTML-yellow)](https://www.w3schools.com/html/html_intro.asp) base for markup text<br>
[![CSS](https://img.shields.io/badge/Styling-CSS-blueviolet)](https://www.w3schools.com/css/) base for cascading styles<br>
[![jQuery](https://img.shields.io/badge/JS%20Functionality-jQuery-darkgreen)](https://jquery.com/) used as the JS functionality<br>
[![Materialize](https://img.shields.io/badge/Design%20Framework-Materialize-%23F5A4A7)](https://materializecss.com/) used as the overall design framework<br>

[![Flask](https://img.shields.io/badge/Microframework-Flask-%238B0000)](https://shields.io/) used as a microframework<br>
[![Jinja](https://img.shields.io/badge/Templating%20with%20Flask-Jinja-%23FF6347)](https://shields.io/) for templating with Flask<br>
[![Werkzeug](https://img.shields.io/badge/Password%20Hashing-Werkzeug-%09%23FFFF00)](https://werkzeug.palletsprojects.com/en/1.0.x/) password hashing, authentication and authorisation<br>
[![Shields](https://img.shields.io/badge/Readme%20Badges-Shields-lightgrey)](https://shields.io/) to create a badge<br>

[![Heroku](https://img.shields.io/badge/App%20Hosting-Heroku-%237B68EE)](https://www.heroku.com/home) used for app hosting<br>
[![Python](https://img.shields.io/badge/Back%20end%20programming-Python-%09%23008000)](https://shields.io/) to create a badge<br>
[![MongoDB Atlas](https://img.shields.io/badge/Cloud%20Database-MongoDB%20Atlas-%09%23006400)](https://shields.io/) to create a badge<br>

[![W3C HTML Validator](https://img.shields.io/badge/HTML%20Validator-W3C%20HTML%20Validator-red)](https://validator.w3.org/) to validate HTML<br>
[![W3C CSS Validator](https://img.shields.io/badge/CSS%20Validator-W3C%20CSS%20Validator-darkred)](https://jigsaw.w3.org/css-validator/) to validate CSS code<br>
[![Pep8 Online](https://img.shields.io/badge/Python%20Validator-PEP8%20online-white)](http://pep8online.com/) to validate Python code<br>
[![JShint](https://img.shields.io/badge/JS%2FjQuery%20Validator-JSHint-%23008e94)](https://jshint.com/) to validate JavaScript/jQuery<br>

[Back to top](#table-of-contents)

# Defensive Design<hr>

## Features Testing<hr>

***Profile***<br>
**Logging in (applicable to a Session User)**<br>
- If Registered, click on the Login button on the navbar
- Is the Login form rendered?
- Submit an empty form, does the system come back with an error to fill in the fields?
- Fill in less than five characters and submit, does the system come back with a message to match the requested format?
- Fill in the username and password and submit, does it render the correct profile?
- Are all details provided at Registration displayed?
- Does Milestone dropdown render correctly?

**Registering an Account**<br>
- Click on Register link in the navbar
- Does it render the Registration form?
- Fill out all details
- Click on the Register button
- Does it bring to the Profile page?
- Does the Flash message confirm registration succeeded?
- Are all details entered onto the form render correctly?

**Adding a Milestone (applicable to a Session User)**<br>
- Go to the Profile section
- Scroll down to the first accordion
- Click on the "Add New" button
- Form to Add Milestone should render
- The Date entry should render a Datepicker
- All fields are compulsory
- Add details and "Save"
- The Milestone should now be visible within the first accordion in Profile

**Editing an Account (applicable to a Session User)**<br>
- Go to the Profile section
- Click on the Edit button
- Enter details to amend
- Click on Save
- Are details successfully amended

**Deleting an Account (applicable to a Session User)**<br>
- Go to the Profile section
- Click on the Delete button
- Does the modal pop up to inform of finality of this action?
- Does the flash message pop up to confirm deletion?
- Is the template rendered that for Registering form
- Has the profile been deleted?


***Recipe***<br>
**Creating a Recipe (applicable to a Session User)**<br>
[**C** in CRUD (Creating)]
- Click on the Add Recipe option in the navbar
- Does the Add Recipe form render?
- Try submitting empty form, does the system come back with an error?
- Fill out all of the required details, click Add Recipe
- Does it render the All Recipes page?
- Does the flash message confirm adding of the recipe?

**Viewing a Recipe**<br>
[**R** in CRUD (Reading/Viewing)]
- Scroll down to where that recipe is and click on Cook
- Does the Recipe page render correctly?
- Does the image uploaded as url render correctly?
- Click on the Share button underneath the Created By, does the modal with social networks pop up?
- Cancel out of the modal, does it work?

**Editing a Recipe (applicable to a Session User)**<br>
[**U** in CRUD (Updating)]
###### Method 1:
- Go to the Recipes section
- Choose a recipe that was created by Session User
- Click on the Edit button
- Does the Edit Recipe form renders correctly?
- Change anything about the recipe and click on save
- Does the information entered updates correctly on the Recipe card?
###### Method 2
- Go to Session User Profile section
- Scroll down to the second accordion
- Open recipe for editing
- Click "Cook"
- You are now in the Recipe page, scroll down to the buttons
- Click on Edit button
- Enter details
- Click Save

**Deleting a Recipe (applicable to a Session User)**<br>
[**D** in CRUD (Deleting)]
###### Method 1:
- Go to the Recipes section
- Choose a recipe that was created by Session User
- Click on the Delete button
- Does the modal pop up to ask if you are sure?
- Click on Cancel button to exit the process
- Click on Delete button to proceed with deletion
###### Method 2
- Go to Session User Profile section
- Scroll down to the second accordion
- Open recipe for editing
- Click "Cook"
- You are now in the Recipe page, scroll down to the buttons
- Click on the Delete button
- Does the modal pop up to ask if you are sure?
- Click on Cancel button to exit the process
- Click on Delete button to proceed with deletion

[Back to top](#table-of-contents)

## Defensive Design Testing<hr>

**Wrong password entered when logging in** <br>
:heavy_check_mark: returns flash "Incorrect Username and/or Password" to ensure that the non-registered user does not guess one or the other if the incorrect entry is provided.<br>
**Duplicate username registration attempt** <br>
:heavy_check_mark: returns flash "Username already exists<br>
**Wrong username entered when logging in** <br>
:heavy_check_mark: returns flash "Incorrect Username and/or Password" to ensure that the non-registered user does not guess one or the other if the incorrect entry is provided.<br>
**Attempt to access "/add_category" by non Administrator** <br>
link for testing: ***http://keto-cookbook.herokuapp.com/add_category***<br> 
:heavy_check_mark: renders About page if user in session but user is not "Administrator"
:heavy_check_mark: renders Login page if user is not in session<br>
**Attempt to access "/get_categories" by non Administrator** <br>
link for testing: ***http://keto-cookbook.herokuapp.com/get_categories***<br>
:heavy_check_mark: renders About page if user in session but user is not "Administrator"
:heavy_check_mark: renders Login page if user is not in session<br>
**Attempt to access "/edit_category/category_id" by non Administrator**<br>
link for testing: ***http://keto-cookbook.herokuapp.com/edit_category/5f6a00eadda48a7a60562ada (category_id as example)***<br>
:heavy_check_mark: renders About page if user in session but user is not "Administrator"
:heavy_check_mark: renders Login page if user is not in session<br>
**Attempt to access "/delete_category/category_id" by non Administrator**<br>
link for testing: ***http://keto-cookbook.herokuapp.com/delete_category/5f6a00eadda48a7a60562ada (category_id as example)***<br>
:heavy_check_mark: renders About page if user in session but user is not "Administrator"
:heavy_check_mark: renders Login page if user is not in session<br>
**As non-logged on user attempt to access "/edit_profile/username"** <br>
link for testing: ***http://keto-cookbook.herokuapp.com/edit_profile/marie***<br>
:heavy_check_mark: renders Login page if user is not in session<br><br>
**As non-logged on user attempt to access "/profile/username"** Login<br>
link for testing: ***http://keto-cookbook.herokuapp.com/profile/marie***<br>
:heavy_check_mark: renders Login page if user is not in session<br><br>
**As non-logged on user attempt to access "/wisemen"** Login<br>
link for testing: ***http://keto-cookbook.herokuapp.com/wisemen***<br>
:heavy_check_mark: renders Login page if user is not in session<br><br>
**As non-logged on user attempt to access "/add_recipe"**<br>
link for testing: ***http://keto-cookbook.herokuapp.com/add_recipe***<br>
:heavy_check_mark: renders Login page if user is not in session<br><br>
**As non-logged on user attempt to access "/edit_recipe"**<br>
link for testing: ***http://keto-cookbook.herokuapp.com/edit_recipe/5f844c38884d26d0d8bd3aac%29***<br>
:heavy_check_mark:renders Login page if user is not in session<br><br>


### *Guest User*
#### As a guest user of this website I want to just browse - I expect this site to have some content available for me
- User that is not logged on nor registered, upon accessing the page for the first or each consecutive time, will first and foremost see the About site. On that site user will  access the opportunity of gaining more information about what the page is about and what the Keto lifestyle is.
#### As a guest user I want to know what the website is about when I am visiting first time
- The About page is what user will see first and therefore they will know whether this site is of their interest or not
#### As a guest user I want to be able to access, search and share recipes
- The All Recipes page is visible to all users, be it registered or not. Once on that page, they can take advantage of viewing and sharing the recipes.
#### As a guest user I want to be able to register and log in easily
- Once user decides they want a full access to the website, they can easily navigate to the Register button from the Navbar
#### As a guest user I want to be able to check out Social Networks of this website
- The footer contains all links to the Social Media<br><br>

### *Logged in User*
#### As a registered user I want to be able to get a confirmation every time I log in
- A flash message always pops up to confirm the user has successfully logged in
#### As a registered user I want to be able to add and edit recipes
- The option of Adding a new Recipe is easily accessible from the Navbar
#### As a registered user I want to be able to search recipes
- The searchbar is available on top of the All Recipes page, for the ease of search, keywords are included within each recipe, to ensure the user gets as many results to their search as possible
#### As a registered user I want to be able to delete recipes I have added
- The button enabling session user the deleting of their recipe is only visible to the user that created the recipe. This gives user the freedom of removing recipes they no longer wish to have publicised
#### As a registered user I want to be able to store my information in a dedicated profile
- Once User registers/logs in, they are being redirected to their own Profile page, which can be customised
#### As a registered user I want to be able to upload my profile picture
- One of methods of customisation is that the user can have their profile photo displayed on their profile as well as on the Members Zone page. 
#### As a registered user I want to be able to be able to share my success within my profile
- A feature of Adding Milestones enables user to share their little and big successes. These are public, so can serve as a motivating factor to other users, that visit profiles or one another
#### As a registered user I want to be able to see other users profiles and check out their achievements
- From Wise Zone the session user may check out the profiles of other users. This can server as source of inspiration or motivation
#### As a registered user I want to be able to delete my profile when I am no longer interested in being part of this group
- From Wise Zone the session user may choose to delete their own profile. The action of profile deletion is preceded by a modal which ensures that the user realises the finality of that action.<br><br>

[Back to top](#table-of-contents)

## Deployment<hr>
***Requirements:***
- Python3 to run your application
- PIP to install all app requirements
- IDE of your choice - I used Gitpod
- A MongoDB Atlas account for database development


## Local Deployment<hr>
- Navigate to the Salmon of Wisdom <a href="https://github.com/bezebee/kasias-KETO-cookbook">repository</a>
- Click on the green "Code" button
- Copy the <a href="https://github.com/bezebee/kasias-KETO-cookbook.git">link</a>
- Using your terminal, type "git clone" followed by that link
- Operate within a virtual environment as widely recommended. The instructions will vary depending on your operating system, so refer to <a href="https://docs.python.org/3/library/venv.html">Python Documentation</a>

- Create a file called ".flaskenv" and add the following:
```
 FLASK_APP=run.py
 FLASK_ENV=development
 ```
- Install the required modules with the command `pip -r requirements.txt`
- Set up a free account on MongoDB and create a new Database called **keto_cookbook**
- The following are the collections in that Database:
***categories***
```
_id:<ObjectId>
category_name:<string>
```
***milestones***
```
_id:<ObjectId>
milestone_name:<string>
milestone_date:<string>
milestone_description:<string>
created_by:<string>
```
***recipes***
```
_id:<ObjectId>
category_name:<string>
recipe_name:<string>
recipe_image:<string>
ingredients_list:<string>
method:<string>
preparation_time:<string>
difficulty:<string>
created_by:<string>
keywords:<string>
```
***users***
```
username:<string>
password:<string>
on_keto_since:<string>
personal_success:<string>
username_image:<string>
about:<string>
```
- You should now be able to run this application locally by typing `flask run`
- The website will be available at `http://127.0.0.1:5000`

## Deploying on Heroku<hr>
- Create a requirements.txt file by typing `pip3 freeze --local > requirements.txt` into the terminal line
- Create a Procfile by typing `echo web: python app.py > Procfile`.
- Add, commit and push these changes to Github
- Navigate to the Heroku website
- Create new app and give it a unique name
- Choose region that is closest to you
- Go to the Deploy tab and choose Github
- Seach for the correct repository and connect
- Go to Heroku Settings and navigate to Config Vars
- Set the following:<br>
```
IP = 0.0.0.0
MONGO_DBNAME = [Name of MongoDB] <br>
MONGO_URI = mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
PORT = 5000
SECRET_KEY = [Secret key]
```
<br>
- Go to the Deploy tab and Deploy Branch, ensuring that master branch is selected

[Back to top](#table-of-contents)

# Credits<hr>

## Content<hr>
<a href="https://www.dietdoctor.com/">DietDoctor</a> - All recipes<br>
The Task Manager Miniproject by <a href="https://codeinstitute.net/">Code Institute</a> used as an excellent source of information on environment, database and templating

## Media<hr>
<a href="https://www.dietdoctor.com/">DietDoctor</a> - All recipe images<br>
<a href="https://www.pexels.com/">Pexels</a> - Profile photos and some images on the About page

## Acknowledgements<hr>
<a href="https://github.com/TravelTimN">Tim Nelson</a> - for helpful and timely guidance, thanks to Tim I learned a great deal about good fundamentals of templating. I will be exploring the Python and Flask path, among others, but this one will be with greatest enthusiasm. I am so grateful.<br>
<a href="https://github.com/precious-ijege">Precious Ijege</a> - for mentorship and honest critique<br>
<a href="https://github.com/Eventyret">Evertyred Mentor</a> - for taking the time to introduce me to a <a href="https://en.wikipedia.org/wiki/Fibonacci_scale_(agile)">Fibonacci Sequence</a> and its benefit in project planning and management<br>
<a href="https://github.com/NgiapPuoyKoh">Ngiap</a> - for continuous moral support and feedbacks on my project<br><hr>


<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1601467758/Logo/salmon_clipart__vyx2yu.png" width="100" height="100" alt="Thank you for visiting my Readme"></p>

[Back to top](#table-of-contents)

