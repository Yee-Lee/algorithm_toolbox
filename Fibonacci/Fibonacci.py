TESTCASES = [
  (2),
  (10)
]
GOLDENANSWERS = [
  1,
  55
]

def Fibonacci(inp):
  ind = inp
  F_1 = 0
  F_2 = 1
  ret = 0
  if ind == 0: return F_1
  if ind == 1: return F_2

  for i in range(ind):
    if i == 0 or i == 1:
      continue
    ret = F_1 + F_2
    F_1 = F_2
    F_2 = ret
  return F_1+F_2

mainfunc = Fibonacci
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

if __name__ == '__main__':    
  try:
    ret = run(mainfunc, TESTCASES, GOLDENANSWERS)
  except Exception as e:
    details = traceback.format_exc()
    print "\nRuntime error: %s\n\n %s"%(e, details)
  else:
    print ret
