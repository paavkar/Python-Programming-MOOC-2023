
def balanced_brackets(my_string: str):
    for char in my_string:
        if char not in "([])":
            my_string = my_string.replace(char, "")
    if len(my_string) == 0:
        return True
    if not (my_string[0] == '(' and my_string[-1] == ')') and not (my_string[0] == '[' and my_string[-1] == ']'):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])

### Example solution 
def balanced_brackets(mj: str):
    # string is empty, so it is ok
    if len(mj) == 0:
        return True
 
    # if first character is not any bracket, let's eat it away
    if not mj[0] in "()[]":
        return balanced_brackets(mj[1:])
 
    # if last is not any bracket, let's eat it away
    if not mj[-1] in "()[]":
        return balanced_brackets(mj[:-1])
    
    # now is known that first and last characters are brackets
    # check if they are a pair
    if mj[0]=="(" and mj[-1]==")":
        return balanced_brackets(mj[1:-1])
    if mj[0]=="[" and mj[-1]=="]":
        return balanced_brackets(mj[1:-1])
 
    # were not, so this string is not ok
    return False
 