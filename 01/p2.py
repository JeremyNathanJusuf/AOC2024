import sys
inFile = sys.argv[1]

with open(inFile,'r') as i:
    lines = i.readlines()

B = []
hm = {}

for line in lines:
    a, b = map(int, line.split())
    B.append(b)
    hm[a] = 0
    
total = 0
for i in range(len(lines)):
    total += B[i] if B[i] in hm else 0
    
print(total)