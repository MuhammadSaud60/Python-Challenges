'''
Create a function counter() that:

  Tracks how many times it has been called.

  Returns the current count.

'''


def counter():
   counter.count = getattr(counter, 'count', 0) + 1

   return counter.count


print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
