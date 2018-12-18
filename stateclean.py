from tqdm import tqdm
#national
with open("yob2017.txt","r") as f:
	natname = [line.strip() for line in f]
maincount = 0
for nat in tqdm(natname):
	count = int(nat[nat.find(",")+3:])
	maincount = maincount + count
preserve = {}
print maincount
for nat in tqdm(natname):
	nomgen = nat[:nat.find(",")+2]
	count = int(nat[nat.find(",")+3:])
	tmp = (count,1000000.0*count/maincount)
	preserve[nomgen] = tmp


#Find ONLY Names That Are In All State Files
with open('statenames.txt', 'r') as f:
    state = [line.strip() for line in f]
state_names = []
for k in preserve:
	state_names.append(k)
print len(state_names)
for s in tqdm(state):
	temp = []
	with open(s, 'r') as fs:
 	   names = [line.strip() for line in fs]
 	for n in names:
 	 	if n[5:9] == "2017":
 			gender = n[2:4]
 			nom = n[10:]
 			name = nom[:nom.find(",")]+gender
 			if name in state_names:
 				temp.append(state_names.pop(state_names.index(name)))

 	del state_names[:]
 	for i in temp:
 		state_names.append(i)
 	del temp[:]
print len(state_names)

maincount = 0
print len(state_names)
with open("yob2017.txt","r") as f:
	natname = [line.strip() for line in f]
for nat in tqdm(natname):
	count = int(nat[nat.find(",")+3:])
	n = nat[:nat.find(",")+2:]
	if n in state_names:
		maincount = maincount + count
reserve = {}
for nat in tqdm(natname):
	nomgen = nat[:nat.find(",")+2]
	if nomgen in state_names:
		count = int(nat[nat.find(",")+3:])
		maincount = maincount + count
		tmp = (count,1000000.0*count/maincount)
		reserve[nomgen] = tmp
print maincount


with open('statenames.txt', 'r') as f:
    state = [line.strip() for line in f]
print state
for s in tqdm(state):
	with open(s, 'r') as f:
 	   names = [line.strip() for line in f]
 	outfilename = "X_"+s
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
 			if name in state_names:
 				natct = reserve[name][0]
				natpct = reserve[name][1]
				output = output + state + "," + name + "," + str(namestatect)  + "," + str(statepct)  + "," + str(natct)  + "," + str(natpct) + "\n"
			
	o = open(outfilename,"w")
	o.write(output)
	o.close()
