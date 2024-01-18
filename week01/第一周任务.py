#2
print('Hello, World!')

#3
print('L 10225501445')

#4
for star_index in range(10):
    print(chr(0x2605), end='')
print()

print(chr(0x2605), end='')
print('dase introduction', end='')
print(chr(0x2605))
for star_index in range(10):
    print(chr(0x2605), end='')
print()

#5
num1 = int(input('Please enter number 1: '))
num2 = int(input('Please enter number 2: '))
num3 = int(input('Please enter number 3: '))
number_list = [num1, num2, num3]
number_list.sort(reverse=True)
print(number_list)

#6
num_a = int(input('Please enter number a: '))
num_b = int(input('Please enter number b: '))
num_c = int(input('Please enter number c: '))
num_d = int(input('Please enter number d: '))

list_sorted = [num_a, num_b, num_c, num_d]
list_sorted.sort()
print(list_sorted)

#7
for odd_num in range(1, 100, 2):
    print(odd_num, end=' ')

#8
total_sum = 0
for number in range(1, 101):
    total_sum += number
print(total_sum)

#9
user_list = input('Enter a list: ').split()
user_list.reverse()
list_length = len(user_list)
for item in range(list_length):
    print(user_list[item])

index = 0
while index <= list_length - 1:
    print(user_list[index])
    index += 1

#10
input_str = input('Enter a string: ')
input_str_list = list(input_str)
print(input_str_list)

for char_index in range(len(input_str_list) - 1):
    if input_str_list[char_index] == input_str_list[char_index + 1]:
        print("YES")
        break

#11
input_string = input('Enter SS: ').replace(' ', '')
print(input_string)

#12
def calculate_cubic_root(value, tolerance=1e-6):
    if value < 0:
        raise ValueError("Cannot compute cubic root for negative numbers")

    lower_bound = 0
    upper_bound = max(1, value)

    while True:
        midpoint = (lower_bound + upper_bound) / 2
        error_margin = midpoint**3 - value

        if abs(error_margin) < tolerance:
            return midpoint

        if error_margin < 0:
            lower_bound = midpoint
        else:
            upper_bound = midpoint

print(calculate_cubic_root(n=3.1415926))

#13
def calculate_factorial(num):
    factorial_result = 1
    for factor in range(1, num + 1):
        factorial_result *= factor
    return factorial_result

print(calculate_factorial(5))
