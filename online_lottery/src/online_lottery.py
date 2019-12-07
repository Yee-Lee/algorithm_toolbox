import sys, functools
import random

def fast_count_segments(starts, ends, points):
  cnt = [0] * len(points)
  #write your code here

  aug_arr = []
  for p in starts:
    aug_arr.append((p, 1))
  for p in ends:
    aug_arr.append((p, -1))
  for p in points:
    aug_arr.append((p, 0))
  
  aug_arr = sorted(aug_arr, key=lambda x: x[0])

  points_count_map = {}
  acc = 0
  for p,sign in aug_arr:
    if sign == 1: acc += 1
    elif sign == -1 : acc -= 1
    else:
      points_count_map[p] = acc
  #print points_count_map
  for i, p in enumerate(points):
    cnt[i] = points_count_map[p]
  #print cnt
  return cnt

  
def main():
  input = sys.stdin.read()
  data = list(map(int, input.split()))
  n = data[0]
  m = data[1]
  starts = data[2:2 * n + 2:2]
  ends   = data[3:2 * n + 2:2]
  points = data[2 * n + 2:]
  #use fast_count_segments
  cnt = fast_count_segments(starts, ends, points)
  print " ".join([str(x) for x in cnt])

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