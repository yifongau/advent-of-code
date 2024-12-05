import os

path = "03-input.txt"

def split_groups(string, start, end):
    groups = []
    i = 0
    while i < len(string):
        candidate = []
        if string[i] == start:
            end_reached = 0
            candidate.append(string[i])
            i+=1
            while end_reached != 1:
                if string[i] != end:
                    candidate.append(string[i])
                    i+=1
                elif string[i] == end:
                    candidate.append(string[i])
                    i+=1
                    end_reached = 1
            groups.append(candidate)
        else: i+=1
    return groups

def fltr_no_illegal_chars(groups, allowed):

    def no_illegal_chars(item, allowed): 
        for i in item:
            if i not in allowed:
                return 0
        return 1

    filtered = []

    for i in groups:
        if check_illegal_chars(i,allowed) == 1:
            filtered.append(i)
    
    return filtered

def fltr_string_at_start(groups, string):
    
    def string_at_start(item, string):
        for i in range(len(string)):
            if item[i] != string[i]:
                return 0
        return 1

    filtered = []

    for i in groups:
        if string_at_start(i, string) == 1:
            filtered.append(i)

    return filtered

def fltr_string_at_index(groups, string_tuple):

    def string_at_index(item, string_tuple):
        if item[i] == index:
            return 1

    filtered = []

    for i in groups:
        if string_at_index(i, string_tuple) == 1:
            filtered.append(i)

    return filtered

# define filter parameters

def allowed_chars():
    allowed = []
    for i in list("mul(,)"):
        allowed.append(i)
    for i in list(range(10)):
        allowed.append(str(i))
    return allowed

allowed_chars = allowed_chars()
start_string = "mul("


# start program
with open(path) as f:
    content = f.read()

groups = split_groups(content,"m",")")        

#print(groups)
#print(fltr_no_illegal_chars(groups,allowed_chars))
print(fltr_string_at_start(fltr_no_illegal_chars(groups,allowed_chars),start_string))


