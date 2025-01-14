# Exercise 2.7: Data Analysis and Visualization in Django

## Reflection Questions

**1. Consider your favorite website/application (you can also take CareerFoundry). Think about the various data that your favorite website/application collects. Write down how analyzing the collected data could help the website/application.**

Collecting data from user interaction with the CareerFoundry website is vital to help the course organisers improve the course content and user experience.  They can track student engagement by measuring metrics like time spend on platform, or identify at risk students by analysing login frequency.  Operational efficiency can be improved by monitoring site performance data that can detect slow-loading pages, broken links. Feedback analysis from course reviews and ratings can help identify areas of the course students enjoy and identify areas where improvement or more support can be offered. User behaviour can be analysed to see which pages users visit more often and understand how users navigate through the site. 

**2. Read the Django official documentation on QuerySet API. Note down the different ways in which you can evaluate a QuerySet.**

A QuerySet can be evaluated in the following ways:  
***-Iteration***  
Executes a database query first time you iterate (ie loop) over it. Results saved in cache.  
***-Slicing***  
Uses Python’s array-slicing syntax. Slicing a non-evaluated `QuerySet` returns a new `QuerySet`. Returned `QuerySet` does’t allow further modifications, but does allow more slicing. Saves results to its cache if you iterate over it.  
***-Pickling***  
Forces all results to be loaded into memory prior to pickling. Pickling usually used as a precursor to caching and when cached query set is reloaded, you want the results to already be present and ready for use. When you unpickle a `QuerySet`, it contains the results at moment it was pickled, rather than results currently in database.  
***-repr()***
Returns printable representational string of the given object. `QuerySet` is evaluated but results not saved to cache.  
***-len()***
Returns length of result list. Saves results to cache.  
***-list()***
Force evaluation and returns list of model objects and saves results in cache.  
***-bool()***
Using `bool()`, `or` , `and` or an `if` statement causes the query to be executed. If at least one result, the `QuerySet` is `True`, otherwise `False`.

**3. In the Exercise, you converted your QuerySet to DataFrame. Now do some research on the advantages and disadvantages of QuerySet and DataFrame, and explain the ways in which DataFrame is better for data processing.***

While Django QuerySets are very good for interacting with the database, they lack some of the advanced data manipulation capabilities offed by DataFrame like Pandas. 
 - **Data Visualisation:** Pandas ingrates will with plotting libraries like Matplotlib and Seaborn, enabling easy data visualisation.  
- **Data Analysis:** Datasets provides a wide range of tools for statistical analysis, grouping and aggregation.
- **Data Transformation** Pandas supports various methods for cleaning, reshaping and transforming data that might be cumbersome with Django’s QuerySet alone.  

Overall, QuerySets are best when working with small datasets or performing simple database enquires where you want to avoid loading all data into memory. DataFrame is better when performing complex data transformations or analysis, integrating with machine learning or visualisation tools and working with data that can fit into memory. 
