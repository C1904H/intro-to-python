# Exercise 2.4: Django Views and Templates

## Reflection Questions

**1. Do some research on Django views. In your own words, use an example to explain how Django views work.**

Django views are Python function or method of a Python class that takes a request and returns a response, such as a HTML document or JSON data. Every view is associated with a template which defines the output structure. The process consists of the following steps:
- Views are defined in `views.py` file in the app folder,
- The template is created in the app’s `templates/ folder`,
- The view is connected to an URL in `urls.py`file (ie URL mapping),
- The URL and view is registered in the project’s `urls.py` file.  

For example, if a user clicks on a ‘contact us’ link on a webpage, the URL maps to the corresponsing view file, which loads the template of the ‘contact us’ html page and displays it as a response to the user’s browser.

**2. Imagine you’re working on a Django web development project, and you anticipate that you’ll have to reuse lots of code in various parts of the project. In this scenario, will you use Django function-based views or class-based views, and why?**

In this scenario class based views (CBVs) would be the best choice, as once created they are easy to reuse or extend. Due to their class-based nature, CBVs reduce the effort spent duplicating or rewriting code.  Whilst function based views (FBVs) are easier to implement, they are harder to use where code needs to be reused or extended.  

**3. Read Django’s documentation on the Django template language and make some notes on its basics.**

Django’s template language is designed to balance power and ease. It connects the backend Python code and the frontend HTML of the project.  A template is a text file that can generate any text-based format (HTML, XML, CSV etc). The most essential Django templating language syntax includes:
- **Variables** {{ variable }}. When template engine encounters a variable, it evaluates it and replaces it with the result. 
- **Filters** {{ name| lower  }} are used to modify variables for display.  Filters can be chained, eg output of one filter is applied to the next, or take arguments.  Django provides about sixty built-in template filters, a few examples are default, length, filesizeformat.
- **Tags** {% tag %} are more complex than variables, some create text in the output, some control flow by performing loops or logic and some load external information into the template to be used by later variables.  
- **Comments** {# #} are used to comment-out part of a line in a template (only used for single-line comments).
Template inheritance is the most powerful and complex part of Django’s template engine. It allows you to build a base ‘skeleton’ template that contains all the comment elements of your site and defines blocks that child templates can override.  

Other examples of Django template language are automatic HTML escaping, accessing method calls and custom tag and filter libraries.
