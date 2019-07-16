class Skill:
    def __init__(self, skill):
        self.skill = skill
        self.naval_data = -1
        self.agri_data = -1
        self.civil_data = -1
        self.elec_data = -1
        self.mech_data = -1
        self.diff = 0

    def __lt__(self, other):
        return self.naval_data < other.naval_data

    def getDiff(self):
        if self.naval_data != -1 and self.agri_data != -1:
            self.diff = self.naval_data - self.agri_data
        else:
            self.diff = self.naval_data - self.agri_data + 1

    def setNaval(self, data):
        self.naval_data = data
        #self.getDiff()
        
    def setAgri(self, data):
        self.agri_data = data
        #self.getDiff()

    def setCivil(self, data):
        self.civil_data = data

    def setElec(self, data):
        self.elec_data = data

    def setMech(self, data):
        self.mech_data = data


    def get(self):
        print "Skill: " + self.skill.ljust(33, ' ') + "\tNaval:"  + str(self.naval_data).ljust(6, ' ') + "\tAgricultural:"  + str(self.agri_data).ljust(6, ' ') + "\tDifference:" + str(self.diff)

    def makeCSV(self):
        return self.skill + "," + str(self.naval_data) + "," + str(self.agri_data) + "," + str(self.civil_data) + "," + str(self.elec_data) + "," + str(self.mech_data)