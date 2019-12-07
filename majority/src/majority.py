import sys, functools

def majority(nums, l, r):
  #print nums, l, r
  ind = int((l+r)/2)
  if l == r :
    return nums[l]
  left_m = majority(nums, l, ind)
  right_m = majority(nums, ind+1, r)
  print left_m, right_m, l, ind, r
  if left_m == right_m :
    return left_m

  vote_left_m = vote_right_m = 0
  for i in range(l, r+1):
    if(left_m == nums[i]): vote_left_m += 1
  for i in range(l, r+1):
    if(right_m == nums[i]): vote_right_m += 1
  
  m = left_m if (vote_left_m > vote_right_m) else right_m
  return m
  
def main():
  inp = sys.stdin.read().split()
  #print inp
  n = int(inp[0])
  nums = [int(x) for x in inp[1:n+1]]
  #print n, nums

  m = majority(nums, 0, n-1)
  c  = sum( 1 for i in range(n) if nums[i] == m)
  print m if c > len(nums)/2 else -1

MAINFUNC = main
###########################################################################################
import traceback

if __name__ == '__main__':
  try:
    ret = MAINFUNC()
  except Exception as e:
    details = traceback.format_exc()
    print "\nRuntime error: %s\n\n %s"%(e, details)
  else:
    pass