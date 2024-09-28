"""
1.4
Palindrome Permutation

Given a string, write a function to check if it is a permutation palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.
You can ignore casing and non-letter characters.

EXAMPLE

Input:      Tact Coa
Output:     True (permutations: "taco cat", "atco cta", etc.)
"""

def palindrome_permutation(s: str):
    char_counts = {}
    s = s.lower().replace(' ', '')
    for i in range(len(s)):
        char_counts[s[i]] = char_counts.get(s[i], 0) + 1
    
    values = set(char_counts.values())
    num_odd_chars = 0
    for val in values:
        if len(s) % 2 == 0 and val % 2 == 1:
            return False
        
        if len(s) % 2 == 1:
            if val % 2 == 1:
                num_odd_chars += 1
        if num_odd_chars > 1:
            return False
    
    return True
            

if __name__ == "__main__":
    print(palindrome_permutation("madam"))