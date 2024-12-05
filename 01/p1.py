import sys
inFile = sys.argv[1]

with open(inFile,'r') as i:
    lines = i.readlines()

A, B = [], []

for line in lines:
    a, b = map(int, line.split())
    A.append(a)
    B.append(b)
    
A.sort()
B.sort()

total = sum([abs(a-b) for a,b in zip(A, B)])
    
print(total)