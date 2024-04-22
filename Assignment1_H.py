def Star(A):
    for i in range(A):
        print('*',end=" ")

def main():
    print("Enter the desire value for star: ")
    A=int(input())
    Star(A)

if __name__=="__main__":
    main()