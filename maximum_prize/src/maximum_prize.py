import sys

def maximum_prize():
  inp = sys.stdin
  segs = []
  for i, line in enumerate(inp):
    if i==0:
      n = int(line)

  remaining = n
  i = 1
  prizes = []
  while(remaining > 0):
    if remaining - i >= 0:
      prizes.append(i)
    else:
      prizes[-1] = prizes[-1] + remaining

    remaining = remaining - i
    i = i + 1    
  print len(prizes)
  print " ".join([str(x) for x in prizes])

MAINFUNC = maximum_prize
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