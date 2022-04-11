# %%
class Duct:

    def __init__(self, area, width, height, quantity):
        self.area = float(area)
        self.width = float(width)
        self.height = float(height)
        self.quantity = float(quantity)

    def printduct(self):
        print('The duct is ', self.height, 'x', self.width, ' and has a total area of ', self.area*self.quantity, 'm2')
   
    def categorize(self):
        if (max(self.width, self.height) < 750) and (self.width + self.height <= 1150):
            return 1
        elif (max(self.width, self.height) < 750) and (self.width + self.height > 1150):
            return 2
        elif (max(self.width, self.height) >= 750) and (max(self.width, self.height) < 1350):
            return 3
        elif (max(self.width, self.height) >= 1350) and (max(self.width, self.height) < 2100):
            return 4
        elif (max(self.width, self.height) >= 2100):
            return 5
    
    def returnarea(self):
        return self.area*self.quantity

    def returnwidth(self):
        return self.width

    def returnheight(self):
        return self.height

    



# %%
