\ Lambda Calculus Project Report
## Author: Futao Yan, Kristian
## Github: yorkmurphy0@gmail.com, kristianderoos@gmail.com
## Introduction

Lambada Calculus, akin to the Turing Machine, utilizes a mechanized approach to prove and deduce complex problems in mathematics.

Lambda Calculus is an essential conceptual framework in computer science, particularly in the field of programming languages. This project aims to implement a lambda calculus interpreter and discuss its implications for programming language design.

In mathematics, a formal system, such as λ-calculus, is a symbolic game that begins with axioms and involves extensive deduction and proof, forming a self-contained system with axioms, theorems, corollaries, and conjectures. Formal languages are the tools used to describe these systems, providing a structured way to express and manipulate their components.


## Background

In 1928, a mathematical challenge was posed by David Hilbert and Wilhelm Ackermann, later known as the "Entscheidungsproblem", or Decision Problem. It asks the question if there is an algorithm that can judge for every logical statement if it is provable or not. The use of such an algorithm for mathematics would be great: for example, one could test for conjectures if they are provable or not. However, to take on this challenge, one first had to answer the question what an algorithm can do. In other words: what are the limits to computability?

Alonzo Church, a pioneering mathematician and logician, answered this  question in a publication in 1932 by developing the λ-calculus as a universal computational model. This system, foundational to functional programming, introduced the concept of functions operating on and returning other functions, symbolized by the Greek letter lambda (λ). According to Church's Thesis in 1936, the λ-calculus encompasses all possible computational functions, en can therefore be seen as a blueprint for all possible algorithms, as it describes the essential functionality of any algorithm: it takes an input, changes it with substitution and reduction, and then gives you an output. 

Shortly after Church's publication, in 1936, another pioneering computer scienstist named Alan Turing, developed his Turing Machine, which is a theoretical machine that in essence works the same as the λ-calculus, although Turing developed this machine independently from Church's λ-calculus. On the basis of this Turing Machine, Alan Turing managed to answer the decision problem negatively: he showed that it is impossible to derive for every logical statement if it is provable or not.

In computer science's evolution, the late 1950s marked a pivotal point with John McCarthy's development of Lisp at MIT. This language, inspired by Alonzo Church's λ-calculus, showcased the practical implementation of theoretical computational concepts on von Neumann computers. The creation of Lisp machines at MIT's AI lab further materialized λ-calculus in hardware form. While adapting to changing computing architectures, Lisp evolved, integrating functional and traditional programming aspects, symbolizing the adaptability and potential of functional languages in advancing computational theory.

Writing a λ-calculus program might at first sight seem like a fairly simple task, as it only consists of substitution and reduction of λ-terms. However, the difficulty lies in understanding the λ-calculus as an abstract machine and writing a program that works for even the most complex λ-terms. The λ-calculus, however simple, has a wide range of capabilities.

## Algorithm and Implementation

### Design

In the implementation of the λ-calculus interpreter, the algorithm design employs object-oriented principles, defining distinct classes for each λ-calculus construct: Variable, Abstraction, and Application. Each class encapsulates specific behaviors and properties of these constructs. The Variable class, for instance, represents variables with unique symbols. Abstraction handles λ-function abstractions, combining a variable with a body expression, while Application manages the application of one λ-term to another. Central to the design is the implementation of substitution methods and β-reduction logic, allowing for the evaluation and simplification of λ-calculus expressions in a manner true to the theoretical foundation of λ-calculus.

### Coding Process
The coding process for your λ-calculus interpreter involved implementing three key classes: Variable, Abstraction, and Application. Each class represents a fundamental aspect of λ-calculus:

Variable: Handles the representation of variables, identified by symbols.

Abstraction: Manages function abstractions, defined as a pair of a variable and a body expression.

Application: Deals with the application of one λ-term to another.
In each class, methods like substitute and reduce were implemented to facilitate the core operations of λ-calculus, such as substitution and β-reduction. This approach ensures your interpreter can process λ-calculus expressions, reflecting both the structural and operational aspects of λ-calculus theory.

### Variables

In the implementation of the Variable class, the focus was on representing variables in λ-calculus expressions. Each variable is identified by a unique symbol, encapsulated within the class. The __init__ method initializes a variable with its symbol, while the __repr__ and __str__ methods provide string representations for ease of understanding and debugging. The substitute method allows for the substitution of variables within expressions, a critical operation in λ-calculus. This representation is foundational for handling variables within the broader context of the λ-calculus interpreter.

### Function Abstractions

In the Abstraction class, function abstractions, a core concept in λ-calculus, are represented. This class models functions as abstractions over variables, comprising a variable and a body, which is itself a λ-term. Implementing this class was challenging but vital, as it embodies the way functions are defined and manipulated in λ-calculus. The __init__, __repr__, __str__, and substitute methods within this class collectively facilitate the creation and representation of these abstractions, allowing for the essential operations of λ-calculus to be executed.

### Function Applications

In the Application class, function applications, which are executions of abstractions in λ-calculus, are handled. This aspect of the interpreter was crucial as it manages how one λ-term (function) is applied to another (argument). Implementing the Application class involved creating a structure where both the function and the argument are λ-terms. The substitute method in this class plays a key role in enabling variable substitution within these applications, while the reduce method applies the logic of β-reduction, central to executing λ-calculus expressions accurately.

### Code Snippets

#### Variable Class
```python
class Variable(LambdaTerm):
    def __init__(self, symbol):
        self.symbol = symbol
    # ... other methods ...
```
#### Abstraction Class
```python
class Abstraction(LambdaTerm):
    def __init__(self, variable, body):
        self.variable = variable
        self.body = body
    # ... other methods ...
```
#### Application Class
```python
class Application(LambdaTerm):
    def __init__(self, function, argument):
        self.function = function
        self.argument = argument
    # ... other methods ...
```

## Manual
### User Guide

This guide demonstrates how to use the λ-calculus interpreter:

#### Creating Variables
Create variables using the `Variable` class:
```python
x = Variable("x") # x
y = Variable("y") # y
```


Create function abstractions by giving two arguments (first a variable, then any other expression):
```python
abstraction = Abstraction(x, x)  # λx.x
abstraction2 = Abstraction(y, abstraction) # λy.λx.x

xy = Variable("xy")
abstraction3 = Abstraction(x, xy) # λx.xy
abstraction4 = Abstraction(x, "xy") # λx.xy
abstraction5 = Abstraction(y, abstraction4) # λy.λx.xy

```
As shown above, if the body of an abstraction consists of multiple variables, we can write this as a string, "xy", or as one variable. They will be treated as single variables in the substitution and reduction functions, but as the Abstraction class only takes two arguments, the body must be one entity.

Create function applications by giving two arguments:
```python
application = Application(abstraction, y)  # Applies (λx.x) to y, which results in the output (λx.x) y
application2 = Application(abstraction5, z) # Applies (λy.λx.xy) to z, which results in the output (λy.λx.xy) z
application3 = Application(abstraction5, x) # Applies (λy.λx.xy) to x, which results in the output (λy.λx.xy) x
```
The first argument will be applied to the second argument, as applications in the λ-calculus are left associative.

Substitute variables within expressions:
```python
substitution = x.substitute({"x": "y"}) # output is y
substitution2 = abstraction.substitute({"x" : "y"}) # output is λy.y
```

Execute β-reductions with the reduce method:
```python
reduced = application.reduce() # reduces "(λx.x) y", which results in output "y"
reduced2 = application2.reduce() # reduces "(λy.λx.xy) z", which results in output "λx.xz"
reduced3 = application2.reduce # reduces (λy.λx.xy) x, which results in output λt.tx
```
β-reductions reduce the application expression by substituting, in the body of the function, the argument (in the first example "y", in the second example "z") with the variable of the function ("λx" and "λy" respectively), which results in function body's with substituted variables ("y" and "λx.xz").
When we take a look at the third reduction, we can see that "y" is substituted with "x". However, as "x" is already present as a bound variable, we must takes measures as to not mix up these two different variables. Therefore, we first substitute the bound "x" with another symbol, which will be "t". The output that follows, is "λt.tx". Note that in such cases, if a bound variable needs to be substituted before the reduction, the program will always substitute the present variable with a "t". This means that λ-terms, in which there is already a variable "t" present or in which such a substitute must take place more than once, will not have a correct reduction outcome. However, it is quite rare that such a substitution should happen more than once with the same string. If the user avoids using "t" as a variable in the λ-terms, the program will work in most cases.

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

In future developments of the λ-calculus interpreter, I aim to integrate a type system. This addition is expected to not only enhance the robustness of the interpreter but also contribute significantly to the field of programming language design. Incorporating a type system will allow the interpreter to handle a wider range of computational concepts and offer more precise error handling and validation capabilities. This enhancement aligns with advancing the interpreter towards a more sophisticated tool for exploring and experimenting with functional programming paradigms.


## References

- For an in-depth understanding of Lambda Calculus and its application in functional programming, refer to ["Lambda Calculus and Functional Programming"](https://lushunjian.gitee.io/2020/04/12/lyan-suan-yu-han-shu-shi-bian-cheng/), which provides comprehensive insights into the basics of λ-calculus.
- For beginners, a helpful guide to understanding λ-calculus can be found at ["Lambda Calculus for Absolute Dummies"](https://palmstroem.blogspot.com/2012/05/lambda-calculus-for-absolute-dummies.html).
- For a basic understanding of substitution, reduction, arithmetic and logical operators in the Lambda Calculus, refer to ["A Tutotrial Introduction to the Lambda Calculus"], R. Rojas, Freie Universität Berlin 2015, (https://arxiv.org/pdf/1503.09060.pdf).
- For a history of the Decision Problem and its relation to the λ-calculus, refer to ["The theory of the foundations of mathematics - 1870 to 1940-"], M. Scheffer, Eindhoven University of Technology 2002, https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=78ffac7cd5efaee3f8967e7f30473a8983dc1a93. 
  
