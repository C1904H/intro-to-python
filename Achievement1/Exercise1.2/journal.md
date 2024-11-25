# Exercise 1.2: Data Types in Python

## Reflection Questions

**1. Imagine you’re having a conversation with a future colleague about whether to use the iPython Shell instead of Python’s default shell. What reasons would you give to explain the benefits of using the iPython Shell over the default one?**

_iPython shell provides more guidance and makes code text visibly clearer by using syntax highlighting, which displays different features of the code in contrasting fonts and colours and automatically indents text for nested statements.
in iPython you can also test out small parts of code quickly and easily as each command is executed immediately after typed and responses printed. This is a huge benefit in quickly and usefully testing small pieces of code.
Tab completion is another handy tool where possible commands for a given object is listed._  


**2. Python has a host of different data types that allow you to store and organize information. List 4 examples of data types that Python recognizes, briefly define them, and indicate whether they are scalar or non-scalar.**

- _Tuples (non-scalar)_
  - _Linear arrays that can store multiple values of any type. Are immutable._
- _Lists (non-scalar)_
  - _Ordered sequence, mutable (modify or delete internal element)._
- _Strings (non-scalar)_
  - _Immutable array of characters, can be composed of alpha number characters and symbols._
- _Dictionaries (non-scalar)_
  - _Stores values and objects using key-value pairs. Values can be of any data type and can be duplicated, keys can’t be repeated and are immutable._


**3. A frequent question at job interviews for Python developers is: what is the difference between lists and tuples in Python? Write down how you would respond.**

_Lists are mutable whilst tuples are immutable. This makes lists more flexible than tuples as they can modified.  However lists are slower to read and access than tuples, especially with large amounts of data._

**4. In the task for this Exercise, you decided what you thought was the most suitable data structure for storing all the information for a recipe. Now, imagine you’re creating a language-learning app that helps users memorize vocabulary through flashcards. Users can input vocabulary words, definitions, and their category (noun, verb, etc.) into the flashcards. They can then quiz themselves by flipping through the flashcards. Think about the necessary data types and what would be the most suitable data structure for this language-learning app. Between tuples, lists, and dictionaries, which would you choose? Think about their respective advantages and limitations, and where flexibility might be useful if you were to continue developing the language-learning app beyond vocabulary memorization.**

_Dictionaries would be the best option for this app. As dictionaries use key-values pairs it makes it easier and quicker to query the different definitions or categories within this app. Adding, deleting and updating entries are straightforward in dictionaries which would be beneficial in a dynamic language-learning app if more features were to be added to it._  
