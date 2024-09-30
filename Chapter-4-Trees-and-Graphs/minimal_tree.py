'''
4.2
Minimal Tree

Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
'''

import random

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_min_tree(arr: list) -> TreeNode:
    return minimal_tree(arr, 0, len(arr)-1)

def minimal_tree(arr: list, beg: int, end: int) -> TreeNode:
    if beg > end: return None

    mid = (beg + end) // 2
    node = TreeNode(arr[mid])

    node.left = minimal_tree(arr, beg, mid-1)
    node.right = minimal_tree(arr, mid+1, end)

    return node
    

def generate_sample_list(size: int) -> list:
    if size <= 0:
        return None
    if size > 100: 
        size = 100

    return_list = set()
    while len(return_list) < size:
        return_list.add(random.randint(0, 99))

    sorted_list = sorted(return_list)
    return sorted_list

"""
Helper function to print the tree in-order for verification
"""
def print_tree(node: TreeNode):
    if not node:
        return
    print_tree(node.left)
    print(node.val)
    print_tree(node.right)

if __name__ == "__main__":
    arr = generate_sample_list(80)
    tree = list_to_min_tree(arr)
    print_tree(tree)
