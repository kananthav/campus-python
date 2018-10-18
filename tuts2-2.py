def main():
    for i in range(5):
        money = eval(input("Enter money amount in cents (e.g. 125) "))
        remainingCents = money
        no50 = money // 50
        money %= 50
        no20 = money // 20
        money %= 20
        no10 = money // 10
        money %= 10
        no5 = money // 5
        money %= 5
        no1 = money // 1
        money %= 1

        print(remainingCents, "cents = ", no50, "50-cent", no20, "20-cent", no10, "10-cent", no5, "5-cent", no1, "1-cent")

main()
