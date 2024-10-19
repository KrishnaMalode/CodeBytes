
## method 1 = use sorted function to sort elements in list in ascending order and return last element
def largest_element(list):
    list = sorted(list)
    return print(f'{list[n-1]} is the largest element in the array')

largest_element(list)

## method 2 = store first element in list in variable (max) and swap if greater element is found in list while iterting over it
def largest_element2(list):
    max = list[0]

    for i in range(0,n):
        if max<list[i]:
            max = list[i]
    print(f'{max} is the largest element in the array')

largest_element2(list)

def main():
    list = []
    n = int(input("Enter no of elements you want to add in list: "))

    for i in range(0,n):
        try:
            ele = int(input())
            if (type(ele)!= int):
                raise ValueError("Enter an integer")
            list.append(ele)
        except ValueError as e:
            print(f'Invalid input {e}')

if __name__ == "__main__":
    main()
