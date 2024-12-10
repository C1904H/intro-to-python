# Exercise 1.6: Databases in Python

## Reflection Questions

**1. What are databases and what are the advantages of using them?**

Databases stores data in organised collections.  They keep data in a standardised format so you are able to store and access it more easily, they can be made secure through password access and you can access them using other applications. 

**2. List 3 data types that can be used in MySQL and describe them briefly:**

`VARCHAR(n)` String of variable length, n represents max no of characters.  
`INT` Standard integers  
`FLOAT` Floating-point decimal numbers

**3. In what situations would SQLite be a better choice than MySQL?**

SQLite would be a better choice when working with very simple database (eg web page for customer’s email address) or if want to test a database without full set up.  SQLite is the portable version, requires no installation or setup, and you can store data in simple .db files. These files can be accessed and modified directly from applications like Python.

**4. Think back to what you learned in the Immersion course. What do you think about the differences between JavaScript and Python as programming languages?**

Python is powerful tool in scientific and specialised applications and supports different programming paradigms.  Python emphasises readability and simplicity and is ideal for tasks like data analysis and  back-end development.  JavaScript can be used to develop the back-end and front-end of an application, especially for web development, servers and user-facing dynamic and interactive functionality. 

- Python is a high-level general-purpose interpreted programming language that was developed to emphasize code readability.	JavaScript is a programming language that conforms to the ECMAScript specification.
- Python is a scripting language used for developing both desktop and web applications.	JavaScript is a client-side scripting language.
- Python uses a class-based inheritance model, an exception is raised when the function is called with the wrong parameters.	JavaScript uses a prototype-based inheritance model, whether functions are called with correct parameters or not is irrelevant.
- In Python List, set, and dict are mutable while int, tuple, bool, Unicode are immutable in python.	In JavaScript, only objects and arrays are mutable.
- Python uses a more conservative programming paradigm similar to C, C++, and Java.	JavaScript is a language of the web browser and one of the easiest to use.
- Python has a comprehensive standard library.	JavaScript has a limited set of utility objects.

**5. Now that you’re nearly at the end of Achievement 1, consider what you know about Python so far. What would you say are the limitations of Python as a programming language?**

Python’s limitations include:
- Limited performance for CPU-intensive tasks due to its interpreted nature
- Global Interpreter Lock (GIL) restricts multi-threading efficiency
- Dependency management can be challenging with conflicting versions
- Less suitable for mobile app development compared to languages like JavaScript
- Limited support for low-level system programming compared to C/C++
- Slower execution speed compared to compiled languages like C++ or Rust
- Difficulty in creating standalone executables without additional tools