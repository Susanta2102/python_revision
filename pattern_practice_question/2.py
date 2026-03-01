#hollow square pattern

def generate_hollow_square(n):
    char = "*"
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print(char, end="")
            else:
                print(" ", end="")
        print()
n = int(input("Enter the size of the square: "))
generate_hollow_square(n)   