import math

def permutations(n, r):
  """Calculates permutations (nPr)."""
  return math.factorial(n) // math.factorial(n - r)

n = int(input("Enter n: "))
r = int(input("Enter r: "))

result = permutations(n, r)
print(f"The number of permutations is: {result}")