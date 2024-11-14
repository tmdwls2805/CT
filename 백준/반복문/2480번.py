num_list = list(map(int, input().split()))
count_dict = {}
money = 0

for num in num_list:
    try: count_dict[num] += 1
    except: count_dict[num]=1

if len(count_dict) == 1:
    money = 10000 + next(iter(count_dict)) * 1000
elif len(count_dict) == 2:
    money = 1000 + max(count_dict, key=count_dict.get) * 100
else:
    money = max(count_dict.keys()) * 100

print(money)
