def ChkNum():
    no1 = int (input("Enter number : "))

    if no1 < 0:
        print("Negative number")
    elif no1 > 0:
        print("Positive number")
    else :
        print("Zero number")

if __name__ == "__main__":
    ChkNum()

 