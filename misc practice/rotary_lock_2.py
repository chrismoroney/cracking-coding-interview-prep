from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
    ans = 0
    lock_one = 1
    lock_two = 1
    
    for c in C:
        dist_one_clockwise = (c - lock_one) % N
        dist_one_counterclockwise = (lock_one - c) % N
        dist_one = min(dist_one_clockwise, dist_one_counterclockwise)
        
        dist_two_clockwise = (c - lock_two) % N
        dist_two_counterclockwise = (lock_two - c) % N
        dist_two = min(dist_two_clockwise, dist_two_counterclockwise)
        
        if dist_one <= dist_two:
            ans += dist_one
            lock_one = c 
        else:
            ans += dist_two
            lock_two = c
    return ans


if __name__ == "__main__":
  N = 10
  M = 4
  C = [9, 4, 4, 8]
  print(getMinCodeEntryTime(N, M, C))