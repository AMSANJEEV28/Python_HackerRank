def print_rangoli(size):
    import string

    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        line = '-'.join(alphabet[size - 1:i:-1] + alphabet[i:size])
        lines.append(line.center(4 * size - 3, '-'))

    print('\n'.join(lines[:0:-1] + lines))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)