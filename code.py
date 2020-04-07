import pandas as pd

data = pd.read_csv("train.csv")
g = data["Genre"].values
a = data["Actors"].values
di = data["Director"].values
success = data["Metascore"].values

l1 = input("Enter Genre:")
l=l1.split(',')
e1 = input("Enter Actors: ")
e=e1.split(',')
d1 = input("Enter Director:")
d=d1.split(',')

numYes = 0
numNo = 0
for i in success:
	if(i >= 65):
		numYes = numYes + 1
	else:
		numNo = numNo + 1
probYes = numYes/data.shape[0]
probNo = numNo/data.shape[0]


numl = 0
nume = 0
numd = 0
for i in g:
    j=i.split(',');
    for k in j:
        for m in l:
            if(k == m):
                numl = numl + 1
                break
probl = numl/data.shape[0]

for i in a:
    j=i.split(',');
    for k in j:
        for m in e:
            if(k == m):
                nume = nume + 1
                break           
probe = nume/data.shape[0]

for i in di:
    j=i.split(',');
    for k in j:
        for m in d:
            if(k == m):
                numd = numd + 1
                break
probd = numd/data.shape[0]
numYesl = 0
numNol = 0

for i1,j in zip(g, success):
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
for i1,j in zip(a, success):
    i=i1.split(',')
    for k in e:
        for k1 in i:
            if(k1 == k):
                if(j >= 50):
                    numYese += 1
                else:
                    numNoe += 1
probYese = numYese/nume
probNoe = numNoe/nume


numYesd = 0
numNod = 0
for i1,j in zip(di, success):
    i=i1.split(',')
    for k in d:
        for k1 in i:
            if(k1 == k):
                if(j >= 50):
                    numYesd += 1
                else:
                    numNod += 1
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

if(yes >= no):
	print("\n Event was Successfull")
else:
	print("\n Event was NOT Successfull")
