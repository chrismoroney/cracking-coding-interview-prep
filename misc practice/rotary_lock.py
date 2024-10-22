from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  ans = 0
  num = 1
  for c in C:
    clock = (c - num) % N
    counter_clock = (num - c) % N
    ans += min(clock, counter_clock)
    num = c 
  return ans


if __name__ == "__main__":
  N = 10
  M = 4
  C = [9, 4, 4, 8]
  print(getMinCodeEntryTime(N, M, C))