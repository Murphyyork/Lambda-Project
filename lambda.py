from abc import ABC, abstractmethod
class LambdaTerm(ABC):
    @abstractmethod
    def fromstring(s):
        pass

    def substitute(self, rules):
        pass

    def reduce(self):
        pass

class Variable(LambdaTerm):
    """Represents a variable."""
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return f"Variable({self.symbol})"

    def __str__(self):
        return self.symbol

    def substitute(self, rules):
        return rules.get(self.symbol, self)


class Abstraction(LambdaTerm):
    """Represents a lambda term of the form (λx.M)."""

    def __init__(self, variable, body):
        self.variable = variable
        self.body = body

    def __repr__(self):
        return f"Abstraction({self.variable}, {self.body})"

    def __str__(self):
        return f"(λ{self.variable}.{self.body})"

    def __call__(self, argument):
        return self.body.substitute({self.variable.symbol: argument})

    def substitute(self, rules):
        if self.variable.symbol in rules:
            # Avoid variable capture
            del rules[self.variable.symbol]
        return Abstraction(self.variable, self.body.substitute(rules))

class Application(LambdaTerm):
    """Represents a lambda term of the form (M N)."""

    def __init__(self, function, argument):
        self.function = function
        self.argument = argument

    def __repr__(self):
        return f"Application({self.function}, {self.argument})"

    def __str__(self):
        return f"({self.function} {self.argument})"

    def substitute(self, rules):
        return Application(self.function.substitute(rules), self.argument.substitute(rules))

    def reduce(self):
        if isinstance(self.function, Abstraction):
            return self.function(self.argument).reduce()
        return Application(self.function.reduce(), self.argument.reduce())



