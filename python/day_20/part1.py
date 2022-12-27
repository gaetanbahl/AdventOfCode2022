
with open("input.txt", 'r') as f:
    lines = f.readlines()
    numbers = [int(l.strip()) for l in lines]

indices = list(range(len(numbers)))

for i in range(len(numbers)):

    orig = indices.index(i)
    number = numbers.pop(orig)
    orig_index = indices.pop(orig)
    new_index = (orig + number) % len(numbers)
    numbers.insert(new_index, number)
    indices.insert(new_index, orig_index)


index_zero = numbers.index(0)

n1000 = numbers[(index_zero + 1000) % len(numbers)]
n2000 = numbers[(index_zero + 2000) % len(numbers)]
n3000 = numbers[(index_zero + 3000) % len(numbers)]

print(n1000 + n2000 + n3000)