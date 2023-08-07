# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)

    
    winner = arr[0]
    
    runner_up = None

    for x in arr:
        if x < winner:
            runner_up = x
            break

    print(runner_up)