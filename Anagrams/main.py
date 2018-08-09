dictionary_reference = {}
for word in open('C:/Users/iFocus/Desktop/CRAP/anagrams/dicto.txt'):
    if len(word) > 8:
        word = word.lower().strip()
        alphabetizer = ''.join(sorted(list(word)))
        if alphabetizer not in dictionary_reference:
            dictionary_reference[alphabetizer] = list()
        dictionary_reference[alphabetizer].append(word)
anagrams_list = dictionary_reference.values()
formatting_list = list()
for i in anagrams_list:
    if len(set(i)) > 1:
        formatting_list.append(set(i))
output_format = ('\n'.join(', '.join(j) for j in sorted(formatting_list, key=len)))
file = open("output3.txt", "w")
file.write(output_format)
file.close()
