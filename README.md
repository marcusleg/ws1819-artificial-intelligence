# Not sure how to name this yet
In this codebase I implemented some of the problems and solutions presented in the Artificial Intelligence class of my masters degree. The class is based on the book *Artificial Intelligence: A Modern Approach* by *Stuart Russell* and *Peter Norvig*.

At the time of writing (2018-11-21) only search algorithms are implemented.

## Goals
* Describe problems in a unified way (see abstract_problems.py).
* Implement generic solving strategies that operate on these abstract problems.


## Possible questions
### Why use classes if (almost) all methods are static?
In order to have a well defined interface we need an abstract class to derive from.