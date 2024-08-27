
import random

HEART = 0
CLUB = 1
DIAMOND = 2
SPADE = 3

htowns = ["Stettin", "Danzig", "Lübeck"]
ctowns = ["Riga", "Novgorod", "Visby"]
dtowns = ["Brügge", "Hamburg", "London"]
stowns = ["Oslo", "Stockholm", "Bergen"]

allt = []
allt.extend(htowns)
allt.extend(ctowns)
allt.extend(dtowns)
allt.extend(stowns)

tdict = {}
tnamedict = {}
for i, t in enumerate(allt):
    tdict[t] = i
    tnamedict[i] = t

cdict = {}
for i in range(3):
    cdict[htowns[i]] = i
    cdict[ctowns[i]] = i
    cdict[dtowns[i]] = i
    cdict[stowns[i]] = i

#color sorted deck without JQK and joker
class Deck:
    def __init__(self):
        self.contents = []
        for j in range(4):
            suit = []
            for i in range(1, 11):
                suit.append(i)
            random.shuffle(suit)   
            self.contents.append(suit)

    def draw4(self):
        if len(self.contents[0]) == 0:
            return None
        else:
            retlist = []           
            for i in range(4):
                retlist.append(self.contents[i].pop())
            return retlist




#generate production

prod = []
for i in range(len(allt)):
    prod.append([])

activeDeck = Deck()
deckCounter = 1

DAYS = 12

for day in range(DAYS):

    for sg in range(3):

        drawn = activeDeck.draw4()
        if drawn == None:
            activeDeck = Deck()
            deckCounter += 1
            drawn = activeDeck.draw4()

        prod[tdict[htowns[sg]]].append(drawn[0])
        prod[tdict[ctowns[sg]]].append(drawn[1])
        prod[tdict[dtowns[sg]]].append(drawn[2])
        prod[tdict[stowns[sg]]].append(drawn[3])

print(f"deckcounter = {deckCounter}")

out1 = "out_full.txt"

with open(out1, "w") as file:
    for i in range(len(prod)):
        file.write(f"{tnamedict[i]}")
        for j in prod[i]:
            file.write(f",{j}")
        file.write("\n")

out2 = "out_singledays.txt"

councilrange = [-1,0,1,2,0,1,2,0,1,2,0,1,2]
predictions = []

with open(out2, "w") as file:
    for d in range(DAYS):
        file.write(f"Den {d}:\n")
        for i in range(len(prod)):
            town = tnamedict[i]            
            tcday = cdict[town]
            file.write(town)
            if tcday == councilrange[d]:
                file.write("*")
                pstr1 = f"{town}: Predikce produkce (den {d}.)\n"
                pdaysleft = (DAYS-1)-d
                pstr2 = ""
                if pdaysleft > 2:
                    pstr2 = f"Dnes: {prod[i][d]}, zítra: {prod[i][d+1]}, pozítří: {prod[i][d+2]}"
                elif pdaysleft == 2:
                    pstr2 = f"Dnes: {prod[i][d]}, zítra: {prod[i][d+1]}"
                elif pdaysleft == 1:
                    pstr2 = f"Dnes: {prod[i][d]}"
                pstr = pstr1 + pstr2 + "\n---------------\n"
                predictions.append(pstr)
            file.write(f" {prod[i][d]}\n")
        file.write("--------\n")


out3 = "predikce.txt"
with open(out3, "w") as file:
    for p in predictions:
        file.write(p)




















