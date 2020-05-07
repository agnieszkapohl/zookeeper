n = int(input())
counter = 1
result = 1

while counter <= n:
    result *= counter
    counter += 1

print(result)