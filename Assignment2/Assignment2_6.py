def checknum():

    no = int(input("Enter number "))

    for i in range (no,0,-1):
        print(" *" * i )

if __name__ == "__main__":
    checknum()