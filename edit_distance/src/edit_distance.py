import sys, functools

def edit_distance(s1, s2):
  D = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

  for i in range(0, len(s2)+1):
    D[0][i] = i
  for j in range(0, len(s1)+1):
    D[j][0] = j
  
  dis = 0
  for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
      d1 = D[i-1][j] + 1    #insert
      d2 = D[i][j-1] + 1    #delete
      d3 = D[i-1][j-1] + 1  #substitue
      d4 = D[i-1][j-1]      #match
      if s1[i-1] != s2[j-1]:
        D[i][j] = min(d1, d2, d3)
      else:
        D[i][j] = min(d1, d2, d4)
  print D
  dis = D[i][j]
  return dis

def main():
  input = sys.stdin.read()
  data = input.split()
  s1, s2 = data
  dis = edit_distance(s1, s2)
  print(dis)

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