class Skill:
    def __init__(self, skill):
        self.skill = skill
        self.naval_data = -1
        self.agri_data = -1
        self.diff = 0

    def __lt__(self, other):
        return self.diff < other.diff

    def getDiff(self):
        if self.naval_data != -1 and self.agri_data != -1:
            self.diff = self.naval_data - self.agri_data
        else:
            self.diff = self.naval_data - self.agri_data + 1

    def setNaval(self, data):
        self.naval_data = data
        self.getDiff()
        
    def setAgri(self, data):
        self.agri_data = data
        self.getDiff()

    def get(self):
        print "Skill: " + self.skill.ljust(29, ' ') + "\tNaval:"  + str(self.naval_data).ljust(6, ' ') + "\tCivil:"  + str(self.agri_data).ljust(6, ' ') + "\tDifference:" + str(self.diff)