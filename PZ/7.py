def count_uppercase_latin_letters(s):
    count = 0
    for char in s:
        if char.isalpha() and char.isupper() and 'A' <= char <= 'Z':
            count += 1
    return count

string = "Hello World! This is an Example with UPPERCASE letters."
result = count_uppercase_latin_letters(string)
print(result)





def count_words_in_russian_sentence(sentence):
    words = sentence.split()
    return len(words)

russian_sentence = "Это пример предложения на русском языке."
result = count_words_in_russian_sentence(russian_sentence)
print(result) 
