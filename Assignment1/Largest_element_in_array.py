
## method 1 = use sorted function to sort elements in list in ascending order and return last element
def largest_element(list1):
    n = len(list1)
    s_list = sorted(list1)
    return print(f'{s_list[n-1]} is the largest element in the array')



## method 2 = store first element in list in variable (max) and swap if greater element is found in list while iterting over it
def largest_element2(list1):
    max = list1[0]
    n = len(list1)
    for i in range(0,n):
        if max<list1[i]:
            max = list1[i]
    print(f'{max} is the largest element in the array')



def main():
    ip_list = []
    n = int(input("Enter no of elements you want to add in list: "))

    for i in range(0,n):
        try:
            ele = int(input())
            if (type(ele)!= int):
                raise ValueError("Enter an integer")
            ip_list.append(ele)
        except ValueError as e:
            print(f'Invalid input {e}')
    largest_element(ip_list)
    largest_element2(ip_list)

if __name__ == "__main__":
    main()
