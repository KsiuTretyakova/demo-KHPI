'''
Напишіть програму, яка переводить натуральне число N (1 ≤ N ≤ 3999)
з римської системи числення в десяткову.
Вхідний рядок містить число N, записане в римській системі числення.
Програма повинна вивести десятковий запис числа N.
'''

values = "IVXLCDM"
numbers = [1, 5, 10, 50, 100, 500, 1000]

# s = input("Enter roman number: ").upper()
s = "IX"

prev = 0
total = 0

for i in range(len(s) - 1, -1, -1):
    ch = s[i] # X, i = 1
    value = numbers[values.index(ch)] # X - 2 -> numbers[2] = 10

    if value < prev:
        total -= value
    else:
        total += prev

    # print(value)

print(f"Roman {s} to desimal: {total}")
