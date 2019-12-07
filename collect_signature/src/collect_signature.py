import sys

def collect_signature():
  inp = sys.stdin
  segs = []
  for i, line in enumerate(inp):
    if i==0:
      n = int(line)
    else:
      segs.append([int(x) for x in line.split()])

  segs = sorted(segs, key=lambda x:x[1])
  #print segs
  points = []
  
  #the beginning point
  point = segs[0][1]
  points.append(point)

  for seg in segs:
    
    if seg[0] > point:
      #Cannot fit the existing point. Set the new point at its end time.
      point = seg[1]
      points.append(point)

  print len(points)
  print " ".join([str(x) for x in points])
  
MAINFUNC = collect_signature
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