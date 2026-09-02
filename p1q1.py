n=input("input an integer n")
LIMIT=int(n)
restricted_list=[]
count=0
i=1
while i<=LIMIT:
    x=str(input("enter string"))
    restricted_list.append(x)
    count+=1
    i+=1
my_dict={}
print(restricted_list)
entry="".join(restricted_list).lower()
for i in entry :
    if i in my_dict:
        my_dict[i]+=1
    else:
        my_dict[i]=1
del my_dict[' ']
print(my_dict)
