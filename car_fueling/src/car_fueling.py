import sys

def car_fueling():
  inp = sys.stdin
  for i, line in enumerate(inp):
    if i==0:
      d = int(line)
    elif i==1:
      m = int(line)
    elif i==2:
      n = int(line)
    elif i==3:
      stops = [int(x) for x in line.split()]
  stops.append(d)
  n = n+1
  #print d, m, n, stops
  num = 0
  run = head = 0
  j = 0
  while(j<n):
    run = stops[j] - head
    if( run > m ):
      num += 1
      head = stops[j-1]
      if (stops[j] - stops[j-1]) > m:
        num = -1
        break
    else:  
      j+=1
  print num

MAINFUNC = car_fueling
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