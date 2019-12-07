import sys, functools

def optimal_sequence(n):
  if n == 1: return [1]

  seq = []
  min_op = [0]*(n+1)
  for i in range(1, n+1):
    min_add1 = min_op[i-1] + 1
    min_mul2 = sys.maxint
    min_mul3 = sys.maxint
    if(i%2 == 0):
      min_mul2 = min_op[i/2] + 1
    if(i%3 == 0):
      min_mul3 = min_op[i/3] + 1
    min_op[i] = min(min_add1, min_mul2, min_mul3)
  
  #backtracking to construct the sequence
  i = min_op[n]
  while(i > 0):
    seq.append(n)
    i -= 1
    if (n % 3 == 0 and i == min_op[n/3]):
      n = n / 3
    elif(n % 2 == 0 and i == min_op[n/2]):
      n = n / 2  
    else:
      n = n - 1
  #print seq
  seq.reverse()
  return seq

# use x+1, x*2, x*3 to calculate x = n from x = 1
def main():
  input = sys.stdin.read()
  n = int(input)
  sequence = optimal_sequence(n)
  print(len(sequence) - 1)
  print " ".join([str(x) for x in sequence])

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