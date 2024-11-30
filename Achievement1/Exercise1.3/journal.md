# Exercise 1.3: Operators & Functions in Python

## Reflection Questions

**1. In this Exercise, you learned how to use if-elif-else statements to run different tasks based on conditions that you define. Now practice that skill by writing a script for a simple travel app using an if-elif-else statement for the following situation:**

**The script should ask the user where they want to travel.**
**The user’s input should be checked for 3 different travel destinations that you define.**
**If the user’s input is one of those 3 destinations, the following statement should be printed: “Enjoy your stay in ______!”**
**If the user’s input is something other than the defined destinations, the following statement should be printed: “Oops, that destination is not currently available.**
```
destination = input(‘Where would you like to travel to?’)

if destination == ‘Thailand’:
    Print (‘Enjoy your stay in Thailand!’)

elif destination == ‘Italy’:
    Print (‘Enjoy your stay in Italy!’)

elif destination == ‘Australia’:
    Print (‘Enjoy your stay in Australia!’) 

else:
      print(‘Oops, that destination is not currently available.’)
```
**2. Imagine you’re at a job interview for a Python developer role. The interviewer says “Explain logical operators in Python”. Draft how you would respond.**

Logical (or Boolean) operators `and`, `or` or `not` are used when we want to check for multiple conditions at the same time. They return a **True** (if conditions are met) or **False** (if conditions are not met) result.  The `and` operator returns **True** only if **ALL** conditions are met, or **False** if **ANY** condition is not met.  Conversely, the `or` operator returns **True** if any condition is not met, or **False** if ALL conditions are met. 

The `not` operator however does not require a condition on either side because it’s used to reverse the result of a logical expression that comes after it. This is useful in checking unmet conditions: 
- In the context of if statements and while loops
- Inverting the truth value of an object or expression
- Checking if a value is not in a given container
- Checking for an object’s identity.

**3. What are functions in Python? When and why are they useful?**

Functions are sets of instructions that process or manipulate code in order to achieve certain things.  Functions can be built-in or user-defined.  
Common or repeated tasks can be put together to make a custom function, so that instead of writing the same code repeatedly for different inputs, we can use function calls to reuse code contained in it again and again. Benefits of using functions are: 
- increased code readability and reusability
- saving time.  

**4. In the section for Exercise 1 in this Learning Journal, you were asked in question 3 to set some goals for yourself while you complete this course. .In preparation for your next mentor call, make some notes on how you’ve progressed towards your goals so far.**

_I want to gain a comprehensive understanding of Python and it's applications._

I feel so far I’ve had a good introduction to the basics of Python but still have a lot to learn about it. It’s useful to learn the building blocks of data structures and operators and how they work together. 

_I want to gain experience in Python and feel confident using Python in backend development._

I feel the code practices and the Exercise tasks have been very useful in giving me practical experience of writing Python and I’ve enjoyed  using the iPython shell and virtual environment to test my code. 