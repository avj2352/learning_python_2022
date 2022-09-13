# Python Basics - Egghead.io

## Important Links

- [Python Basics](https://egghead.io/lessons/python-install-python)

## Installing Python (Macbook)

```bash
# install python
brew install python3

# check python version
python -V
```

- Python 3 (with 10 version updates)
- Python 3 was released in 2008

## Installing Python (Windows)

# FIXME: update notes

## Python 3 REPL

- NOTE: print() is a function in Python 3, not a keyword

## Check for None (NULL) in Python3

In Python, `null` variables are known as `None`. Let's create a variable and set it to none. The correct way to check for this is with the `is` operator. There's another way you could do it. You could do if `foo = none` and that works, but it's not the preferred way in Python.

```python
# None datatype
# similar to NULL type in Javascript
# But Javascript also has an undefined 😅
foo = None
if foo is None:
    print("It's not there")
if foo == None:
    print("It's still not there")
```
### IS versus ==

- In Python everything has an `ID` and a `value`.
- Think of `ID` as a pointer
- So in the above code `foo` and `None` share the same `ID`
- Whenever we use the is operator, it does an ID comparison
- Whereas if we use the equals, then it requires a dictionary `dict` look up and has to iterate through it to do the comparison. 
- The end result is the is, `is` much faster than using `equals(==)` when checking for `none`.

