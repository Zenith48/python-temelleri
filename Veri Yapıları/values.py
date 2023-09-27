# values => y'de yapılan değişiklik x'i etkilemez
x = 5
y = 25

x = y

y = 10

print(x, y)

# referance types => b'de yapılan değişiklik a'yı da etkiler.
a = ["apple", "banana"]
b = ["apple", "banana"]

a = b

b[0] = "grape"

print(a, b)
