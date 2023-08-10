def print_door_mat(n, m):
    pattern = [(".|." * (2 * i + 1)).center(m, "-") for i in range(n // 2)]
    welcome = "WELCOME".center(m, "-")
    door_mat = "\n".join(pattern + [welcome] + pattern[::-1])
    print(door_mat)

if __name__ == "__main__":
    n, m = map(int, input().split())
    if n % 2 == 1 and m == 3 * n:
        print_door_mat(n, m)
    else:
        print("Invalid input. Make sure N is an odd number and M is 3 times N.")
