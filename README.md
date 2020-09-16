# Kasia's KETO Cookbook

In the ever evolving world of different diets, the Food Pyramid as we know it no longer applies for most people. Many diets would at this stage have eliminated certain contents of the pyramid, in Keto's case that pyramid has been literally turned up-side-down. **enter animation for reference** This website was developed to assist those who are embarking on their lifestyle change as well as those who are looking for some inspiration to their existing journey.

 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

-----------------------------------------------------------------------------------------------------------------------------------------------------------
The theme of this page is cooking, and there are various types of users this page may appeal to:

*User type 1: Person interested in changing their lifestyle and considering starting KETO*


*User type 2: Those already practicing the KETO lifestyle and diet, but looking for inspiration for daily menus*


*User type 3: Advertisers looking to tap into the wide group of users. As one of the website pages is shop, there is an opportunity of affiliation or paid sponsorship

# User Stories

*Guest User

- As a guest user of this website I might not want to sign up for anything immediately, I want to browse - I expect this site to have some content available for me
- As a guest user I appreciate that the website is intuitive to navigate, I am visiting it first time
- As a guest user I might not go past the Home page, so I expect some overall information there about the page, to catch my attention
- As a guest user I appreciate the colours should be easy on the eye, with food as a subject matter, I appreciate the colorfullness
- As a guest user, without signing up, I expect some educational value to the website, so the content of Home page is very important to me

*Logged in User

- As a registered user I appreciate that the page delivers a functionality of providing me with ideas for my daily menu
- As a registered user I can log onto my account and add some recipes I already own or know
- As a registered user I can see more information available that non registered user
- 

*Advertiser

*Owner

----------------------------------------------------------------------------------------------------------------------------------------------------------
## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

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

1.	A ‘procfile’ which will tell Heroku what kind of application it is and how it should be run.
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
1.	On the GitHub project page, there is a ‘code’ tab which will dropdown to allow you to download a zip file.
2.	Once downloaded, extract the files to a desired folder on the desktop.
# Option 2 is to clone the repository.
1.	Under the same code tab, click to copy the url for your repository.
2.	Open Git Bash on your local computer and ensure you are in the right directory. Then run the following command:
git clone https://github.com/cgpalmer/ms3-project-2.git

It is recommended to use a virtual environment for the Python interpreter. Python's own built in environment can utilised by this code:
python -m .venv venv
Please note: Different IDE and operating systems, your python command may be slightly different. Once you have your virtual environment, you can activate it with:
.venv\Scripts\activate 
I have attached a link to the documentation on setting up a virtual environment, in case the commands are different. Python interpreter
Next, you will need to download all of your requirements for the project. You can do this manually or you can run this code:
pip -r requirements.txt.
All that is left to set up now is your SECRET_KEY and a MONGO_URI. You can store these in a file:- .flaskenv. You must ensure your database name is the same as the one in MongoDB so it connects properly. For this project it is “projectDB”.
There are three collections to interact with: report, categories, user_credentials. Now, you are ready to run the app in browser. The command is:
python3 app.py
This will open a port (which may be different depending on your IDE) and gives you the open to see your app.



## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
