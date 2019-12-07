import sys

def ad_max_revenue():
  inp = sys.stdin
  for i, line in enumerate(inp):
    if i==0:
      n = int(line)
    elif i==1:
      a = [int(x) for x in line.split()]
    elif i==2:
      b = [int(x) for x in line.split()]
  a.sort()
  b.sort()
  sum = 0
  for A,B in zip(a,b):
    sum += A*B
    #print A,B
  print sum
    
MAINFUNC = ad_max_revenue
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