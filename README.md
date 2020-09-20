# Kasia's KETO Cookbook

In the ever evolving world of different diets, the Food Pyramid as we know it no longer applies for most people. Many diets would at this stage have eliminated certain contents of the pyramid, in Keto's case that pyramid has been literally turned up-side-down. **enter animation for reference** This website was developed to assist those who are embarking on their lifestyle change as well as those who are looking for some inspiration to their existing journey.

 
## UX
 
The theme of this page is cooking, and there are various types of users this page may appeal to:

*User type 1: Person interested in changing their lifestyle and considering starting KETO*


*User type 2: Those already practicing the KETO lifestyle and diet, but looking for inspiration for daily menus*


*User type 3: Advertisers looking to tap into the wide group of users. As one of the website pages is shop, there is an opportunity of affiliation or paid sponsorship

# User Stories

*Guest User*
- As a guest user of this website I might not want to sign up for anything immediately, I want to browse - I expect this site to have some content available for me
- As a guest user I appreciate that the website is intuitive to navigate, I am visiting it first time
- As a guest user I might not go past the Home page, so I expect some overall information there about the page, to catch my attention
- As a guest user I appreciate the colours should be easy on the eye, with food as a subject matter, I appreciate the colorfullness
- As a guest user, without signing up, I expect some educational value to the website, so the content of Home page is very important to me

*Logged in User*
- As a registered user I appreciate that the page delivers a functionality of providing me with ideas for my daily menu
- As a registered user I can log onto my account and add some recipes I already own or know
- As a registered user I can see more information available that non registered user

*Advertiser*
- As an advertiser I appreciate that my products are displayed in a way that would invite a potential customer and make it easy to reach my products
- As an advertiser I expect this page to be easy to navigate, as this will increase chances for the customer to get to my web-shop

*Owner*
- As the owner of the website I want encorage user to register and visit my site as often as possible, so I ensure the content varies and addresses as wide user group as possible


## Wireframes

![](images/desktop_view.png)
![](images/mobile_view.png)

----------------------------------------------------------------------------------------------------------------------------------------------------------
## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
*Home*
This page will provide some inspiration for the user, be it registered or not registered. The aim is to give as much info about the diet as possible, if follows order of __What, How, Why__. Ideally a potential user will immediately know what this page has to offer and continue on exploring it. Categories are readily available on this page, so the user does not need to go looking for the next step.
*Shop*
This page is created for the potential advertiser or affiliate. The products are presented in a way that makes them linked to the diet, the display follows a suit of __Starter Keto-Kit__ and it will appeal to both registered and unregistered user. The links under the products bring user to the relevant advertiser's ecommerce site, so no need for them to register with the cookbook website.

*Recipes*
This page is visible to both types of user, be it registered or not registered. The aim is just to pass on the information and invite user to explore this diet. *There might be a searchbox*
*Register*
Once decided they want to have access to more information, the unregistered user may register here
*Profile*
After signing up and logging in, user has access to more information and may also add some of his own favourite recipes
 
### Existing Features


### Features Left to Implement


## Technologies Used



## Testing


## Deployment

# To run the app on Heroku.

Create a Heroku account. 
Click to start a new app. 
Pick your location based on the closest free version (or paid version) to your actual location. 
For this project it was Europe. Choose an appropriate name for the app and click to create.

Once your app has been created, then move to the ‘deploy’ tab. 
You can connect to GitHub through one of the tabs. I, however, have used the CLI. 
You can link to an existing repository by using the following command in your IDE:
$ heroku git:remote -a "enter-your-heroku-app-name"

Then, head over to the ‘settings’ tab and click on the ‘reveal config vars’ button. Configure the following:

``` 
Key: value
IP: 0.0.0.0
PORT: 8080
MONGO_URI: "link to your MongoDB"

```

You can find your MongoDB link by going into your MongoDB Atlas account and clicking the ‘connect’ button. From there you have the option to choose to connect to your application and can select the correct language and version.

With the Heroku settings sorted, you can head back to your IDE. There a few things you now need to set up:

1.	A ‘Procfile’ which will tell Heroku what kind of application it is and how it should be run.
2.	A ‘requirements.txt’ which will tell Heroku which dependencies it needs to install in order for the app to run. The command for ‘procfile’ is:
echo web: python run.py > Procfile

The command for requirements is:
```
pip3 freeze --local > requirements.txt
```

Please note that you need to re-run the requirements command if you add any dependencies mid-project. Otherwise, Heroku will not deploy the app correctly.
With those set up, you can now push your project to Heroku directly from your IDE.
```
$ heroku login -i
```

Enter your username and password. Push your commits to Heroku using this command:
```
$ git push -u Heroku master
```

# To run the app locally

To run this project locally, please ensure you have an IDE installed on your computer. Popular ones are gitpod, Visual Studio or PyCharm (for python projects specifically).

Regardless of which IDE you choose, you will also need the following installed.
•	This project uses MongoDB as a database, and therefore you will need either a MongoDB Atlas account or have MongoDB running locally on your machine. 
o	To set up MongoDB Atlas please see the documentation MongoDB Atlas
•	PIP – to install packages such as pyMongo
•	Python3 – the project uses Python3 for the backend language – specially Python 3.8
•	Git – for easy version control

The next step is to access your github repository. 

# Option 1 is to download a zip file.

# Option 2 is to clone the repository.


## Credits

### Content


### Media


### Acknowledgements

