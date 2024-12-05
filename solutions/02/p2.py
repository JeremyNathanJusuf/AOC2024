import sys
inFile = sys.argv[1]


def is_safe(nums):
    assert len(nums) >= 4
    asc = 0
    
    for i in range(3):
        if nums[i] < nums[i+1]:
            asc += 1
        else:
            asc -= 1
            
    direction = 'a' if asc > 0 else 'd'
    prev = nums[0]
    for i in range(1, len(nums)):
        diff = nums[i] - prev
        prev = nums[i]
        if (direction == 'a' and (diff <= 0 or diff >= 4)) or (direction == 'd' and (diff >= 0 or diff <= -4)):
            return False
        
    
    return True

def is_safe_remove_one_element(nums):
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i+1:]
        if is_safe(new_nums):
            return True
        
    return False

with open(inFile, 'r') as i:
    lines = i.readlines()
    
num_safe = 0

for line in lines:
    nums = list(map(int, line.split()))
    if is_safe(nums) or is_safe_remove_one_element(nums):
        num_safe += 1
    
print(num_safe)