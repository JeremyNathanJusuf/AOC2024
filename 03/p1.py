import sys
inFile = sys.argv[1]
with open(inFile, 'r') as i:
    lines = i.readlines()

instruction = []
for line in lines:
    instruction.append(line)

instruction = ''.join(instruction)

ans = 0
count = 0

for i in range(len(instruction)-3):
    if instruction[i:i+4] == 'mul(':
        j = i+4
        num1 = []
        while 48 <= ord(instruction[j]) <= 57:
            num1.append(instruction[j])
            j += 1
            
        num1 = int(''.join(num1))
        
        if instruction[j] != ',':
            continue
            
        j += 1
        num2 = []
        while 48 <= ord(instruction[j]) <= 57:
            num2.append(instruction[j])
            j += 1
            
        num2 = int(''.join(num2))
        
        if instruction[j] != ')':
            continue
        
        ans += num1 * num2
        print(instruction[i:j+1])
        count += 1
        

print(count)        
print(ans)
        
        
    
    