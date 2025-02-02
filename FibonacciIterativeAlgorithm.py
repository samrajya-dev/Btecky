#Python code for fibonacci Series
def factorial(n):
   # base case
   if n == 0:
      return 1
   else:
      return n * factorial(n-1)

def fibonacci(n):
   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
   n = 5
   print("Factorial of", n, ":", factorial(n))
   print("Fibonacci of", n, ": ")
   for i in range(n):
      print(fibonacci(i))
