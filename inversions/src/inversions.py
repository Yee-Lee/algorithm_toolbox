import sys, functools

def get_number_of_inversions(a, b, left, right):
  number_of_inversions = 0
  if right - left <= 1:
    return number_of_inversions
  ave = (left + right) // 2
  number_of_inversions += get_number_of_inversions(a, b, left, ave)
  number_of_inversions += get_number_of_inversions(a, b, ave, right)
  #write your code here------------------------------------------------
  
  #b[left:ave] and b[ave:right] are two sorted arrays
  b[left:right] = a[left:right]
  ##print left, ave, right, b[left:ave], b[ave:right]
  i, j = left, ave
  k = i
  while(i < ave and j < right):
    if b[i] <= b[j]:
      a[k] = b[i]
      i += 1
    else:
      a[k] = b[j]
      j += 1
      number_of_inversions += (ave - i)
      ##print ave - i
    k += 1
  while i < ave:
    a[k] = b[i]
    i+=1
    k+=1
  while j < right:
    a[k] = b[j]
    j+=1
    k+=1
  ##print a
  return number_of_inversions 
  
def main():
  input = sys.stdin.read()
  input = list(map(int, input.split()))
  n, a = input[0], input[1:]
  b = n * [0]
  print(get_number_of_inversions(a, b, 0, len(a)))

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