#!/usr/bin/python3

# This script will showcase how to do simple math operations in Python


# Gauss summation
def summation(n):
    return int(n*(n+1)/2)


# This part is executed when running from commandline
if __name__ == "__main__":
    
    number = 10
    print(f"The Gauss summation of {number} is {summation(number)}")
