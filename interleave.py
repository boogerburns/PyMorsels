"""
I want you to write a function that accepts two lists and returns a new iterable with each of the given items
"interleaved" (item 0 from iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on).

Here's an example (which returns lists):

>>> interleave([1, 2, 3, 4], [5, 6, 7, 8])
[1, 5, 2, 6, 3, 7, 4, 8]

I want you to assume that the lists have the same length.
Don't worry at all about what to do with different length lists.
We'll actually handle that in a future exercise.

Bonus 1

As a bonus, I'd like you to make your function accept any iterable, not just lists/sequences ✔️:

>>> nums = [1, 2, 3, 4]
>>> interleave(nums, (n**2 for n in nums))
[1, 1, 2, 4, 3, 9, 4, 16]

Bonus 2

For a second bonus, return an iterator (for example a generator) from your interleave function instead of a list. ✔️

>>> interleave([1, 2, 3, 4], [5, 6, 7, 8])
<generator object interleave at 0x7f6174c18b48>
>>> list(interleave([1, 2, 3, 4], [5, 6, 7, 8]))
[1, 5, 2, 6, 3, 7, 4, 8]
This should allow your interleave function to accept infinitely long iterables (or other lazy iterables).
"""


def interleave(list1, list2):
    for i, j in zip(list1, list2):
        yield i
        yield j