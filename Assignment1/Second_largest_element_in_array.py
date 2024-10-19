
def main():
    list = []
    n = int(input("Enter no of elements you want to add in list: "))

    for item in range(0,n):
        try:
            ele = int(input())
            if (type(ele)!= int):
                raise ValueError("Enter an integer")
            list.append(ele)
        except ValueError as e:
            print(f'Invalid input {e}')

    print(f'list = {list}')
    second_largest_element(list)

## method 1 = use sorted function to sort elements in list in ascending order and return second last element
def second_largest_element(list):
    n = len(list)  # n has length of list
    list = sorted(list)
    return print(f'{list[n-2]} is the second largest element in the array')




if __name__ =="__main__":
    main()
