import math

def combinations(n, r):
  """Calculates combinations (nCr) with error handling."""
  if not isinstance(n, int) or not isinstance(r, int):
    raise ValueError("n and r must be integers.")
  if n < 0 or r < 0 or r > n:
    raise ValueError("Invalid input: n and r must be non-negative, and r must be less than or equal to n.")
  return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

try:
  n = int(input("Enter n: "))
  r = int(input("Enter r: "))
  result = combinations(n, r)
  print(f"The number of combinations is: {result}")
except ValueError as e:
  print(f"Error: {e}")