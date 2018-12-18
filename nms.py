from tqdm import tqdm
#national
with open("yob2017.txt","r") as f:
	natname = [line.strip() for line in f]
maincount = 0
for nat in tqdm(natname):
	count = int(nat[nat.find(",")+3:])
	maincount = maincount + count
reserve = {}
print maincount
for nat in tqdm(natname):
	nomgen = nat[:nat.find(",")+2]
	count = int(nat[nat.find(",")+3:])
	tmp = (count,1000000.0*count/maincount)
	reserve[nomgen] = tmp


with open('statenames.txt', 'r') as f:
    state = [line.strip() for line in f]
print state
for s in tqdm(state):
	with open(s, 'r') as f:
 	   names = [line.strip() for line in f]
 	outfilename = "Y_"+s
 	output = "state,name,gender,statecount,statepercent,natcount,natpercent\n"
 	statecount = 0
 	for n in names:
 	 	if n[5:9] == "2017":
 			ct = n[10:]
 			ct = ct[ct.find(",")+1:]
 			statecount = statecount + int(ct)
 	print statecount
 	for n in names:
 		if n[5:9] == "2017":
 			state = n[:2]
 			gender = n[2:4]
 			nom = n[10:]
 			namestatect = int(nom[nom.find(",")+1:])
 			statepct = 1000000.0*namestatect/statecount
 			name = nom[:nom.find(",")]+gender
 			natct = reserve[name][0]
			natpct = reserve[name][1]
			output = output + state + "," + name + "," + str(namestatect)  + "," + str(statepct)  + "," + str(natct)  + "," + str(natpct) + "\n"
			
	o = open(outfilename,"w")
	o.write(output)
	o.close()
