
mylist = []
n = int(input("How many elements are you going to enter? "))
print("Enter the list of elements:")
i = 0
while i < n:
    element = int(input())
    mylist.append(element)
    i = i+1
search_element = int(input("Enter the element to be searched:"))
sorted_list = sorted(mylist)
print(sorted_list)


def lesser(mid, sorted_list):
    low = 0
    high = mid
    mid_index = int(low+(high-low)/2)
    if search_element == sorted_list[mid_index]:
        print("The element is found at:", mid_index)
    elif search_element > sorted_list[mid_index]:
        greater(mid_index, sorted_list)
    else:
        lesser(mid_index, sorted_list)


def greater(mid, sorted_list):
    low = mid
    high = len(sorted_list)
    mid_index = int(low+(high-low)/2)
    if search_element == sorted_list[mid_index]:
        print("The element is found at:", mid_index)
    elif search_element > sorted_list[mid_index]:
        greater(mid_index, sorted_list)
    else:
        lesser(mid_index, sorted_list)


low = 0
length = len(mylist)
high = length
print(high)
mid_index = int(low+(high-low)/2)
# print(mid_index)
if search_element == sorted_list[mid_index]:
    print("The element is found at", mid_index)
elif search_element < sorted_list[mid_index]:
    lesser(mid_index, sorted_list)
else:
    greater(mid_index, sorted_list)
if search_element not in mylist:
    print("The element is not found")
