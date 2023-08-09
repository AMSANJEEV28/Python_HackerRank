if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        command = input().split()
        task = command[0]
        values = list(map(int, command[1:]))
                
        if task == "insert":
            index = values[0]
            inserted_values = values[1:]
            for value in inserted_values:
                my_list.insert(index, value)
                index += 1  # Adjust the index for the next insertion
        elif task == "print":
            print(my_list)
        elif task == "remove":
            value = values[0]
            if value in my_list:
                my_list.remove(value)
        
        elif task == "append":
            value = values[0]
            my_list.append(value)
        elif task == "sort":
            my_list.sort()
        elif task == "pop":
            if my_list:
                popped_value = my_list.pop()
            else:
                print("List is empty")
        elif task == "reverse":
            my_list.reverse()
        else:
            print("Give the right command in lowercase only")
