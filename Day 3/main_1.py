import re

strings = []

while True:
    line = input()
    if not line:
        break
    strings.append(line)

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

total = 0

for string in strings:
    matches = re.findall(pattern,string)

    for x,y in matches:
        total += int(x) * int(y)

    print(len(matches))
print(total)