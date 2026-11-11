# gird=((1,2,3),(4,5,6))
# print(sum(gird)

grid = ((1, 2, 3), (4, 5, 6))

total_sum = 0
for row in grid:
    for num in row:
        total_sum += num

print(total_sum)  # Output: 21