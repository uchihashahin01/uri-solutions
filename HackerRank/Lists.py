def insert(item, list):
    list.insert(int(item[1]), int(item[2]))
    return list

def print_func(list):
    return print(list)

def remove_func(item , list):
    list.remove(int(item[1]))
    return list

def append_func(item,list):
    list.append(int(item[1]))
    return list

def sort_func(list):
    list.sort()
    return list

def pop_func(list):
    list.pop()
    return list
    
def reverse_func(list):
    list.reverse()
    return list

my_list= []
for _ in range(int(input())):
    command_values = input().split()
    
    if command_values[0] == 'insert':
        # my_list.insert(int(command_values[1]), int(command_values[2]))
        insert(command_values, my_list)
    
    elif command_values[0] == 'print':
        print_func(my_list)
        
    elif command_values[0] == 'remove':
        remove_func (command_values,my_list)
        
    elif command_values[0] == 'append':
        append_func(command_values, my_list)
        
    elif command_values[0] == 'sort':
        sort_func(my_list)
        
    elif command_values[0] == 'pop':
        pop_func(my_list)
        
    else:
        reverse_func(my_list)

# print(my_list)
