numbers = [1, 2, 3, 4, 5]

print(1 in numbers)
print(10 in numbers)
numbers.append(6)
print(numbers)

numbers.insert(0, -1)
print(numbers)

numbers.insert(6, -1)
print(numbers)

numbers.remove(3)
print(numbers)

numbers.clear()
print(numbers)

print(len(numbers))