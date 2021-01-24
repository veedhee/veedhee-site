---
title: Random Python Tricks for Random Moods ✨ 
published: 2020-02-29T20:18:13Z
published_verbose: March 1, 2020
tags: python,regex,programming,regular-expressions
keywords: python
        beginners
header_image: https://www.hindustantimes.com/rf/image_size_444x250/HT/p2/2020/01/13/Pictures/_67acd868-35de-11ea-bb16-55584621af3a.jpg
canonical_url: https://medium.com/@vidbagadia/https-medium-com-vidbagadia-breaking-down-regular-expressions-0-a6675d7f102c
description: A Quick and Step by Ste Guide to Regular Expression using Python
---

If you have been using Python for quite a duration, you might already be familiar with all, or most of the tricks that we'll discuss below. But I guess it's always best to go over them briskly if it has been days you've used something in particular.

This will also include snippets, so you can just open your Python Interactive Shell and get started along with the examples.

####✨ Let's start with something small and one-liner
One of the major concepts of code is to write as less code as possible and make the code as reusable as possible. Functions is one way, yes - the one example everybody gives when talking about reusability. Let's take it down one notch.
Say you want a list in Python of length 5 with all elements as 1. Writing it as `lst = [1, 1, 1, 1, 1]` would be the way to go, right? But isn't it... repeating and we're diverting from the reusability everybody talks about?
Good news, we can cut our efforts here.
We can write it as:
`lst = [1]*5`
This is followed for strings too. If you want, for example, to hide a phone number and show only the last 3 digits of the number to the user, you can do something like:
```python
number = '1234567890'
hidden_number = "x"*7 + number[-3:]
'xxxxxxx890'
```

####✨ Reverse a string/ list in a snap
If you're coming from C/C++, you would probably remember iterating from the last element explicitly and copying it over to a new variable to get the reverse of a string/array. With Python, you can:
```python
a = [1, 2, 3, 4, 5]
a[::-1]
[5, 4, 3, 2, 1]
```

####✨ Else is not only if's sibling but also for's sibling
`else` is something all the tutorial covers with the conditionals. It's the same old _if this, then this; else this_. But did you know that we can use `else` with our other favourite member of the family - `for`?
Here's how it goes.
Do you remember times when you would `break` out of the loop when you found something, or a condition satisfied, and you'd use a flag right before you broke out o the loop to let the code after the loop know that you hit a `break` specifically and it was not the normal end of the loop? The use of `for..else` eliminates the use o flags wth a simpler syntax.
```python
a = [1, 3, 5, 7, 9]
b = [1, 3, 2, 5, 7, 9]

for i in a:
    if i % 2 == 0:
        print("list contains even elements")
        break
else:
    print("list has no even elements")

>>> list has no even elements

for i in b:
    if i % 2 == 0:
        print("list contains even elements")
        break
else:
    print("list has no even elements")

>>> list contains even elements
```

####✨ Revelio
Suppose you have a Python object, it can be anything - functions/ modules/ dictionaries, and it can be created by you or fetched via an API or third-party code. Often times, we need to know the list of attributes and methods that are available on the object. Instead of looking at the code, we can simply list those out using `dir`.
```python
class Example:
    name = "example"
    ex_id = 1
    def ex_print(self):
        print("example instance")

>>> ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ex_id', 'ex_print', 'name']
```
The above list is the list of attributes and methods of the object without the values. Notice the `ex_id`, `ex_print`, `name` in the list - this could come very handy while dealing with objects and to know what methods/attributes are available on them.

####✨ Passing attributes to a function for the unknown
Let's take a function where you have a bunch of optional arguments and you need to call the function a couple of times, every time with a different set of arguments.

If you've worked with Django ORM, you'd know that `filter()` accepts a bunch of filter values. For the ones who are new to this:
In Django, databases are made easier with an Object Relation Mapper. This also makes querying the database easier for certain records. Suppose we have a table of users who can be a staff user or not, and belong to a certain department of the organization. Long story short, we want a function that fetches the records based on different filter combinations and calculates their ranking points for the organization's benefit plans.
One way to do this would be to fetch records separately for each filter combination we need and then calculate the ranking points, or the other would be to perform the filtering inside the function. We'll go with the latter option for this article. Let's take a look in more detail:

For filtering, the syntax goes 
```python
records = UserTable.objects.filter(is_staff=<value>, department=<value>)
```

Instead of saying `department=None` (which would search for None values) when not wanting o filter on the department, we could just not pass the department to the filter - it's optional! But we do need only one instruction that would handle all the combinations and cases. Maybe an example would help:
```python
args1 = {'is_staff': True}
args2 = {'is_staff': True, 'department': 'Mgmt'}
args3 = {'department': 'Ops'}
```
Let these be the 3 filters you want to perform but you have a common function where you want to pass the filtering values:
```python
def get_ranking(args):
   members = UserTable.objects.filter(**args)
   for member in  members:
        # do something
        pass
```
With this, we do not need to worry about calling `get_ranking()` with different sets of arguments. We can:
```python
rankings = get_ranking(args1)
rankings = get_ranking(args2)
rankings = get_ranking(args3) 
```
Here's what the function actually unpacks to:
```python
members = UserTable.objects.filter(**args)
members = UserTable.objects.filter(is_staff=True)    # with args1
members = UserTable.objects.filter(is_staff=True, department='Mgmt')    # with args2
members = UserTable.objects.filter(department='Ops')    # with args3
```

---
That's all for this post, maybe I will come across some more exciting stuff (which I'm sure Python is full of) and continue this series for any and every mood that you might have. Let me know where and how you've used the tricks or plan to use them, so we can all bathe in the magic of Python.