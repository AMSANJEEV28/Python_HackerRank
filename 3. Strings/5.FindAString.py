def count_substring(string, sub_string):
    len_ss=len(sub_string)
    len_s =  len(string)
    count=0
    for i in range (len_s - len_ss + 1):
        if sub_string == string[i:i+len_ss]:
            count+=1
    return count 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)