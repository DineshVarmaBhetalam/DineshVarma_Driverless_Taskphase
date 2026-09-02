user_input = input("enter numbers: ").split()
numbers = [int(x) for x in user_input]

hash_table = [[] for _ in range(10)]

def hash_func(num):
    return num % 10
for num in numbers:
    index = hash_func(num)
    hash_table[index].append(num)
print("\nHash Table :")
for i, val in enumerate(hash_table):
    print(f"Index {i}: {val}")

