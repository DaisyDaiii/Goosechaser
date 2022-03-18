import sys

from creature import Creature,Goose
from item import Item
from location import Location
from preprocessing import process_locations, process_exits,\
                          process_items, process_creatures

def turn():
  i=0
  while i<len(creatures):
    if creatures[i].location==currentlocation.name and creatures[i].runtime<=2:
      if creatures[i].terror_rating>=goose.terror_rating or creatures[i].runtime==2:
        print()
        print(creatures[i].name+" is trying to catch you!")
        print("Oh no, you've been caught!")
        print("========= GAME OVER =========")
        quit()
      else:
        creatures[i].runtime+=1
        print()
        print(creatures[i].name+" is trying to catch you!")
        print("But your presence still terrifies them...")

    else:
      n=0
      while n<len(locations):
        if locations[n].name==creatures[i].location:
          t=locations[n]
          break
        n+=1
      if len(t.direction)>0:
        h=0
        s=0
        while h<len(t.direction):
          if t.dir_dest[t.direction[h]].name==currentlocation.name:
            s=1
            creatures[i].direction=t.direction[h]
            creatures[i].location=currentlocation.name
            t.remove_creature(creatures[i])
            currentlocation.add_creature(creatures[i])
            creatures[i].runtime=1
            print()
            print(creatures[i].name+" has arrived at "+currentlocation.name+".")
            break
          h+=1
        if s==0:
          if len(t.locationitem)>0:
            creatures[i].take(t.locationitem[0])
            t.remove_item(t.locationitem[0])
          else:
            if creatures[i].direction in t.dir_dest:
              aftermove=t.dir_dest[creatures[i].direction]
              creatures[i].location=aftermove.name
              aftermove.add_creature(creatures[i])
              t.remove_creature(creatures[i])
            else:
              around=['north','northeast','east','southeast','south','southwest','west','northwest']
              direc=creatures[i].direction.lower()
              u=0
              j=0
              while u<len(around):
                if around[u]==direc:
                  j=u
                  break
                u+=1
              m=j
              while direc not in t.dir_dest:
                j+=1
                if j==len(around):
                  j=0
                direc=around[j]
                if j==m:
                  break
              if direc in t.dir_dest:
                location2=t.dir_dest[direc]
                creatures[i].direction=direc
                creatures[i].location=location2.name
                location2.add_creature(creatures[i])
                t.remove_creature(creatures[i])
                creatures[i].runtime=1
                if location2.name==currentlocation.name:
                  print()
                  print(creatures[i].name+" has arrived at "+currentlocation.name+".")
      else:
        if len(t.locationitem)>0:
          creatures[i].take(t.locationitem[0])
          t.remove_item(t.locationitem[0])
    i+=1   
  
  
if len(sys.argv)<5:
  print("Usage: python3 game.py <PATHS> <ITEMS> <CHASERS> <EXITS>")
  quit()
i=0
while i<len(sys.argv):
  try:
    f=open(sys.argv[i],'r')
  except FileNotFoundError:
    print("You have specified an invalid configuration file.")
    quit()
  i+=1
  
direction=[]
destination=[]
dir_dest={}
locations=process_locations(sys.argv[1])
items=process_items(sys.argv[2],locations)
creatures=process_creatures(sys.argv[3],locations)
exits=process_exits(sys.argv[4],locations)

f=open(sys.argv[1],'r')
j=0
line1=""
while j<len(locations):
  if line1=="":
    line=f.readline()
  while line!="\n":
    line2=line.rstrip("\n")
    line2=line2.split(">")
    i=0
    while i<len(line2):
        line2[i]=line2[i].rstrip(" ")
        line2[i]=line2[i].lstrip(" ")
        i+=1
    if line2[0] == locations[j].name:
      line1=""
      direction.append(line2[1].lower())
      i=0
      while i<len(locations):
        if locations[i].name == line2[2]:
          dir_dest[line2[1].lower()]=locations[i]
          destination.append(locations[i])
          break
        i+=1
    if line2[0]!=locations[j].name:
      line1=line
      break
    line=f.readline()
    if line=="":
      break
    if line=="\n":
      line=f.readline()
      line2=line.rstrip("\n")
      line2=line2.split(">")
      if line2[0]==locations[j].name:
        continue
  locations[j].other_location(direction,destination,dir_dest)
  j+=1
  direction=[]
  destination=[]
  dir_dest={}
f.close()



i=0
creaturesname=[]
while i<len(creatures):
  creaturesname.append(creatures[i].name.lower())
  i+=1
i=0
itemsname=[]
while i<len(items):
  itemsname.append(items[i].short_name)
  i+=1
locations[0].locationmap(exits)
i=0
while i<len(exits):
  if exits[i].name==locations[0].name:
    print("The path to freedom is clear. You can FLEE this place.")
  i+=1
print()
currentlocation=locations[0]
itemcanpick=currentlocation.locationitem
currentcreature=currentlocation.locationcreature
goose=Goose(locations[0])
commandd=input(">> ")
commandd=commandd.lower()

while commandd!="quit":
  commandd=commandd.split(" ")
  if commandd[0]=="help":
    print("HELP            - Shows some available commands.")
    print("INV             - Lists all the items in your inventory.")
    print("TAKE <ITEM>     - Takes an item from your current location.")
    print("DROP <ITEM>     - Drops an item at your current location.")
    print()
    print("LOOK or L       - Lets you see the map/location again.")
    print("LOOK <ITEM>     - Lets you see an item in more detail.")
    print("LOOK ME         - Sometimes, you just have to admire the feathers.")
    print("LOOK <CREATURE> - Sizes up a nearby creature.")
    print("LOOK HERE       - Shows a list of all items in the room.")
    print()
    print("NORTHWEST or NW - Moves you to the northwest.")
    print("NORTH or N      - Moves you to the north.")
    print("NORTHEAST or NE - Moves you to the northeast.")
    print("EAST or E       - Moves you to the east.")
    print()
    print("SOUTHEAST or SE - Moves you to the southeast.")
    print("SOUTH or S      - Moves you to the south.")
    print("SOUTHWEST or SW - Moves you to the southwest.")
    print("WEST or W       - Moves you to the west.")
    print()
    print("FLEE            - Attempt to flee from your current location.")
    print("HONK or Y       - Attempt to scare off all creatures in the same location.")
    print("WAIT            - Do nothing. All other creatures will move around you.")
    print("QUIT            - Ends the game. No questions asked.")
    print()
    
  elif commandd[0]=="inv":
    if len(goose.takelist)==0:
      print("You are carrying nothing.")
    elif len(goose.takelist)==1:
        print("You, a goose, are carrying the following item:")
        print(" - "+goose.takelist[0].item_name)
    else:
      print("You, a goose, are carrying the following items:")
      i=0
      while i<len(goose.takelist):
        print(" - "+goose.takelist[i].item_name)
        i+=1
    print()
  elif commandd[0]=="flee":
    if currentlocation in exits:
      print("You slip past the dastardly Goosechasers and run off into the wilderness! Freedom at last!")
      print("========= F R E E D O M =========")
      quit()
    else:
      print("There's nowhere you can run or hide! Find somewhere else to FLEE.")
      print()
        
  elif commandd[0]=="honk" or commandd[0]=="y":
    currentcreature=currentlocation.locationcreature
    if len(currentcreature)==0:
      print("All shall quiver before the might of the goose! HONK!")
    else:
      print("You sneak up behind your quarry and honk with all the force of a really angry airhorn! HONK!")
      catch=[]
      q=0
      while q<len(currentcreature):
        if currentcreature[q].terror_rating<goose.terror_rating:
          print(currentcreature[q].name+" is spooked! They flee immediately!")
          creatures.remove(currentcreature[q])
          currentcreature.remove(currentcreature[q])
          q=q-1
        else:
          print(currentcreature[q].name+" is not spooked :(")
          catch.append(currentcreature[q])
        q+=1
      if len(creatures)==0:
        print()
        print("None can stand against the power of the goose!")
        print("========= V I C T O R Y =========")
        quit()
      elif len(catch)>0:
        print()
        k=0
        while k<len(catch):
          print(catch[k].name+" is trying to catch you!")
          k+=1
        print("Oh no, you've been caught!")
        print("========= GAME OVER =========")
        quit()
    turn()
    print()
  elif commandd[0]=="wait":
    print("You lie in wait.")
    turn()
    print()
      
  elif (commandd[0]=="look" or commandd[0]=="l")and len(commandd)==1:
    currentlocation.locationmap(exits)
    i=0
    while i<len(exits):
        if exits[i].name==locations[0].name:
            print("The path to freedom is clear. You can FLEE this place.")
        i+=1  
    print()
      
  elif commandd[0]=="look" and commandd[1]=="me":
    print("You are a goose. You are probably quite terrifying.")
    print("In fact, you have a terror rating of: "+str(goose.terror_rating))
    print()
  elif commandd[0].lower()=="look" and commandd[1].lower()=="here":
    itemcanpick=currentlocation.locationitem
    if len(itemcanpick)==0:
      print("There is nothing here.")
    else:
      i=0
      while i<len(itemcanpick):
        name=itemcanpick[i].short_name.upper()
        a=len(name)
        b=16-a
        print(name+" "*b+"| "+itemcanpick[i].item_name)
        i+=1
    print()
      
  elif commandd[0]=="north" or commandd[0]=="n":
    temple="north"
    if temple in currentlocation.dir_dest:
      t=currentlocation.dir_dest['north']
      currentlocation=t
      print("You move north, to "+currentlocation.name+".")
      turn()
      currentlocation.locationmap(exits)
    else:
      print("You can't go that way.")
    print()
  
  elif commandd[0]=="south" or commandd[0]=="s":
    temple="south"
    if temple in currentlocation.dir_dest:
      t=currentlocation.dir_dest['south']
      currentlocation=t
      print("You move south, to "+currentlocation.name+".")
      turn()
      currentlocation.locationmap(exits)
    else:
      print("You can't go that way.")
    print()
    
  elif commandd[0]=="west" or commandd[0]=="w":
    temple="west"
    if temple in currentlocation.dir_dest:
      t=currentlocation.dir_dest['west']
      currentlocation=t
      print("You move west, to "+currentlocation.name+".")
      turn()
      currentlocation.locationmap(exits)
    else:
      print("You can't go that way.")
    print()
  elif commandd[0]=="east" or commandd[0]=="e":
    temple="east"
    if temple in currentlocation.dir_dest:
      t=currentlocation.dir_dest['east']
      currentlocation=t
      print("You move east, to "+currentlocation.name+".")
      turn()
      currentlocation.locationmap(exits)
    else:
      print("You can't go that way.")
    print()
  elif commandd[0]=="northwest"or commandd[0]=="nw":
    temple="northwest"
    if temple in currentlocation.dir_dest:
      t=currentlocation.dir_dest['northwest']
      currentlocation=t
      print("You move northwest, to "+currentlocation.name+".")
      turn()
      currentlocation.locationmap(exits)
    else:
      print("You can't go that way.")
    print()
  elif commandd[0]=="northeast"or commandd[0]=="ne":
    temple="northeast"
    if temple in currentlocation.dir_dest:
      t=currentlocation.dir_dest['northeast']
      currentlocation=t
      print("You move northeast, to "+currentlocation.name+".")
      turn()
      currentlocation.locationmap(exits)
    else:
      print("You can't go that way.")
    print()
  elif commandd[0]=="southwest"or commandd[0]=="sw":
    temple="southwest"
    if temple in currentlocation.dir_dest:
      t=currentlocation.dir_dest['southwest']
      currentlocation=t
      print("You move southwest, to "+currentlocation.name+".")
      turn()
      currentlocation.locationmap(exits)
    else:
      print("You can't go that way.")
    print()
  elif commandd[0]=="southeast" or commandd[0]=="se":
    temple="southeast"
    if temple in currentlocation.dir_dest:
      t=currentlocation.dir_dest['southeast']
      currentlocation=t
      print("You move southeast, to "+currentlocation.name+".")
      turn()
      currentlocation.locationmap(exits)
    else:
      print("You can't go that way.")
    print()

  elif commandd[0]=="take":
    i=0
    j=0
    while i<len(currentlocation.locationitem):
      itemcanpick=currentlocation.locationitem
      if itemcanpick[i].short_name==commandd[1].lower():
        print("You pick up the "+itemcanpick[i].item_name+".")
        goose.take(itemcanpick[i])
        currentlocation.remove_item(itemcanpick[i])
        turn()
        j=1
        break
      i+=1
    if j==0:
      print("You don't see anything like that here.")
    print()
      
  elif commandd[0]=="drop":
    i=0
    j=0
    while i<len(goose.takelist):
      if goose.takelist[i].short_name==commandd[1].lower():
        print("You drop the "+goose.takelist[i].item_name+".")
        currentlocation.add_item(goose.takelist[i])
        goose.drop(goose.takelist[i])
        j=1
        break
      i+=1
    if j==0:
      print("You don't have that in your inventory.")
    elif j==1:
      turn()
    print()
    
  elif commandd[0]=="look":
    if commandd[1] in itemsname:
      i=0
      while i<len(goose.takelist):
        if goose.takelist[i].short_name==commandd[1].lower():
          print(goose.takelist[i].item_name+" - Terror Rating: "+str(goose.takelist[i].terror_rating))
          k=1
        i+=1
      j=0
      itemcanpick=currentlocation.locationitem
      while j<len(itemcanpick):
        if itemcanpick[j].short_name==commandd[1].lower():
          print(itemcanpick[j].item_name+" - Terror Rating: "+str(itemcanpick[j].terror_rating))
          k=1
        j+=1

    elif commandd[1].lower() in creaturesname:
      i=0
      j=0
      currentcreature=currentlocation.locationcreature
      while i<len(currentcreature):
        if currentcreature[i].name.lower()==commandd[1]:
          j=1
          t=currentcreature[i].terror_rating-goose.terror_rating
          if t>=5:
            print(currentcreature[i].name+" doesn't seem very afraid of you.")
          elif t<=-5:
            print(currentcreature[i].name+" looks a little on-edge around you.")
          else:
            print("Hmm. "+currentcreature[i].name+" is a bit hard to read.")
        i+=1
    else:
      print("You don't see anything like that here.")
    print()
  else:
    print("You can't do that.")
    print()
  commandd=input(">> ")
  commandd=commandd.lower()
  
if commandd.lower()=="quit":
  print("Game terminated.")
  quit()

