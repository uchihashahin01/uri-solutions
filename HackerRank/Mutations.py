def mutate_string(string, position, character):
    return string[: position] + character + string[position+1 :]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
    
# def mutate_string(string, position, character):
#     my_list = list(string)
#     my_list[position] = character
#     return ''.join(my_list)

# if name == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)
