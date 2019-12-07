import sys, functools

##
##  The capacity of knapsack is W, n items, weight(wi): w1~wn not ordered, value(vi): v1~vn not ordered.
##  Input format:
##
#   W n
#   w1 w2 .... wn
#   v1 v2 .... vn
# #
#   Output fromat:
#   maximal value
##

##
#  Solution: 2 dimensions array for x: taken weights 0~capacity; y: The item number, 0~n-1
#     D[i][j] = [  max( D[i-wj][j-1]+vk, D[i][j-1]), k=1~n, i>0,j>0 ]  #D[i][j-1] is the max value of not taking item j.
#               [  0, i=j=0                                         ]
# #

def knapsack_dp(W, n, ws, vs):
  #print ws, vs
  D = [[0 for x in range(W+1)] for y in range(n)]
  
  for j in range(0, n):
    for i in range(1, W+1):
      if j == 0:
        D[0][i] = vs[0] if i-ws[0] > 0 else 0
      else:
        d1 = D[j-1][i-ws[j]] + vs[j] if i-ws[j] >= 0 else 0
        d2 = D[j-1][i]
        D[j][i] = max(d1, d2)

  #print D
  return D[n-1][W]

def main():
  input = sys.stdin.read()
  data = [int(x) for x in input.split()]
  W = data[0]
  n = data[1]
  ws = data[2:n+2]
  vs = data[n+2:]
  
  ret = knapsack_dp(W, n, ws, vs)
  print(ret)

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