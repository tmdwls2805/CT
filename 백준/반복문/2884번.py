H = int(0)
M = int(30)

if 45 > M:
    if H == 0:
        H = 23
    else:
        H = H -1
    remain_T = 15 + M
    print(f'{H} {remain_T}')
else:
    print(f'{H} {M-45}')