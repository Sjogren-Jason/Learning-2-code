prices = []
total = 0
maxListLength = int(input("How many items did you purchase? "))
print("How much did each item cost?")

while len(prices) < maxListLength:
    price = int(input(">$ "))
    prices.append(price)
    total += price

avg = total / len(prices)
print(f"Total: ${total}")
print(f"Average: ${avg}")


