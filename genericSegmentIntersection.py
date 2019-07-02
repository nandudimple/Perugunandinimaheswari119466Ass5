from random import random, randint

#draw segment between coordinates
def segment(point1, point2):
    xd = (point1[1] - point2[1])
    yd = (point2[0] - point1[0])
    s = (point1[0]*point2[1] - point2[0]*point1[1])
    return xd, yd, -s

#sort segments
def sortSegments(segmentss): #using selection sort algorithm
    segments = []
    for i in range(len(segmentss)):
        segments.append(segmentss[i][0])
    for i in range(len(segments)):
        min_idx = i
        for j in range(i + 1, len(segments)):
            if segments[min_idx] > segments[j]:
                min_idx = j
        segments[i], segments[min_idx] = segments[min_idx], segments[i]

#check intersect or not
def intersection(segment1, segment2):
    m  = segment1[0] * segment2[1] - segment1[1] * segment2[0]
    xm = segment1[2] * segment2[1] - segment1[1] * segment2[2]
    ym = segment1[0] * segment2[2] - segment1[2] * segment2[0]
    if m != 0:
        x = xm / m
        y = ym / m
        return x,y
    else:
        return False
#random points
points = []

for i in range(20):
    points.append([random()*1000+1000,random()*1000+1000])

#random segments
segments = []

for i in range(20):
    segments.append(segment(points[randint(1,19)], points[randint(1,19)]))
#sort segments
sortSegments(segments)

#check segments are intersected or not
intersected = intersection(segments[randint(1,19)], segments[randint(1,19)])

if intersected:
    print("Segments are Intersected:", intersected)
else:
    print("No Segments are Intersected")