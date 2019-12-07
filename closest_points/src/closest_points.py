import sys, functools

def distance(x1, y1, x2, y2):
  return ((x1-x2)**2 + (y1-y2)**2) ** 0.5

def minimum_distance(x, y):
  #write your code here
  d = 10**18
  pts = zip(x,y)
  if(len(pts)==1): return d
  elif(len(pts)<3): return distance(pts[0][0], pts[0][1], pts[1][0], pts[1][1])

  pts = sorted(pts, key=lambda pt: pt[0])

  m = len(pts)//2
  x_m = (pts[m][0] + pts[m+1][0])/2
  pts_l, pts_r = pts[:m], pts[m:]
  d_l = minimum_distance([pt[0] for pt in pts_l], [pt[1] for pt in pts_l])
  d_r = minimum_distance([pt[0] for pt in pts_r], [pt[1] for pt in pts_r])
  d = min(d_l, d_r)
  #print pts_l, pts_r, x_m, d

  pts_flr = [pt for pt in pts if pt[0]>=x_m-d and pt[0]<=x_m+d]
  pts_flr = sorted(pts_flr, key=lambda pt: pt[1])
  #print pts_flr
  for i in range(len(pts_flr)):
    pt_i = pts_flr[i]
    for j in range(i+1, min(len(pts_flr), i+8)):
      pt_j = pts_flr[j]
      dd = distance(pt_i[0], pt_i[1], pt_j[0], pt_j[1])
      if dd < d : d = dd
  
  return d

def main():
  input = sys.stdin.read()
  data = list(map(int, input.split()))
  n = data[0]
  x = data[1::2]
  y = data[2::2]
  print("{0:.9f}".format(minimum_distance(x, y)))

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