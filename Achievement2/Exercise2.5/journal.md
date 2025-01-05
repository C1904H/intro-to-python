# Exercise 2.5: Django MVT Revisited

## Reflection Questions

**1. In your own words, explain Django static files and how Django handles them.**

In Django static files include images, JavaScript or CSS. These files are used in the front-end of an application. Static files are files that are not generated dynamically and remain the same for every user. They’re typically provided by the developer during project creation.

To configure static files:
In a project’s `settings.py` file, there is a section for defining static files: `STATIC_URL = ‘/static/‘`, 
In templates, use the static template tag `{% load static %}` to build the URL for the given relative path using the configures static files STORAGES alias
Store static files in a folder called ‘static’ in the app.

To serve static files during development:
In `urls.py` file of app, import settings and static:
``` python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

**2. Look up the following two Django packages on Django’s official documentation and/or other trusted sources. Write a brief description of each.**

***ListView Package***  
It is a Class-Based View (CBV). Refers to a view to list all or particular instances of a table from the database in a particular order. ListView is used to display multiple types of data on a single page or view (ie displays data as a list). 

***DetailView Package***  
Is also a CBV. It provides a detailed view of a single object in a model. It is one of the simplest and most commonly used views for presenting object details based on its primary key or other unique identifier.

**3. You’re now more than halfway through Achievement 2! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with?**  

This achievement has been flying past! I find the course content is very thorough and has supported my learning. I feel like I'm able to follow along in each exercise, but I often find I quickly forget previous learning and have to frequently go back and refer to previous exercises.  I think I just need to practice a lot to cement all the learning firmly in my mind!
