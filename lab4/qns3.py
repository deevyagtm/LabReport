def number_generator():
    for i in range(1, 6):
        yield i

# Using the generator
for num in number_generator():
    print(num)
