def NumChk(A):
    if A>0:
        ans="Positive number"
    elif A<0:
        ans="Negative number"
    elif A==0:
        ans="Zero"
    
    return ans

def main():
    print("welcome to digit check program: ")
    print("Please enter the integer value to classify between positive or negative value: ")
    A=int(input())

    Result=NumChk(A)
    print("The provided number is: ",Result)

if __name__=="__main__":
    main()