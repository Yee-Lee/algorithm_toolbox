import sys, functools

def bsearch(A, b):
  head, tail = 0, len(A)-1
  while(tail >= head):      
    ind = int((head+tail)/2)
    #print ind, head, tail
    if( b == A[ind] ):
      return ind
    elif( b > A[ind] ):
      head = ind + 1
    else :
      tail = ind - 1
  return -1
  
def main():
  inp = sys.stdin.read().split()
  #print inp
  n = int(inp[0])
  A = [int(x) for x in inp[1:n+1]]
  m = int(inp[n+1])
  B = [int(x) for x in inp[n+2:]]
  #print n, A, m, B
  ret = []
  for b in B:
    ret.append(bsearch(A, b))

  print " ".join([str(x) for x in ret])

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