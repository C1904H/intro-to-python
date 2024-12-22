# Exercise 2.2: Django Project Set Up

## Reflection Questions

**1. Suppose you’re in an interview. The interviewer gives you their company’s website as an example, asking you to convert the website and its different parts into Django terms. How would you proceed? For this question, you can think about your dream company and look at their website for reference.**  

The whole website can be thought of as a Django project. I would look at their website and divide it into sections, eg homepage, user authentication, blog, e-commerce functionality etc.  These sections can then be considered **Apps**, ie modules with specific functionality. These may include:  
`login` for authentication and user profiles  
`blog` for news and articles  
`store` for ecommerce  
`pages` for static contact such as 'About us' or 'Contact details'

**2. In your own words, describe the steps you would take to deploy a basic Django application locally on your system.**  

To deploy a basic Django application locally I would take the following steps:
- set up a virtual environment
- open VS Code and terminal window, enter the following command `workon <virtual_environment_name>`
- execute `django-admin startproject <project_name>`
- open Explorer and navigate to new folder `<project_name>`
- rename top-level directory to `src` to avoid confusion with project package with same name
- close and reopen `src` project
- execute `python manage.py migrate` to run migrations to create database, check status marked as ok
- run server by entering `python manage.py runserver`
- copy URL link and open in browser, if Django server successfully installed will see congratulations message
- stop server
- back in src directory run `python manage.py startapp <app_name>`, repeat for each app required
- create superuser by executing `python manage.py createsuperuser`, enter desired username and password
- run server again as above
- on browser navigate to local host adding **admin/** to end of address to navigate to Django admin login page, login with username and password
- navigate to **Users**, check created superuser on list
- return to terminal and quit server (**Ctrl+C**)
- set up complete!

**3. Do some research about the Django admin site and write down how you’d use it during your web application development.**

The Django admin site is one of the powerful  ***'batteries included'*** features of Django.  It reads metadata from my models to provide a quick, model-centric interface where trusted users can mange content to the app. It's a valuable resource that saves time during development making it easier to test models and see if I have the right data.

In my web application development I could utilise it for:
- adding different users, changing passwords and editing access rights
- add new recipes, update or delete existing recipes (eg CRUD operations)
- manage categories, ingredients, or users
- seed initial data
- validate and test models
- simplify model management (eg list display for recipe name, cooking time, ingredients, difficulty)
- quick prototyping and feedback (eg add new model field and test how it works in the admin interface)
- monitoring and auditing live application (track recent additions or monitor content added by user).