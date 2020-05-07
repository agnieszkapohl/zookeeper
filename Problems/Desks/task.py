# put your python code here
group1 = abs(int(input()))
group2 = abs(int(input()))
group3 = abs(int(input()))

desk1 = (group1 // 2) + (group1 % 2)
desk2 = (group2 // 2) + (group2 % 2)
desk3 = (group3 // 2) + (group3 % 2)

desks = desk1 + desk2 + desk3

print(desks)

