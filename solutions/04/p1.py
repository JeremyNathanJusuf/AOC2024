import sys
inFile = sys.argv[1]

with open(inFile, 'r') as i:
    lines = i.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

def show_valid(used):
    for i in range(n):
        for j in range(m):
            print(
                lines[i][j] if used[i][j] else '*', 
                end=''
            )
        print()
            
def check_valid(i, j, lines, m, n, used):
    found = 0
    # check horizontal
    if j+3 < m and (lines[i][j:j+4] == 'XMAS' or lines[i][j:j+4] == 'SAMX'):
        found += 1
        for k in range(4):
            used[i][j+k] = 1
    
    # check vertical
    temp = []
    for k in range(4):      
        if i+k < n: 
            temp.append(lines[i+k][j])
        else: 
            break
        
    temp = ''.join(temp)
    if temp == 'XMAS' or temp == 'SAMX':
        found += 1
        for k in range(4):
            used[i+k][j] = 1

    # upper diagonal
    temp = []
    for k in range(4):      
        if i-k >= 0 and j+k < m: 
            temp.append(lines[i-k][j+k])
        else: 
            break
        
    temp = ''.join(temp)
    if temp == 'XMAS' or temp == 'SAMX':
        found += 1
        for k in range(4):
            used[i-k][j+k] = 1
    
    # lower diagonal
    temp = []
    for k in range(4):      
        if i+k < n and j+k < m: 
            temp.append(lines[i+k][j+k])
        else: 
            break
        
    temp = ''.join(temp)
    if temp == 'XMAS' or temp == 'SAMX':
        found += 1
        for k in range(4):
            used[i+k][j+k] = 1
        
    return found
        
        
n, m = len(lines), len(lines[0])
used = [[0]*m for _ in range(n)]
total = 0
# print(m, n)
for i in range(n):
    for j in range(m):
        total += check_valid(i, j, lines, m, n, used)    

show_valid(used)        
print(total)