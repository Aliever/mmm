numbers = [5, -12, 15, 100, 9, 22, -45, 10, 99, 8]

two_digit_positives = []

for num in numbers:
    if num > 0 and 10 <= num <= 99:
        two_digit_positives.append(num)

two_digit_positives.sort()

print("Положительные двузначные числа (отсортированные):", two_digit_positives)