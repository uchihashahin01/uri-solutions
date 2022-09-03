def count_substring(string, sub_string):
    count = 0    
    finding = string.find(sub_string)
    
    while finding !=-1:
        count += 1
        finding = string.find(sub_string, finding + 1)
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)