class BOQ:

    def __init__(self,cat1, cat2, cat3, cat4, cat5):
        self.cat1 = cat1
        self.cat2 = cat2
        self.cat3 = cat3
        self.cat4 = cat4
        self.cat5 = cat5

    def add_to_cat(self,cat, area):
        if cat == 1:
            self.cat1 += area
        elif cat == 2:
            self.cat2 += area
        elif cat == 3:
            self.cat3 += area
        elif cat == 4:
            self.cat4 += area
        elif cat == 5:
            self.cat5 += area
    
    def returncat(self):
        return self.cat1, self.cat2, self.cat3, self.cat4, self.cat5

    def returncost(self):
        return self.cat1, self.cat2*2, self.cat3*3, self.cat4*4, self.cat5*5
