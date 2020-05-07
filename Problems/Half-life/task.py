n = int(input())
r = int(input())
HALF_LIFE = 12
counter = 0

while n > r:
    n /= 2
    counter += 1

print(counter * HALF_LIFE)