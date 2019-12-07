import sys, functools

def compare(x, y):
  if x == y : return 0
  X = str(x)
  Y = str(y)
  for i in range(max(len(X), len(Y))):
    #print len(X), len(Y)
    a = X[i] if i <len(X) else X[-1]
    b = Y[i] if i <len(Y) else Y[-1]
    if a != b: 
      #print a, b
      return int(a) - int(b)
  return 0

def maximum_salary():
  inp = sys.stdin
  for i, line in enumerate(inp):
    if i==0:
      n = int(line)
    else:
      nums = [int(x) for x in line.split()]
  nums = sorted(nums, key=functools.cmp_to_key(compare), reverse=True)

  print "".join([str(x) for x in nums])

MAINFUNC = maximum_salary
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