# collections

* [namedtuple()](#namedtuple())
* [deque](#deque)
* [Counter](#counter)
* [OrderedDict](#ordereddict)
* [defaultdict](#defaultdict)

## namedtuple()

_Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index._

Example:

```python
import collections
Person = collections.namedtuple('Person', ['gender', 'age', 'x'])
Andy = Person(gender='Male', age=18, x=100)
print(Andy)
# output: Person(gender='Male', age=18, x=100)
print(Andy[0])
# output: Male
print(Andy.age + Andy.x)
# output: 118
```

Example:

```python
import collections
Person = collections.namedtuple('Person', ['gender', 'age', 'x'])
tmp = ['Female', 19, 50]
Emily = Person._make(tmp)
print(Emily)
# output: Person(gender='Female', age=19, x=50)
tmp = {'gender': 'male', 'age': 40, 'x': 80}
Kevin = Person(**tmp)
print(Kevin)
# output: Person(gender='male', age=40, x=80)
```

## deque

_Deques are a generalization of stacks and queues (the name is short for "double-ended queue")._

_Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction._

Methods:

**append(x)**:  
Add x to the right side of the deque.

**appendleft(x)**:  
Add x to the left side of the deque.

**clear()**:  
Remove all elements from the deque leaving it with length 0.

**copy()**:  
Create a shallow copy of the deque.

**count(x)**:  
Count the number of the deque elements equal to x.

**insert(i, x)**:  
Insert x into the deque at position i.

**pop()**:  
Remove and return an element from the right side of the deque.

**popleft()**:  
Remove and return an element from the left side of the deque.

## Counter

_A Counter is a dict subclass for counting hashable objects._

Example:

```python
import collections
classmates = ['Kevin', 'Andy', 'Mike', 'Kevin']
c = collections.Counter(classmates)
print(c['Kevin'])
# output: 2
print(c['Henry'])
# output: 0
```

Example:

```python
import collections
classmates = ['Kevin', 'Andy', 'Mike', 'Kevin']
c = collections.Counter(classmates)
c['Andy'] = 0
print(c)
# output: Counter({'Kevin': 2, 'Mike': 1, 'Andy': 0})
del c['Andy']
print(c)
# output: Counter({'Kevin': 2, 'Mike': 1})
```

Example;

```python
import collections
classmates = ['Kevin', 'Andy', 'Mike', 'Kevin']
c = collections.Counter(classmates)
print(sorted(c.elements()))
# output: ['Andy', 'Kevin', 'Kevin', 'Mike']
print(c.most_common(1))
# output: [('Kevin', 2)]
```

## OrderedDict

_An **ordered** dict subclass._

Example:

```python
import collections
tmp = (('A', 1), ('B', 2), ('C', 3))
r_dict = collections.OrderedDict(tmp)
[print(k, v) for k, v in r_dict.items()]
# output: A 1 B 2 C 3
r_dict.move_to_end('A')
[print(k, v) for k, v in r_dict.items()]
# output: B 2 C 3 A 1
```

## defaultdict

_A subclass of the built-in dict class._

Example:

```python
import collections
members = [('male', 'John'), ('male', 'Jack'), ('Female', 'Lucy')]
result = collections.defaultdict(list)
for gender, name in members:
    result[gender].append(name)
print(result)
# output: defaultdict(<class 'list'>, {'male': ['John', 'Jack'], 'Female': ['Lucy']})
```