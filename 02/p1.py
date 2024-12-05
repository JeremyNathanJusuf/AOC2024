import sys
inFile = sys.argv[1]

with open(inFile, 'r') as i:
    lines = i.readlines()
    
num_safe = 0

for line in lines:
    nums = list(map(int, line.split()))
    direction = 'a' if nums[0] < nums[1] else 'd'
    prev = nums[0]
    count = 1
    
    for num in nums[1:]:
        diff = num - prev
        if direction == 'a' and (diff <= 0 or diff >= 4):
            break
        elif direction == 'd' and (diff >= 0 or diff <= -4):
            break
        
        count += 1
        prev = num
    
    if count == len(nums):
        num_safe += 1
    
print(num_safe)