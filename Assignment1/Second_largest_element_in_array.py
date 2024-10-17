list = []
n = int(input("Enter no of elements you want to add in list: "))

for item in range(0,n):
    ele = int(input())
    list.append(ele)

print(f'list = {list}')

## method 1 = use sorted function to sort elements in list in ascending order and return last element
def second_largest_element(list):
    list = sorted(list)
    return print(f'{list[n-2]} is the second largest element in the array')

second_largest_element(list)


