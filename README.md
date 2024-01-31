\ Lambda Calculus Project Report
## Author: Futao Yan, Kristian
## Github: yorkmurphy0@gmail.com, kristianderoos@gmail.com
## Introduction

Lambda Calculus, akin to the Turing Machine, utilizes a mechanized approach to prove and deduce complex problems in mathematics.

Lambda Calculus (λ-calculus) is an essential conceptual framework in computer science, particularly in the field of programming languages. This project aims to implement a lambda calculus interpreter and discuss its implications for programming language design.

In mathematics, a formal system, such as λ-calculus, is a symbolic game that begins with axioms and involves extensive deduction and proof, forming a self-contained system with axioms, theorems, corollaries, and conjectures. Formal languages are the tools used to describe these systems, providing a structured way to express and manipulate their components.

In short, the λ-calculus processes λ-terms. There are three types of λ-terms: variables, abstractions and applications. A variable speaks for itself: it is a character that can take any value. An abstraction can be thought of as a function: it is denoted as a "λ", followed by a variable, a dot, and a function. An example of this would be λx.x + 1, which has the same meaning as the common notation F(x) = x + 1. An application is a λ-term in which one value or expression is given to some other expression. It is denoted as (λx.x) y, in which x is given the "value" y. For example, the output of the application (λx.x + 1) 7 is 8, as 7 + 1 = 8.


## Background

In 1928, a mathematical challenge was posed by David Hilbert and Wilhelm Ackermann, later known as the "Entscheidungsproblem", or Decision Problem. It asks the question if there is an algorithm that can judge for every logical statement if it is provable or not. The use of such an algorithm for mathematics would be great: for example, one could test for conjectures if they are provable or not. However, to take on this challenge, one first had to answer the question what an algorithm can do. In other words: what are the limits to computability?

Alonzo Church, a pioneering mathematician and logician, answered this  question in a publication in 1932 by developing the λ-calculus as a universal computational model. This system, foundational to functional programming, introduced the concept of functions operating on and returning other functions, symbolized by the Greek letter lambda (λ). According to Church's Thesis in 1936, the λ-calculus encompasses all possible computational functions, en can therefore be seen as a blueprint for all possible algorithms, as it describes the essential functionality of any algorithm: it takes an input, changes it with substitution and reduction, and then gives you an output. 

Shortly after Church's publication, in 1936, another pioneering computer scienstist named Alan Turing, developed his Turing Machine, which is a theoretical machine that in essence works the same as the λ-calculus, although Turing developed this machine independently from Church's λ-calculus. On the basis of this Turing Machine, Alan Turing managed to answer the decision problem negatively: he showed that it is impossible to derive for every logical statement if it is provable or not.

In computer science's evolution, the late 1950s marked a pivotal point with John McCarthy's development of Lisp at MIT. This language, inspired by Alonzo Church's λ-calculus, showcased the practical implementation of theoretical computational concepts on von Neumann computers. The creation of Lisp machines at MIT's AI lab further materialized λ-calculus in hardware form. While adapting to changing computing architectures, Lisp evolved, integrating functional and traditional programming aspects, symbolizing the adaptability and potential of functional languages in advancing computational theory.

Writing a λ-calculus program might at first sight seem like a fairly simple task, as it only consists of substitution and reduction of λ-terms. However, the difficulty lies in understanding the λ-calculus as an abstract machine and writing a program that works for even the most complex λ-terms. The λ-calculus, however simple, has a wide range of capabilities.

## Algorithm and Implementation

### Design
In the implementation of the λ-calculus interpreter, the algorithm design employs object-oriented principles, defining distinct classes for each λ-calculus construct: Variable, Abstraction, and Application. Each class encapsulates specific behaviors and properties of these constructs. Furthermore, there is a fourth class, named LambdaTerm, which is subject only to the fromString method, in which a string is converted into a variable, abstraction or application. 

### Coding Process
The coding process for your λ-calculus interpreter involved implementing three key classes: Variable, Abstraction, and Application. Each class represents a fundamental aspect of λ-calculus:

Variable: Handles the representation of variables, identified by symbols.

Abstraction: Manages function abstractions, defined as a pair of a variable and a body expression.

Application: Deals with the application of one λ-term to another.

In each class, methods like substitute and reduce were implemented to facilitate the core operations of λ-calculus, such as substitution and β-reduction. This approach ensures the interpreter can process λ-calculus expressions, reflecting both the structural and operational aspects of λ-calculus theory.

### Variables
In the implementation of the Variable class, the focus was on representing variables in λ-calculus expressions. Each variable is identified by a unique symbol, encapsulated within the class. The __init__ method initializes a variable with its symbol, while the __repr__ and __str__ methods provide string representations for ease of understanding. These functions are easy to read and have a time complexity of O(n) = 1. 

The substitute method is a bit more complicated: 
```python
def substitute(self, rules):
        if isinstance(rules, dict) == False:
            raise ValueError ("Substitution argument must be dictionary in form {'a' : 'b'}")
        
        for var in self.symbol:
            for item in rules.keys():
                if isinstance(item, str) == False:
                    raise ValueError ("Only strings allowed as keys in dictionary")
                if isinstance(rules[item], str) == False:
                    raise ValueError ("Only strings allowed as values in dictionary")
                if var == item:
                    self.symbol = self.symbol.replace(var, rules[item])
        
        return Variable(self.symbol)
```
As visualized above, the function first makes sure that the input is correct; it requires a dictionary with both keys and values as strings. A for loop is used for this, which give this a time complexity of O(n) = n, n being the number of key-value pairs in the dictionary. In the substitution itself, for each character in the variable, the dictionary is searched. If the character is a key in the dictionary, the replace function is called, which itself has a time complexity of O(m) = m, with m being the number of characters in the string, as it loops through the string. This whole substitution method has a total time complexity O(n,m) = n + n * (m ** 2) , n being the number of key-value pairs in the dictionary and m the number of characters in the variable. Usually, a variable ony has one character, but as discussed in the manual below, certain expressions will be recognized as one variable by the program. For example, in the abstraction λx.xyz, xyz is stored as one Variable("xyz").

### Function Abstractions
In the Abstraction class, function abstractions, a core concept in λ-calculus, are represented. This class models functions as abstractions over variables, comprising a variable and a body, which is itself a λ-term. Implementing this class was challenging but vital, as it embodies the way functions are defined and manipulated in λ-calculus. The __init__, __repr__, and __str__ methods within this class collectively facilitate the creation and representation of these abstractions, allowing for the essential operations of λ-calculus to be executed. In the __init__ method, two attributes of the abstraction (self) are defined: the variable (self.variable) and the body (self.body). 

The substitution in this class is rather straightforward, as these two parts will be put into the substitution method individually, which in the end leads back to the substitution in the variable class:
```python
def substitute(self, rules):
        return Abstraction(self.variable.substitute(rules), self.body.substitute(rules))
```
The time complexity of abstraction substitution is dependent on the amount of variables in the abstraction; the self.variable will always be O(n,m) = n + n * m, but the self.body can be an expression with a lot of expressions nested in it. In the end, it matters how often the variable substitution takes place.



### Function Applications
In the Application class, function applications, which are executions of abstractions in λ-calculus, are handled. This aspect of the interpreter was crucial as it manages how one λ-term (function) is applied to another (argument). Implementing the Application class involved creating a structure where both the function and the argument are λ-terms. 

The substitution method is very much alike to that of the abstraction class, as it substitutes the two parts, in this case the function and the argument, individually:
```python
def substitute(self, rules):
        return Application(self.function.substitute(rules), self.argument.substitute(rules))
```

The reduction method is more complicated, let us especially pay close attention to reduction when the function is an abstraction. The first part makes sure that the argument on which the functions is applied, does not occur in the function itself, as that can lead to different variables symbolized by the same character. This substitution is called capture-avoiding substitution:
```python
        if f"{self.argument}" in f"{self.function.body}" and f"{self.argument}" != f"{self.function.variable}":
            self.function = self.function.substitute({f"{self.argument}" : "t"})
```
The program searches for the argument in the body of the function, which has a time complexity of O(n) = n, with n as the number of characters in the body of the function. Next, if this capture-avoiding substitution should take place, the time complexity of the substitution itself again is dependent on the amount of variables inside the function.

What follows is a reduction for nested expressions, in which only free variables, variables that are not bound due to an abstraction, have to be substituted. For example, in the expression λx.xy, variable x is bound, while variable y remains unbound. Reduction for nested expressions looks as follows:
```python
        if isinstance(self.function.body, Abstraction) or isinstance(self.function.body, Application):
                
                #loop to ensure only free variables are replaced
                a = self.function.body
                while isinstance(a, Variable) == False:
                    if isinstance(a, Abstraction):
                        if f"{a.variable}" == f"{self.function.variable}":
                            break
                        else:
                            if isinstance(a.body, Abstraction) or isinstance(a.body, Application):
                                a = a.body
                            else:
                                a = a.substitute({f"{self.function.variable}" : f"{self.argument}"})
                                break
                    if isinstance(a, Application):
                        a.argument = a.argument.substitute({f"{self.function.variable}" : f"{self.argument}"})
                        a = a.function
                    
                return self.function.body
```
The character "a" is taken as a name that changes into more and more specific parts of the nested expression. It is subject to substitution if it is a variable in the body of an abstraction (e.g., if "a" is the body of λx.x) or if it is an argument in an application (e.g., if "a" is the argument of (λx.x) y). The while loop as shown above, halts when "a" is a variable, because then the innermost part of the expressions has been reached. The time complexity of substitution in this loop is O(n) = n, n being the number of characters of "a". How often such a substitution takes place, depends on the number of nested expressions and types of expressions. 

This complex structure begs the question if there is not a simpler method to substitute only free variables, unfortunately, we have not found one. The difficulty in this specific substitution is understanding how one can access all the different parts of an expression, as the "self" in this class only has two attributes: an argument and a function. It is tempting to think that it would be much easier to encorporate these rules of substituting free or bound variables in the variable class itself, but in the variable class it is impossible to know if the variable is bound or not, as the expression in which the variable occurs is not known in the variable class itself. It may be possible to write these rules in the abstraction class, which is then called upon in the reduction method. However, a consequence might be that substitution as a method independent of reduction might not function as well.
## Manual

### User Guide
This guide demonstrates how to use the λ-calculus interpreter:

#### Creating Variables
Create variables using the `Variable` class:
```python
x = Variable("x") # x
y = Variable("y") # y
```
The variable class only takes a string as input; otherwise it will raise a value error. 

### Creating Abstractions
Create function abstractions by giving two arguments (first a variable, then any other expression):
```python
abstraction = Abstraction(x, x)  # λx.x
abstraction2 = Abstraction(y, abstraction) # λy.λx.x

xy = Variable("xy")
abstraction3 = Abstraction(x, xy) # λx.xy
abstraction4 = Abstraction(y, abstraction3) # λy.λx.xy
```
As shown above, if the body of an abstraction consists of multiple variables, this should be written as one variable consisting of multiple characters, as the abstraction class only takes two arguments as input. Furthermore, if the second argument is not of the type variable, abstraction or application, the program will raise a value error; the first argument can only be a variable. 

### Creating Applications
Create function applications by giving two arguments:
```python
application = Application(abstraction, y)  # Applies (λx.x) to y, which results in the output (λx.x) y
application2 = Application(abstraction4, z) # Applies (λy.λx.xy) to z, which results in the output (λy.λx.xy) z
application3 = Application(abstraction4, x) # Applies (λy.λx.xy) to x, which results in the output (λy.λx.xy) x
```
The first argument will be applied to the second argument, as applications in the λ-calculus are left associative. Again, this class only takes applications, abstractions and variables as input.

### Representation
This function shows the classes of each part of an expression:
```python
representation = repr(abstraction) # Abstraction(Variable("x"), Variable("x"))
representation2 = repr(a) # Abstraction(Variable("a"), Abstraction(Variable("b"), Variable("ab")))
```
In other words: the representation function shows how to build a certain λ-term. 

### Substitution
Substitute variables within expressions:
```python
substitution = x.substitute({"x": "y"}) # output is y
substitution2 = abstraction.substitute({"x" : "y"}) # output is λy.y
```
The substitution input must be written as a dictionary

### Reduction
Execute β-reductions with the reduce method:
```python
reduced = application.reduce() # reduces "(λx.x) y", which results in output "y"
reduced2 = application2.reduce() # reduces "(λy.λx.xy) z", which results in output "λx.xz"
reduced3 = application2.reduce # reduces (λy.λx.xy) x, which results in output λt.tx
```
β-reductions reduce the application expression by substituting, in the body of the function, the argument (in the first example "y", in the second example "z") with the variable of the function ("λx" and "λy" respectively), which results in function body's with substituted variables ("y" and "λx.xz").
When we take a look at the third reduction, we can see that "y" is substituted with "x". However, as "x" is already present as a bound variable, we must takes measures as to not mix up these two different variables. Therefore, we first substitute the bound "x" with another symbol, which will be "t". The output that follows, is "λt.tx". These substitutions are often referred to as capture-avoiding substitutions. Note that in such cases, if a bound variable needs to be substituted before the reduction, the program will always substitute the present variable with a "t". This means that λ-terms, in which there is already a variable "t" present or in which such a substitute must take place more than once, will not have a correct reduction outcome. However, it is quite rare that such a substitution should happen more than once in the same expression. If the user avoids using "t" as a variable in the λ-terms, the program will work in most cases.

### fromString
Turn a string into a λ-term using the fromString method:
```python
a = LambdaTerm.fromString(r'\a b. a b') # turns string into the λ-term λa.λb.ab
b = LambdaTerm.fromstring(r"(\ a b. a b) (\x y. x y)") # (λa.λb.ab) λx.λy.xy
```
With this function, we can type a λ-term as a string and turn it into a λ-term; either a variable, abstraction or application. There are, however, a few notes to the use of this function. First of all, the "λ" is signified with a "\", because the "λ" is not easily accesible on a keyboard, but as the "\" symbol has a function in python of escaping the next character, it is important to use an r-string or raw string, so the "\" symbol will be read as a character of the string. Second, it is important that we use a space between each expression or variable, or the output will not be correct.


## Challenges and Solutions

One of the most challenging aspects was understanding and implementing beta-reduction. In the `Application` class, the process required ensuring that function abstractions were correctly applied to their arguments and appropriately simplified. Furthermore, it required the substitution of free variables, while leaving bound variables untouched. This may have been the hardest part of the beta-reduction and, to look back on the code critically, does not have a clear and easily understandable structure, although it has worked perfectly in our trials. 

The primary difficulty in the `fromstring` method was correctly parsing the string representations of lambda calculus expressions. These expressions can be complex, containing nested structures, and require accurate identification of variables, abstractions, and applications. The recursive nature of these expressions adds another layer of complexity, as it requires the parsing logic to work correctly at multiple levels of nesting. To overcome these challenges, we employed a recursive design that calls the `fromstring` method within itself to handle nested expressions. This method accurately maintains the hierarchical nature of lambda expressions. Smart string manipulation, such as replacing backslashes with lambda characters and using `split` to dissect the string, simplifies the parsing process. The use of reversal for variables during abstraction construction is a key innovation that respects the order of operations in lambda calculus, ensuring the correct assembly of the expression tree.


## Results

In this project, we have achieved to write a basis for the λ-calculus, and therefore have layed a foundation for an abstract formal system. Three classes have been succesfully implemented (Variable, Abstraction and Application) and with it, the most important functions have been computed, namely the substitution and beta-reduction. In addition, a fromString method has been added. In almost all trials, these functions have worked flawlessly, for very simple expressions as well as more advanced, nested expressions. Only the most complicated expressions, for example expressions consisting of more than five nested expressions, may not work flawlessly in our program.


## Conclusion and discussion

In conclusion, with three basic classes and functions for substitution and reduction of expressions, we have computed the basis for a λ-calculus; a formal system that can take abstract expressions as input and convert them into or apply them on other expressions. However, our program does have some limitations.

First of all, arithmetical and logical operators have not been added, so exact mathematics cannot yet be expressed in this λ-calculus. This would make a good next addition to the program; how such arithmetical and logical operators can be expressed in λ-terms, is described clearly in ["A Tutotrial Introduction to the Lambda Calculus"] by R. Rojas. 

Furthermore, as previously mentioned, λ-terms in which capture-avoiding substitution must take place more than once, will not have a correct output. This is very easily fixed: one can simply add more lines in which symbols are replaced not with "t", but with other symbols. There will, of course, always be some limit to the amount of capture-avoiding substitution one can do.

In future developments of the λ-calculus interpreter, we will aim to integrate a type system. This addition is expected to not only enhance the robustness of the interpreter but also contribute significantly to the field of programming language design. Incorporating a type system will allow the interpreter to handle a wider range of computational concepts and offer more precise error handling and validation capabilities. This enhancement aligns with advancing the interpreter towards a more sophisticated tool for exploring and experimenting with functional programming paradigms.


## References

- For an in-depth understanding of Lambda Calculus and its application in functional programming, refer to ["Lambda Calculus and Functional Programming"](https://lushunjian.gitee.io/2020/04/12/lyan-suan-yu-han-shu-shi-bian-cheng/), which provides comprehensive insights into the basics of λ-calculus.
- For beginners, a helpful guide to understanding λ-calculus can be found at ["Lambda Calculus for Absolute Dummies"](https://palmstroem.blogspot.com/2012/05/lambda-calculus-for-absolute-dummies.html).
- For a basic understanding of substitution, reduction, arithmetic and logical operators in the Lambda Calculus, refer to ["A Tutotrial Introduction to the Lambda Calculus"], R. Rojas, Freie Universität Berlin 2015, (https://arxiv.org/pdf/1503.09060.pdf).
- For a history of the Decision Problem and its relation to the λ-calculus, refer to ["The theory of the foundations of mathematics - 1870 to 1940-"], M. Scheffer, Eindhoven University of Technology 2002, https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=78ffac7cd5efaee3f8967e7f30473a8983dc1a93. 
  
