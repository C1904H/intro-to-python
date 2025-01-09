# Exercise 2.6: User Authentication in Django

## Reflection Questions

**1. In your own words, write down the importance of incorporating authentication into an application. You can take an example application to explain your answer.**

Authentication is an important feature of many apps. It adds a level of security and protection to an app and user’s data and can display customised user-specific information. An example of this is the Spotify App.  When a user logs in they can see their own created playlists, saved music, and recommended songs and playlists.

**2. In your own words, explain the steps you should take to create a login for your Django web application.**

To create a login for a Django web application the following steps should be taken:  

***1- Create the login_view***  
The login_view should include import the following:  
`from django.contrib.auth import authenticate, login`  
`from djangocontrib.auth.forms import AuthenticationForm`  
Code should then be written for a POST request to be generated when the user clicks the Login button, and a login form completed. If the form is valid the app will read the username and password. Django’s built in `authenticate()` function checks username and password and if successful, directs user to desired page.  

***2- Create the HTML template for login page***  
An html page for login should be created, including the form Django security token.  A basic login page should contain the following code:  
html  
```
<h1>Login</h1>     

{% if error_message %}
   {{error_message}}
{% endif %}

<form action="" method="POST" >
   {% comment %} add Django security token {% endcomment %}
   {% csrf_token %}   
   {{form}}           
  <button type="submit" >Login</button>
</form>
```
Django will need to be directed to look for this template and so in the `settings.py` file of app, in the `TEMPLATES` list variable the following code should be added:
`DIRS`: [BASE_DIR / ‘templates’];  

***3- Specify URL mapping***  
If required (ie coding within an app).

***4- Register the URL to the project*** 
In app `urls.py` file import `login_view` from views and include the `login_view` path in `urlpatterns`:  
`path(‘login/‘, login_view, name=‘login’),`

**3. Look up the following three Django functions on Django’s official documentation and/or other trusted sources and write a brief description of each.**

***authenticate()*** - Verifies a set of credentials. Takes credentials as keyword arguments (eg username and password) and returns `User` object if credentials are valid for a backend. Returns `None` if credentials are invalid or if backend raises `PermissionsDenied`.

***redirect(***) - Returns a HttpResponseRedirect to the appropriate URL for arguments passed.

***include()*** - A function that takes full Python import path to another URLconf module that should be ‘included’ in this place. The application namespace and instance namespace where the entries will be included into can also be specified.  