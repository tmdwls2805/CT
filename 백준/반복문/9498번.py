score = 100

if not isinstance(int, score):
    raise Exception('Please enter an integer.')
elif score > 100:
    raise Exception('Do not enter numbers over 100.')
elif 100 >= score >=90:
    print('A')
elif 90 > score >=80:
    print('B')
elif 80 > score >= 70:
    print('C')
elif 70 > score >=60:
    print('D')
else:
    print('F')