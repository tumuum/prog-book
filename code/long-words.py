import statistics

rd = open("tr-word-list.txt","r")
wr = open("tr-long-words.txt","w")

ws = rd.readlines()
rd.close()

lengths = []
for w in ws:
	lengths.append(len(w))

mean = statistics.mean(lengths)
sd = statistics.stdev(lengths)

treshold = round(mean + 2*sd)
print(mean,sd,treshold)

long_words=[]
for w in ws:
	if len(w) > treshold:
		long_words.append(w)	

wr.writelines(long_words)
wr.close()
