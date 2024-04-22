def Add(A,B):
    ans=A+B
    return ans

def main():
    print("Welcome to addition program...")
    print("Enter first number for addition: ")
    A=int(input())
    print("Enter second number for addition: ")
    B=int(input())

    Result=Add(A,B)
    print("The addition of 2 given number is: ",Result)

if __name__=="__main__":
    main()