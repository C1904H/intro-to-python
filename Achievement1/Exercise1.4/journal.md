# Exercise 1.4: File Handling in Python

## Reflection Questions

**1. Why is file storage important when you’re using Python? What would happen if you didn’t store local files?**

_The ability to read data from files and write data to them is vital in preserving data, even after programme or application has closed. If they weren’t stored, the variables in the script to assign and keep track of values no longer exists when the script stops running and can’t be retrieved for later use._

**2. In this Exercise you learned about the pickling process with the pickle.dump() method. What are pickles? In which situations would you choose to use pickles and why?** 

_Pickles convert complex data into packaged stream of bytes (pickles), then write them into a binary file. A binary file can store complex information that can be read by machine, not humans. Pickles are useful for writing to and reading from external files composed of data structures such as lists and dictionaries._

**3. In Python, what function do you use to find out which directory you’re currently in? What if you wanted to change your current working directory?**

_The `os.getcwd()` command is used to find out which file directory you’re currently in.  If you wanted to change your current working director you would enter `os.chdir(“<path to desired folder>”)` to navigate to your chosen directory._

**4. Imagine you’re working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?**

_You would employ the `try-except` block. First you would place the `print` statement in a try block (ie where the error is expected). Then display an error message in the `except` block saying that the user has entered an erroneous value. The program will not terminate after the error, but report an error message that the user can then try again and enter a value that works, the program can then continue until it’s end._

**5. You’re now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? Feel free to use these notes to guide your next mentor call.**

_I feel the course material is intuitive to follow and builds nicely on the previous learning.  I sometimes feel like I follow along nicely but then when we move onto the next section I quickly forgot what I have just learnt and practiced, and have to retreat back and do a lot of re-reading._  

_I feel proud that I’ve managed to keep to my study and task submission schedule, as there has been a lot of recent challenges at work that has taken up a lot of my time and energy._ 

_In addition to my issue above about retaining new learning, I sometimes struggle with starting off a code from scratch. I find when I look at the examples in the exercise or someone else’s code I can understand and follow it but find it difficult to do without a guide._
