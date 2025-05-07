import random

collection = []
for i in range(10):
    collection.append(random.randint(1, 100))

print(collection)
print(min(collection))