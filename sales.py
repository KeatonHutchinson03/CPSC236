def display():
    tax = .6
    print("ENTER ITEMS (ENTER 0 TO END)")
    item = 1
    total = 0
    while item > 0:
        item = float(input("Cost of Item:"))
        total = total + item
    salesTax = total * tax
    compTotal = total + salesTax
    total = round(total, 2)
    salesTax = round(salesTax, 2)
    compTotal = round(compTotal, 2)
    print("Total: ", total)
    print("Sales tax: ", salesTax)
    print("Total after tax: ", compTotal)
    