def ChkNum(A):
    if (A%2==0):
        ans="Even number"
    else:
        ans="Odd number"
    return ans

def main():
    print("Enter a number to check Even/Odd: ")
    A=int(input())
    Result=ChkNum(A)
    print("The Provided number is: ",Result)
        
if __name__=="__main__":
    main()
    