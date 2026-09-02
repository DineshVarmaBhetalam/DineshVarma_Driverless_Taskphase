user_input = input("enter numbers: ").split()
numbers = [int(x) for x in user_input]

hash_table = [[] for _ in range(10)]

def hash_func(num):
    return num % 10

for num in numbers:
    index = hash_func(num)
    hash_table[index].append(num)

for bucket in hash_table:
    bucket.sort()


print("\nHash Table :")
for i, val in enumerate(hash_table):
    print(f"Index {i}: {val}")


new_num=input("number to be added: ")


def insert_with_binary_search( hash_table ,new_num):

    index = int(new_num) % 10
    bucket = hash_table[index]


    low = 0
    high = len(bucket)

    while low < high:
        mid = (low + high) // 2
        if bucket[mid] < int(new_num):
            low = mid + 1
        else:
            high = mid

    bucket.insert(low, new_num)

insert_with_binary_search(hash_table, new_num)
print(hash_table[index])

for i, bucket in enumerate(hash_table):
    print(f"Index {i}: {bucket}")









