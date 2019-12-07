TESTCASES = [
  (18,35),
  (28851538,1183019)
]
GOLDENANSWERS = [
  1,
  17657
]
import sys, functools

def GCD(inp):
  n1, n2 = inp
  
  (dividend, divisor) = (n1,n2) if n1 > n2 else (n2,n1)
  reminder = dividend % divisor
  if(reminder == 0): return n2
  n1 = divisor 
  n2 = reminder
  return GCD((n1,n2))
  
def GCD_iter(inp):
  n1, n2 = inp
  (dividend, divisor) = (n1,n2) if n1 > n2 else (n2,n1)
  reminder=dividend % divisor
  while(reminder > 0):
    reminder=dividend % divisor
    dividend = divisor
    divisor = reminder
  return dividend

import sys
def main():
  data = sys.stdin.read().split()
  n1, n2 = map(int, data)
  print GCD_iter((n1,n2))

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