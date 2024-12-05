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
    dl, dr = [], []
    
    if lines[i][j] != 'A':
        return 0
    
    for k in range(-1, 2):
        # right diagonal
        if n > i+k >= 0 and m > j-k >= 0:
            dr.append(lines[i+k][j-k])
        else:
            break
        
        # left diagonal
        if n > i+k >= 0 and m > j+k >= 0:
            dl.append(lines[i+k][j+k])
        else:
            break
        
    
    dr = ''.join(dr)
    dl = ''.join(dl)
        
    
    if (dr == 'MAS' or dr == 'SAM') and (dl == 'MAS' or dl == 'SAM'):
        found += 1
        for k in range(-1, 2):
            used[i+k][j-k] = 1
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