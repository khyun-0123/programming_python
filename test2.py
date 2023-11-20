a = 10
b = 10
print(a is b)   # Output: True

a = 1000
b = 1000
print(a is b)   # Output: True

a = 1000
b = 150
b = b + 850

print(a is b)   # Output: False
