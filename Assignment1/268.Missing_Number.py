def Missing_Number(list1):
    ## first we will return highest element in array to generate an list which contains elements in range(0,n)
    sorted_list = sorted(list1)
    length = len(list1)
    max = sorted_list[length - 1]
    
    # now create a new list with no of elements from 0 till the max number 
    new_list = list(range(0,max+1))
    
    # now compare both lists and return the missing elements
    missing_numbers = []
    for item in new_list:
        if item not in sorted_list:
            missing_numbers.append(item)
    
    print(f'Missing numbers in the list are: {missing_numbers}')


def main():
    list = []
    try :
        n = int(input("Enter Number of elements in array/list: "))

        for i in range(0,n):
            ele = int(input())
            list.append(ele)
        
        if ((type(n)!= int) or(type(ele)!= int)):
            raise ValueError("Please Enter Integer")
    except ValueError as e:
        print(f'Invalid Input: {e}')
    
    Missing_Number(list)


if __name__ == "__main__":
    main()