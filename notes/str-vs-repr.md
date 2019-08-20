# str() vs repr()

Both str() and repr() are used to get a string representation of object.

* [Difference](#differences)
* [Examples](#examples)

## Differences

* str() is used for creating output for end user while repr() is mainly used for debugging and development.
* repr() __compute the "official" string representation of an object__ (a representation that has all information about the object) and str() is used to __compute the "informal" string representation of an object__ (a representation that is useful for printing the object).


## Examples

Code:
```python
import datetime
today = datetime.datetime.now()
print(str(today))
print(repr(today))
```
Output:
```
2019-08-20 17:38:04.078030
datetime.datetime(2019, 8, 20, 17, 38, 4, 78030)
```
* str() displays today's date in a way that the user can understand easily.
* repr() prints "official" representation of a datetime object.

__How to make them work for user-defined classes?__

* A user defined class should have __repr__ if we need detailed information for debugging.
* If we think it would be useful to have a string version for users, we can also create a __str__ function.

For example:
```python
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __repr__(self):
        return "Rational(%s, %s)" % (self.real, self.imag)
    
    def __str__(self):
        return "%s + i%s" % (self.real, self.imag)

example = Complex(3, 4)
print(str(example))
print(repr(example))
```

Output:
```
3 + i4
Rational(3, 4)
```
