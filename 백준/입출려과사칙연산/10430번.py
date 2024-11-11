a, b, c = map(int, [5, 8, 4])

def remainder_with_c(input_int_value):
    return input_int_value%c

print(remainder_with_c(a+b))
print(remainder_with_c(remainder_with_c(a) + remainder_with_c(b)))
print(remainder_with_c(a*b))
print(remainder_with_c(remainder_with_c(a) * remainder_with_c(b)))