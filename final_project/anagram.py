words = []
e_dict = open("e_dict.txt","r")
read = e_dict.readlines()
for i in range(len(read)):
	if len(read[i])>7:
		words.append(read[i].rstrip('\n'))
		
def compare1(string1, string2):
	for i in string1:
		if string2.find(i) == -1:
			return -1
		else:
			string2 = string2[0:string2.find(i)] + string2[string2.find(i)+1:]
	if string2 == "":
		return 1
	else:
		return -1

anagram = []

print(compare1("ala","alaif"))

def findAnagrams():
	while words != []:
		tempAna = []
		ref = words[0]
		words.pop(0)
		for i in words:
			if len(i) == len(ref) and compare1(ref,i) == 1:
				tempAna.append(i)
				words.remove(i)
		if len(tempAna) != 0:
			tempAna.append(ref)
			print(tempAna)
			anagram.append(tempAna)

findAnagrams()			
print(anagram)
		