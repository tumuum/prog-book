# The file we will read has a single word in each line
# Therefore reading all the lines in a file into a list
# directly gives a word list. Words, however, come with 
# a newline character '\n' at the end; to get rid of this 
# python provides the method strip(). Observe its use below.

f = open("tr-word-list.txt", "r")

sum = 0
wlist = f.readlines()

# we no longer need the file, so we close the
# stream
f.close()

for w in wlist:
	sum += len(w.strip())

meanwl = sum/len(wlist) 

print("The mean word length = ",str(meanwl))
