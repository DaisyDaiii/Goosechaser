class Item:
    def __init__(self, short_name, item_name, full_desc, terror_rating,location):
        self.short_name=short_name
        self.item_name=item_name
        self.full_desc=full_desc
        self.terror_rating=int(terror_rating)
        self.location=location
        self.taken=0
    def iftake(self):
        for item in creature.takelist:
            self.taken=1
        return self.taken
