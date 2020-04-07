import pandas as pd

data = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
l1 = test["Genre"].values
e1 = test["Actors"].values
d1 = test["Director"].values
s1 = test["Metascore"].values
location = data["Genre"].values
event = data["Actors"].values
time = data["Director"].values
success = data["Metascore"].values


#l1 = input("Enter Genre:")
#l=l1.split(',')
#e1 = input("Enter Actors: ")
#e=e1.split(',')
#d1 = input("Enter Director:")
#d=d1.split(',')

numYes = 0
numNo = 0
for i in success:
	if(i >= 65):
		numYes = numYes + 1
	else:
		numNo = numNo + 1
probYes = numYes/data.shape[0]
probNo = numNo/data.shape[0]

tp=0
tn=0
fp=0
fn=0
for x in range(200):
    l=l1[x].split(',')
    e=e1[x].split(',')
    d=d1[x].split(',')
    
    numl = 0
    nume = 0
    numd = 0
    for i in location:
        j=i.split(',');
        for k in j:
            for m in l:
                if(k == m):
                    numl = numl + 1
                    break
    probl = numl/data.shape[0]

    for i in event:
        j=i.split(',');
        for k in j:
            for m in e:
                if(k == m):
                    nume = nume + 1
                    break           
    probe = nume/data.shape[0]

    for i in time:
        j=i.split(',');
        for k in j:
            for m in d:
                if(k == m):
                    numd = numd + 1
                    break
    probd = numd/data.shape[0]
    numYesl = 0
    numNol = 0

    for i1,j in zip(location, success):
        i=i1.split(',');
        for k in l:
            for k1 in i:
                if(k1 == k):
                    if(j>= 50):
                        numYesl = numYesl + 1
                    else:
                        numNol = numNol + 1
        probYesl = numYesl/numl

        probNol = numNol/numl


    numYese = 0
    numNoe = 0
    for i1,j in zip(event, success):
        i=i1.split(',')
        for k in e:
            for k1 in i:
                if(k1 == k):
                    if(j >= 50):
                        numYese += 1
                    else:
                        numNoe += 1
    if nume==0:
        continue
    else:
        probYese = numYese/nume
        probNoe = numNoe/nume


        numYesd = 0
        numNod = 0
        for i1,j in zip(time, success):
            i=i1.split(',')
            for k in d:
                for k1 in i:
                    if(k1 == k):
                        if(j >= 50):
                            numYesd += 1
                        else:
                            numNod += 1
    if numd==0:
        continue
    else:
        probYesd = numYesd/numd
        probNod = numNod/numd

        problYes = (probl*probYesl)/probYes
        probeYes = (probe*probYese)/probYes
        probdYes = (probd*probYesd)/probYes


        problNo = (probl*probNol)/probNo
        probeNo = (probe*probNoe)/probNo
        probdNo = (probd*probNod)/probNo


        yes = problYes*probeYes*probdYes
        no = problNo*probeNo*probdNo

        if(yes >= no and s1[x]>=65):
            tp=tp+1
        elif(yes>=no and s1[x]<65):
            fp=fp+1
        elif(yes<=no and s1[x]<65):
            tn=tn+1
        else:
            fn=fn+1
            
print(tp)
print(fp)
print(tn)
print(fn)

print((tp+tn)/(tp+fp+tn+fn))
