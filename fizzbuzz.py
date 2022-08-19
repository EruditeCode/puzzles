"""
Fizzbuzz Program
----------------
Generates a list of integers in a given range.
If those integers are multiples of a series of
rules a key word is returned instead of the
number.

Rule Requirements
-----------------
Avoid factors of previous rule numbers.
Must always order the largest multicomponent
tuple before a lesser tuple. If there are 
multiple tuples of the same length, order by
value size (largest to smallest).

Video Link
----------
A video walkthrough for this code:
##########
"""

rules = {(3, 5):"Fizzbuzz", (7,):"Buzz", (3,):"Fizz"}

def fizzbuzz(r_min=0,r_max=100):
	for i in range(r_min, r_max + 1):
		if i != 0:
			print(rule_check(i))
		else:
			print(i)

def rule_check(number):
	for key in rules.keys():
		multiple = True
		for value in key:
			if number % value > 0:
				multiple = False
				break
		if multiple is True:
			return rules[key]
	return number

if __name__ == "__main__":
	fizzbuzz(0, 20)
