C = "a"
A = ["apple", "ala", "area", "a", "ada", "alarm", "axa", "aa"]

count = 0
for word in A:
    if len(word) > 1 and word.startswith(C) and word.endswith(C):
        count += 1

print(f"Количество подходящих строк: {count}")