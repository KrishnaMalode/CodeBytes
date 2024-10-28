#Function to return a list containing the union of the two arrays.
def findUnion(a,b):
    a.extend(b)
    a = set(a)
        
    return sorted(a)

def main():
    try:
        n = int(input('Enter no of elements to be added in list a: '))
        m = int(input("Enter no of elements to be added in list b: "))

        print('Enter elements of a seperated with an enter: ')
        a =[int(input()) for i in range(0,n)]
        print('Enter elements of b seperated with an enter: ')
        b =[int(input()) for i in range(0,m)]

        if type(n)!=int or type(m)!=int or n<0 or m<0:
            raise ValueError('Number of elements cannot be non-numeric or negaive!')
    

    except ValueError as e:
        print(f'INVALID INPUT {e}')
    
    print(f'Union:{findUnion(a,b)}')


if __name__ == "__main__":
    main()