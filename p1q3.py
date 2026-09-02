n=int(input("input an integer n"))
my_list=[]
num_items = n
for i in range(n):
    item = input(f"Enter item {i + 1}: ")
    my_list.append(item)

target=input("enter the item you are searching for: ")

print(f"initial list is {my_list}")
class sort:
    def __init__(self,my_list):
        self.my_list=my_list
    def new(self):
         for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if my_list[j]<my_list[min_index]:
                    min_index=j
                my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
         return my_list
    def binary_search(self,my_list, target):
        low = 0
        high = len(my_list) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if my_list[mid] == target:
                return mid
            elif my_list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

list1=sort(my_list)


print(list1.new())
print(list1.binary_search(my_list,target))