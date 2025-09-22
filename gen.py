import pandas as pd
import numpy as np
import random as random

random.seed(0)

def roll_dX(X):
 return random.choice(list(range(X)))+1

startDay = 117
endDay = 3016

nSectors = 12

wdayList = []
archibaldList = []
archiwiseList = []
averillList = []
azeruList = []
boltholopewList = []
burovaList = []
caynList = []
dannyList = []
dankonList = []
gnarckList = []
gouberiList = []
lomeriusList = []
moonList = []
nettieList = []
pentaList = []
ricewinedList = []
tehamiList = []
yungreenList = []
zancroList = []
zeledinList = []

dayList = []
healList = []
sectorList = []

averillSeedDay = 0
averillSeedLoc = 0

for i in range(startDay,endDay):#Years are 513 days long, weeks are 8 days long
 #Wizard roll call!
 
 #Archibald summers in the posh districts
 
 archibald=0
 if ((i%513)>207) and ((i%513)<333):
  archibald = random.choice([roll_dX(4)+roll_dX(4)-1, 3])
 
 archibaldList.append(archibald)
 
 #Archiwise is just here for work, takes weekends off
 
 archiwise=0
 if i%8<6:
  archiwise = random.choice([5]*57+[7]*43)
 
 archiwiseList.append(archiwise)
 
 #Averill shows up at random
 averill = 0
 
 if len(averillList)>4:
  if (averillList[-5:] == [0,0,0,0,0]) and (roll_dX(4)==4):
   averill = random.choice([roll_dX(4), 3+roll_dX(4), 6, 14-roll_dX(4)-roll_dX(6)])
   averillSeedDay = i+roll_dX(4)
   averillSeedLoc = averill
 
 averillList.append(averill)
 
 #Azeru is working her way around the clock, except when she's Cayn
 
 azeru=0
 if random.choice([True]*623+[False]*377):
  azeru = (i%12)+1
 
 azeruList.append(azeru)
 
 #Boltholopew is just here for fun, takes threekends on, slumming it in the poor areas
 
 boltholopew = 0
 if ((i%8)>4):
  boltholopew = max(12-roll_dX(8),12-roll_dX(8)) 
 
 boltholopewList.append(boltholopew)
 
 #Burova visits family at the end of a year
 
 burova=0
 if i%513>470:
  burova = random.choice([4,12])
 
 burovaList.append(burova)
 
 #Cayn is working her way around the clock, except when she's Azeru
 
 cayn = 0
 if azeru==0:
  cayn = (i%12)+1
 
 caynList.append(cayn)
 
 #Danny Nova visits at random, more not than often.
 
 danny = 0
 if roll_dX(6)==6 or roll_dX(4)==4:
  danny = min(roll_dX(12), roll_dX(8)+roll_dX(4))
 
 dannyList.append(danny)
 
 #Dankon Ground makes a pitstop while travelling for work every now and then 
 
 dankon = 0
 
 if roll_dX(8)==8:
  dankon = random.choice([roll_dX(12), roll_dX(4), 5, 6+roll_dX(4)])
 
 dankonList.append(dankon)
 
 #Gnarck only shows up for The Festival; gets there early
 
 gnarck = 0
 
 if ((i%513) >= 203) and ((i%513) <= 230):
  gnarck = 7+roll_dX(2)+roll_dX(2)
 
 gnarckList.append(gnarck)
 
 #Gouberi spends all its time in the University sector, only showing its face in the Spring
 
 gouberi = 6
 
 if ((i%513)>=107):
  gouberi = 0
 
 gouberiList.append(gouberi)
 
 #Lomerius Xardus hangs out with the middle classes, because someone has to; occasionally leaves for a weekend
 
 if (i<610) or ((i%8>5) and (roll_dX(6)==6)):
  lomerius=0
 else:
  lomerius = random.choice([4]*5 + [5]*29 + [6]*52 + [7]*11 + [8]*3)
 
 lomeriusList.append(lomerius)
 
 #Moon Finder just kinda shows up randomly, usually slumming it; also goes to The Festival
 
 if roll_dX(6)==6 or roll_dX(20)==20:
  moon=0
 else:
  if ((i%513) >= 210) and ((i%513) <= 230):
   moon = gnarck
  else:
   moon = random.choice([3+ roll_dX(8), 5+ roll_dX(6), max(12-roll_dX(4), 12-roll_dX(6)), roll_dX(4)])
 
 moonList.append(moon)
   
 #Nettie Silver wanders around healing when able, stays in her bed at the Barracks when not: is unable more frequently as age gets the better of her.
 
 nettie = random.choice([random.choice(i*[12]+(5000-i)*[1+roll_dX(10)]), max(12-roll_dX(6), 12-roll_dX(8))])
 
 nettieList.append(nettie)
 
 #Penta Vasi showed up like twice.
 
 penta=0
 
 if (i==1056) or (i==1577):
  penta=6
 
 pentaList.append(penta)
 
 #Ricewined visits for a few days every now and then; religiously attends the Festival
 
 ricewined = 0
 
 if i>1100:
  if ((i%513) >= 210) and ((i%513) <= 230):
   ricewined = gnarck
  else:
   if len(ricewinedList)>0:
    if ricewinedList[-1]!=0:
     ricewined = random.choice([6, 2+roll_dX(8), 5+roll_dX(6), 0])
    else:
     ricewined = random.choice([0]*83+[6]*17)
 
 ricewinedList.append(ricewined)
 
 #Tehami Darke usually sticks to the University sector, but occasionally leaves or makes excursions to others
 
 tehami = 0
 
 if i>277:
  if (roll_dX(6)==0) or (roll_dX(12)>0):
   tehami=random.choice([6]*69+[12-roll_dX(4)]*19+[1+roll_dX(6)+roll_dX(4)]*12)
 
 tehamiList.append(tehami)
 
 #Yungreen passed through here for like two weeks, then completed his mission
 
 yungreen=0
 
 if ((i>2007) and (i<2025)):
  yungreen=12
 
 yungreenList.append(yungreen)
 
 #Zancro keeps teleporting into literally completely random sectors and teleporting out
 
 zancro=0
 
 if roll_dX(100)>78:
  zancro=roll_dX(12)
 
 zancroList.append(zancro)
 
 #Zeledin Zura was very boring
 
 zeledin = 0
 
 if ((i>542) and (i<2533)):
  zeledin = 4
 
 zeledinList.append(zeledin)
 
 
 #==Who's feelin like healin?==
 
 day = i-startDay+1
 
 wdayList.append(day)
 
 #Averill buries Healing Seeds, which hatch 1d4 days after and heal Rumblepox in particular
 
 if i == averillSeedDay:
  cases = max(roll_dX(4), roll_dX(6), roll_dX(averillSeedLoc))
  for c in range(cases):
   dayList.append(day)
   healList.append("Rumblepox")
   sectorList.append(averillSeedLoc)
 
 #Danny heals all poxes
 
 if danny>0:
  cases = min(roll_dX(4), roll_dX(4))
  for c in range(cases):
   dayList.append(day)
   healList.append(random.choice(["Babblepox"]*19+["Bumblepox"]*14+["Chucklepox"]*33+["Gurglepox"]*9+["Rumblepox"]*13+["Scramblepox"]*12))
   sectorList.append(danny)
 
 #Dankon heals Gurglepox or Itchy Throat if he can find some in the opposite sector to him
 
 if dankon>0:
  if roll_dX(20)>3:
   targetSector = (dankon+5)%12+1
   dayList.append(day)
   healList.append(random.choice(["Gurglepox"]*(57+targetSector)+["Mildly But Persistently Itchy Throat"]*(43-targetSector)))
   sectorList.append(targetSector)
 
 #Azeru heals people of bumblepox and scramblepox in the sector next door (Cayn would NEVER do such a thing!)
 
 if azeru>0:
  targetSector=random.choice([azeru%12+1, (azeru-2)%12+1])
  dayList.append(day)
  healList.append(random.choice(["Bumblepox"]*27+["Scramblepox"]*73))
  sectorList.append(targetSector)
  
 #Whenever Bolt and Moon Finder find themselves with a sector between them (OTHER than 12) they heal a dozen or so cases of PD/DS/Pa in it
 
 if ((boltholopew>0) and (moon>0)):
  if (abs(boltholopew-moon)==2):
   cases= roll_dX(6)+roll_dX(8)+roll_dX(10)
   for c in range(cases):
    targetSector=int((boltholopew+moon)/2)
    dayList.append(day)
    healList.append(random.choice(["Problems Disorder"]*(22+targetSector)+["Disease Syndrome"]*(47-targetSector*3)+["Parachondria"]*(31-targetSector*2)))
    sectorList.append(targetSector)
    
 #Nettie compulsively heals Smokesickness whenever she sees it
 
 if (nettie>0) and (nettie<12):
  cases=random.choice([roll_dX(nettie)-1, min(roll_dX(10)-1,roll_dX(10)-1), roll_dX(4)-1])
  for c in range(cases):
   dayList.append(day)
   healList.append("Smokesickness")
   sectorList.append(nettie)
  
 #Tehami Darke heals DSBS remotely from the University: occasionally heals in person
 
 if (i>505) and (tehami>0):
  if tehami==6:
   cases = roll_dX(8)
   for c in range(cases):
    dayList.append(day)
    healList.append("Disquietingly Serene Bowel Syndrome")
    sectorList.append(min(roll_dX(12),max(roll_dX(12),roll_dX(12))))
  else:
   cases = roll_dX(4)-1
   for c in range(cases):
    dayList.append(day)
    healList.append("Disquietingly Serene Bowel Syndrome")
    sectorList.append(tehami)
    
 #Lomerius Xardus heals Chucklepox remotely from a tower in Sector 5.
 
 if lomerius==5:
  dayList.append(day)
  healList.append("Chucklepox")
  sectorList.append(roll_dX(12))
 
 #Zancro doesn't know he's not supposed to heal Scrapes; whoops; heals more of them in the Barracks because there are more.
 
 if zancro>0:
  cases = roll_dX(4)-1 + (zancro==12)*(roll_dX(8)-1)
  for c in range(cases):
   dayList.append(day)
   healList.append(random.choice(["Scraped Elbow"]*27+["Scraped Knee"]*73))
   sectorList.append(zancro)
 
 #A slowly decaying spell Gouberi set running years ago heals random Shiverers.
 
 if roll_dX(40)>(7+i/300):
  dayList.append(day)
  healList.append("The Shivers")
  sectorList.append(random.choice([6]*32+ [12]*11+ [min(roll_dX(12), roll_dX(12))]*20+ [roll_dX(12)]*37))



locationDf = pd.DataFrame({"Day":wdayList,"Archibald the Wise":archibaldList, "Archiwise the Bald":archiwiseList, "Averill": averillList, "Azeru":azeruList, "Boltholopew":boltholopewList, "Burova":burovaList, "Cayn": caynList, "Danny Nova": dannyList, "Dankon Ground":dankonList, "Gnarck": gnarckList, "Gouberi": gouberiList, "Lomerius Xardus": lomeriusList, "Moon Finder": moonList, "Nettie Silver": nettieList, "Penta Vasi": pentaList, "Ricewined": ricewinedList, "Tehami Darke": tehamiList, "Yungreen": yungreenList, "Zancro": zancroList, "Zeledin Zura": zeledinList})

locationDf = locationDf.replace(0,"N/A")

locationDf.to_csv("locations.csv")

healDf = pd.DataFrame({"Day": dayList, "Disease Healed": healList, "Sector": sectorList})

healDf.to_csv("heals.csv")

