a = int(input())
b = int(input())

num_list = reversed(list(map(int, str(b))))
for num in num_list:
    print(a * num)
print(a * b)