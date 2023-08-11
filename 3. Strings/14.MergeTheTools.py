def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub = string[i:i+k]  # Get the current substring of length k
        # Initialize an empty list to store unique characters
        unique_chars = []
        for char in sub:
            if char not in unique_chars:
                unique_chars.append(char)

        
        # Print the merged string by joining the unique characters
        print(''.join(unique_chars))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)