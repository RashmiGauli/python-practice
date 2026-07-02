data_list = input("enter numbers with spaces")
numbers = [int(x) for x in data_list.split()]

max = numbers[0]
min = numbers[0]


for i in numbers:
    if i > max:
        max = i
    if i < min:
        min = i

avg = sum(numbers)/len(numbers)

print(f"Max = {max}\nMin = {min}\nAverage = {avg}")
