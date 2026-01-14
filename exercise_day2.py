prices  = [6.66, 15.99, 279.99, 13.99, 1999.99]

pricePlusTax = []

for p in prices:
    pricePlusTax.append(p + (p * .1))
    print(p)

total = 0
for p in pricePlusTax:
    total += p

print(f"total is {total:.2f}")

