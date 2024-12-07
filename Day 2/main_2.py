reports = []

while True:
    line = list(map(int,input().split()))
    if not line:
        break
    reports.append(line)

count = 0

for report in reports:
    safe = False
    for i in range(len(report)):
        excluded = report[:i] + report[i+1:]
        inc_or_dec = (excluded==sorted(excluded) or excluded==sorted(excluded,reverse=True))
        ok = True
        for j in range(len(excluded)-1):
            diff = abs(excluded[j] - excluded[j+1])
            if not 1<=diff<=3:
                ok = False
        
        if inc_or_dec and ok:
            safe = True

    if safe:
        count += 1


    

print(count)
