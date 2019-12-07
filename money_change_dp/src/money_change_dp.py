import sys, functools


##
##  num_coin(n, S) = [ infinite, if n=0                            ]
##                   [ min{ num_coin(n-c, S) + 1, for c in S}, else]
##
def money_change_dp(n, S):
  num_coin = [0]*(n+1)
  
  for i in range(1, n+1):
    num_min = 10**10
    for c in S:
      if i - c >= 0:
        num = num_coin[i-c] + 1
      else: 
        continue
      num_min = min(num_min, num)
    num_coin[i] = num_min
    #print num_coin
  
  return num_coin[n]

def main():
  input = sys.stdin.read().split()
  n = int(input[0])
  S = [1,3,4]
  ret = money_change_dp(n, S)

  print ret

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