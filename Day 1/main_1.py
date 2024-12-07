left_hand = []
right_hand = []

while True:
    line = input()
    if not line:
        break

    left,right = map(int,line.split())
    left_hand.append(left)
    right_hand.append(right)

right_hand.sort()
left_hand.sort()

total = 0

for i in range(len(right_hand)):
    total += right_hand[i] - left_hand[i] if right_hand[i] > left_hand[i] else left_hand[i] - right_hand[i]

print(total)