TESTCASES = [
  (2),
  (28)
]
GOLDENANSWERS = [
  2,
  6
]

#// Use minimal number of coins to change the money with coin value of 1, 5, 10.

def money_change(inp):
  target = inp
  num = 0
  for coin in (10, 5, 1): 
    if target >= coin:
      num += int(target / coin)
      target = target % coin
   
  return num

MAINFUNC = money_change
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
