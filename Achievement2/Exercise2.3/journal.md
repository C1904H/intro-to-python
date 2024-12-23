# Exercise 2.3: Django Models

## Reflection Questions

**1. Do some research on Django models. In your own words, write down how Django models work and what their benefits are.**

A Django model is another batteries-included feature of Django that creates tables, their fields and various constraints. In other words it is the SQL Database to use with Django. Django models is much more straightforward than using SQL and simplifies tasks and organises tables into models. It ensures consistency, version control and advanced metadata handling. Generally, each model maps to a single database table.  

Each model is a Python class that subclasses django.db.models.Model and each attribute of the model represents a database field, automatically generating a database-access API. 

**2. In your own words, explain why it is crucial to write test cases from the beginning of a project. You can take an example project to explain your answer.**  

It's crucial to write test cases from the beginning of a project in order to catch bugs as they occur.  This can save developers a huge amount of time, especially as the application grows, and lets them focus on development. Not only do tests uncover bugs, but they can also prevent them from occurring as the developer is already thinking about the actual requirements and expected results from the application.  

Tests can cover minuscule details of an app's functionality which can be easy for a developer to overlook. They also make code more trustworthy as it's 'tried and tested' - especially important in collaborative projects. Testing the code's strength and any hazards can stop it being broken by anyone else, and vice versa. Significantly tests provide documentation for an application's code, with test cases indicating how the app should behave.