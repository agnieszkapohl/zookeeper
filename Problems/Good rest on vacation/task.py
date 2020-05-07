# put your python code here
days = int(input())
nights = days - 1
food_per_day = int(input())
one_way_ticket = int(input())
cost_per_night = int(input())

print(cost_per_night * nights + food_per_day * days + one_way_ticket * 2)
