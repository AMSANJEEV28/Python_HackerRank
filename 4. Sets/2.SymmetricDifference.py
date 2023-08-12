# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    # Read the size and elements of set A
    m = int(input())
    set_a = set(map(int, input().split()))

    # Read the size and elements of set B
    n = int(input())
    set_b = set(map(int, input().split()))

    # Calculate the symmetric difference
    symmetric_diff = set_a.symmetric_difference(set_b)

    # Print the symmetric difference in ascending order
    for num in sorted(symmetric_diff):
        print(num)
