def count_th(word):
    
    var_length = 2
    if len(word) < var_length:
        return 0

    if (word[0 : var_length] == "th"):
        return 1 + count_th(word[var_length - 1:])
    else:
        return count_th(word[var_length - 1:])

print(count_th("theworstthebest"))
