def Run():
    a=0
    no=1
    while a<10:
        if no%2==0:
            print(no,end=" ")
            a=a+1
        no=no+1

def main():
    Run()

if __name__=="__main__":
    main()