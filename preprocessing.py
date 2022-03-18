from creature import Creature
from item import Item
from location import Location

def process_locations(source):
    try:
        f=open(source,'r')
        line=f.readlines()
        f.close()
        if len(line)==0:
            raise IndexError
    except IndexError:
        print("The game cannot run without any rooms :(")
        quit()
        
    locations=[]
    f=open(source,'r')
    line=f.readline()
    line=line.rstrip("\n")
    line=line.split(">")
    line[0]=line[0].rstrip(" ")
    line[0]=line[0].lstrip(" ")
    line[2]=line[2].rstrip(" ")
    line[2]=line[2].lstrip(" ")
    locations.append(Location(line[0]))
    locations.append(Location(line[2]))
    while True:
        line=f.readline()
        if line=="":
            break
        if line=="\n":
            continue
        line=line.rstrip("\n")
        line=line.split(">")
        line[0]=line[0].rstrip(" ")
        line[0]=line[0].lstrip(" ")
        line[2]=line[2].rstrip(" ")
        line[2]=line[2].lstrip(" ")
        i=0
        h=0
        j=0
        while i<len(locations):
            if line[0]==locations[i].name:
                h=1
            elif line[2]==locations[i].name:
                j=1
            i+=1
        if h==0:
            location=Location(line[0])
            locations.append(location)
        elif j==0:
            location2=Location(line[2])
            locations.append(location2)
    f.close()
    return locations

def process_items(source, locations):
    items=[]
    f=open(source,'r')
    while True:
        line=f.readline()
        if line=="":
            break
        line=line.rstrip("\n")
        line=line.split("|")
        i=0
        while i<len(line):
            line[i]=line[i].rstrip(" ")
            line[i]=line[i].lstrip(" ")
            i+=1
        if len(line)==5:
            item=Item(line[0],line[1],line[2],line[3],line[4])
        i=0
        while i<len(locations):
            if item.location==locations[i].name:
                if item not in locations[i].locationitem:
                    locations[i].add_item(item)
                break
            i+=1
        items.append(item)
    f.close()    
    return items

def process_creatures(source, locations):
    try:
        f=open(source,'r')
        line=f.readlines()
        f.close()
        if len(line)==0:
            raise IndexError
    except IndexError:
        print("There is nothing chasing you!")
        quit()
        
    creatures=[]
    f=open(source,'r')
    while True:
        line=f.readline()
        if line=="" or line=="\n":
            break
        line=line.rstrip("\n")
        line=line.split("|")
        i=0
        while i<len(line):
            line[i]=line[i].rstrip(" ")
            line[i]=line[i].lstrip(" ")
            i+=1
        creature=Creature(line[0],line[1],line[2],line[3],line[4])
        i=0
        while i<len(locations):
            if locations[i].name == line[3]:
                locations[i].add_creature(creature)
                break
            i+=1
        
        creatures.append(creature)
    f.close()
    return creatures

def process_exits(source, locations):
    canuse_flee=[]
    f=open(source,'r')
    while True:
        line=f.readline()
        if line=="":
            break
        line=line.rstrip()
        i=0
        while i<len(locations):
            if line==locations[i].name:
                canuse_flee.append(locations[i])
            i+=1
    f.close()
    return canuse_flee
