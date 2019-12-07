TESTCASES = [
  [[3,50], [60, 20], [100,50], [120,30]],
  [[1,10], [500,30]]
]
GOLDENANSWERS = [
  180.0000,
  166.6667
]

def fractional_knapsack(inp):
  (n, W) = inp[0]
  v = []
  w = []
  for i in range(1,n+1):
    v.append(inp[i][0])
    w.append(inp[i][1])
  

  bound_value = 9999999
  Remaining = W
  V = 0

  f = [float(v[i])/w[i] for i in range(n) ]
  while(Remaining > 0):  
    max_value_i = 0
    max_value = 0
    for i in range(n):
      if f[i] > max_value and f[i] < bound_value:
        max_value_i = i
        max_value = f[i]
    Taken = w[max_value_i] if Remaining >= w[max_value_i] else Remaining 
    V += Taken * max_value
    Remaining = Remaining - Taken
    bound_value = max_value
    #print Remaining, max_value, Taken, V
  
  #post-process 
  V_tmp = int(V * 10000)
  if V_tmp % 10 > 4:
    V_tmp += 1
  V = float(V_tmp) / 10000

  return V


MAINFUNC = fractional_knapsack
###########################################################################################
import traceback

def run(func, testcases, goldenanswers):
  msg = "Pass!"
  for i, tc in enumerate(testcases):
    ret = func(tc)
    ans = GOLDENANSWERS[i]
    if(ret != ans):
      msg = "\nFail(testcase #{0}) :\nGolden Answer is {1} \nYour answer is {2}".format(i+1, ans, ret)
      break
  return msg

if __name__ is '__main__':
  try:
    ret = run(MAINFUNC, TESTCASES, GOLDENANSWERS)
  except Exception as e:
    details = traceback.format_exc()
    print "\nRuntime error: %s\n\n %s"%(e, details)
  else:
    print ret
