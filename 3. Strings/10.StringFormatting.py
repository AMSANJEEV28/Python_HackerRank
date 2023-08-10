def print_formatted(number):
    width = len(bin(number)[2:])  # Calculate the width based on the binary representation

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = (hex(i)[2:]).upper()
        binary = bin(i)[2:]

        # Print formatted values using the calculated width
        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)