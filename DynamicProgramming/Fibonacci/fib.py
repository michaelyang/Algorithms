#!/usr/bin/env python2.7
import sys, os

def fibRecursive(n):
	memo = [None] * (n+1)
	def fib(n, memo):
		if memo[n] is not None:
			return memo[n]
		if n <= 2:
			f = 1
		else:
			f = fib(n-1, memo)+fib(n-2, memo)
		memo[n] = f
		print memo
		return f
	return fib(n, memo)

def fibBottomUp(n):
	if n <= 2:
		return 1
	bottomUp = [None] * (n+1)
	bottomUp[1] = 1
	bottomUp[2] = 1
	for i in range(3, n+1):
		bottomUp[i] = bottomUp[i-1] + bottomUp[i-2]
		print bottomUp
	return bottomUp[n]

def main():
	n = int(input("fib(n) for n = "))
	print fibBottomUp(n)
	print fibRecursive(n)

if __name__ == "__main__":
	main()