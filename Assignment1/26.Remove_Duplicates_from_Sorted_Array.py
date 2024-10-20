# def Remove_Duplicates(list1):
#     s_list = sorted(list1) # constraint = list is sorted (confirmation)

#     # make a new empty list where unique elements will be added from s_list
#     new_list = []
#     n = len(s_list)
#     for i in range(0,n-1):
#         if s_list[i] not in new_list:
#             new_list.append(s_list[i])
#         else:
#             s_list.pop(i)
#             i=0
#     print(s_list)

def Remove_Duplicates2(nums):
    ## define k =1 where the loop will start, as the forst element at loc 0 in a sorted array will always be sorted
    ## k also keeps track of number of unique elements
    k=1 
    
    for i in range(1,len(nums)):
        if nums[i] != nums[k-1]:
            nums[k] = nums[i]
            k +=1 ## increment k for number of unique elements
    print(f'Number of unique elements in list are {k} and those are: {nums[:k]}')


def main():
    list1 = []
    try:
        n = int(input("Enter number of elements to be added in list: "))

        for i in range(0,n):
            ele = int(input("enter element: "))
            list1.append(ele)
        
        if((type(n)!= int) or (type(ele)!= int )):
            raise ValueError("Please enter an integer")
        
    except ValueError as e:
        print(f'Invalid Input: {e}')
    
    Remove_Duplicates2(list1)

if __name__ == "__main__":
    main()