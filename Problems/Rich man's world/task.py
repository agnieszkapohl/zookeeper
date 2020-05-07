deposit = int(input())
interest_rate = 7.1 / 100
counter = 0

while deposit < 700000:
    deposit += interest_rate * deposit
    counter += 1

print(counter)
