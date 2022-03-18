from item import Item
from creature import Creature
class Location:
    def __init__(self, name):
        self.name=name
        self.locationitem=[]
        self.locationcreature=[]
        self.direction=""
        self.destination=""
        self.dir_dest=""
    
    def add_item(self, item):
        self.locationitem.append(item)
        
    def remove_item(self, item):
        self.locationitem.remove(item)
    
    def other_location(self,direction,destination,dir_dest):
        self.direction=direction
        self.destination=destination
        self.dir_dest=dir_dest

    def add_creature(self,creature):
        self.locationcreature.append(creature)
        
    def remove_creature(self,creature):
        self.locationcreature.remove(creature)
    
    def locationmap(self,exits):
        x1=x2=x3=x4=x5=x6=x7=x8=x9=" "
        a1=a2=a3=a4=a5=a6=a7=a8=" "
        d1=d2=d3=d4=d5=d6=d7=d8=d9=" "
        c1=c2=c3=c4=c5=c6=c7=c8=c9=" "
        x5="[x]"
        i=0
        j=0
        if len(self.destination)>0:
            while i<len(self.direction):
                if len(self.destination[i].locationcreature)>0:
                    inside="C"
                else:
                    inside=" "
                if self.direction[i] == "north":
                    d2="["
                    c2="]"
                    x2=inside
                    a2="|"
                elif self.direction[i] == "south":
                    d8="["
                    c8="]"
                    x8=inside
                    a5="|"
                elif self.direction[i] == "west":
                    d4="["
                    c4="]"
                    x4=inside
                    a7="-"
                elif self.direction[i] == "east":
                    d6="["
                    c6="]"
                    x6=inside
                    a8="-"
                elif self.direction[i] == "northwest":
                    d1="["
                    c1="]"
                    x1=inside
                    a1="\\"
                elif self.direction[i] == "northeast":
                    d3="["
                    c3="]"
                    x3=inside
                    a3="/"
                elif self.direction[i] == "southwest":
                    d7="["
                    c7="]"
                    x7=inside
                    a4="/"
                elif self.direction[i] == "southeast":
                    d9="["
                    c9="]"
                    x9=inside
                    a6="\\"
                i+=1
        line1="{}{}{}".format(d1,x1,c1)+" "+"{}{}{}".format(d2,x2,c2)+" "+"{}{}{}".format(d3,x3,c3)
        line2="   {} {} {}   ".format(a1,a2,a3)
        line3="{}{}{}".format(d4,x4,c4)+"{}".format(a7)+"{}".format(x5)+"{}".format(a8)+"{}{}{}".format(d6,x6,c6)
        line4="   {} {} {}   ".format(a4,a5,a6)
        line5="{}{}{}".format(d7,x7,c7)+" "+"{}{}{}".format(d8,x8,c8)+" "+"{}{}{}".format(d9,x9,c9)
        print(line1.rstrip())
        print(line2.rstrip())
        print(line3.rstrip())
        print(line4.rstrip())
        print(line5.rstrip())
        print("You are now at: {}.".format(self.name))
        i=0
        j=0
        k=0
        if len(self.locationitem)>0:
            while i<len(self.locationitem)-1:
                print(self.locationitem[i].full_desc+" ",end='')
                j=1
                i+=1
            m=len(self.locationitem)-1
            print(self.locationitem[m].full_desc,end='')
            j=1

        if len(self.locationcreature)>0:
            k=1
            if j==0:
                print(self.locationcreature[0].description,end='')
            else:
                print(" "+self.locationcreature[0].description,end='')
            i=1
            while i<len(self.locationcreature):
                print(" "+self.locationcreature[i].description,end='')
                i+=1
        if j==0 and k==0:
            print("There is nothing here.")
        else:
            print()
        if self in exits:
            print("The path to freedom is clear. You can FLEE this place.")


