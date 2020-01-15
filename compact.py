"""
Hi! ✨

For this week's exercise I want you to write a function that accepts a sequence (a list for example) and returns a new iterable (anything you can loop over) with adjacent duplicate values removed.

For example:

>>> compact([1, 1, 1])
[1]
>>> compact([1, 1, 2, 2, 3, 2])
[1, 2, 3, 2]
>>> compact([])
[]
There are two bonuses for this exercise.

I recommend solving the exercise without the bonuses first and then attempting each bonus separately.
"""


def compact(inlist):
    previousitem = object()
    for i in inlist:
        if i != previousitem:
            yield i
            previousitem = i
