def test_range(n):
   if n in range(3, 9):
      print("It's in range")
   else:
      print("It's outside")

test_range(3)

n = 5
fact = 1

for i in range(1, n+1):
    fact = fact * i

print("The factorial is : ", end="")
print(fact)

def fact(x):
    pd = 1
    for i in range(1, x+1):
        pd = pd * i
    return pd

print(fact(5))
