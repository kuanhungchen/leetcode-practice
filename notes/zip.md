# zip

The purpose of zip() is to __map the similar index of multiple containers__ so that they can be used just using as single entity.

* [zip](#zip())
* [zip(*)](#zip(*))

## zip()

Code:
```python
names = ["John", "Mary", "Hank"]
ages = [40, 18, 25]
mapped = zip(names, ages)
print(mapped)
```

Output:
```python
[('John', 40), ('Mary', 18), ('Hank', 25)]
```

We can see that the two lists is mapped to a list. And this can be useful in the next example.

Code:
```python
names = ["John", "Mary", "Hank"]
ages = [40, 18, 25]
mapped = zip(names, ages)

for n, a in mapped:
    print("Name: %s, Age: %d" % (n, a))
```

Output:
```python
Name: John, Age: 40
Name: Mary, Age: 18
Name: Hank, Age: 25
```

Using zip() makes us easier to manipulate data in multiple containers. 

## zip(*)

Code:
```python
member = [("John", 40), ("Mary", 18), ("Hank", 25)]
unmapped = zip(*member)
print(unmapped)
```

Output:
```python
[('John', 'Mary', 'Hank'), (40, 18, 25)]
```

Zip(*) is kind of an opposite operation of zip(). After zip(*), data will be separated into multiple containers. And this can be useful in the next example.

Code:
```python
member = [("John", 40), ("Mary", 18), ("Hank", 25)]
names, ages = zip(*member)
print(names)
print(ages)
```

Output:
```python
('John', 'Mary', 'Hank')
(40, 18, 25)
```

In this example, we use zip(*) to get the two origin lists.