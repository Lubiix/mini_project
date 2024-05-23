words_list = ["Madam", "Civic", "House", "Car", "Radar"]

def find_palindrome(words):
    palindrome_list = []
    for word in words:
        reverse = word.lower()[::-1]
        if word.lower() == reverse:
            palindrome_list.append(word)
    return palindrome_list

result = find_palindrome(words_list)
print(result)
