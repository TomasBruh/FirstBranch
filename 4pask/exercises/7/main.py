def count_upper_lower_letters(a_word):
    upper = 0
    lower = 0
    for letter in a_word:
        if letter.islower():
            lower += 1
        elif letter.isupper():
            upper += 1
    return upper, lower


answer = count_upper_lower_letters("Kuršių Nerija")
print(f"Nr of uppercase letters: {answer[0]}")
print(f"Nr of lowercase letters: {answer[1]}")
