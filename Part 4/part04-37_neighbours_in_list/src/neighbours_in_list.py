# Write your solution here
def longest_series_of_neighbours(numbers: list):
    length = 0
    current_length = 1
    for i in range(len(numbers)-1):
        if(numbers[i] == numbers[i+1]+1 or numbers[i] == numbers[i+1]-1):
            current_length += 1
            if(i == len(numbers)-2 and current_length > length):
                length = current_length
        else:
            if(current_length > length):
                length = current_length
            current_length = 1
    return length

#def longest_series_of_neighbours(my_list: list):
    #longest = 1
    #result = 1
    #for i in range(1, len(my_list)):
        # function abs calculates the absolute value
        #if abs(my_list[i-1]-my_list[i]) == 1:
            #result += 1
        #else:
            #result = 1
        # function max returns the highest of the parameters
        #longest = max(longest, result)
    #return longest