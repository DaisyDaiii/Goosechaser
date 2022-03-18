from item import Item

class Creature:
    def __init__(self, name, description, terror_rating, location, direction):
        self.name=name
        self.description=description
        self.terror_rating=int(terror_rating)
        self.location=location
        self.direction=direction
        self.takelist=[]
        self.runtime=1

    def take(self, item):
        self.terror_rating+=item.terror_rating
        self.takelist.append(item)
    def drop(self, item):
        self.terror_rating-=item.terror_rating
        self.takelist.remove(item)
    def get_terror_rating(self):
        return self.terror_rating
        

    
class Goose:
    def __init__(self,location):
        self.takelist=[]
        self.terror_rating=5
        self.location=location.name
    def take(self,item):
        self.terror_rating+=int(item.terror_rating)
        self.takelist.append(item)
    def drop(self, item):
        self.terror_rating-=int(item.terror_rating)
        self.takelist.remove(item)
