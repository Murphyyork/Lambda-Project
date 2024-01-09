# Voorbeeldgedrag Lambdacalculus

```python
>>> x = Variable('x')
>>> id = Abstraction(Variable('a'), Variable('a'))
>>> id_x = Application(id, x)

>>> for t in [x, id, id_x]: print(str(t))
...
x
λa.a
(λa.a) x

>>> for t in [x, id, id_x]: print(repr(t))
...
Variable('x')
Abstraction(Variable('a'), Variable('a'))
Application(Abstraction(Variable('a'), Variable('a')), Variable('x'))

>>> # In het algemeen zou moeten gelden:  eval(repr(t)) == t

>>> print(id_x, "-->", id_x.reduce())
(λa.a) x --> x

>>> true = Lambdacalculus.fromString(r"\a b. a")
>>> repr(true)
"Abstraction(Variable('a'), Abstraction(Variable('b'), Variable('a')))"
>>> str(true)
'λa.λb.a'  # of 'λa b.a'
```
