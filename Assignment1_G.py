def Divisible(A):
    if A%5==0:
        ans=True
    else:
        ans=False
    
    return ans

def main():
    print("Enter the number of your choice: ")
    A=int(input())

    Result=Divisible(A)
    print(Result)

if __name__=="__main__":
    main()