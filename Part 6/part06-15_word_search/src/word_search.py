# Write your solution here
def find_words(search_term: str):
    found_words = []
    with open("words.txt") as file:
        words = []
        for line in file:
            words.append(line.strip())
    if(search_term.endswith("*")):
        index = search_term.find("*")
        start = search_term[:index]
        for word in words:
            if(word.startswith(start)):
                found_words.append(word)
    elif(search_term.startswith("*")):
        index = search_term.find("*")
        end = search_term[index+1:]
        for word in words:
            if(word.endswith(end)):
                found_words.append(word)
    elif("." in search_term):
        index = search_term.find(".")
        for word in words:
            if(index == 0 and word.endswith(search_term[index+1:]) and len(word) == len(search_term)):
                found_words.append(word)
            elif(index == (len(search_term)-1) and word.startswith(search_term[:index]) and len(word) == len(search_term)):
                found_words.append(word)
            elif(word.startswith(search_term[0]) and word.endswith(search_term[-1]) and len(word) == len(search_term)):
                found_words.append(word)
            elif(search_term.endswith(".") and search_term.startswith(".") and len(word) == len(search_term) and (word.find(search_term[1:-1]) != -1)):
                found_words.append(word)
            elif(search_term.endswith(".") and search_term.count(".") > 1 and word.startswith(search_term[0]) and len(word) == len(search_term) and word[-2] == search_term[-2]):
                found_words.append(word)
            elif(search_term.startswith(".") and search_term.count(".") > 1 and word.endswith(search_term[-1]) and len(word) == len(search_term)):
                found_words.append(word)
    else:
        for word in words:
            if(word == search_term):
                found_words.append(word)
    return found_words

### Example solution
def find_words(search_term: str):
    results = []
 
    with open("words.txt") as file:
        # Tätä tarvitaan myöhemmin
        hakusana_ilman_tahtea = search_term.replace("*","")
 
        for word in file:
            word = word.replace("\n","")
            # Is there an asterisk?
            if "*" in search_term:
                # start or end?
                if search_term[0] == "*":
                    if word.endswith(hakusana_ilman_tahtea):
                        results.append(word)
                else:
                    if word.startswith(hakusana_ilman_tahtea):
                        results.append(word)
            # Is there a dot?
            elif "." in search_term:
                # same length?
                if len(search_term) == len(word):
                    found = True
                    for i in range(len(search_term)):
                        if search_term[i] != "." and search_term[i] != word[i]:
                            found = False
                            break
                    if found:
                        results.append(word)
            # No special characters, only whole word matches count
            else:
                if word == search_term:
                    results.append(word)
    return results