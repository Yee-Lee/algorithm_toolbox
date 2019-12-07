import sys, functools

def LCS(s1, s2):
  
  n = len(s1)
  m = len(s2)
  D = [[0 for x in range(m)] for y in range(n)]
  
  for i in range(n):
    for j in range(m):
      if s1[i] == s2[j]:
        D[i][j] = D[i-1][j-1] + 1
      else:
        D[i][j] = max(D[i-1][j], D[i][j-1])

  print D
  return D[n-1][m-1]

def main():
  input = sys.stdin.read()
  data = input.split()
  n = int(data[0])
  s1 = data[1:n+1]
  m = int(data[n+1])
  s2 = data[n+2:]

  ret = LCS(s1, s2)
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