import re

strings = []

while True:
    line = input()
    if not line:
        break
    strings.append(line)

pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"

total = 0
lengths = 0
enable = True

for string in strings:
    matches = re.findall(pattern,string)
    print(matches)
    print(len(matches))

    for match in matches:
        if match == "don't()":
            enable = False
            continue
        elif match == "do()":
            enable = True
            continue

        
        if enable:
            lengths += 1
            x,y = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", match)[0]
            total += int(x) * int(y)

    
print(lengths)
            

print(total)