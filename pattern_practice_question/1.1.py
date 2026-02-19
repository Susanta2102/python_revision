def generate_square(n):
    result = []
    char = "*"
    for i in range(n):
        row = char * n 
        result.append(row)
    return result

n = int(input("Enter the size of the square: "))
square = generate_square(n)
for row in square:
    print(row)

    