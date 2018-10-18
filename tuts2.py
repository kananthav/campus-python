def main():
    item = (input("Please enter item name: "))
    price = float(eval(input("Please enter price: ")))
    quantity = eval(input("Please enter quantity: "))

    totalCost = float(price * quantity)

    print("item\tprice\tqty\ttotal cost")
    print("~~~~~\t~~~~~\t~~~\t~~~~~~~~~")
    print(item, "\t", price, "\t", quantity, "\t", "RM", totalCost)

main()
