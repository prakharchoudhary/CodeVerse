"""
Problem:
The eight queen's problem is a classic recursion problem.
Given 8 queens on a chessboard and the position of the first queen we must determine the locations
of all other queen such that no queen threatens the other.

Solution:

1. define what a conflict is, that is the conditions in which a queen threatens the other.

2. Now consider the base case:
	Only the last queen has to be placesd, then we must check for conflict with all other queens for all present options,
	until we either exhaust all our options or find the right location

3. Now think of the recursive case for the same. 

"""
import random

def conflict(state, nextX):
	"""
	checks if for a given postion is the new queen threatened by any other queen.
	"""
	nextY = len(state)
	for i in range(nextY):
		if abs(state[i]-nextX) in (0, nextY-i):
			return True
	return False

def queens(num=8, state=()):
	"""
	uses an exhasutive recursive approach to find the position for each queen to be places
	"""	
	for pos in range(num):
		if not conflict(state, pos):
			if len(state) == num-1:
				'''
				this is the base case
				'''
				yield (pos,)
			else:
				'''
				when more than 1 queen are left to be placed
				'''
				for result in queens(num, state + (pos,)):
					yield (pos,) + result


def prettyprint(solution):
	"""
	show the out as queen placed on a chessboard
	"""
	def line(pos, length=len(solution)):
		return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)

	for pos in solution:
		print(line(pos))

if __name__ == "__main__":
	
	num = int(input("Enter the number of queens: "))
	solutions = list(queens(num))
	print("There are {} solutions.".format(len(solutions)))
	ques = input("Do you wish to see the postions of queens on chess board?[y/n]")
	while True:
		if ques == 'y':	
			prettyprint(random.choice(solutions))
			#prints any random solution out of the many obtainted
			ques = input("Wanna try another?[y/n]")

		if ques == 'n':
			print("Tada! We have the solution(s).")
			break
		
		else:
			ques = input("Oops! Looks like your keyboard is giving you troubles, enter either 'y' or 'n':")

