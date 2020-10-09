![](wireframes/screens.png)



# [Salmon of Wisdom, the keto cookbook](https://keto-cookbook.herokuapp.com/)<hr>

In the ever evolving world of different diets, the Food Pyramid as we know it no longer applies for most people. Many diets would at this stage have eliminated certain contents of the pyramid, in Keto's case that pyramid has been literally turned up-side-down. This website was developed to assist those who are embarking on their lifestyle change as well as those who are looking for some inspiration to their existing journey.



## :art: UX<hr>
 
The theme of this page is cooking, and there are various types of users this page may appeal to:

*User type 1: Person interested in changing their lifestyle and considering starting KETO*


*User type 2: Those already practicing the KETO lifestyle and diet, but looking for inspiration for daily menus*


*User type 3: Advertisers looking to tap into the wide group of users. As one of the website pages is shop, there is an opportunity of affiliation or paid sponsorship*

### User Stories

#### *Guest User*
- As a guest user of this website I want to just browse - I expect this site to have some content available for me
- As a guest user I want to know what the website is about when I am visiting first time
- As a guest user I want to be able to access, search and share recipes
- As a guest user I want to be able to register and log in easily
- As a guest user I want to be able to check out Social Networks of this website
- As a guest user I want to be able to visit some recommended by this website shops

#### *Logged in User*
- As a registered user I want to be able to get a confirmation every time I log in
- As a registered user I want to be able to add recipes
- As a registered user I want to be able to search recipes
- As a registered user I want to be able to delete recipes I have added
- As a registered user I want to be able to store my information in a dedicated profile
- As a registered user I want to be able to upload my profile picture
- As a registered user I want to be able to be able to share my success within my profile
- As a registered user I want to be able to see other users profiles and check out their achievements
- As a registered user I want to be able to edit my profile when any of my details change
- As a registered user I want to be able to delete my profile when I am no longer interested in being part of this group

#### *Advertiser*
- As an advertiser I appreciate that my products are displayed in a way that would invite a potential customer and make it easy to reach my products
- As an advertiser I expect this page to be easy to navigate, as this will increase chances for the customer to get to my web-shop



## :hammer_and_wrench: Wireframes<hr>
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


## :clipboard: Features<hr>

### :white_check_mark: Existing Features

#### Visible to all users

##### About Keto
##### All Recipes
##### Login
##### Register
##### Shop

#### Accessible only by registered users

##### Profile
##### Edit Profile
##### Delete Profile
##### Wise Zone
##### Add Recipe
##### Edit Recipe
##### Delete Recipe

#### Accessible only by Administrator

##### Manage Categories


### :negative_squared_cross_mark: Features Left to Implement


## :floppy_disk: Technologies Used<hr>



## :toolbox: Testing<hr>


## :checkered_flag: Deployment<hr>

#### To run the app on Heroku.

Create a Heroku account. 
Click to start a new app. 
Pick your location based on the closest free version (or paid version) to your actual location. 
For this project the location selected was Europe

Once your app has been created, then move to the ‘deploy’ tab. 
Choose connect via Gitpod and find your repository.

Go to Settings tab and click on the Reveal Config Vars button. 
Configure the following:

``` 
IP: 0.0.0.0
PORT: 5000
MONGO_URI: "link to your MongoDB"
MONGODB_NAME: "name of your database"
SECRET_KEY: "your secret key"

```
Go to Deploy tab and Enable Automatic Deployments to Gitpod.

With the Heroku settings in place, you can head back to your IDE. The below will need to be set up:

1.	A ‘Procfile’ which will tell Heroku what kind of application it is and how it should be run.
2.	A ‘requirements.txt’ which will tell Heroku which dependencies it needs to install in order for the app to run. The command for ‘procfile’ is:

```
$ echo web: python run.py > Procfile
```

The command for requirements is:
```
pip3 freeze --local > requirements.txt
```
This needs to me re-run if any other dependencies are added mid-project, otherwise the application might not be deployed to Heroku correctly.
As the repository is now connected to push all changes simultanously to Heroku and Gitpod, you may use the terminal to add, commit and push as usual:

```
git add .
```

```
git commit -m "Connected app to Heroku"
```

```
git push
```


### To run the app locally



#### Option 1 is to download a zip file.

#### Option 2 is to clone the repository.


## :heavy_dollar_sign: Credits<hr>

#### Content


#### Media


#### Acknowledgements

