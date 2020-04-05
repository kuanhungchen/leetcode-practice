# lru_cache

This a decorator to wrap a function with a memorizing callable that saves up to maxsize most recent calls. It can save time when an expensive or I/O bound function is periodically called with the same arguments.

## Usage

@functools.lru_cache(user_function)
@functools.lru_cache(maxsize=128, typed=False)

If _user_function_ is specified, it must be a callable. This allows the _lru_cache_ decorator to be applied directly to a user function, leaving the _maxsize_ at its default value of 128.

If _maxsize_ is set to `None`, the LRU feature is disabled and the cache can grow without bound. The LRU feature performs best when _maxsize_ is a power-of-two.

If _typed_ is set to true, function arguments of different types will be cached separately. For example, f(3) and f(3.0) will be treated as distinct calls with distinct results.

## Example:

```python
@lru_cache
def count_vowels(sentence):
    sentence = sentence.casefold()
    return sum(sentence.count(vowel) for vowel in 'aeiou') 

```


Example of an LRU cache for static web content:
```python
@lru_cache(maxsise=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'
```


Example of efficiently computing Fibonacci numbers using a cache to implement a dynamic programming technique:
```python
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2) 
```