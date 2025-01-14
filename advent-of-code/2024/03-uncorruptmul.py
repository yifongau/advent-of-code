import os

path = "03-input.txt"

def split_groups(raw_string, match_string):
    groups = []
    i = 0
    while i < len(raw_string):
        candidate = []
        if raw_string[i] == match_string[0]:
            end_reached = 0
            candidate.append(raw_string[i])
            i+=1
            while end_reached != 1:
                if raw_string[i] != match_string[len(match_string)-1]:
                    candidate.append(raw_string[i])
                    i+=1
                elif raw_string[i] == match_string[len(match_string)-1]:
                    candidate.append(raw_string[i])
                    i+=1
                    end_reached = 1
            groups.append(candidate)
        else: i+=1
    return groups

def match_groups(groups, match_string):

    def match_group(group, match_string):
        for i in range(len(string)):
            if string


def fltr_no_illegal_chars(groups, allowed):

    def no_illegal_chars(item, allowed): 
        for i in item:
            if i not in allowed:
                return 0
        return 1

    filtered = []

    for i in groups:
        if no_illegal_chars(i,allowed) == 1:
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

def create_match_string():
    match_string = []
    for char in 'mul(':
        match_string.append(char)
    
    substring = []
    for possibility in range(3):
        sub2string = []
        for i in range(possibility+1):
            sub3string = []
            for i in range(10):
                sub3string.append(str(i))
            sub2string.append(sub3string)
        substring.append(sub2string)
    match_string.append(substring)
    
    for char in ',':
        match_string.append(char)

    substring = []
    for possibility in range(3):
        sub2string = []
        for i in range(possibility+1):
            sub3string = []
            for i in range(10):
                sub3string.append(str(i))
            sub2string.append(sub3string)
        substring.append(sub2string)
    match_string.append(substring)

    for char in ')':
        match_string.append(char)
    
    return match_string

match_string = create_match_string()

def allowed_chars():
    allowed = []
    for i in list("mul(,)"):
        allowed.append(i)
    for i in range(10):
        allowed.append(str(i))
    return allowed

allowed_chars = allowed_chars()
start_string = "mul("


# start program
with open(path) as f:
    content = f.read()

#groups = split_groups(content,"m",")")        

#print(fltr_string_at_start(fltr_no_illegal_chars(groups,allowed_chars),start_string))
#print(legit_strings)

print(split_groups(content, match_string))
