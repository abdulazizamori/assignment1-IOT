def calculate_average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)
# Calculate the average of numbers
result_average = calculate_average(1, 2, 3, 4, 5)
print("Average:", result_average)