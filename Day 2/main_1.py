reports = []

while True:
    line = list(map(int,input().split()))
    if not line:
        break
    reports.append(line)

count = 0

for report in reports:
    increasing = report[0] < report[1]
    safe = True

    for i in range(1,len(report)):
        diff = report[i] - report[i-1]
        if increasing and diff < 0:
            safe = False
            break
        if not increasing and diff > 0:
            safe = False
            break
        if diff == 0:
            safe = False
            break
        if increasing and diff > 3:
            safe = False
            break
        if not increasing and diff < -3:
            safe = False
            break
    
    if safe:
        count += 1

print(count)
