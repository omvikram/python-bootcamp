ls = [1,2,3,4,5,6,7,8,9]
new_ls = []
new_item = 0
print(ls)
for item in ls:
    new_item = item + new_item
    new_ls.append(new_item)
    print(new_item)

print(new_ls)

last_result = 0
for i in range(10):
    if(i != 0):
        last_result = i+last_result
        print last_result 
