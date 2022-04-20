n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


a = sorted(a) # default 값은 오름차순
b = sorted(b, reverse=True) # reverse=True 하면 내림차순으로

for i in range(k):
    # 삽입정렬 사용
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

# result = 0
# for i in range(len(a)):
#     result += a[i]
#
# print(result)