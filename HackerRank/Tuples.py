if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    result = hash(t)
    
    # print(type(result))
    print(result)
