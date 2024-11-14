#1
hour, minute = 23, 48
time_taken = 1440 + 25
full_time = minute + time_taken

if full_time > 59:
    full_hour = hour + full_time // 60
    if full_hour > 23:
        if full_hour // 24 == 0:
            pass
        else:
            full_hour = full_hour % 24
    print(f'{full_hour} {full_time%60}')
else:
    print(f'{hour} {full_time}')

#2
h, m = map(int, input().split())
t = int(input())

h += t // 60
m += t % 60

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24

print(h, m)

#3
hour, minute = 23, 48
time_taken = 1440 + 25
total_minutes = minute + time_taken

full_hour = (hour + total_minutes // 60) % 24
full_minute = total_minutes % 60

print(f'{full_hour} {full_minute}')