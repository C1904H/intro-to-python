# Exercise 2.8: Deploying a Django Application

## Reflection Questions

**1.Explain how you can use CSS and JavaScript in your Django web application.**  

CSS and JavaScript can be used as a static files in Django projects.  CSS allows developers to create styling to template files, making the app more visually appealing and engaging to app users.

JavaScript is utilised to introduce dynamic elements in an application, further engaging users. It can be used when complex UI elements are required or even for useful traffic analysis like installing a visitor counter

**2. In your own words, explain the steps you’d need to take to deploy your Django web application.**  

1 - Prepare application for hosting by updating `settings.py` file:  
Set `DEBUG=FALSE`  
Add domain to `ALLOWED_HOSTS`  
Add `STATIC_ROOT` path to collect static files  

2 - Set up server with required software.  

3- Set up a virtual environment and install dependencies from `requirements.txt`.  

4- Deploy the app on chosen web hosting platform, eg if using Heroku:
-push repository to heroku  
-set up database table  
-create superuser  
-set heroku URL in `ALLOWED_HOSTS` in `settings.py`  
-add data to application  
-set `SECRET_KEY`

**3. You’ve now finished Achievement 2 and, with it, the whole course! Take a moment to reflect on your learning:**  
**What went well during this Achievement?**  
**What’s something you’re proud of?**  
**What was the most challenging aspect of this Achievement?**  
**Did this Achievement meet your expectations? Did it give you the confidence to start working with your new Django skills?**

Overall I enjoyed this Achievement and learning about Django, to me it seems the most intuitive of the coding languages I’ve learnt so far.  

I’m proud I managed to produce a fully functional Django app, using advanced coding practices that lets users utilise a wide range of functions within the app and hopefully they find it an appealing and engaging platform.  

I found the most challenging aspect with deploying my Django app on a web hosting service.  The course material is woefully outdated and the recommended version of Python is no longer supported on Heroku.  This caused a great deal of stress and added extra time to my course, trying to explore different ways to deploy my app.  Thankfully I had a very engaging Mentor who took the time to suggest a different options and provided me with guidance and support to enable me to complete this achievement. I’m sure I wouldn’t have been able to complete it without him!

If I was asked how my confidence levels were before this last exercise, I would have said quite high. Unfortunately this last exercise has taken a huge knock of my confidence, although I can be confident that I explored other options, persevered and managed to complete it.