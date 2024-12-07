from collections import defaultdict

left_hand = []
right_hand = []

while True:
    line = input()
    if not line:
        break

    left,right = map(int,line.split())
    left_hand.append(left)
    right_hand.append(right)

count = defaultdict(int)

for num in right_hand:
    if num in left_hand:
        count[num] += 1

total = 0

for num in left_hand:
    if num in count:
        total += num * count[num]

print(total)