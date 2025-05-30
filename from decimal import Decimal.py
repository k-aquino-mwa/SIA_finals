from decimal import Decimal

n = Decimal(input("Enter the base (n): "))
r = Decimal(input("Enter the exponent (r): "))

result = n ** r
print(f"{n} raised to the power of {r} is: {result}")

