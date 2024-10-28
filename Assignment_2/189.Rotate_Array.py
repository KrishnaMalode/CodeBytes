## rotate list elements to k steps to right

def rotate_right(list_ip,k):
    list_ip = list_ip[-k:]+list_ip[:-k]
    print(list_ip)

def main():
    list_ip = []
    try:
        n = int(input("Enter Number of elements in list: "))
        if type(n)!=int or n<0:
            raise  ValueError("Number of elements in a list must be positive!!")
        for i in range(1,n+1):
            ele =int(input(f'Enter Element no.{i}: '))
            list_ip.append(ele)
    except ValueError as e:
        print(f'INVALID INPUT!! ={e}')
        
    k = int(input("Enter Positive 'k' to rotate right: "))
    k = k % n
    
    rotate_right(list_ip,k)


    
if __name__ == "__main__":
    main()