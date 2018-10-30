def main():
    actNum = int(input("Enter number 5-digit integer number: "))
    
    if (actNum >= 10000 and actNum <= 99999):
        checkDigit = actNum % 10
        accNum = actNum // 10
        num1 = (accNum // 1000)
        num2 = (accNum // 100) % 10
        num3 = (accNum // 10) % 10
        num4 = (accNum % 10)
        
        total = num1 + num2 + num3 + num4

        valid = (total % 7) == checkDigit
        if valid:
            print("Valid!")
        else:
            print("Invalid")

main()
