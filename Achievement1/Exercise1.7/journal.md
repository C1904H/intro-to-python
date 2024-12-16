# Exercise 1.7: Finalizing Your Python Program

## Reflection Questions

**1. What is an Object Relational Mapper and what are the advantages of using one?**

Object Relational Mapper (ORM) makes database conversion easier, especially moving from one database management system (DBMS) to another. ORM converts the contents and structure of a database into classes and objects that can be interacted with directly, without having to use SQL syntax.  

Key concepts of ORM include:
- Object-Orientated Paradigm
- Mapping
- CRUD operations.

Advantages of ORM include:
- Abstraction of database complexity as insulated developers from the complexity of SQL queries and database schema features.
- Portability of code through abstraction between the application and database. Developers can switch between various database systems with little code changes.
- Code reusability by classic way of relationship with databases, therefor easier to maintain and scale applications.
- Maintenance and scalability via ORM facilitated application maintenance via schema change and updates management.

As ORM simplifies the complexities of database interactions, it increases productivity, shortens development time and produces a neater and more maintainable code quality. 

**2. By this point, you’ve finished creating your Recipe app. How did it go? What’s something in the app that you did well with? If you were to start over, what’s something about your app that you would change or improve?**

I felt the last couple of exercises were quite involvedg and took me more time to develop and test properly than anticipated.  I also had a few problems installing and running mySQLclient. 

I enjoyed learning about mySQL and CRUD opeerations. I thought I did well in developing the main menu user interface, and tried to make options clear to the user. I realised through the course of developing this app, that it’s important to have robust error handling in place and try to anticipate all the different variables a user may enter and to get the app to respond with the correct response and not crash the programme. 

**3. Imagine you’re at a job interview. You’re asked what experience you have creating an app using Python. Taking your work for this Achievement as an example, draft how you would respond to this question.**

During my CareerFoundry Fullstack Web Development Course, I built a command-line Recipe app using Python. This project showcased my ability to design and implement a CRUD application that managed user recipes stored in a MySQL database. I used SQLAlchemy as an ORM, allowing me to abstract complex SQL queries and focus on data modelling and interactions.

Key features of the app include:
Recipe Search: Users can search for recipes based on specified ingredients.
Automated Recipe Rating: A Python function dynamically calculated recipe difficulty based on the number of ingredients and cooking time.
Detailed Recipe Display: Additional recipe information (e.g., ingredients, cooking time, difficulty) is displayed on request.

One challenge I faced was optimizing the recipe search to handle large datasets efficiently. By implementing database indexing and refining SQLAlchemy queries, I ensured the app performed well even as the dataset grew.
This project helped me strengthen my Python programming skills, understand relational database management, and effectively use ORMs for streamlined database interactions.
  
 
**4. Take a moment to reflect on your learning in the course so far:** 
***What went well during this Achievement?***  
I enjoyed learning Python and felt a lot of aspects of it were straightforward and made more sense to me compared to JavaScript!

***What’s something you’re proud of?***  
I’m proud to have utilised the teachings in the course to produce a functional and interactive command line Recipe app, with only a few setbacks and delays along the way. Largely, I was able to keep to my timetable for completion.

***What was the most challenging aspect of this Achievement?***  
I felt the `edit_recipe()` function was quite challenging, as there were so many parts of it to consider, ie the different options available to the user and the possible input errors that might occur. I also had to make sure I was able to recalculate the difficulty whenever the recipe cooking time or ingredient length was updated. 

***Did this Achievement meet your expectations? Did it give you the confidence to start working with your new Python skills?***  
Whilst there are some aspects of Python I feel I have a good grasp on, I sometimes struggle with knowing how all the components come together to be able to run a functional script. I’m also aware that there is still lots to discover and learn about Python, and I look forward to delving into it more in the next Achievement!

***What’s something you want to keep in mind to help you do your best in Achievement 2?***  
I think I must always make sure I include error handling when planning my Python apps. In this achievement I felt I wasn’t always aware of potential user inputs until I came to testing the app and inadvertently crashed it or got an incorrect response if I entered an unexpected value. I need to be proactive at integrating error handling and that will help improve the functionality, decrease testing time and ultimately speed up my app development time. 