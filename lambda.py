from abc import ABC, abstractmethod
class LambdaTerm(ABC):
    @staticmethod
    def fromstring(s):
        if len(s) ==0:
            raise ValueError ("No string is implemented")

        s = s.replace('\\', 'λ').strip()

        #Remove parentheses or turn into application if written as (...) (...)
        if s.startswith("(") and s.endswith(")"):
            if ") (" in s:
                x = s.index(") (")
                return Application(LambdaTerm.fromstring(s[:x + 1]), LambdaTerm.fromstring(s[x + 1:]))
            else:
                s = s[1:-1]
            
        #Abstraction
        if s.startswith('λ'):
            parts = s[1:].split('.', 1)
            variables = parts[0].strip().split(' ')
            body = LambdaTerm.fromstring(parts[1].strip())
            for var in reversed(variables):
                body = Abstraction(Variable(var), body)
            return body
            
        #Application
        elif s.startswith("("):
            func = s[:-1]
            arg = s[len(s) - 1]
            return Application(LambdaTerm.fromstring(func.strip()), LambdaTerm.fromstring(arg.strip()))
            
        #Variable(s)
        else:
            s = s.replace(" ", "")
            return Variable(s)


class Variable(LambdaTerm):
    """Represents a variable."""
    def __init__(self, symbol):
        self.symbol = symbol

        if isinstance(self.symbol, str) == False:
            raise ValueError ("Only string allowed as input")
            
    def __repr__(self):
        return f"Variable('{self.symbol}')"

    def __str__(self):
        return self.symbol

    def substitute(self, rules):
        if isinstance(rules, dict) == False:
            raise ValueError ("Substitution argument must be dictionary in form {'a' : 'b'}")
        for item in rules.keys():
            if isinstance(item, str) == False:
                raise ValueError ("Only strings allowed as keys in dictionary")
                
        for var in self.symbol:
            if var in rules:
                if isinstance(rules.get(var), str) == False:
                    raise ValueError ("Only strings allowed as values in dictionary")
                self.symbol = self.symbol.replace(var, rules.get(var))
        return Variable(self.symbol)
   
class Abstraction(LambdaTerm):
    """Represents a lambda term of the form (λx.M)."""

    def __init__(self, variable, body):
        self.variable = variable
        self.body = body

        if isinstance(self.variable, Variable) == False:
            raise ValueError ("Only Variable allowed as first argument")
        if isinstance(self.body, Abstraction) == False and isinstance(self.body, Application) == False and isinstance(self.body, Variable) == False:
            raise ValueError ("Only Variable, Abstraction or Application allowed as second argument")
            
    def __repr__(self):
        return f"Abstraction({self.variable.__repr__()}, {self.body.__repr__()})"

    def __str__(self):
        if isinstance(self.body, Application):
            return f"λ{self.variable}.({self.body})"
        else:
            return f"λ{self.variable}.{self.body}"

    def __call__(self, argument):
        return self.body.substitute({self.body : argument})

    def substitute(self, rules):
        return Abstraction(self.variable.substitute(rules), self.body.substitute(rules))

class Application(LambdaTerm):
    """Represents a lambda term of the form (M N)."""

    def __init__(self, function, argument):
        self.function = function
        self.argument = argument

        if isinstance(self.function, Abstraction) == False and isinstance(self.function, Application) == False and isinstance(self.function, Variable) == False:
            raise ValueError ("Only Variable, Abstraction or Application allowed as first argument")
        if isinstance(self.argument, Abstraction) == False and isinstance(self.argument, Application) == False and isinstance(self.argument, Variable) == False:
            raise ValueError ("Only Variable, Abstraction or Application allowed as second argument")
            
    def __repr__(self):
        return f"Application({self.function}, {self.argument})"

    def __str__(self):
        return f"({self.function}) {self.argument}"

    def substitute(self, rules):
        return Application(self.function.substitute(rules), self.argument.substitute(rules))

    def reduce(self):
        #capture-avoiding substitution
        if f"{self.argument}" in f"{self.function.body}" and f"{self.argument}" != f"{self.function.variable}":
            self.function = self.function.substitute({f"{self.argument}" : "t"})
            
        
        #loop to ensure only free variables are replaced
        if isinstance(self.function.body, Abstraction) or isinstance(self.function.body, Application):
            a = self.function.body
            while "." in f"{a}":
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
        
        #beta-reduction  
        else:
            self.function = self.function.substitute({f"{self.function.variable}" : f"{self.argument}"})
            return self.function.body





