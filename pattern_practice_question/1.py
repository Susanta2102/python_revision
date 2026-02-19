def generate_sqaure(n):
    input = n
    char = "*"

    for i in range(input):
        for j in range(input):
            print(char, end="")
        print()

n = int(input("Enter the size of the square: "))
generate_sqaure(n)  


