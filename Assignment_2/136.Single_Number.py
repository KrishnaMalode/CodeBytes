# for item in nums:
#             if nums.count(item) == 1:
#                 return item

def single_num(nums):
    for item in nums:
        if nums.count(item)==1:
            return item

def main():
    nums = []
    try:
        n = int(input("Enter Number of Elements in list: "))
        for i in range(0,n):
            ele=int(input())
            nums.append(ele)
        
    except ValueError as e:
        print(f'INVALID INPUT {e}')
    
    print(f'single number in list is :{single_num(nums)}')

if __name__ == "__main__":
    main()
        
