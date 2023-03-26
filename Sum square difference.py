sum_squares = 0
for i in range(1,101,1):
    sum_squares = sum_squares + i**2

total_sum = 0
for l in range(1,101,1):
    total_sum = total_sum + l
squares_sum = total_sum**2

print((squares_sum) - (sum_squares))