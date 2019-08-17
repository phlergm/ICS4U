word = input("what word\n")
while(len(word) > 1): 
	if(word[0] == word[-1]): 
		word = word[1:-2]
	else: 
		print ("False")