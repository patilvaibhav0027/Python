# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

class Solution:
    def isUgly(self, n: int) -> bool:
        n=int(input("enter number:"))
        if n>0:
            while(n%2==0):
                n=n//2
            while(n%3==0):
                n=n//3
            while(n%5==0):
                n=n//5
            return n==1
        return False

