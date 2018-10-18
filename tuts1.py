def main():
    print("A program to find the cost for three purchased items")
    cost1 = float(input("What is the const of item 1? "))
    print(cost1)
    cost2 = float(input("What is the const of item 2? "))
    print(cost2)
    cost3 = float(input("What is the const of item 3? "))
    print(cost3)

    totalCostItems = (cost1 + cost2 + cost3)
    print("Cost of 3 items = RM", totalCostItems)

    discount = (totalCostItems * 0.1)
    print("10% discount = RM", discount)

    netCost = (totalCostItems - discount)
    print("Net cost = ", netCost)

main()
