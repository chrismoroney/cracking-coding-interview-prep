"""
1.1
Is Unique
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""


"""
My approach to determining if every char in a string is unique without additional data structures. 
Without additional datastructures, I would iterate through the string and compare each element to the subsequent elements. 

Time Complexity: O(n^2)
Breakdown:
Iterating through string: O(n)
Comparing next value: O(n) for every iteration
"""
def is_unique_without_data_structures(s: str) -> bool:
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True



"""
My approach to determining if every char in a string is unique. 
In a set, you cannot have duplicate elements. This means that if there are duplicates in the string, the length of the set will be different from the length of the string. 

Time complexity: O(n).
Breakdown: 
Creating the set: O(n)
Comparing length of set vs. string: O(1)
"""
def is_unique(s: str) -> bool:
    return len(s) == len(set(s))
    


if __name__ == "__main__":
    test_true = "abcdefg";
    test_false = "butterfly";
    print(test_true + ": ", is_unique(test_true))
    print(test_false + ": ", is_unique(test_false))

    print(test_true + ": ", is_unique_without_data_structures(test_true))
    print(test_false + ": ", is_unique_without_data_structures(test_false))