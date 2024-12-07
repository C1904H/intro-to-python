# Exercise 1.5: Object-Oriented Programming in Python

## Reflection Questions

**1. In your own words, what is object-oriented programming? What are the benefits of OOP?**  

_Object-oriented programming is a programming model that abstracts data and methods into classes.  The main concept is to bind data and functions that work together into a single unit so that no other part of the code can access the data.  OOPs concepts in Python include:_
- _Class_
-_ Objects_
- _Polymorphism_
- _Inheritance and hierarchies_
_By grouping related data and functions into logical classes, OOP promotes code structure and simplifies maintenance, especially as programs grow in size and complexity. A modular approach makes it easier to understand, modify and reuse code, and so reduces development time. OOP also provides a clear and relatable programming style. The use of objects and the relationships between them mirror real-world concepts. Inheritance contributes to code robustness by promoting data protection and code reusability._

**2. What are objects and classes in Python? Come up with a real-world example to illustrate how objects and classes work.**

_Nearly everything in Python is an object, with its properties and methods. A class is like an object constructor ('blueprint') for creating objects.
To illustrate: a class could be a_ `book`,  
_with attributes such as:_ `title`, `author`, `isbn`, `in stock`  
_and methods:_ `check_out()`, `return()`.  
Object:
```python
book1 = Book("Wuthering Heights", "Emily Bronte", "555444", True)
book2 = Book("Life of Pi", "Yann Martel", "303030", False)
```

**3. In your own words, write brief explanations of the following OOP concepts:**  

**Inheritance**  
_Inheritance is where you can 'inherit' methods and properties from one class to another. The class being inherited from is known as the parent (or base) class, and the class to which all data attributes and procedures are copied over is known as the subclass (or inherited) class. Inheritance only works in one direction: from parent to subclass. This avoids duplicate code, permits the creation of hierarchial classifications, extensibility and less demanding support and debugging._

**Polymorphism**  
_Polymorphism is where a given data attribute or method has the same name across different classes or data types, but performs different operations depending on where it was defined.  A single set of code can handle any object, even if the objects are of different types. Polymorphism allows for the execution of dynamic dispatch and the implementation of interfaces, reduces the number of lines of code and so simpler to maintain, permits for the execution of more generic algorithms and more adaptable programs._

**Operator Overloading**  
_Operator overloading means giving extended meaning beyond their predefined operational meaning. For example operator `+` is used to add two integers and joining two strings and merge two lists. It is achievable because `+` operator is overloaded by int class and str class. To use operators on a custom class you need to define your own methods for them._  