val = 125
str = str(val)
ls = []
ls.append(val)
print(ls)
print(list(str))
exit()

def fib(n):
    current, next = 0, 1
    for i in range(n+1):
        yield current
        current, next = next, current + next

fib = fib(1)
for i, val in enumerate(fib):
    print(val)