## to check if the array is sorted
def solution(list):
    #step1 = sort array in ascending order
    sorted_list = sorted(list)
    sol = False
    # to rotate in possible combinations from 0 to len(list)
    for k in range(0,len(list)+1):
        # for left rotation of list i.e. taking last k elements and rotating them to start of the list, using list slicing 
        rotated_list = sorted_list[k:] + sorted_list[:k]
        if(rotated_list == list):
            sol = True
    
    if (sol == True):
        print(f'list {list} was sorted and rotated')
    else:
        print(f'list {list} was NOT sorted and rotated')


def main():
    list = []
    try:
        n = int(input('enter no of elements to be added in list: '))
        for i in range(0,n):
            ele = int(input())
            list.append(ele)
        if ((type(n)!= int) or (type(ele)!= int)):
            raise ValueError("Please Integer Value")
    except ValueError as e:
        print(f'Invalid input enetered, error {e} occured')
    solution(list)
    
if __name__ == "__main__":
    main()

