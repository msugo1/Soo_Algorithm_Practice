# https://leetcode.com/problems/reorder-data-in-log-files/

"""
logs have both digits and letters as elements with their own identifier
dig - for digits, and let - for letters

However, identifiers  don't specifically come in useful unless letters are tie
and can't be sorted without the usage of identifiers

First of all, separate those two types (letter for letter, digit for digit)

Python has isdigit here that judges if an element is a number or not.
split is useful when it comes to removing white space (as well as turn it into a list)

Lambda comes in real handy in sorting.
How to use
sorted  (a list that needs sorting, lambda x(a name as a variable): x.split()[1:], x.split()[0])
- reference point: sort by letters first if can't, use identifier

(ex. let1 art can, let2 art can / split will create two lists automatically for these
like [let1, art, can], [let2, art, can]
then, try ordering by elements from index 1 as elements on index 0 are just identifiers
but they have exactly the same letters so now compare identifier(letters.split()[0]) here
let1 > let2 so the order would be the same as it already was)

or
sort    (lambda x: (x.split()[1:], x.split()[0]))
NOTE: sort takes no arguments whereas sorted does (one argument)

then return the two list by adding those two (+ combines even lists together in Python) the letter one first followed by
the digit one.

"""
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        sorted_list = sorted(letters, key=lambda x: (x.split()[1:], x.split()[:1]))

        return sorted_list + digits