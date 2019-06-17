"""Find Palindromes in a dictionary file"""
import dictionary_import
word_list = dictionary_import.load('greentea_dictionary.txt')
pali_list = []

for word in word_list:
    if len(word) > 1  and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
