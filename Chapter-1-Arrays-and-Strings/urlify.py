"""
1.3
URLify
Write a method to replace all spaces in a string with '%20'. 
You may assume that the string has sufficient space at the end to hold the additional characters, and
that you are given the "true" length of the string. (Note: If implementing in Java please 
use a character array so that you can perform this operation in place.)

EXAMPLE
Input:      "Mr John Smith      ", 13
Output:     "Mr%20John%20Smith"
"""

"""
Using a simple replace method in python
"""
def urlify(s: str, l: int) -> str:
    return s.replace(' ', '%20')


if __name__ == "__main__":
    print(urlify("Hello World!", 12))