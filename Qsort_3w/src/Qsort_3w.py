import sys, functools
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    i = l+1
    L = []
    C = [x]
    R = []
    lt = l
    gt = r+1
    for i in range(l+1, r+1):
      if a[i] < x:
        L.append(a[i])
        lt += 1
      elif a[i] == x:
        C.append(a[i])
      else:
        R.append(a[i])
        gt -= 1
    #print x, L, C, R
    a[l:r+1] = L + C + R
    #print a[l:r+1], lt, gt
    return lt-1, gt

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #m = partition2(a, l, r)
    
    #use partition3
    lt, gt = partition3(a, l, r)

    randomized_quick_sort(a, l, lt);
    randomized_quick_sort(a, gt, r);
  
def main():
  input = sys.stdin.read()
  input = list(map(int, input.split()))
  n, a = input[0], input[1:]
  randomized_quick_sort(a, 0, n - 1)
  
  print " ".join([str(x) for x in a])

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