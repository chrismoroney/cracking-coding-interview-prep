"""
1.2
Check Permutation
Given two strings, write a method to decide if one is a permutation of the other.
"""

"""
My approach to determining if one string is a permutation of another.
A permutation is a possible arrangement for a given set of elements. 
In this case, a permutation is an arrangement that can be assemebled with all the characters from one string. Using a dictionary (or map) can help you track the number of each character in a string, then compare with each character in the other string.
We can create a default case if the lengths of the two strings are not the same, since this wouldn't be a permutation.

Time Complexity: O(n)
Breakdown:
Iterate through string a: O(n)
Insert into dictionary: O(1) 
Iterate through string b: O(n)
Look up items in dictionary: O(1)
"""

def check_permutation(a: str, b: str) -> bool:
    if len(a) != len(b): return False

    char_counts = {}

    for char in a:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in b:
        if char not in char_counts or char_counts == 0:
            return False
        char_counts[char] -= 1

    return True


if __name__ == "__main__":
    print(check_permutation("abcde", "edabc"))
    print(check_permutation("hello", "world"))
    print(check_permutation("abcde", "abc"))