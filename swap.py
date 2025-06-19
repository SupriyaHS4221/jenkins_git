import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
